# NOTICE: noit-godot-skills

Copyright (C) 2026 noit2.com

This project is licensed under the GNU General Public License v3.0 or later
(see [`LICENSE`](LICENSE)). It includes and builds on MIT-licensed work by others,
whose copyright and permission notices are kept in [`licenses/`](licenses/), as
the MIT License requires.

## Credits chain

1. **noit-godot-skills** v2.0: © 2026 noit2.com, GPL-3.0-or-later.
   ↳ built on
2. **godot-claude-skills** v1.0 (<https://github.com/alexmeckes/godot-claude-skills>):
   © 2025, author Alex Meckes, MIT. Notice: `licenses/MIT-godot-claude-skills.txt`.
   The five original skills (`godot-code-gen`, `godot-scene-design`, `godot-shader`,
   `godot-live-edit`, `godot-interactive`) derive from it, with modifications.
   ↳ which documents and uses
3. **Godot Engine** (<https://github.com/godotengine/godot>): © 2014-present Godot Engine
   contributors, © 2007-2014 Juan Linietsky, Ariel Manzur, MIT. Notice: `licenses/GODOT-LICENSE.txt`.
   The files in `skills/godot-migration/references/` are derived from Godot's class reference
   XML (`doc/classes`, `modules/*/doc_classes`) at tags 4.3-stable through 4.7.2-stable.
4. **godot-mcp** (<https://github.com/alexmeckes/godot-mcp>): © 2026 Alex Meckes, MIT.
   Notice: `licenses/MIT-godot-mcp.txt`. Not bundled. `scripts/start-godot-mcp.sh` launches
   the user's own install, and tool names are documented in the skills.
5. **GUT** (<https://github.com/bitwes/Gut>): © 2018 Tom "Butch" Wesley, MIT. Not bundled; documented only.
6. **GdUnit4** (<https://github.com/godot-gdunit-labs/gdUnit4>): © 2023-2026 Mike Schulze, MIT.
   Not bundled; documented only.

All upstream licenses were checked against each project's LICENSE file on 2026-11-12.
MIT-licensed code may be combined into a GPL-licensed work, provided the MIT notices are kept.

## Changes (as required by GPLv3 section 5a)

### 2026-11-16: v2.0.0, noit2.com
Relative to godot-claude-skills v1.0.0:
- Relicensed the combined work as GPL-3.0-or-later and renamed the plugin to `noit-godot-skills`.
- Added the missing `name`/`description` frontmatter to `godot-code-gen`, `godot-scene-design`,
  `godot-shader` and `godot-live-edit`.
- Removed references to five tools that do not exist in godot-mcp from `godot-live-edit`.
- Fixed code errors in the examples: untyped `load()` → `instantiate()`, undeclared `animation_player`,
  an invalid `.tscn` bitmask expression and inline comments, a wrong `body_entered` connection,
  a missing AnimationLibrary, screen shaders sampling `TEXTURE` instead of a `hint_screen_texture`
  sampler, and a particle shader using non-existent built-ins.
- Updated content for Godot 4.4–4.7 (scene format, GDScript features, shader notes).
- Added skills: project-architecture, physics, ui, animation, input, audio, navigation, testing,
  export-ci, performance, migration, multiplayer, csharp, setup, check.
- Added the `godot-reviewer` agent, the GDScript parse-check hook, the godot-mcp launcher and
  MCP config, the `api_diff.py` tool and the generated API change references.

<!-- Forks: add a new entry under "Changes", newest first: date, version, who, what changed. -->

## Trademarks

"Godot" and the Godot logo are trademarks of the Godot Foundation. "Claude" is a trademark
of Anthropic. This is an independent community project, not affiliated with or endorsed by either.
