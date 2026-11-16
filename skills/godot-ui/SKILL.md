---
name: godot-ui
description: Builds Godot 4.x user interfaces with Control nodes - containers, anchors and size flags, themes and StyleBoxes, menus, HUDs, dialogs, focus and gamepad navigation, responsive scaling, localization, accessibility, and the 4.7 VirtualJoystick. Use for main menus, HUDs, inventories, settings screens, pause menus, or when UI layout misbehaves. Pairs with godot-mcp godot_ui_* tools.
---

# Godot UI

## Layout Model

- **Containers decide child layout.** Inside a container, a child's position and size come from the container plus the child's **size flags** (`Fill`, `Expand`, `Shrink Center`, ...) and `custom_minimum_size`. Setting `position`/`size` on a container child does nothing lasting.
- **Anchors and offsets** position a Control relative to its parent **only when the parent is not a container**. Use layout presets (`set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)`).
- Build screens as: root `Control` (Full Rect) → `MarginContainer` → `VBoxContainer`/`HBoxContainer`/`GridContainer` → widgets.
- Use `CanvasLayer` for HUDs so the game camera does not move them.
- **4.7:** Control **offset transforms** let you animate a control's visual position, scale and rotation (hover pop, shake) without disturbing container layout. Set `offset_transform_enabled = true`, then tween `offset_transform_position`, `offset_transform_scale` or `offset_transform_rotation` (pivot: `offset_transform_pivot_ratio`). Before 4.7, animate a child wrapper or `pivot_offset` + `scale`.
- **4.6:** `pivot_offset_ratio` sets the pivot relative to size (`Vector2(0.5, 0.5)` = center).

| Container | Use |
|-----------|-----|
| `VBoxContainer` / `HBoxContainer` | Stacks; `separation` theme constant for spacing |
| `GridContainer` | Inventories (`columns`) |
| `MarginContainer` | Padding (`margin_*` theme constants) |
| `CenterContainer` | Center a fixed-size panel |
| `PanelContainer` | Background StyleBox + one child |
| `ScrollContainer` | Lists that overflow |
| `TabContainer` | Settings tabs |
| `AspectRatioContainer` | Keep portraits or minimaps square |
| `FlowContainer` (`H`/`V`) | Wrapping tags and chips |
| `FoldableContainer` (4.5+) | Collapsible sections; `FoldableGroup` for accordion behavior |
| `SplitContainer` | Resizable panes (tools, editors) |

## godot-mcp UI Tools

| Task | Tool |
|------|------|
| Theme (.tres) from a color palette and fonts | `godot_ui_create_theme` |
| Main or pause menu scene | `godot_ui_create_menu` |
| HUD (health, score, ammo) | `godot_ui_create_hud` |
| Confirm/alert dialogs | `godot_ui_create_dialog` |
| Panels, containers, layouts | `godot_ui_create_panel`, `godot_ui_create_container`, `godot_ui_create_layout` |
| StyleBox resources | `godot_ui_create_stylebox` |
| Look up anchor presets or container behavior | `godot_ui_list_anchors`, `godot_ui_get_anchor_config`, `godot_ui_list_containers`, `godot_ui_list_presets` |

Call `godot_help tool="<name>"` for the exact argument template; the tools do not share one naming style. After generating, run `godot_validate_scene`, open the scene, and check it at more than one window size.

## Themes

- Make one project theme (`gui/theme/custom` in Project Settings) and override per node only when needed.
- Define **type variations** (for example `TitleLabel` based on `Label`) instead of per-node overrides, and set `theme_type_variation` on the node.
- StyleBoxFlat covers most panels and buttons: `bg_color`, `corner_radius_*`, `border_width_*`, `content_margin_*`, `shadow_*`.
- 4.6 separates mouse and keyboard focus styles. Always give buttons a visible `focus` StyleBox for gamepad and keyboard players.

## Responsive Scaling

Project Settings > Display > Window:
- Pixel art: `stretch/mode = viewport`, `stretch/scale_mode = integer`.
- HD or vector UI: `stretch/mode = canvas_items`, `stretch/aspect = expand`.
- Test 16:9, 16:10, 21:9, 4:3 and portrait (mobile). Anchor HUD elements to corners, not to absolute positions.
- Use `DPITexture`/SVG import (4.5+) for crisp scalable icons.

