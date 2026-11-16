---
name: godot-migration
description: Upgrades and version-checks Godot projects - Godot 3.x to 4.x conversion, 4.x minor upgrades (4.3 → 4.4 → 4.5 → 4.6 → 4.7), new, changed, deprecated and removed engine classes, methods, properties and signals per release, and writing code that matches the project's engine version. Use when upgrading a project, when code uses an API that may not exist in the project's Godot version, when a method "does not exist", or when asked what changed in a Godot release.
---

# Godot Migration & API Versions

## Step 1: Know the Project's Version

Read `project.godot`:
```ini
config/features=PackedStringArray("4.7", "Forward Plus")
```
Generate code for **that** version. Before using any API added after 4.3, confirm in the references below that it exists in the project's version. If the project is older, use the fallback or suggest upgrading.

## Step 2: Use the API Change References

These files were generated from the engine's own class reference XML at each release tag. They list every new class and every added, signature-changed, newly deprecated or removed method, property, signal and constant.

| Upgrade step | File | Size |
|--------------|------|------|
| 4.3 → 4.4 | [references/api-4.3-to-4.4.md](references/api-4.3-to-4.4.md) | 32 new classes, 202 changed |
| 4.4 → 4.5 | [references/api-4.4-to-4.5.md](references/api-4.4-to-4.5.md) | 18 new, 5 newly deprecated, 146 changed |
| 4.5 → 4.6 | [references/api-4.5-to-4.6.md](references/api-4.5-to-4.6.md) | 52 new, 82 changed |
| 4.6 → 4.7.2 | [references/api-4.6-to-4.7.md](references/api-4.6-to-4.7.md) | 13 new, 138 changed |

Search, don't read whole files: `grep -n "^#### Tween" references/*.md`, or `grep -n "tween_await" references/*.md`. A class heading (`#### ClassName`) followed by `+`, `~`, `⚠` and `−` lines shows what changed in that step.

With godot-mcp, `godot_get_class_docs` / `godot_search_docs` give the server's built-in docs. Check the version reference when the server's docs and the project version might differ.

## Highlights by Version (for game code)

### 4.4
- GDScript: **typed dictionaries** (`Dictionary[K, V]`), `@export_tool_button`, `@warning_ignore_start`/`@warning_ignore_restore`. `Color8()`, `inst_to_dict()` and `dict_to_inst()` are deprecated.
- **`.uid` sidecar files** for scripts and shaders. Commit them; `load("uid://...")` works.
- Jolt Physics available (experimental) for 3D.
- Tween: `tween_subtween()`, `set_ignore_time_scale()`. AnimationPlayer: sections and markers (`play_section_with_markers`).
- `AudioStreamPlayer*.volume_linear`, `ResourceLoader.list_directory()`, `Node3D.get_global_transform_interpolated()`.
- New: `LookAtModifier3D`, `SpringBoneSimulator3D`, `RetargetModifier3D`, `SubtweenTweener`, `TranslationDomain`, `ColorPalette`.

### 4.5
- GDScript: **`@abstract`** classes and methods, **variadic functions** (`...args: Array`), `@export_file_path`, `ord()`.
- **Script backtraces** (`Engine.capture_script_backtraces()`, `ScriptBacktrace`), and custom **`Logger`** via `OS.add_logger()`.
- UI: `FoldableContainer`/`FoldableGroup`, `DPITexture` (scalable SVG), screen-reader **accessibility** properties on Control (`accessibility_name`, …), `focus_behavior_recursive`/`mouse_behavior_recursive`.
- Rendering: stencil buffer in spatial shaders, shader baker at export.
- Bone constraints: `AimModifier3D`, `CopyTransformModifier3D`, `ConvertTransformModifier3D`, `ModifierBoneTarget3D`.
- **Deprecated:** `ParallaxBackground`/`ParallaxLayer` (use `Parallax2D`), `PackedDataContainer`.
- `Camera2D.limit_enabled`.

### 4.6
- **Jolt is the default 3D physics engine for new projects.** Existing projects keep their engine.
- **TSCN format:** `load_steps` no longer written; nodes get `unique_id=` (re-save scenes via Project > Tools > Upgrade Project Files; expect big VCS diffs once).
- **IK framework:** `IKModifier3D`, `TwoBoneIK3D`, `FABRIK3D`, `CCDIK3D`, `JacobianIK3D`, `SplineIK3D`, `ChainIK3D`, `JointLimitationCone3D`, `BoneTwistDisperser3D`, `LimitAngularVelocityModifier3D`.
- `SceneTree.change_scene_to_node()`; `Input.set_joy_light()`/`has_joy_light()`; `AnimationPlayer.get_queue()` returns `Array[StringName]`; `FileAccess.get_as_text()` lost its `skip_cr` argument.
- Signals starting with `_` hidden from docs and autocomplete; new warning `missing_await`; `debug/gdscript/warnings/exclude_addons` was replaced by `directory_rules`.
- Glow blends before tonemapping (look change); Windows new projects default to D3D12; profiling with Tracy, Perfetto and Instruments; ObjectDB snapshots.
- `NavigationServer2DManager`/`3DManager` (swappable navigation engines), Unix-socket `UDSServer`/`StreamPeerUDS`, `GodotInstance` (LibGodot embedding).

