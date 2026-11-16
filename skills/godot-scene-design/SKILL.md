---
name: godot-scene-design
description: Designs Godot 4.x scenes and .tscn files: node hierarchies, scene composition, collision layer plans, groups, instancing, and procedural level layouts. Use when creating or restructuring scenes, choosing node types, writing .tscn text by hand, or generating dungeons, tilemaps, or enemy waves.
---

# Godot Scene Design Skill

You are an expert at designing and creating Godot 4.x scenes (.tscn files), node hierarchies, and level layouts.

## Scene File Format (TSCN)

Godot uses a text-based scene format that's highly readable and AI-friendly.

### Basic Structure (as saved by Godot 4.6+)
```ini
[gd_scene format=3 uid="uid://b8x2k4v1qnm3p"]

[ext_resource type="Script" uid="uid://c4ylq0s2m1t8a" path="res://scripts/player.gd" id="1_abc"]
[ext_resource type="Texture2D" uid="uid://dj3w5n7r0p2kq" path="res://sprites/player.png" id="2_def"]

[sub_resource type="CircleShape2D" id="CircleShape2D_xyz"]
radius = 16.0

[sub_resource type="RectangleShape2D" id="RectangleShape2D_hit"]
size = Vector2(24, 32)

[node name="Player" type="CharacterBody2D" unique_id=1840563921]
collision_layer = 2
collision_mask = 37
script = ExtResource("1_abc")
speed = 200.0

[node name="Sprite2D" type="Sprite2D" parent="." unique_id=902314567]
texture = ExtResource("2_def")

[node name="CollisionShape2D" type="CollisionShape2D" parent="." unique_id=377120458]
shape = SubResource("CircleShape2D_xyz")

[node name="Hitbox" type="Area2D" parent="." unique_id=1203398841]

[node name="CollisionShape2D" type="CollisionShape2D" parent="Hitbox" unique_id=640021987]
shape = SubResource("RectangleShape2D_hit")

[connection signal="body_entered" from="Hitbox" to="." method="_on_hitbox_body_entered"]
```

### Key Sections
1. **Header**: `[gd_scene format=3 uid="uid://..."]`. Godot 4.0–4.5 also wrote `load_steps=N` (number of resources + 1). 4.6+ no longer writes it, and either form loads in any 4.x version.
2. **External resources**: `[ext_resource]` for scripts, textures and scenes. The `uid` attribute is optional when hand-writing; Godot fills it in on the next save.
3. **Sub-resources**: inline resources such as shapes, materials, animations and curves. Declare them before any node that uses them.
4. **Nodes**: the first node has no `parent`. Direct children use `parent="."`, deeper nodes use a path relative to the root (`parent="Hitbox"`).
5. **Connections**: `[connection signal=... from=... to=... method=...]`. The signal must exist on the `from` node: a body has no `body_entered` signal, but an `Area2D` does.

### Hand-Writing Rules
- **Comments:** .tscn has no inline `#` comments. Keep explanations out of the file.
- **Bitmasks:** `collision_layer` and `collision_mask` are integers. Layers 1, 3 and 6 are `1 + 4 + 32 = 37`, so write `collision_mask = 37`, not `1 | 3 | 6`.
- **Unique IDs (4.6+):** `unique_id=` is written by the editor. When hand-writing you may omit it, and Godot assigns IDs on the next save. Never copy the same `unique_id` to two nodes.
- **Saved values:** properties equal to their default are not saved. Don't expect them in the file.
- **Prefer tools over raw text:** use `godot_add_node`/`godot_modify_node` and `godot_validate_scene` when godot-mcp is available, and only write raw text for new files.

## Common Scene Patterns

### Player Character (2D Platformer)
```
Player (CharacterBody2D)
├── Sprite2D
├── CollisionShape2D
├── AnimationPlayer
├── Camera2D
│   └── (smooth follow settings)
├── Hitbox (Area2D)
│   └── CollisionShape2D
└── RayCast2D (ground detection)
```

### Player Character (3D)
```
Player (CharacterBody3D)
├── CollisionShape3D
├── MeshInstance3D (or imported model)
├── AnimationTree
├── Camera3D
│   └── SpringArm3D (for collision)
└── Marker3D (weapon attachment points)
```

### Enemy (2D)
```
Enemy (CharacterBody2D)
├── Sprite2D
├── CollisionShape2D
├── AnimationPlayer
├── DetectionArea (Area2D)
│   └── CollisionShape2D
├── Hitbox (Area2D)
│   └── CollisionShape2D
├── NavigationAgent2D
└── Timer (attack cooldown)
```

