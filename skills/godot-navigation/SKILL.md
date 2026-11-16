---
name: godot-navigation
description: Builds Godot 4.x pathfinding and enemy AI movement - NavigationRegion2D/3D baking, NavigationAgent2D/3D path following, avoidance, NavigationLink jumps and doors, TileMapLayer navigation, AStarGrid2D for grid games, and simple AI behaviors (chase, patrol, flee). Use when enemies or NPCs need to move around obstacles, when paths are wrong, or when baking navmeshes. Pairs with godot-mcp godot_navigation_* tools.
---

# Godot Navigation

## Choose an Approach

| Game | Use |
|------|-----|
| Free movement in 2D/3D levels | `NavigationRegion2D/3D` (navmesh) + `NavigationAgent2D/3D` |
| Tile-based levels with irregular walkable areas | TileSet navigation layers on `TileMapLayer` (agents work the same) |
| Strict grid movement (tactics, roguelikes, puzzles) | `AStarGrid2D`: simpler and deterministic |
| Graph of waypoints (rails, rooms) | `AStar2D/3D` |

## godot-mcp Navigation Tools

| Task | Tool |
|------|------|
| Add or configure a region | `godot_navigation_add_region`, `godot_navigation_configure_region` |
| Add or configure an agent on an actor | `godot_navigation_add_agent`, `godot_navigation_configure_agent` |
| Off-mesh connections (jumps, ladders, teleporters) | `godot_navigation_add_link` |
| Produce a bake plan (parsed geometry, cell size, agent radius) | `godot_navigation_build_bake_plan` |
| Check that key points are connected | `godot_navigation_validate_paths` |
| List navigation nodes in a scene | `godot_navigation_list_nodes` |

Baking itself happens in the editor (select the region, then Bake) or at runtime with `bake_navigation_polygon()` / `bake_navigation_mesh()`. After file edits, open the scene live and bake, or bake at runtime on level load.

## Navmesh Setup Rules

- Set the **agent radius** in the NavigationPolygon/NavigationMesh to the actor's collision radius, so baked edges keep actors off walls.
- Keep `cell_size` equal across the region resources and the map (Project Settings `navigation/2d|3d/default_cell_size`). 4.6 warns on mismatch (`navigation/*/warnings/navmesh_cell_size_mismatch`).
- 2D baking parses collision shapes or meshes from `source_geometry_group_name` / child nodes. Make sure walls are in the parsed group or under the region.
- Adjacent regions connect only when their edges overlap within `edge_connection_margin`.
- Re-bake after level geometry changes. For runtime-generated levels, bake on a thread (`bake_navigation_polygon(true)`) and wait for `bake_finished`.

## Agent Following a Path

```gdscript
extends CharacterBody2D

@export var speed := 120.0
@onready var agent: NavigationAgent2D = $NavigationAgent2D

func _ready() -> void:
    agent.velocity_computed.connect(_on_velocity_computed)
    # The map isn't synced on the first frame; wait one physics frame before querying.
    await get_tree().physics_frame
    agent.target_position = global_position

func chase(target: Node2D) -> void:
    agent.target_position = target.global_position

func _physics_process(_delta: float) -> void:
    if agent.is_navigation_finished():
        velocity = Vector2.ZERO
        move_and_slide()
        return
    var next := agent.get_next_path_position()
    var desired := global_position.direction_to(next) * speed
    if agent.avoidance_enabled:
        agent.velocity = desired          # result arrives in velocity_computed
    else:
        _on_velocity_computed(desired)

func _on_velocity_computed(safe_velocity: Vector2) -> void:
    velocity = safe_velocity
    move_and_slide()
```

Agent tips:
- Don't set `target_position` every frame for a moving target. Repath on a Timer (0.2–0.5 s) or when the target has moved more than a threshold.
- Tune `path_desired_distance` and `target_desired_distance`: too small and agents orbit waypoints, too large and they cut corners.
- **Avoidance** (RVO) only avoids other agents and obstacles, not walls; the navmesh handles walls. Use `NavigationObstacle2D/3D` for dynamic blockers, and use `avoidance_layers`/`avoidance_mask` to group crowds.
- `navigation_layers` on the agent must match a layer of the regions it should use (for example, flying units on a separate layer).

## Grid Pathfinding with AStarGrid2D

```gdscript
var astar := AStarGrid2D.new()

func build(layer: TileMapLayer) -> void:
    astar.region = layer.get_used_rect()
    astar.cell_size = layer.tile_set.tile_size
    astar.diagonal_mode = AStarGrid2D.DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES
    astar.update()
    for cell in layer.get_used_cells():
        var data := layer.get_cell_tile_data(cell)
        if data and data.get_custom_data("solid"):
            astar.set_point_solid(cell, true)

func path(from_cell: Vector2i, to_cell: Vector2i) -> Array[Vector2i]:
    return astar.get_id_path(from_cell, to_cell)
```
Convert cells with `layer.map_to_local(cell)` / `layer.local_to_map(pos)`. Call `update()` after changing `region`, `cell_size` or `diagonal_mode`, but not after `set_point_solid`.

## Simple AI Behaviors

Combine navigation with a small state machine (see `godot-code-gen`):
- **Patrol:** cycle `target_position` through `Marker2D` waypoints, and switch to the next on `navigation_finished`.
- **Chase:** repath on a timer while the player is inside a detection `Area2D` **and** a line-of-sight raycast hits the player first.
- **Flee:** target `global_position + (global_position - threat.global_position).normalized() * distance`, then snap to the navmesh with `NavigationServer2D.map_get_closest_point(agent.get_navigation_map(), point)`.
- **Give up:** if `agent.is_target_reachable()` is false, or the path length exceeds a limit, return to patrol.

For larger AI, use behavior trees (addons such as LimboAI or Beehave) instead of growing one enormous state machine.

## Debugging

1. Turn on Debug > Visible Navigation to see the navmesh and agent paths.
2. The agent doesn't move: there is no baked polygon, the agent's `navigation_layers` don't overlap the region, or the target was set before the map synced (wait one physics frame).
3. Paths go through walls: the walls weren't included in the bake source geometry, so re-bake.
4. Agents jitter at corners: increase `path_desired_distance`, or enable path postprocessing (`PATH_POSTPROCESSING_EDGECENTERED`/corridor funnel).
5. 4.6+ can swap navigation engines (`navigation/2d|3d/navigation_engine`). Keep the default unless a plugin requires another.
