---
name: godot-check
description: Runs a full health check on a Godot 4.x project - parses every GDScript file, validates scenes, runs the GUT or GdUnit4 test suite headlessly, scans for deprecated or version-incompatible APIs, and reports results with file and line references. Use when the user runs /godot-check, asks to "check", "validate", "lint" or "test" the Godot project, or before a commit or release.
---

# Godot Check

Collect evidence, don't guess. Each step reports PASS, FAIL or SKIPPED (with the reason).

## 1. Context

- Project root (folder with `project.godot`) and `config/features` version.
- Godot binary: `$GODOT_BIN`, `godot`, `godot4`, or the macOS app path. Without one, skip steps 2 and 4 and say so.
- Make sure the project has been imported: if `.godot/` is missing, run `godot --headless --path . --import` first.

## 2. Parse All Scripts

```bash
find . -name "*.gd" -not -path "./addons/*" -not -path "./.godot/*" | while read -r f; do
  out=$(godot --headless --path . --check-only --script "res://${f#./}" 2>&1)
  echo "$out" | grep -qiE "SCRIPT ERROR|Parse Error" && { echo "== $f"; echo "$out" | grep -iE -A1 "SCRIPT ERROR|Parse Error"; }
done
```
Report each failing file with the error line.

## 3. Validate Scenes and Scripts (godot-mcp, if connected)

- `godot_list_scenes` → `godot_validate_scene` on each scene (or the changed ones).
- `godot_list_scripts` → `godot_validate_script` on changed scripts.
- If the editor bridge is connected: `godot_editor_get_errors` for current editor and runtime errors.

## 4. Run Tests

Detect the framework and run it headless (see `godot-testing` for the exit codes):
```bash
# GUT
godot --headless --path . -s addons/gut/gut_cmdln.gd -gdir=res://test -ginclude_subdirs -gexit
# GdUnit4
./addons/gdUnit4/runtest.sh --godot_binary "$(command -v godot)" --headless --ignoreHeadlessMode -a res://test
```
No framework: SKIPPED, and suggest adding one.

## 5. API Compatibility Scan

Compare code against the project's engine version using the `godot-migration` references:
- **Deprecated APIs:** grep for names marked `⚠ deprecated` in versions at or below the project version, for example `ParallaxBackground`, `ParallaxLayer`, `TileMap` (not `TileMapLayer`), `SkeletonIK3D`, `Color8(`, `inst_to_dict(`, `type_exists(`.
  ```bash
  grep -rnE --include=*.gd --include=*.tscn "\b(ParallaxBackground|ParallaxLayer|SkeletonIK3D|Color8\(|inst_to_dict\(|dict_to_inst\(|type_exists\()" . | grep -v "/addons/"
  grep -rnE --include=*.tscn 'type="TileMap"' . | grep -v "/addons/"
  ```
- **Too-new APIs:** if the project is older than 4.7, flag uses of members the references list as added later (for example `tween_await`, `VirtualJoystick`, `change_scene_to_node`, `@abstract`, `Dictionary[`).
- **Godot 3 leftovers:** `yield(`, `.connect("`, `export var`, `onready var`, `instance()`, `KinematicBody`.

## 6. Hygiene

- `.gd.uid` files present and tracked for each script (4.4+): `git ls-files '*.gd' | while read f; do git ls-files --error-unmatch "$f.uid" >/dev/null 2>&1 || echo "untracked uid: $f"; done`
- AI Bridge / test addons excluded from release export presets (`export_presets.cfg` `exclude_filter`).
- Untyped declarations in hot scripts (optional style note).

## Report Format

```
Godot check — MyGame (4.7, Forward Plus), Godot 4.7.2

Scripts parsed ..... 84/86   FAIL
  res://entities/player/player.gd:42  Parse Error: Identifier "spd" not declared
  res://ui/hud.gd:10                  Parse Error: Expected end of statement
Scenes validated ... 31/31   PASS
Tests (GUT) ........ 52 passed, 1 failed   FAIL
  test_inventory.gd::test_stack_merges  expected 5, got 3
API scan ........... 2 deprecated uses   WARN
  levels/forest.tscn: ParallaxBackground (deprecated 4.5 → Parallax2D)
Hygiene ............ PASS
```
End with the 1–3 most important fixes. Offer to fix them; don't edit anything unasked during a check.