### UI Screen
```
UIScreen (Control)
├── Background (TextureRect/ColorRect)
├── VBoxContainer
│   ├── Title (Label)
│   ├── HSeparator
│   └── ButtonContainer (VBoxContainer)
│       ├── StartButton (Button)
│       ├── OptionsButton (Button)
│       └── QuitButton (Button)
└── AnimationPlayer (transitions)
```

### HUD
```
HUD (CanvasLayer)
└── Control
    ├── MarginContainer
    │   └── HBoxContainer
    │       ├── HealthBar (ProgressBar/TextureProgressBar)
    │       └── ScoreLabel (Label)
    ├── Minimap (SubViewportContainer)
    │   └── SubViewport
    │       └── Camera2D
    └── DialogBox (PanelContainer)
        └── VBoxContainer
            ├── SpeakerLabel
            └── DialogText (RichTextLabel)
```

### Inventory Item
```
Item (Area2D)
├── Sprite2D
├── CollisionShape2D (pickup area)
├── AnimationPlayer (bob/glow)
└── AudioStreamPlayer2D (pickup sound)
```

### Level/World
```
Level (Node2D)
├── TileMapLayer (one node per layer; TileMap is deprecated since 4.3)
├── Entities (Node2D)
│   ├── Player
│   ├── Enemies (Node2D)
│   │   ├── Enemy1
│   │   └── Enemy2
│   └── Items (Node2D)
├── NavigationRegion2D
│   └── (navigation polygon)
├── Parallax2D (4.3+, replaces ParallaxBackground/ParallaxLayer)
│   └── Sprite2D
└── Camera2D (level bounds)
```

### Dialogue System
```
DialogueManager (Node)
├── CanvasLayer
│   └── DialogueBox (Control)
│       ├── Portrait (TextureRect)
│       ├── NameLabel (Label)
│       ├── TextLabel (RichTextLabel)
│       └── ChoicesContainer (VBoxContainer)
├── Timer (text reveal)
└── AudioStreamPlayer (voice/sfx)
```

## Node Selection Guide

### Physics Bodies
| Node | Use Case |
|------|----------|
| `CharacterBody2D/3D` | Player, enemies, NPCs with custom movement |
| `RigidBody2D/3D` | Physics-driven objects (crates, balls) |
| `StaticBody2D/3D` | Immovable collision (walls, floors) |
| `Area2D/3D` | Triggers, detection zones, pickups |

### Visual Nodes (2D)
| Node | Use Case |
|------|----------|
| `Sprite2D` | Static images |
| `AnimatedSprite2D` | Frame-based animations |
| `TileMapLayer` | Level geometry, backgrounds |
| `Line2D` | Trails, lasers, drawing |
| `Polygon2D` | Custom shapes |
| `CPUParticles2D` | Effects (compatible) |
| `GPUParticles2D` | Effects (performant) |

### Visual Nodes (3D)
| Node | Use Case |
|------|----------|
| `MeshInstance3D` | 3D models |
| `CSGBox3D`, `CSGSphere3D`, etc. | Prototyping geometry |
| `MultiMeshInstance3D` | Many identical objects |
| `GPUParticles3D` | 3D particle effects |
| `Decal` | Projected textures |

### UI Nodes
| Node | Use Case |
|------|----------|
| `Control` | Base container |
| `Label/RichTextLabel` | Text display |
| `Button/TextureButton` | Clickable elements |
| `ProgressBar/TextureProgressBar` | Health bars, loading |
| `HBoxContainer/VBoxContainer` | Auto-layout |
| `MarginContainer` | Padding |
| `PanelContainer` | Styled backgrounds |
| `ScrollContainer` | Scrollable content |
| `TabContainer` | Tabbed interfaces |

### Audio Nodes
| Node | Use Case |
|------|----------|
| `AudioStreamPlayer` | Global audio (music, UI) |
| `AudioStreamPlayer2D` | Positional 2D audio |
| `AudioStreamPlayer3D` | Positional 3D audio |

### Utility Nodes
| Node | Use Case |
|------|----------|
| `Timer` | Delayed actions, cooldowns |
| `AnimationPlayer` | Property animations |
| `AnimationTree` | Complex animation state machines |
| `Tween` | Programmatic animations |
| `RayCast2D/3D` | Line-of-sight, ground detection |
| `ShapeCast2D/3D` | Swept collision detection |

## Collision Layers Best Practice

