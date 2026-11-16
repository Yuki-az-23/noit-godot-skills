---
name: godot-project-architecture
description: Structures Godot 4.x projects - folder layout, autoloads, scene composition, signal buses, custom Resources for data, save/load systems, scene switching, and project.godot settings. Use when starting a new Godot project, organizing a growing codebase, adding a save system, deciding between autoloads, groups and signals, or bootstrapping a project with godot_init_project.
---

# Godot Project Architecture

Make structural decisions that keep a Godot project easy to change. Favor composition (small scenes with one job), data in Resources, and communication through signals over hard-coded node paths.

## Start a Project

1. With godot-mcp available, call `godot_init_project`, then `godot_input_apply_preset` for the genre's controls.
2. Otherwise create `project.godot` by opening the folder in Godot once. Do not hand-write it from scratch.
3. Read `config/features` in `project.godot` (for example `PackedStringArray("4.7", "Forward Plus")`) to learn the engine version and renderer before writing any code. Gate version-specific APIs on it (see `godot-migration`).

## Folder Layout

Group by feature, not by file type, once the project has more than a handful of scenes:

```
res://
├── addons/                # third-party and editor plugins (godot_ai_bridge, gut, gdUnit4)
├── autoload/              # global singletons (keep few)
├── common/                # shared components: hitbox/, hurtbox/, health/, state_machine/
├── entities/
│   ├── player/            # player.tscn, player.gd, player_states/, sprites
│   └── enemies/slime/
├── levels/
├── ui/                    # menus, hud, themes/
├── data/                  # .tres Resources: items, enemy stats, dialogue
├── audio/                 # music/, sfx/, default_bus_layout.tres
└── test/                  # unit and integration tests
```

Rules:
- Use `snake_case` for files and folders, `PascalCase` for node names and `class_name`.
- Keep a script next to the scene it drives (`player.tscn` + `player.gd`).
- Commit `.gd.uid`, `.gdshader.uid` and `*.import` files. Never commit `.godot/`.
- Move or rename files only inside the Godot FileSystem dock, or with `godot_editor_refresh_filesystem` afterwards, so UIDs and references stay valid.

## Choosing a Communication Pattern

| Need | Use | Avoid |
|------|-----|-------|
| Child tells parent something happened | Signal on the child, connected by the parent | `get_parent().do_thing()` |
| Parent commands a child | Direct call through `@onready var x: Type = %UniqueName` | Long `$A/B/C/D` paths |
| Many unrelated listeners (score changed, player died) | Event-bus autoload with signals | Polling in `_process` |
| "All enemies", "everything damageable" | Groups + `get_tree().call_group()` / `get_nodes_in_group()` | Hard-coded lists |
| Shared static data (item stats, enemy tuning) | Custom `Resource` + `.tres` files | Dictionaries in scripts |
| Truly global services (save, audio, scene loading) | Autoload | One autoload per feature |

Mark nodes that scripts reference as **unique names** (`%HealthBar`) so scene restructuring does not break paths.

### Event Bus Autoload

```gdscript
# autoload/events.gd   (Project Settings > Globals > Autoload, name: Events)
extends Node

@warning_ignore_start("unused_signal")
signal player_died
signal score_changed(new_score: int)
signal item_collected(item: ItemData)
@warning_ignore_restore("unused_signal")
```

Emit with `Events.score_changed.emit(score)` and listen with `Events.score_changed.connect(_on_score_changed)`. The `@warning_ignore_start`/`@warning_ignore_restore` pair (4.4+) silences "signal declared but never emitted in this class". On 4.3 or earlier, annotate each signal with `@warning_ignore("unused_signal")`.

### Component Composition

Build entities from small reusable scenes:

```
Enemy (CharacterBody2D)
├── HealthComponent (Node)      # health.gd: max_health, damage(), signal died
├── Hurtbox (Area2D)            # forwards hits to HealthComponent
├── Hitbox (Area2D)             # deals damage on contact
└── StateMachine (Node)
```

