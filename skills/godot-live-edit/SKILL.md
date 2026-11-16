---
name: godot-live-edit
description: Lightweight guidance for driving a running Godot 4.x editor through the AI Bridge plugin and godot-mcp: connect, inspect the scene tree, add or modify nodes, run scenes, read errors. Use for quick one-off live edits; prefer godot-interactive for longer inspect-edit-run-verify sessions.
---

# Godot Live Edit Skill

You are an expert at using the Godot AI Bridge to control a running Godot editor in real-time. This skill guides you through live editing workflows.

## Connection Workflow

### Step 1: Connect to Godot
```
First, ensure:
1. Godot 4.x is running with your project open
2. The godot-ai-bridge plugin is installed and enabled
3. The plugin shows "AI Bridge listening on port 6550" in output

Then use: godot_connect
```

### Step 2: Verify Connection
```
Use: godot_connection_status

Expected response:
{
  "connected": true,
  "port": 6550,
  "projectPath": "/path/to/project"
}
```

### Step 3: Explore the Scene
```
Use: godot_editor_get_scene_tree

This shows all nodes in the current scene with their types and hierarchy.
```

## Common Live Edit Operations

### Adding UI Elements
```
To add a health bar:

1. godot_editor_add_node
   - parentPath: "HUD" (or ".")
   - name: "HealthBar"
   - type: "ProgressBar"
   - properties: { "value": 100, "max_value": 100 }

2. godot_editor_modify_node
   - nodePath: "HUD/HealthBar"
   - properties: {
       "position": {"_type": "Vector2", "x": 20, "y": 20},
       "size": {"_type": "Vector2", "x": 200, "y": 30}
     }
```

### Modifying Node Properties
```
To reposition a player:

godot_editor_modify_node
- nodePath: "Player"
- properties: {
    "position": {"_type": "Vector2", "x": 100, "y": 200},
    "scale": {"_type": "Vector2", "x": 2, "y": 2}
  }
```

### Inspecting Nodes
There is no dedicated "get properties" tool. Read values with a short editor-side query:
```
godot_editor_execute_gdscript
- code: "var n = editor_interface.get_edited_scene_root().get_node('Player'); return {'position': n.position, 'scale': n.scale, 'visible': n.visible}"
```
For the full serialized state of a saved scene, use `godot_list_scene_nodes` (cheap) or `godot_read_scene` (full .tscn).

### Building Scene Hierarchies
```
To create a character scene structure:

1. Root: godot_editor_add_node (parentPath: ".", type: CharacterBody2D, name: Player)
2. Sprite: godot_editor_add_node (parentPath: "Player", type: Sprite2D)
3. Collision: godot_editor_add_node (parentPath: "Player", type: CollisionShape2D)
4. Camera: godot_editor_add_node (parentPath: "Player", type: Camera2D)

A CollisionShape2D needs a `shape` resource. Assign it in the editor, or build the scene with file tools where sub-resources are easy to express.
```

### Running and Testing
```
Test your changes:

1. godot_editor_save_scene  - Save current work
2. godot_editor_run_scene   - Run and test
3. godot_editor_stop_scene  - Stop when done
4. godot_editor_get_errors  - Check for issues
```

## Property Type Formatting

When modifying properties via live editing, use these JSON formats:

### Vector2
```json
{
  "_type": "Vector2",
  "x": 100.0,
  "y": 200.0
}
```

### Vector3
```json
{
  "_type": "Vector3",
  "x": 1.0,
  "y": 2.0,
  "z": 3.0
}
```

### Color
```json
{
  "_type": "Color",
  "r": 1.0,
  "g": 0.5,
  "b": 0.0,
  "a": 1.0
}
```

### Simple Values
```json
{
  "visible": true,
  "rotation": 1.57,
  "speed": 200.0,
  "text": "Hello World"
}
```

## Workflow Patterns

### Iterative UI Design
```
1. Connect to editor
2. Get current scene tree
3. Add container nodes (VBoxContainer, HBoxContainer)
4. Add UI elements (Label, Button, ProgressBar)
5. Adjust positions/sizes with modify_node
6. Run scene to preview
7. Iterate until satisfied
8. Save scene
```

### Level Building
```
1. Connect to editor
2. Instantiate pre-made scenes (see Scene Management below)
3. Position them with modify_node
4. Duplicate nodes as needed
5. Run to test gameplay
6. Adjust and iterate
```

### Debugging
```
1. Connect to editor
2. Run scene
3. Use get_errors to check for problems
4. Execute GDScript to inspect runtime state:
   godot_editor_execute_gdscript
   - code: "return get_tree().current_scene.get_node('Player').position"
5. Stop scene
6. Fix issues
```

## Best Practices

1. **Always save before running** - `godot_editor_save_scene` first
2. **Work incrementally** - Add one node, verify, then continue
3. **Use descriptive names** - "PlayerHealthBar" not "ProgressBar2"
4. **Check the scene tree** - Use `godot_editor_get_scene_tree` to verify structure
5. **Inspect before modifying** - Read current values with a short `godot_editor_execute_gdscript` query
6. **Use undo if needed** - All operations support Ctrl+Z in the editor
7. **Refresh filesystem** - After external file changes, use `godot_editor_refresh_filesystem`

## Error Handling

Common issues:

| Error | Cause | Solution |
|-------|-------|----------|
| "Not connected" | Plugin not running | Start Godot, enable plugin |
| "Node not found" | Wrong path | Use get_scene_tree to find correct path |
| "No scene open" | No scene loaded | Open a scene in Godot first |
| "Parent not found" | Invalid parent path | Check parent exists in tree |
| "Failed to create node" | Invalid node type | Verify type name (case-sensitive) |

## Finding Node Types

There is no node-type listing tool. Use the docs tools instead:
```
godot_list_documented_classes          # classes the server documents
godot_search_docs   - query: "progress bar"
godot_get_class_docs - className: "TextureProgressBar"
```
Type names are case-sensitive (`CharacterBody2D`, not `characterbody2d`).

## Scene Management

```
# List scenes in the project (file tool)
godot_list_scenes

# Open a different scene
godot_editor_open_scene
- scenePath: "res://scenes/main_menu.tscn"

# Save the open scene
godot_editor_save_scene
```

There is no "save as" or "instantiate scene" tool. Instance a packed scene under a live parent with an editor-side script, then save:
```
godot_editor_execute_gdscript
- code: |
    var root = editor_interface.get_edited_scene_root()
    var inst = load("res://scenes/enemy.tscn").instantiate()
    inst.name = "Enemy1"
    root.get_node("Enemies").add_child(inst)
    inst.owner = root   # without this the node is not saved
    return str(root.get_path_to(inst))
```
To create a new scene file, write it with `godot_write_scene` (or copy an existing .tscn), then `godot_editor_refresh_filesystem` and `godot_editor_open_scene`.

## Tool Surface Changes

Older notes may mention `godot_editor_get_node_properties`, `godot_editor_get_node_types`, `godot_editor_list_assets_by_type`, `godot_editor_save_scene_as`, or `godot_editor_instantiate_scene`. None of these exist in current godot-mcp. Call `godot_help` when unsure.
