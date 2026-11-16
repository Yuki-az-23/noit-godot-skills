---
name: godot-physics
description: Implements Godot 4.x 2D and 3D physics - CharacterBody, RigidBody, StaticBody, AnimatableBody, Area triggers, collision layers and masks, raycasts and shape queries, Jolt Physics (default for new 3D projects since 4.6), physics interpolation, and common collision bugs. Use for movement controllers, hit detection, projectiles, platforms, ragdolls, or "my collision doesn't work" problems.
---

# Godot Physics

## Pick the Body Type

| Body | Moved by | Use for |
|------|----------|---------|
| `CharacterBody2D/3D` | Your code (`velocity` + `move_and_slide()`) | Players, enemies, NPCs |
| `RigidBody2D/3D` | The physics engine (forces, impulses) | Crates, debris, balls, ragdoll parts |
| `StaticBody2D/3D` | Nothing (or `constant_linear_velocity` for conveyors) | Walls, floors |
| `AnimatableBody2D/3D` | Animation or code, pushes others correctly | Moving platforms, doors, elevators |
| `Area2D/3D` | Not a solid body: detects overlap | Triggers, pickups, hit/hurt boxes, gravity zones |

Every body and area needs at least one `CollisionShape*` or `CollisionPolygon*` child with a shape. A missing shape is the most common reason for "nothing collides".

## Collision Layers and Masks

- **Layer:** what the object *is*. **Mask:** what it *detects or collides with*.
- Two bodies collide if A's mask contains B's layer **or** B's mask contains A's layer. Areas detect only what is in their own mask.
- Layers are numbered 1–32 in the editor and code helpers, but stored as bitmasks: layer *n* = `1 << (n - 1)`.

```gdscript
set_collision_layer_value(2, true)    # 1-based layer number
set_collision_mask_value(1, true)
collision_mask = 0b100101             # layers 1, 3, 6
```

Name layers in Project Settings > Layer Names > 2D/3D Physics. A standard plan:

| # | Name | Typical mask |
|---|------|-------------|
| 1 | world | — |
| 2 | player | world, enemy, pickup, trigger |
| 3 | enemy | world, player |
| 4 | player_attack | enemy_hurtbox |
| 5 | enemy_attack | player_hurtbox |
| 6 | pickup | — |
| 7 | trigger | — |
| 8 | player_hurtbox / 9 enemy_hurtbox | — |

## CharacterBody Essentials

```gdscript
extends CharacterBody2D

@export var speed := 220.0
@export var jump_velocity := -420.0
@export var coyote_time := 0.1
@export var jump_buffer := 0.1

var _coyote := 0.0
var _buffer := 0.0

func _physics_process(delta: float) -> void:
    if is_on_floor():
        _coyote = coyote_time
    else:
        _coyote -= delta
        velocity += get_gravity() * delta

    _buffer = jump_buffer if Input.is_action_just_pressed("jump") else _buffer - delta
    if _buffer > 0.0 and _coyote > 0.0:
        velocity.y = jump_velocity
        _buffer = 0.0
        _coyote = 0.0
    if Input.is_action_just_released("jump") and velocity.y < 0.0:
        velocity.y *= 0.5            # variable jump height

    var dir := Input.get_axis("move_left", "move_right")
    velocity.x = move_toward(velocity.x, dir * speed, speed * 10.0 * delta)
    move_and_slide()

    for i in get_slide_collision_count():
        var col := get_slide_collision(i)
        if col.get_collider() is RigidBody2D:
            (col.get_collider() as RigidBody2D).apply_central_impulse(-col.get_normal() * 40.0)
```

Settings worth knowing:
- `motion_mode`: Grounded for platformers, Floating for top-down and space games.
- `floor_max_angle`, `floor_snap_length` (stick to slopes and stairs), `floor_stop_on_slope`, `floor_constant_speed`.
- `up_direction` must match your gravity. The default is `Vector2.UP` / `Vector3.UP`.
- `platform_on_leave` controls the velocity inherited when jumping off moving platforms.
- `get_gravity()` (4.3+) includes Area gravity overrides. Prefer it to reading the project setting.