```gdscript
# common/health/health_component.gd
class_name HealthComponent
extends Node

signal health_changed(current: int, maximum: int)
signal died

@export var max_health: int = 10
var health: int

func _ready() -> void:
    health = max_health

func damage(amount: int) -> void:
    if health <= 0:
        return
    health = maxi(health - amount, 0)
    health_changed.emit(health, max_health)
    if health == 0:
        died.emit()
```

## Data in Resources

```gdscript
# data/enemy_stats.gd
class_name EnemyStats
extends Resource

@export var display_name: String = "Slime"
@export_range(1, 999) var max_health: int = 10
@export var speed: float = 60.0
@export var loot: Array[ItemData] = []
@export var resistances: Dictionary[StringName, float] = {}   # typed dictionary, 4.4+
```

- Resources loaded with `load()`/`preload()` are **shared**. Call `.duplicate()` (or `duplicate(true)` for nested Resources) before mutating per-instance state, or enable `resource_local_to_scene`.
- Use `ResourceLoader.list_directory("res://data/items")` (4.4+) to enumerate data files. It works in exported builds, unlike `DirAccess` on `res://`.

## Scene Switching

```gdscript
get_tree().change_scene_to_file("res://levels/level_2.tscn")
get_tree().change_scene_to_packed(preloaded_scene)
get_tree().change_scene_to_node(level_instance)   # 4.6+: switch to an already-built node
```

For loading screens, use `ResourceLoader.load_threaded_request()` + `load_threaded_get_status()` (see `godot-code-gen`). Persist cross-scene state in an autoload, not in the outgoing scene.

## Save / Load

Prefer typed data over serializing nodes:

```gdscript
# autoload/save_manager.gd
extends Node

const SAVE_PATH := "user://save_%d.json"
const VERSION := 2

func save_game(slot: int, data: Dictionary) -> Error:
    data["version"] = VERSION
    var file := FileAccess.open(SAVE_PATH % slot, FileAccess.WRITE)
    if file == null:
        return FileAccess.get_open_error()
    file.store_string(JSON.stringify(data, "\t"))
    return OK

func load_game(slot: int) -> Dictionary:
    var path := SAVE_PATH % slot
    if not FileAccess.file_exists(path):
        return {}
    var parsed: Variant = JSON.parse_string(FileAccess.get_file_as_string(path))
    if parsed is not Dictionary:
        push_warning("Corrupt save in slot %d" % slot)
        return {}
    return _migrate(parsed)

func _migrate(data: Dictionary) -> Dictionary:
    var v: int = data.get("version", 1)
    if v < 2:
        data["settings"] = data.get("settings", {})
    return data
```

- **Paths:** always write under `user://`. `res://` is read-only in exported games.
- **JSON types:** JSON turns `Vector2` and other engine types into strings, and ints into floats. Convert explicitly (`{"x": pos.x, "y": pos.y}`), or use `var_to_str`/`str_to_var`.
- **Security:** `ResourceSaver.save()` with a `.tres` save file is convenient but can execute embedded scripts when loaded. Never load `.tres`/`.res` saves from untrusted sources such as downloaded or shared saves.
- **Nodes that save:** add them to a `persist` group and implement `save() -> Dictionary` / `load_state(d: Dictionary)`.
- **Versioning:** store a `version` field and migrate on load.

## Autoload Hygiene

- Keep autoloads few: Events, SaveManager, AudioManager, SceneLoader, Settings.
- Do not hold references to scene nodes in autoloads past the scene's lifetime. Connect to `tree_exiting` or check `is_instance_valid()`.
- The AI Bridge plugin registers its own runtime autoload. Leave it alone.

## Checklist Before Adding Code

- [ ] Does a node or Resource already do this?
- [ ] Can this be a small scene instanced where needed?
- [ ] Is communication upward via signals and downward via calls?
- [ ] Is data in a Resource instead of a magic-number script?
- [ ] Will this survive renaming or moving nodes (unique names, groups)?
