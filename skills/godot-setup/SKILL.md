---
name: godot-setup
description: Sets up a Godot 4.x project for AI-assisted development - finds the Godot binary and engine version, installs and builds godot-mcp, copies and enables the AI Bridge editor plugin, verifies the live connection, and optionally installs a test framework. Use when the user runs /godot-setup, says "set up Godot with Claude", or when godot-mcp or the AI Bridge isn't working.
---

# Godot Setup

Run each step, report what passed, and stop at the first step that needs the user (installing Godot, opening the editor). Ask before installing anything into the user's project or home directory.

## 1. Locate the Project and Engine

```bash
# Project root = folder containing project.godot
find . -maxdepth 3 -name project.godot -not -path "*/.godot/*" -not -path "*/addons/*"
grep -E '^config/(name|features)=' project.godot
```
Then find a Godot 4 binary: `$GODOT_BIN`, `godot`, `godot4`, or `/Applications/Godot.app/Contents/MacOS/Godot` on macOS. Run `<bin> --version`.
- No binary: the plugin still works through file-based tools, but parse checks, tests and exports need one. Tell the user where to download it (godotengine.org/download) and how to set `GODOT_BIN`.
- If the editor version differs from `config/features`, warn the user, because opening the project upgrades it (see `godot-migration`).

## 2. godot-mcp Server

The plugin starts the server through `scripts/start-godot-mcp.sh`, which looks in `$GODOT_MCP_DIR`, `~/godot-mcp`, `~/.local/share/godot-mcp`, then for `godot-mcp` on PATH.

If none exists, ask, then install:
```bash
git clone https://github.com/alexmeckes/godot-mcp ~/godot-mcp
cd ~/godot-mcp && npm install && npm run build
```
Requirements: Node.js (check `node --version` against the `engines` field in godot-mcp's `package.json`). After installing, the user must **restart Claude** (or reload plugins) so the MCP server starts. Verify by calling `godot_help`.

To target a specific project or port, set `GODOT_PROJECT` / `GODOT_BRIDGE_PORT` in the environment Claude is launched from.

## 3. AI Bridge Editor Plugin (live editing and runtime automation)

Ask before modifying the project. Then:
```bash
mkdir -p addons
cp -r ~/godot-mcp/addons/godot_ai_bridge addons/
```
Enable it in `project.godot`. Merge into an existing `[editor_plugins]` section; don't duplicate it:
```ini
[editor_plugins]

enabled=PackedStringArray("res://addons/godot_ai_bridge/plugin.cfg")
```
If other plugins are already enabled, append to the existing `PackedStringArray`. The bridge registers a runtime autoload itself when the editor loads it.

The user then opens the project in the Godot editor; the Output panel should show the bridge listening (default port 6550). Verify:
```
godot_connect {}
godot_connection_status {}
godot_editor_get_project_info {}
```

**Release builds:** the bridge must not ship. Add `addons/godot_ai_bridge/*` to every export preset's exclude filter and remove its autoload for release (see `godot-export-ci`).

## 4. Optional Extras (ask first)

- **Test framework:** if neither `addons/gut` nor `addons/gdUnit4` exists, offer GUT (GDScript projects) or GdUnit4 (C# or mixed). See `godot-testing`.
- **Static typing warnings:** set `debug/gdscript/warnings/untyped_declaration=1` (warn) in `project.godot`.
- **.gitignore:** ensure `.godot/` and `*.translation` builds are ignored and `*.uid` files are **not** ignored.

## 5. Report

Summarize as a checklist:
```
Godot binary ........ 4.7.2.stable (godot)      ✅
Project version ..... 4.7 Forward Plus          ✅
godot-mcp ........... ~/godot-mcp (built)       ✅
AI Bridge plugin .... installed + enabled       ✅
Live connection ..... connected :6550           ✅ / ⏳ open the editor
Tests ............... GUT 9.x                   ✅ / — not installed
```