## RigidBody Essentials

- Apply forces in `_physics_process` or `_integrate_forces(state)`. Never set `position` directly on an active RigidBody; use `PhysicsServer` or teleport inside `_integrate_forces` via `state.transform`.
- Impulses (`apply_impulse`, `apply_central_impulse`) are one-off; forces (`apply_force`, `constant_force`) are continuous.
- Enable `contact_monitor` and set `max_contacts_reported > 0` to receive `body_entered`.
- Fast small objects: enable `continuous_cd` (CCD), or use a raycast or ShapeCast instead.
- Use `freeze` + `freeze_mode` (Static or Kinematic) to disable simulation temporarily.

## Areas

```gdscript
extends Area2D   # hurtbox

signal hit(damage: int, from: Node)

func _ready() -> void:
    area_entered.connect(_on_area_entered)

func _on_area_entered(area: Area2D) -> void:
    if area.has_method("get_damage"):
        hit.emit(area.get_damage(), area.owner)
```

- `body_entered` reports PhysicsBodies and TileMapLayer collisions; `area_entered` reports Areas.
- Toggle `monitoring`/`monitorable` with `set_deferred()` while inside a physics callback. Direct changes during a flush cause errors.
- An Area can override gravity (`gravity_space_override`), damping and wind for bodies inside it.

## Queries

```gdscript
# Node-based (simple, persistent)
@onready var ground_ray: RayCast2D = $GroundRay
if ground_ray.is_colliding(): print(ground_ray.get_collider())

# Immediate query (one-off, from _physics_process)
var space := get_world_2d().direct_space_state
var q := PhysicsRayQueryParameters2D.create(global_position, target, collision_mask, [get_rid()])
var hit := space.intersect_ray(q)
if hit: print(hit.collider, hit.position, hit.normal)

# Shape overlap
var circle := CircleShape2D.new()
circle.radius = 64.0
var sq := PhysicsShapeQueryParameters2D.new()
sq.shape = circle
sq.transform = global_transform
sq.collision_mask = 1 << 2   # layer 3
var results := space.intersect_shape(sq, 16)
```

3D equivalents: `get_world_3d().direct_space_state`, `PhysicsRayQueryParameters3D`, `RayCast3D`, `ShapeCast3D`. Mouse picking in 3D: `camera.project_ray_origin(mouse)` + `project_ray_normal(mouse)`.

## Jolt Physics (3D)

- Jolt is the **default 3D engine for new projects since 4.6**. Existing projects keep their setting: `physics/3d/physics_engine` (`Jolt Physics` or `GodotPhysics3D`).
- Jolt gives better stacking stability and performance. Differences to check when switching:
  - Some joint and soft-body parameters behave differently.
  - **4.7 change:** with Jolt, `WorldBoundaryShape3D.plane.d` now follows Godot's sign convention, so flip the sign if you tuned it on 4.6 Jolt.
  - Prefer convex shapes and primitives; trimesh (concave) shapes only for static geometry.
- 2D always uses Godot Physics 2D.

## Physics Interpolation

Enable `physics/common/physics_interpolation` for smooth motion when the render rate exceeds the physics tick (high-refresh monitors). With it on:
- Move physics objects only in `_physics_process`.
- Call `reset_physics_interpolation()` after teleporting a node.
- `Node3D.get_global_transform_interpolated()` (4.4+) gives the rendered transform, for example for a camera following a body.

## Debugging Checklist

1. Debug > Visible Collision Shapes: are the shapes where you expect, and the right size?
2. Layers/masks: does at least one side's mask include the other's layer?
3. Is the shape `disabled`, or is the Area's `monitoring` off?
4. Is the node scaled non-uniformly? Scale the shape resource instead of the body.
5. Tunneling: raise `physics/common/physics_ticks_per_second`, enable CCD, or use ray or shape casts.
6. Jittery CharacterBody on slopes: tune `floor_snap_length` and enable `floor_constant_speed`.
7. Use `godot_editor_run_scene` + `godot_editor_get_errors` to catch "flushing queries" errors (use `set_deferred`/`call_deferred`).
