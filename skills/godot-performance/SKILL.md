---
name: godot-performance
description: Profiles and optimizes Godot 4.x games - built-in profiler and monitors, Tracy/Perfetto/Instruments integration (4.6+), GDScript hot-path optimization, object pooling, MultiMesh and server APIs, physics and navigation costs, rendering (draw calls, occlusion, LOD, renderer choice), memory leaks, and threading. Use when the game stutters, has low FPS, long load times, rising memory, or before shipping to mobile or web.
---

# Godot Performance

## Measure Before Changing Anything

1. **Debugger > Profiler** (editor): start it, reproduce the slowdown, and sort by self time. Separate script functions from physics and rendering.
2. **Debugger > Monitors**: FPS, process and physics time, draw calls, objects, nodes, **orphan nodes** (leaks), video memory.
3. **Visual Profiler**: CPU and GPU time per render pass.
4. **External profilers (4.6+):** Tracy, Perfetto and Instruments can profile GDScript, C# and GDExtension. Use them for frame-by-frame spikes the built-in profiler averages away.
5. In code, read the same numbers with `Performance.get_monitor(Performance.TIME_PROCESS)`, `OBJECT_ORPHAN_NODE_COUNT` and `RENDER_TOTAL_DRAW_CALLS_IN_FRAME`, and register custom monitors with `Performance.add_custom_monitor()`.
6. Always profile an **exported release build** on the target device before concluding. The editor and debug builds are slower.

Set a budget: 16.6 ms per frame at 60 FPS (8.3 ms at 120). Find which part (script, physics, render, GPU) is over budget.

## GDScript Hot Paths

- **Static typing** enables faster typed instructions. Type every variable, argument and return in hot code.
- Cache lookups: `@onready var sprite: Sprite2D = $Sprite2D`, not `get_node()` every frame. Cache `get_tree().get_nodes_in_group()` results when the set is stable.
- Avoid per-frame allocations in loops: reuse Arrays (`clear()`), prefer `PackedVector2Array`/`PackedFloat32Array` for bulk numbers, and avoid building strings every frame.
- Turn off what isn't needed: `set_process(false)` / `set_physics_process(false)` on idle entities; use `VisibleOnScreenNotifier2D/3D` (or `VisibleOnScreenEnabler`) to pause off-screen actors.
- Use Timers or a `_process` accumulator for logic that doesn't need every frame (AI repath at 5 Hz).
- Signals and `call_group` are fine for events. Don't emit signals per entity per frame.
- Use `distance_squared_to` instead of `distance_to` for comparisons.
- Move heavy pure computation (procgen, pathfinding batches) to `WorkerThreadPool.add_task()`, and touch the scene tree only on the main thread (`call_deferred`).

## Object Pooling

Instantiating and freeing many nodes per second (bullets, particles, damage numbers) causes spikes:
```gdscript
class_name Pool
extends Node

@export var scene: PackedScene
@export var size := 64
var _free: Array[Node] = []

func _ready() -> void:
    for i in size:
        var n := scene.instantiate()
        n.process_mode = Node.PROCESS_MODE_DISABLED
        n.hide()
        add_child(n)
        _free.append(n)

func acquire() -> Node:
    if _free.is_empty():
        return null            # or grow
    var n: Node = _free.pop_back()
    n.process_mode = Node.PROCESS_MODE_INHERIT
    n.show()
    return n

func release(n: Node) -> void:
    n.process_mode = Node.PROCESS_MODE_DISABLED
    n.hide()
    _free.append(n)
```

## Many Objects

| Situation | Use |
|-----------|-----|
| Thousands of identical meshes or sprites (grass, bullets, crowds) | `MultiMeshInstance2D/3D`, updating transforms in a `PackedFloat32Array` buffer |
| Thousands of simple bullets with collision | Server APIs: `PhysicsServer2D` areas + `RenderingServer` canvas items, no nodes |
| Particles | `GPUParticles*` (GPU) over `CPUParticles*` except on the Compatibility renderer or for very few particles |
| Big tile worlds | `TileMapLayer` (chunked internally). Avoid thousands of individual Sprite2D nodes |

## Physics Costs

- Prefer primitive shapes (circle, capsule, box) over polygons and trimesh. Use convex decomposition for dynamic 3D objects.
- Restrict layers and masks so broadphase pairs stay low.
- Lower `physics_ticks_per_second` only if gameplay tolerates it, and enable physics interpolation for smoothness.
- 3D: Jolt (default in new 4.6+ projects) scales better with many bodies. Let bodies sleep (`can_sleep`).
- Areas with `monitoring` on and big shapes overlapping many bodies are expensive. Turn off monitoring when not needed.

## Rendering

- **Pick the renderer for the target:** Forward+ (desktop, high-end), Mobile (mobile and VR), Compatibility (web, old GPUs). Per-platform overrides are in Project Settings > Rendering > Renderer.
- **Draw calls (2D):** batching works when consecutive items share texture and material. Use texture atlases and avoid unique materials per sprite.
- **3D:** enable occlusion culling (`OccluderInstance3D` + bake) for indoor levels; enable mesh LOD (on import) and `visibility_range` for distant objects.
- **Lights and shadows:** limit shadow-casting lights, reduce `shadow_atlas` sizes, and use baked lighting (LightmapGI) on static scenes. 4.7's `AreaLight3D` is more expensive than point and spot lights, so use it sparingly on mobile.
- **Post-processing:** SSAO, SSR, SSIL, volumetric fog and glow are costly. Expose them as quality settings. 4.6 has an optional half-size SSR.
- **Resolution scaling:** `scaling_3d_mode` (FSR 2.2, MetalFX on Apple, 4.4+) and `scaling_3d_scale` for GPU-bound 3D.
- **First-frame shader stutter:** 4.5+ shader baker at export, plus warm-up by rendering materials once behind a loading screen.

## Memory and Leaks

- Watch **orphan nodes** in Monitors. A rising count means nodes removed with `remove_child` but never freed, so use `queue_free()`.
- `Print Stray Nodes`: `Node.print_orphan_nodes()` in debug builds.
- 4.6+ **ObjectDB snapshots** in the debugger compare live objects between two moments to find leaks.
- RefCounted cycles (A holds B, B holds A) never free. Break them with `WeakRef` or explicit cleanup.
- Large textures: use VRAM compression, mipmaps for 3D, and size limits for mobile.

## Loading

- Use `ResourceLoader.load_threaded_request()` for level loads, with a loading screen.
- Prefer `preload` for small, always-needed resources and threaded `load` for large optional ones.
- Keep autoload `_ready` light. Heavy autoload work delays the first frame.

## Platform Budgets (rule of thumb)

| Target | Draw calls/frame | Notes |
|--------|------------------|-------|
| Desktop | 2,000–5,000 | Forward+ |
| Mobile | 100–300 | Mobile renderer, few dynamic lights, no SSR or SSAO |
| Web | 100–500 | Compatibility, single-threaded by default |

## Workflow with godot-mcp

1. `godot_editor_run_scene` → reproduce the slowdown.
2. `godot_editor_execute_gdscript` cannot read the running game's monitors (it runs in the editor). Add a debug overlay autoload that prints `Performance.get_monitor()` values, then read them with `godot_editor_get_output`.
3. Change one thing, re-measure, and keep notes of before and after numbers in the response.
