---
name: godot-input
description: Sets up Godot 4.x input - InputMap actions, keyboard/mouse/gamepad/touch bindings, input event flow (_input vs _unhandled_input), rebinding menus, deadzones, mouse capture, gamepad rumble and LED, 4.7 gyro/accelerometer motion sensors, and the VirtualJoystick. Use when adding controls, control presets, remapping, local multiplayer devices, or debugging input that doesn't fire. Pairs with godot-mcp godot_input_* tools.
---

# Godot Input

## Define Actions, Never Raw Keys

Gameplay code reads **actions** (`jump`, `move_left`), and bindings live in the InputMap (`[input]` in `project.godot`).

| Task | godot-mcp tool |
|------|----------------|
| Apply a genre preset (platformer, top-down, FPS, UI) | `godot_input_list_presets`, then `godot_input_apply_preset` |
| Add or update one action with keys, buttons and axes | `godot_input_set_action` |
| Inspect existing actions | `godot_input_list_actions`, `godot_input_get_action` |
| Remove an action | `godot_input_remove_action` |

Use `godot_help tool="godot_input_set_action"` for the binding payload format. After editing `project.godot` externally while the editor is open, call `godot_editor_refresh_filesystem`. InputMap changes may still need an editor restart to show in Project Settings.

Bind every gameplay action to **keyboard + gamepad** at minimum. Use `physical_keycode` for WASD-style layouts so AZERTY and Dvorak players get the same physical keys.

## Reading Input

```gdscript
# Polling, for continuous movement, in _physics_process
var move := Input.get_vector("move_left", "move_right", "move_up", "move_down")   # deadzone-aware, length ≤ 1
var aim := Input.get_vector("aim_left", "aim_right", "aim_up", "aim_down", 0.2)
if Input.is_action_just_pressed("jump"): jump()
var throttle := Input.get_action_strength("accelerate")   # analog triggers 0..1

# Events, for discrete actions and UI-aware gameplay
func _unhandled_input(event: InputEvent) -> void:
    if event.is_action_pressed("interact"):
        interact()
        get_viewport().set_input_as_handled()
```

Event flow: `_input` → `_shortcut_input` → `_unhandled_key_input` → Control GUI input → `_unhandled_input`. Put gameplay in **`_unhandled_input`** so open menus consume clicks and keys first. Use `_input` only for things that must work regardless of UI, such as a debug console toggle.

Avoid:
- `Input.is_key_pressed(KEY_SPACE)` in gameplay. It bypasses remapping.
- Reading `is_action_just_pressed` in `_process` for physics logic. It can miss or duplicate presses across ticks; read it in `_physics_process`, or buffer from `_unhandled_input`.
- Echo events: `event.is_action_pressed("x", false)` ignores key-repeat echoes, and that is the default. Pass `true` to allow echoes, for example for text-like navigation.

## Mouse

```gdscript
func _ready() -> void:
    Input.mouse_mode = Input.MOUSE_MODE_CAPTURED   # FPS look

func _unhandled_input(event: InputEvent) -> void:
    if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
        rotate_y(-event.screen_relative.x * sensitivity)
        head.rotate_x(-event.screen_relative.y * sensitivity)
        head.rotation.x = clampf(head.rotation.x, -PI / 2, PI / 2)
    if event.is_action_pressed("ui_cancel"):
        Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
```
Use `screen_relative` (4.3+) for camera look so it is unaffected by viewport stretch. 2D world mouse position: `get_global_mouse_position()`.

## Gamepads

- Device IDs: `Input.get_connected_joypads()`, and the `Input.joy_connection_changed(device, connected)` signal for hot-plug and "controller disconnected" pause screens.
- Per-player input for local multiplayer: check `event.device` in `_unhandled_input`, or duplicate actions per player (`p1_jump`, `p2_jump`) with device-specific events. 4.7 adds `InputEvent.DEVICE_ID_KEYBOARD` / `DEVICE_ID_MOUSE` constants to tell keyboard and mouse apart from pads.
- Rumble: `Input.start_joy_vibration(device, weak, strong, duration)`. 4.7 adds `has_joy_vibration()`, `is_joy_vibrating()` and `get_joy_vibration_remaining_duration()`.
- LED color (4.6+): `if Input.has_joy_light(device): Input.set_joy_light(device, Color.RED)`.
- **Motion sensors (4.7+):** `has_joy_motion_sensors(device)`, `set_joy_motion_sensors_enabled(device, true)`, then `get_joy_gyroscope(device)` (rad/s) for gyro aiming, plus `get_joy_accelerometer()` and `get_joy_gravity()`. Calibrate with `start_joy_motion_sensors_calibration()` / `stop_joy_motion_sensors_calibration()` while the pad rests on a surface.
- `Input.ignore_joypad_on_unfocused_application` (4.7+) stops background pads from driving the game.
- Show button prompts per controller family from `Input.get_joy_name(device)` or the GUID.

## Touch

- `InputEventScreenTouch` / `InputEventScreenDrag` carry an `index` per finger.
- Enable `input_devices/pointing/emulate_mouse_from_touch` to make UI work with no extra code.
- **On-screen stick:** `VirtualJoystick` (4.7+) presses your actions, so gameplay code is unchanged (see `godot-ui`). Before 4.7, use `TouchScreenButton` with `action` set.
- Phone accelerometer and gyro: `Input.get_accelerometer()`, `Input.get_gyroscope()` (mobile only; enable sensors in project settings).

## Rebinding Menu

```gdscript
func rebind(action: StringName, event: InputEvent) -> void:
    for old in InputMap.action_get_events(action):
        if old.get_class() == event.get_class():   # replace only same device type
            InputMap.action_erase_event(action, old)
    InputMap.action_add_event(action, event)
    _save_bindings()

func _save_bindings() -> void:
    var cfg := ConfigFile.new()
    for action in InputMap.get_actions():
        if String(action).begins_with("ui_"):
            continue
        cfg.set_value("bindings", action, InputMap.action_get_events(action))
    cfg.save("user://input.cfg")
```
Load the saved bindings at startup, in an autoload, before any gameplay scene reads input. Ignore `ui_*` built-in actions unless you deliberately support UI remapping.

## Testing Input

- Runtime automation: `godot_runtime_press_action` / `godot_runtime_release_action` / `godot_runtime_tap_action` for action-driven gameplay, and `godot_runtime_click` + `godot_runtime_type_text` for UI.
- `Input.action_press()` does **not** trigger `_input`/`_unhandled_input`; it only affects polling. To test event handlers, use `Input.parse_input_event()` with a real `InputEventAction` or `InputEventKey`.
- Headless mouse clicks don't press Buttons. Run click tests under a virtual display (see `godot-testing`).

## Debug Checklist

1. Is the action name spelled exactly as in the InputMap? Unknown actions print errors at runtime.
2. Is a Control with `mouse_filter = STOP` or focus swallowing the event before `_unhandled_input`?
3. Is the node paused? Set `process_mode` to `ALWAYS` for pause menus.
4. Gamepad stick drift: raise that action's `deadzone` in the Input Map (per action), or pass an explicit deadzone to `get_vector`.
