---
name: godot-animation
description: Animates Godot 4.x games - AnimationPlayer clips and libraries, AnimationTree state machines and blend spaces, sprite animation, Tweens (including 4.4 subtweens and 4.7 tween_await), animation sections and markers, skeletal 3D animation, retargeting, and the 4.6 IK framework (TwoBoneIK3D, FABRIK3D, CCDIK3D, SplineIK3D). Use for character animation, UI motion, cutscenes, procedural motion, or wiring animation to gameplay state. Pairs with godot-mcp godot_animation_* tools.
---

# Godot Animation

## Choose the Tool

| Need | Use |
|------|-----|
| Fire-and-forget motion from code (UI pop, knockback, fade) | `Tween` (`create_tween()`) |
| Authored clips (walk cycle, door, cutscene) | `AnimationPlayer` |
| Frame-by-frame 2D sprites | `AnimatedSprite2D` + `SpriteFrames`, or AnimationPlayer keying `Sprite2D.frame` |
| Blending and state logic (idle↔run↔jump, 8-way movement) | `AnimationTree` with state machine or blend space |
| Procedural bone aiming, foot placement, reaching | `SkeletonModifier3D` family (IK, LookAt, constraints) |

## godot-mcp Animation Tools

| Task | Tool |
|------|------|
| Add AnimationPlayer/AnimationTree scaffolding to a scene | `godot_animation_setup_scene` |
| Create, list or read clips | `godot_animation_create_clip`, `godot_animation_list_clips`, `godot_animation_read_clip` |
| Add or remove keys | `godot_animation_add_keyframe`, `godot_animation_remove_keyframe` |
| Plan an AnimationTree state machine or blend space | `godot_animation_build_state_machine_plan`, `godot_animation_build_blend_space_plan` |

Use `godot_help tool="<name>"` for argument templates. Validate with `godot_validate_scene`, then run the scene to see the motion. Scene-tree evidence alone doesn't prove an animation looks right; use a runtime screenshot or a manual check (see `godot-interactive`).

## AnimationPlayer

