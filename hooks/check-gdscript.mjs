#!/usr/bin/env node
// SPDX-License-Identifier: GPL-3.0-or-later
// Copyright (C) 2026 noit2.com — part of noit-godot-skills
// PostToolUse hook: after Claude writes or edits a .gd file, ask a local Godot
// binary to parse it (`--check-only`) and report parse errors back to Claude.
//
// Best-effort and non-intrusive:
//   - Silently does nothing if the file isn't .gd, no project.godot is found,
//     or no Godot binary is available.
//   - Set GODOT_BIN to point at your Godot executable if it isn't on PATH.
//   - Set GODOT_CLAUDE_SKIP_CHECK=1 to disable.
// Exit code 2 + stderr feeds the errors back to Claude so it can fix them.

import { spawnSync } from "node:child_process";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";

if (process.env.GODOT_CLAUDE_SKIP_CHECK === "1") process.exit(0);

let input = "";
try {
  input = readFileSync(0, "utf8");
} catch {
  process.exit(0);
}

let payload;
try {
  payload = JSON.parse(input);
} catch {
  process.exit(0);
}

const filePath = payload?.tool_input?.file_path || payload?.tool_input?.path;
if (!filePath || !filePath.endsWith(".gd")) process.exit(0);

const absFile = path.resolve(payload?.cwd || process.cwd(), filePath);
if (!existsSync(absFile)) process.exit(0);

// Find the enclosing Godot project.
let projectDir = path.dirname(absFile);
while (!existsSync(path.join(projectDir, "project.godot"))) {
  const parent = path.dirname(projectDir);
  if (parent === projectDir) process.exit(0);
  projectDir = parent;
}

// Skip third-party addons: their warnings are not ours to fix.
const rel = path.relative(projectDir, absFile).split(path.sep).join("/");
if (rel.startsWith("addons/")) process.exit(0);

function findGodot() {
  const candidates = [
    process.env.GODOT_BIN,
    "godot",
    "godot4",
    "Godot",
    "/Applications/Godot.app/Contents/MacOS/Godot",
    "/Applications/Godot_mono.app/Contents/MacOS/Godot",
  ].filter(Boolean);
  for (const c of candidates) {
    const probe = spawnSync(c, ["--version"], { encoding: "utf8", timeout: 10000 });
    if (probe.status === 0 && /^4\./.test((probe.stdout || "").trim())) return c;
  }
  return null;
}

const godot = findGodot();
if (!godot) process.exit(0);

const result = spawnSync(
  godot,
  ["--headless", "--path", projectDir, "--check-only", "--script", `res://${rel}`],
  { encoding: "utf8", timeout: 45000 }
);

if (result.error) process.exit(0); // timeout or spawn failure: don't block the session

const output = `${result.stdout || ""}\n${result.stderr || ""}`;
const lines = output.split(/\r?\n/);
const errorLines = [];
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (/SCRIPT ERROR|Parse Error|Parser Error|Compile Error/i.test(line)) {
    errorLines.push(line.trim());
    // Godot prints the location on the following "at:" line.
    if (lines[i + 1] && /^\s*at:/.test(lines[i + 1])) errorLines.push(lines[i + 1].trim());
  }
}

if (errorLines.length === 0 && result.status === 0) process.exit(0);
if (errorLines.length === 0) {
  // Non-zero exit without recognizable parse errors (e.g. project import needed).
  // Report briefly but don't treat it as a script error.
  process.exit(0);
}

process.stderr.write(
  `Godot parse check failed for res://${rel}:\n` +
    errorLines.slice(0, 20).join("\n") +
    `\n(Checked with: ${godot} --headless --check-only. Fix the script, or set GODOT_CLAUDE_SKIP_CHECK=1 to disable this hook.)\n`
);
process.exit(2);
