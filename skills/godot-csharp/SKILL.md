---
name: godot-csharp
description: Writes C# for Godot 4.x (.NET build) - project setup, partial classes, [Export]/[Signal] attributes, signal delegates and events, GDScript-to-C# API naming, Variant and collection marshalling, async with ToSignal, interop with GDScript, and C# testing and export caveats (no web export). Use when a project has a .csproj or .cs scripts, or the user asks for C# instead of GDScript.
---

# Godot C#

## Detect and Set Up

- C# projects have a `<ProjectName>.csproj` and `.sln`, and need the **.NET build** of Godot ("Godot Engine - .NET") plus the matching .NET SDK (check `TargetFramework` in the `.csproj`).
- Build with `dotnet build` or the editor's Build button. Godot doesn't see new `[Export]` members until a build succeeds.
- **Platforms:** desktop, Android and iOS are supported. **Web export is not supported for C# projects** in 4.x. Recommend GDScript for web-first games.

## Script Shape

```csharp
using Godot;

public partial class Player : CharacterBody2D      // must be partial; file name must match the class
{
    [Signal] public delegate void HealthChangedEventHandler(int current, int max);
    [Signal] public delegate void DiedEventHandler();

    [Export] public float Speed { get; set; } = 220f;
    [Export(PropertyHint.Range, "1,999")] public int MaxHealth { get; set; } = 10;
    [Export] public PackedScene BulletScene { get; set; }

    private int _health;
    private AnimationPlayer _anim;

    public override void _Ready()
    {
        _health = MaxHealth;
        _anim = GetNode<AnimationPlayer>("AnimationPlayer");
    }

    public override void _PhysicsProcess(double delta)
    {
        Vector2 velocity = Velocity;
        if (!IsOnFloor())
            velocity += GetGravity() * (float)delta;

        float dir = Input.GetAxis("move_left", "move_right");
        velocity.X = dir * Speed;
        Velocity = velocity;                 // structs: modify a copy, then assign back
        MoveAndSlide();
    }

    public void Damage(int amount)
    {
        _health = Mathf.Max(_health - amount, 0);
        EmitSignal(SignalName.HealthChanged, _health, MaxHealth);
        if (_health == 0) EmitSignal(SignalName.Died);
    }
}
```

## Naming Map (GDScript → C#)

| GDScript | C# |
|----------|----|
| `snake_case` methods and properties | `PascalCase` (`move_and_slide()` → `MoveAndSlide()`, `global_position` → `GlobalPosition`) |
| `$Node` / `get_node("X")` | `GetNode<T>("X")`; `%Unique` → `GetNode<T>("%Unique")` |
| `signal died` | `[Signal] public delegate void DiedEventHandler();` (suffix `EventHandler` is required) |
| `died.emit()` | `EmitSignal(SignalName.Died)` |
| `x.died.connect(f)` | `x.Died += F;` (unsubscribe with `-=` in `_ExitTree`) or `x.Connect(SignalName.Died, Callable.From(F))` |
| `await get_tree().create_timer(1).timeout` | `await ToSignal(GetTree().CreateTimer(1), SceneTreeTimer.SignalName.Timeout);` |
| `preload(...)` | `GD.Load<PackedScene>("res://...")` (no compile-time preload) |
| `print()` / `push_error()` | `GD.Print()` / `GD.PushError()` |
| `Array[int]` / `Dictionary` | `Godot.Collections.Array<int>` / `Godot.Collections.Dictionary` for engine interop; use .NET `List<T>` internally |
| `delta: float` | `double delta`; cast to `float` for vector math |
| Constants like `Vector2.UP` | `Vector2.Up` |

## Pitfalls

- **Struct copies:** `Position.X = 5` doesn't compile, because `Position` returns a copy. Assign a whole new vector.
- **Lambda signal connections** with `+=` to engine objects keep both alive. Disconnect them, or use `Callable.From` with `CONNECT_ONE_SHOT`.
- **Disposed objects:** check `IsInstanceValid(node)` before using nodes that may have been freed; `QueueFree()` doesn't null your reference.
- **Hot reload:** C# reloads assemblies on rebuild. Static state resets, and `[Tool]` scripts must handle reload.
- **Allocation:** avoid allocating `Godot.Collections.*` or `Variant` in hot loops, because marshalling costs. Cache `StringName`s for frequently used names (`static readonly StringName Jump = "jump";`).

## Interop with GDScript

- From GDScript, a C# node's methods and exported properties are callable with their **C# names** (`node.Damage(3)`, `node.MaxHealth`).
- From C# to GDScript: `node.Call("take_damage", 3)`, `node.Get("health").AsInt32()`, `node.Connect("died", Callable.From(OnDied))`.
- Keep a clear boundary: pick one language per system and avoid ping-pong calls in hot paths.

## Testing and CI

- Use GdUnit4 (native C# support) or plain xUnit/NUnit for logic in non-Godot classes.
- CI needs the .NET Godot build and `*_mono_*` export templates, plus `actions/setup-dotnet`. Run `dotnet build` before `--import` and export (see `godot-export-ci`).
- Validation hooks in this plugin check `.gd` files only. Run `dotnet build` to catch C# errors.