## Focus and Gamepad Navigation

```gdscript
func _ready() -> void:
    %StartButton.grab_focus()          # always focus something when a menu opens
    visibility_changed.connect(func(): if visible: %StartButton.grab_focus())
```
- Set `focus_neighbor_*` when automatic neighbor detection picks the wrong control.
- Use `ui_accept`/`ui_cancel` actions so keyboard, gamepad and remapped inputs all work.
- `focus_behavior_recursive` / `mouse_behavior_recursive` (4.5+) disable focus or mouse for a whole subtree, which is useful for disabled panels.
- Set decorative overlays to `mouse_filter = MOUSE_FILTER_IGNORE`, otherwise they eat clicks.

## Common Patterns

**Pause menu** (works while the tree is paused):
```gdscript
extends CanvasLayer

func _ready() -> void:
    process_mode = Node.PROCESS_MODE_ALWAYS
    hide()

func _unhandled_input(event: InputEvent) -> void:
    if event.is_action_pressed("pause"):
        get_tree().paused = not get_tree().paused
        visible = get_tree().paused
        if visible:
            %ResumeButton.grab_focus()
        get_viewport().set_input_as_handled()
```

**Health bar bound to a component:**
```gdscript
@onready var bar: ProgressBar = %HealthBar

func bind(health: HealthComponent) -> void:
    bar.max_value = health.max_health
    bar.value = health.health
    health.health_changed.connect(func(cur: int, mx: int) -> void:
        bar.max_value = mx
        create_tween().tween_property(bar, "value", cur, 0.2))
```

**Floating damage number:** spawn a `Label` under a `Node2D` in world space, then tween `position:y` and `modulate:a`, and `queue_free` on finish. Keep it out of containers.

## Touch Controls (4.7)

`VirtualJoystick` (a Control) is a built-in on-screen stick that presses your existing input actions, so gameplay code keeps using `Input.get_vector()`:
```gdscript
var stick := VirtualJoystick.new()
stick.joystick_mode = VirtualJoystick.JOYSTICK_DYNAMIC      # or JOYSTICK_FIXED / JOYSTICK_FOLLOWING
stick.visibility_mode = VirtualJoystick.VISIBILITY_WHEN_TOUCHED
stick.action_left = &"move_left"
stick.action_right = &"move_right"
stick.action_up = &"move_up"
stick.action_down = &"move_down"
stick.deadzone_ratio = 0.15
$HUD.add_child(stick)
stick.visible = DisplayServer.is_touchscreen_available()
```
Before 4.7, use `TouchScreenButton` nodes or a custom Control that calls `Input.action_press()`.

## Text and Localization

- Wrap user-facing strings in `tr("KEY")` or set `auto_translate_mode`. Store translations in CSV or PO files under `res://locale`.
- `RichTextLabel` with `bbcode_enabled` for colored or animated text. 4.7 changes `add_image()`/`update_image()` sizing to an `ImageUnit` (pixel, percent, em) argument.
- Enable `autowrap_mode` on Labels in containers, otherwise long text stretches the layout.

## Accessibility (4.5+)

Godot 4.5+ exposes UI to screen readers (AccessKit). Set `accessibility_name` on icon-only buttons and `accessibility_description` for extra context. Avoid conveying state by color alone, and respect a "reduce motion" setting for tweens and screen shake.

## UI Debug Checklist

1. A control doesn't resize: its parent is a container, so use size flags or `custom_minimum_size`, not `size`.
2. A click doesn't register: an overlay with `mouse_filter = STOP` is on top. Check with Debug > Debug Canvas Item Redraw, or inspect the tree.
3. A menu is not navigable by gamepad: no initial `grab_focus()`, or `focus_mode = FOCUS_NONE`.
4. UI moves with the camera: it is not under a `CanvasLayer`.
5. Blurry text: use stretch mode `canvas_items` and MSDF fonts for scalable text.