### 4.7
- **HDR output** (`display/window/hdr/request_hdr_output`), **`AreaLight3D`**, `DrawableTexture2D` + `BlitMaterial`.
- **`VirtualJoystick`** control; gamepad **motion sensors** (`Input.get_joy_gyroscope()` and more), `has_joy_vibration()`, `ignore_joypad_on_unfocused_application`; `InputEvent.DEVICE_ID_KEYBOARD`/`DEVICE_ID_MOUSE`.
- Tween: **`tween_await(signal)`** (`AwaitTweener`), `has_tweeners()`.
- Control **offset transforms** (`offset_transform_*`); `AccessibilityServer` singleton.
- `Object.is_class()` takes `StringName`; `type_exists()` deprecated; `RichTextLabel.add_image()` uses `ImageUnit`; `AnimationPlayer.current_animation_changed` argument renamed to `anim_name`.
- Jolt: `WorldBoundaryShape3D.plane.d` sign now matches Godot Physics (flip it if tuned on 4.6 Jolt).
- New Asset Store replaces the Asset Library; wasm64 web exports; GABE Android builds.
- New int limit constants: `INT32_MAX`, `INT64_MIN`, `UINT8_MAX`, and so on.

## Godot 3.x → 4.x Conversion

1. **Back up** (commit), then open in Godot 4 and run Project > Tools > Upgrade Project from Godot 3. Fix the remainder by hand.
2. Common renames and replacements:

| Godot 3 | Godot 4 |
|---------|---------|
| `KinematicBody2D/3D`, `move_and_slide(vel, up)` | `CharacterBody2D/3D`; set `velocity`, call `move_and_slide()` with no args |
| `Spatial`, `Particles`, `Navigation` | `Node3D`, `GPUParticles3D`, `NavigationRegion*` + agents |
| `TileMap` | `TileMapLayer` (4.3+; TileMap deprecated) |
| `export var x = 1`, `onready var`, `tool` | `@export var x := 1`, `@onready var`, `@tool` |
| `yield(obj, "signal")` | `await obj.signal` |
| `connect("sig", self, "_on_x")` | `sig.connect(_on_x)` |
| `emit_signal("sig", a)` | `sig.emit(a)` |
| `instance()` | `instantiate()` |
| `PoolStringArray`, `PoolVector2Array` | `PackedStringArray`, `PackedVector2Array` |
| `setget` | Property syntax `var x: int: set(v): ...` / `get: ...` |
| `rand_range()` | `randf_range()` / `randi_range()` |
| `OS.get_ticks_msec()` | `Time.get_ticks_msec()` |
| `get_tree().change_scene("...")` | `change_scene_to_file("...")` |
| `$AnimatedSprite.play("x")` on `AnimatedSprite` | `AnimatedSprite2D` |
| `rect_position`, `rect_size`, `rect_min_size` | `position`, `size`, `custom_minimum_size` |
| `SCREEN_TEXTURE` (shaders) | `uniform sampler2D s : hint_screen_texture;` |
| `hint_color`, `hint_albedo` | `source_color` |
| `WORLD_MATRIX`, `CAMERA_MATRIX` | `MODEL_MATRIX`, `INV_VIEW_MATRIX` |
| `Tween` node | `create_tween()` (Tween is RefCounted) |
| `funcref(obj, "f")` | `Callable(obj, "f")` / `obj.f` |
| `deg2rad`, `stepify` | `deg_to_rad`, `snapped` |

3. Re-check physics layers, input actions (the format changed), and shaders by hand; automated conversion is incomplete there.

## Minor-Version Upgrade Procedure (4.x → 4.y)

1. Commit. Read the official "Upgrading from X to Y" page and the matching reference file above.
2. Open the project in the new editor. Let it re-import, then run **Project > Tools > Upgrade Project Files** (rewrites scenes and resources; needed for 4.4 UIDs and 4.6 node IDs).
3. Search the codebase for every `−` removed and `~` changed member in the reference that the project uses:
   ```bash
   grep -rn --include=*.gd -E "\b(get_as_text|is_class|get_queue|add_image)\(" .
   ```
4. Run the project's tests (`godot-testing`) and play-test key scenes. Compare rendering, because glow, tonemapping and SSR changed in 4.6.
5. Update CI's `GODOT_VERSION` and export templates (`godot-export-ci`).
6. Regenerate references for future releases with the plugin's `scripts/api_diff.py` (see the README).