- Clips live in **AnimationLibraries**. The default library has the empty name `""`, so `play("walk")` is short for `play("/walk")`, and other libraries are `play("combat/slash")`.
- Track paths are relative to `root_node` (default `..`, the player's parent): `NodePath("Sprite2D:frame")`, `NodePath(".:position")`.
- Keep a `RESET` animation with every animated property's rest value. The editor uses it to restore state and to avoid dirty scene diffs.
- Call methods from **Call Method** tracks (footstep sounds, spawn hitbox) instead of polling time in code.
- Play by **section or markers** (4.4+): `play_section_with_markers("attack", &"windup_end", &"recover_start")` to loop or skip part of a clip.
- `animation_finished(anim_name)` fires for non-looping clips. 4.7 renamed the `current_animation_changed` argument to `anim_name`; connect by Callable so the change doesn't matter.
- 4.6: `get_queue()` returns `Array[StringName]`, and `is_animation_active()` was added.

```gdscript
@onready var anim: AnimationPlayer = $AnimationPlayer

func attack() -> void:
    anim.play("attack")
    await anim.animation_finished
    anim.play("idle")
```

## AnimationTree

```
AnimationTree (anim_player = ../AnimationPlayer, active = true)
└── tree_root: AnimationNodeStateMachine
    ├── Locomotion: AnimationNodeBlendSpace2D (idle/walk/run by velocity)
    ├── Jump, Fall, Land
    └── Attack (OneShot via AnimationNodeBlendTree)
```

```gdscript
@onready var tree: AnimationTree = $AnimationTree
@onready var playback: AnimationNodeStateMachinePlayback = tree.get("parameters/playback")

func _physics_process(_delta: float) -> void:
    tree.set("parameters/Locomotion/blend_position", velocity / max_speed)
    if not is_on_floor() and velocity.y > 0.0:
        playback.travel("Fall")
```

- Parameter paths come from the tree. Hover a parameter in the inspector to copy its exact path.
- Use transition **advance conditions** or expressions (`advance_expression`) for data-driven transitions, and `travel()` for code-driven ones.
- For one-shots (attacks, hits), set `parameters/<OneShot>/request` to `AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE`.
- `AnimationNodeExtension` (4.4, experimental) lets you write custom blend nodes in GDScript.

## Tweens

```gdscript
var t := create_tween().set_trans(Tween.TRANS_BACK).set_ease(Tween.EASE_OUT)
t.tween_property(self, "scale", Vector2.ONE * 1.2, 0.12)
t.tween_property(self, "scale", Vector2.ONE, 0.12)

# Parallel steps
t = create_tween().set_parallel()
t.tween_property(sprite, "modulate:a", 0.0, 0.3)
t.tween_property(sprite, "position:y", sprite.position.y - 20.0, 0.3)
t.chain().tween_callback(queue_free)

# 4.4+: nest a reusable tween
var shake := create_tween()
for i in 4:
    shake.tween_property(camera, "offset", Vector2(randf_range(-6, 6), randf_range(-6, 6)), 0.03)
var seq := create_tween()
seq.tween_subtween(shake)
seq.tween_property(camera, "offset", Vector2.ZERO, 0.05)

# 4.4+: keep animating while Engine.time_scale is slowed (hit-stop, UI during slow-mo)
create_tween().set_ignore_time_scale().tween_property(ui, "modulate:a", 1.0, 0.2)

# 4.7+: pause a sequence until a signal fires
var intro := create_tween()
intro.tween_property(title, "modulate:a", 1.0, 0.5)
intro.tween_await(dialogue_box.closed)
intro.tween_property(title, "modulate:a", 0.0, 0.5)
```

Rules:
- Tweens bound by `create_tween()` on a node die with that node. Kill the previous tween before starting a conflicting one: `if _t and _t.is_valid(): _t.kill()`.
- Paused trees pause tweens unless `set_pause_mode(Tween.TWEEN_PAUSE_PROCESS)`.
- Use `set_process_mode(Tween.TWEEN_PROCESS_PHYSICS)` for tweens that move physics bodies.

## 3D Skeletal Animation

- Import animations from glTF (`.glb`). Set loop modes and split clips in the Advanced Import dialog, not after import.
- **Retargeting:** use a `SkeletonProfileHumanoid` BoneMap on import to share animations between humanoid models. `RetargetModifier3D` (4.4+) copies poses between skeletons at runtime.
- **SkeletonModifier3D stack** (children of `Skeleton3D`, processed in order):
  - `LookAtModifier3D` (4.4+): head and eye tracking with angle limits.
  - `SpringBoneSimulator3D` (4.4+): hair, tails, cloth-like jiggle, with `SpringBoneCollision*3D`.
  - `AimModifier3D`, `CopyTransformModifier3D`, `ConvertTransformModifier3D` (4.5+): bone constraints.
  - **IK (4.6+):** `TwoBoneIK3D` (arms and legs, deterministic), `FABRIK3D`/`CCDIK3D`/`JacobianIK3D` (iterative chains), `SplineIK3D` (spines and tentacles along a `Path3D`), with `JointLimitationCone3D` limits and `BoneTwistDisperser3D` and `LimitAngularVelocityModifier3D` for natural results. The old `SkeletonIK3D` is deprecated in favor of these.
  - `ModifierBoneTarget3D` (4.5+): a Node3D that follows a bone, useful as an IK target or attachment.
- Foot IK recipe: raycast down from each foot, move a target Marker3D to the hit point, drive `TwoBoneIK3D` for each leg, and offset the hips by the lowest foot delta.

## Debugging

1. A clip plays but nothing moves: the track path is wrong relative to `root_node`, or an AnimationTree is active and overriding the player.
2. A property snaps back: another track or RESET keys the same property, or a tween and an animation fight over it.
3. A state machine is stuck: check transition conditions and the `switch_mode`, and watch `playback.get_current_node()`.
4. Jitter in 3D: enable physics interpolation, or animate in the same process mode as the movement.
