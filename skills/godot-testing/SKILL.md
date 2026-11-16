---
name: godot-testing
description: Writes and runs automated tests for Godot 4.x projects with GUT (9.x) or GdUnit4 (6.x) - unit tests, scene and integration tests, signal assertions, input simulation, doubles/mocks, headless CLI runs, exit codes, and CI. Use when the user asks for tests, TDD, regression checks, test coverage, or wants to verify gameplay logic without manual play-testing.
---

# Godot Testing

## Pick a Framework

Detect an existing one first: `addons/gut/` → GUT; `addons/gdUnit4/` → GdUnit4. Never install a second framework into a project that already has one.

| | GUT (9.x, MIT) | GdUnit4 (6.x, MIT) |
|---|---|---|
| Style | `extends GutTest`, `assert_eq(a, b)` | `extends GdUnitTestSuite`, fluent `assert_int(x).is_equal(5)` |
| C# support | Minimal | Native |
| Scene runner and input simulation | `simulate`, `InputSender` | `scene_runner()` with `simulate_*` |
| Headless | `-s addons/gut/gut_cmdln.gd` | `runtest.sh`/`.cmd` (needs `--ignoreHeadlessMode`) |

Default to **GUT** for pure-GDScript projects and **GdUnit4** for C# or mixed projects. Install from the in-editor Asset Store (4.7+; Asset Library before that) or from each project's GitHub releases, into `addons/`, then enable the plugin.

## What to Test

- **Pure logic first:** damage formulas, inventory stacking, save migration, state transitions. Put this logic in `RefCounted`/`Resource` classes or static functions so it can be tested without a scene tree.
- **Components:** instantiate one scene (`HealthComponent`), call methods, assert signals.
- **Integration:** load a small test scene, simulate input for N frames or seconds, and assert the outcome (score changed, door opened).
- Don't unit-test the engine (that `move_and_slide` moves) or exact float physics trajectories.

## GUT Examples

```gdscript
# test/unit/test_health_component.gd
extends GutTest

var health: HealthComponent

func before_each() -> void:
    health = HealthComponent.new()
    health.max_health = 10
    add_child_autofree(health)          # calls _ready, freed after the test

func test_damage_reduces_health() -> void:
    health.damage(3)
    assert_eq(health.health, 7)

func test_died_emitted_once_at_zero() -> void:
    watch_signals(health)
    health.damage(20)
    health.damage(5)
    assert_signal_emit_count(health, "died", 1)

func test_health_never_negative() -> void:
    health.damage(999)
    assert_eq(health.health, 0)
```

Integration with input (GUT):
```gdscript
extends GutTest

const Level := preload("res://test/scenes/jump_test.tscn")

func test_player_jumps() -> void:
    var level: Node = add_child_autofree(Level.instantiate())
    var player: CharacterBody2D = level.get_node("%Player")
    await wait_physics_frames(5)                 # let it land
    var start_y := player.global_position.y
    var sender := InputSender.new(Input)
    sender.action_down("jump").hold_for(0.15)
    await wait_seconds(0.3)
    assert_lt(player.global_position.y, start_y, "player should be above start")
    sender.release_all()
    sender.clear()
```

## GdUnit4 Example

```gdscript
# test/test_inventory.gd
extends GdUnitTestSuite

func test_stack_merges() -> void:
    var inv := Inventory.new()
    inv.add(load("res://data/items/potion.tres"), 3)
    inv.add(load("res://data/items/potion.tres"), 2)
    assert_int(inv.count_of(&"potion")).is_equal(5)

func test_player_moves_right() -> void:
    var runner := scene_runner("res://test/scenes/move_test.tscn")
    var player: Node2D = runner.find_child("Player")
    var x0 := player.position.x
    runner.simulate_action_press("move_right")
    await await_millis(500)
    runner.simulate_action_release("move_right")
    assert_float(player.position.x).is_greater(x0)
```

## Running Tests from the Command Line

Import the project once (fresh clone or CI) so class names and UIDs resolve:
```bash
godot --headless --path . --import
```

**GUT:**
```bash
godot --headless --path . -s addons/gut/gut_cmdln.gd -gdir=res://test -ginclude_subdirs -gexit
# Exit code: 0 = all passed, 1 = failures
```
Optional: `-gjunit_xml_file=res://test-results.xml` for CI reports, or a `.gutconfig.json` for shared settings.

**GdUnit4:**
```bash
./addons/gdUnit4/runtest.sh --godot_binary "$(command -v godot)" --headless --ignoreHeadlessMode -a res://test
# Exit codes: 0 = passed, 100 = failures, 103 = refused headless (missing --ignoreHeadlessMode)
```
On Windows use `addons\gdUnit4\runtest.cmd`. Reports go to `reports/` (HTML + JUnit XML).

### Gotchas (verified with Godot 4.7.2, GUT 9.7.1, GdUnit4 6.2.3)
- **Headless clicks:** under `--headless`, simulated mouse clicks reach `_input` but **do not press Buttons**. Run click or UI tests under a virtual display, e.g. `xvfb-run -a godot --path . -s addons/gut/gut_cmdln.gd -gdir=res://test -gcompact_mode -gexit`. Key and action tests work headless.
- **GUT panel:** without `-gcompact_mode`, GUT's results panel can cover the game and block clicks.
- **Timing:** frame counts vary with frame rate. Prefer time waits (`wait_seconds` / `hold_for` in GUT, `await_millis` in GdUnit4) for gameplay.
- **Press and release:** `simulate_action_pressed` (GdUnit4) presses and releases immediately. For held input use `simulate_action_press` → wait → `simulate_action_release`.
- **Action vs event:** `Input.action_press()` does not trigger `_input`/`_unhandled_input`. Event-driven code needs `Input.parse_input_event()` or the framework's key and action simulators.
- **Modifiers:** pass Shift/Ctrl by holding the key with `simulate_key_press`. Modifier booleans on `simulate_key_pressed` are deprecated in GdUnit4 6.2.

## Test Layout and Conventions

```
test/
├── unit/          # no scene tree needed, or tiny
├── integration/   # loads scenes, simulates input
└── scenes/        # minimal fixture scenes used only by tests
```
- Prefix files `test_*.gd` (GUT default) or suffix `*_test.gd` (GdUnit4 default). Keep whichever the project uses.
- Seed randomness (`seed(1234)`) and set fixed physics ticks in tests that touch gameplay.
- Free what you create (`add_child_autofree`, `autofree`, or `auto_free()` in GdUnit4) so orphan warnings stay clean.

## With godot-mcp

Tests run in a separate Godot process, not through the editor bridge. Use the shell commands above (or the plugin's `godot-check` action). Use `godot_runtime_*` tools for exploratory checks, and convert anything worth keeping into a real test.

## CI

See `godot-export-ci` for a GitHub Actions workflow that imports, runs tests, and exports.
