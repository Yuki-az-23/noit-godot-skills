#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 noit2.com — part of noit-godot-skills
# Launches the godot-mcp server for the Godot project in the current workspace.
# Resolution order for the server:
#   1. $GODOT_MCP_DIR/dist/index.js
#   2. `godot-mcp` on PATH (npm install -g @genai-gametools/godot-mcp)
#   3. ~/godot-mcp/dist/index.js, ~/.local/share/godot-mcp/dist/index.js
# Resolution order for the project:
#   1. $GODOT_PROJECT
#   2. nearest directory containing project.godot, walking up from $PWD
#   3. first project.godot found up to 3 levels below $PWD
set -euo pipefail

find_project() {
  if [[ -n "${GODOT_PROJECT:-}" ]]; then echo "$GODOT_PROJECT"; return; fi
  local d="$PWD"
  while [[ "$d" != "/" ]]; do
    [[ -f "$d/project.godot" ]] && { echo "$d"; return; }
    d="$(dirname "$d")"
  done
  local f
  f="$(find "$PWD" -maxdepth 3 -name project.godot -not -path '*/.godot/*' -not -path '*/addons/*' 2>/dev/null | head -n1)"
  [[ -n "$f" ]] && { dirname "$f"; return; }
  echo "$PWD"
}

PROJECT="$(find_project)"
PORT_ARGS=()
[[ -n "${GODOT_BRIDGE_PORT:-}" ]] && PORT_ARGS=(--port "$GODOT_BRIDGE_PORT")

for candidate in "${GODOT_MCP_DIR:-}" "$HOME/godot-mcp" "$HOME/.local/share/godot-mcp"; do
  if [[ -n "$candidate" && -f "$candidate/dist/index.js" ]]; then
    exec node "$candidate/dist/index.js" --project "$PROJECT" ${PORT_ARGS[@]+"${PORT_ARGS[@]}"}
  fi
done

if command -v godot-mcp >/dev/null 2>&1; then
  exec godot-mcp --project "$PROJECT" ${PORT_ARGS[@]+"${PORT_ARGS[@]}"}
fi

cat >&2 <<MSG
[noit-godot-skills] godot-mcp server not found.
Install it once:
  git clone https://github.com/alexmeckes/godot-mcp ~/godot-mcp
  cd ~/godot-mcp && npm install && npm run build
or set GODOT_MCP_DIR to an existing checkout. Then restart Claude.
The plugin's skills still work without it (file-based guidance only).
MSG
exit 1