```
Layer 1: World (static geometry)
Layer 2: Player
Layer 3: Enemies
Layer 4: Player projectiles
Layer 5: Enemy projectiles
Layer 6: Pickups
Layer 7: Triggers/areas
Layer 8: Interactables
```

Set in scene (Player is on layer 2 and collides with world, enemies and pickups: layers 1, 3, 6 = 1 + 4 + 32):
```ini
[node name="Player" type="CharacterBody2D"]
collision_layer = 2
collision_mask = 37
```
Name the layers in Project Settings > Layer Names so the inspector shows names, and set them from code with `set_collision_mask_value(3, true)`, where layer numbers start at 1. See the `godot-physics` skill for the full collision model.

## Groups for Organization

Use groups to organize and find nodes:
```ini
[node name="Enemy" type="CharacterBody2D" groups=["enemies", "damageable"]]
```

Common groups:
- `enemies` - All enemy nodes
- `damageable` - Anything that can take damage
- `interactable` - Objects player can interact with
- `persistent` - Nodes that persist between scenes
- `pausable` - Nodes affected by pause

## Scene Instancing

Reference external scenes:
```ini
[ext_resource type="PackedScene" path="res://scenes/enemy.tscn" id="enemy_scene"]

[node name="Enemy1" parent="Enemies" instance=ExtResource("enemy_scene")]
position = Vector2(100, 200)

[node name="Enemy2" parent="Enemies" instance=ExtResource("enemy_scene")]
position = Vector2(300, 200)
```

## Property Overrides

Override instanced scene properties:
```ini
[node name="Enemy1" parent="Enemies" instance=ExtResource("enemy_scene")]
position = Vector2(100, 200)
speed = 150.0
```
`speed` is an exported property of the instanced scene's root script, overridden for this instance only.

## Animation Setup

### AnimationPlayer in Scene
```ini
[sub_resource type="Animation" id="Animation_idle"]
length = 1.0
loop_mode = 1
tracks/0/type = "value"
tracks/0/path = NodePath("Sprite2D:frame")
tracks/0/interp = 1
tracks/0/keys = {
"times": PackedFloat32Array(0, 0.25, 0.5, 0.75),
"transitions": PackedFloat32Array(1, 1, 1, 1),
"update": 1,
"values": [0, 1, 2, 3]
}

[sub_resource type="AnimationLibrary" id="AnimationLibrary_abc"]
_data = {
&"idle": SubResource("Animation_idle")
}

[node name="AnimationPlayer" type="AnimationPlayer" parent="."]
libraries = {
&"": SubResource("AnimationLibrary_abc")
}
```

Prefer `godot_animation_create_clip` / `godot_animation_add_keyframe` over hand-writing tracks. See the `godot-animation` skill.

## Procedural Level Generation (godot-mcp)

| Goal | Tool | Follow-up |
|------|------|-----------|
| Room-and-corridor dungeon layout | `godot_generate_dungeon` | Write the result into a `TileMapLayer` scene, then `godot_validate_scene` |
| Repeating tile patterns (floors, walls, decoration) | `godot_generate_tilemap_pattern` | Check that the TileSet source and atlas coordinates exist in the project |
| Enemy wave schedules | `godot_generate_wave_config` | Save as a `.tres` or JSON, and have a spawner script read it |

Rules:
- Seed every generator and store the seed so layouts can be reproduced and bugs reported.
- After generating, place navigation (`godot-navigation` skill) and check reachability with `godot_navigation_validate_paths`.
- For runtime generation, write a generator script (for example a random walk or BSP over `TileMapLayer.set_cell`) instead of baking the output into a scene.

## Tips for AI Scene Generation

1. **Start with the root node type** - Choose based on the scene's purpose (CharacterBody2D for characters, Control for UI, Node2D for levels)

2. **Build hierarchy logically** - Visual nodes as children of physics bodies, UI elements in containers

3. **Use appropriate collision shapes** - RectangleShape2D for boxes, CapsuleShape2D for characters, circles for projectiles

4. **Set up layers correctly** - Avoid "everything collides with everything"

5. **Name nodes descriptively** - "PlayerSprite" not "Sprite2D", "HealthBar" not "ProgressBar"

6. **Use groups for runtime queries** - `get_tree().get_nodes_in_group("enemies")`

7. **Instance reusable scenes** - Don't duplicate complex node trees

8. **Consider processing order** - Parent nodes process before children

9. **Z-index for 2D layering** - Background < World < Entities < Effects < UI

10. **Use CanvasLayer for HUD** - Keeps UI separate from game camera
