---
name: godot-multiplayer
description: Implements Godot 4.x networked multiplayer - high-level MultiplayerAPI with ENet or WebSocket/WebRTC peers, server authority, @rpc annotations, MultiplayerSpawner and MultiplayerSynchronizer, lobbies, lag handling, and testing multiple instances. Use for co-op, PvP, lobbies, dedicated servers, or when RPCs and synchronization misbehave.
---

# Godot Multiplayer

## Architecture Rules

- **Server-authoritative by default.** The server (peer ID 1) owns game state. Clients send *inputs and requests*, and the server validates and replicates *results*.
- Each node has a **multiplayer authority** (default: server). `set_multiplayer_authority(peer_id)` lets a client own its player input node, not its health or score.
- Keep networking code out of gameplay logic where possible. Gameplay calls `request_attack()`, and the network layer decides how it reaches the server.

## Hosting and Joining (ENet)

```gdscript
# autoload/network.gd
extends Node

const PORT := 7777
signal player_joined(id: int)
signal player_left(id: int)

func host(max_clients := 8) -> Error:
    var peer := ENetMultiplayerPeer.new()
    var err := peer.create_server(PORT, max_clients)
    if err != OK:
        return err
    multiplayer.multiplayer_peer = peer
    multiplayer.peer_connected.connect(func(id: int) -> void: player_joined.emit(id))
    multiplayer.peer_disconnected.connect(func(id: int) -> void: player_left.emit(id))
    return OK

func join(address: String) -> Error:
    var peer := ENetMultiplayerPeer.new()
    var err := peer.create_client(address, PORT)
    if err != OK:
        return err
    multiplayer.multiplayer_peer = peer
    multiplayer.connected_to_server.connect(func() -> void: print("connected"))
    multiplayer.connection_failed.connect(func() -> void: multiplayer.multiplayer_peer = null)
    multiplayer.server_disconnected.connect(_on_server_gone)
    return OK

func _on_server_gone() -> void:
    multiplayer.multiplayer_peer = null
    get_tree().change_scene_to_file("res://ui/main_menu.tscn")
```
Web builds can't use ENet. Use `WebSocketMultiplayerPeer` (client-server) or `WebRTCMultiplayerPeer` (P2P, needs signaling). Steam and Epic networking use GDExtension peers.

## RPCs

```gdscript
@rpc("any_peer", "call_local", "reliable")
func request_fire(direction: Vector2) -> void:
    if not multiplayer.is_server():
        return
    var sender := multiplayer.get_remote_sender_id()
    if not _can_fire(sender):          # validate: rate limit, ammo, owns the player
        return
    _spawn_bullet.rpc(sender, direction)

@rpc("authority", "call_local", "reliable")
func _spawn_bullet(owner_id: int, direction: Vector2) -> void:
    pass  # visual/logic spawn on every peer
```
- Annotation options: mode `"authority"` (only the authority may call) / `"any_peer"`, `"call_local"` / `"call_remote"`, `"reliable"` / `"unreliable"` / `"unreliable_ordered"`, plus a channel int.
- Call with `func_name.rpc(args)` (everyone) or `func_name.rpc_id(peer_id, args)`.
- The RPC function must exist **at the same node path** on every peer. Spawn nodes consistently (see below) and give them deterministic names.
- Use **unreliable** for frequent state (positions) and **reliable** for events (damage, chat, spawns).
- **Never trust `any_peer` input.** Validate with `get_remote_sender_id()` on the server.

## Spawning and Synchronizing

```
Level
├── MultiplayerSpawner (spawn_path = ../Players, auto spawn list: player.tscn)
└── Players (Node)
    └── Player (MultiplayerSynchronizer child replicates position, velocity, animation state)
```
- **MultiplayerSpawner:** the server adds a child under `spawn_path`, and it appears on all clients. Use `spawn_function` + `spawn(data)` for custom init data (team, skin).
- **MultiplayerSynchronizer:** configure the replication config in the editor: properties, **spawn** (sent once), **sync** (continuous), **watch** (on change). Set `replication_interval` / `delta_interval`.
- Give the player's *input* synchronizer authority to the owning peer, and keep the main body synchronized from the server.

```gdscript
# player.gd
func _enter_tree() -> void:
    set_multiplayer_authority(name.to_int())      # Player named after its peer ID
    $InputSync.set_multiplayer_authority(name.to_int())

func _physics_process(delta: float) -> void:
    if not is_multiplayer_authority():
        return                                     # remote copies just display synced state
    # read local input, move, etc.
```

## Lag and Feel

- Interpolate remote entities between the last two received states. Don't snap to each update.
- Client-side prediction for the local player, with server reconciliation, for action games.
- Send inputs, not positions, from clients in competitive games.
- Simulate bad networks while testing (clumsy on Windows, `tc netem` on Linux).

## Testing Locally

- Debug > Customize Run Instances: run 2–4 instances, with launch arguments such as `--server` / `--client` per instance.
- Read `OS.get_cmdline_user_args()` to auto-host or auto-join in debug.
- With godot-mcp, `godot_editor_run_scene` launches one instance. Run extra clients from the shell: `godot --path . -- --client`.
- Headless dedicated server: `godot --headless --path . -- --server`. Export a server build with a "dedicated_server" feature preset (strips rendering resources).

## Debug Checklist

1. "Node not found" on RPC: node paths or names differ between peers. Check spawn order and naming.
2. RPC silently ignored: wrong mode (`authority` called by a non-authority), or the function is missing `@rpc`.
3. Synchronizer not updating: the property isn't in the replication config, the authority is wrong, or visibility is filtered.
4. Everything works for the host only: logic is gated on `is_server()` where it should check `is_multiplayer_authority()`, or the reverse.
5. Firewall or NAT: ENet needs the UDP port open. Use a relay (Steam, EOS, WebRTC TURN) for internet play without port forwarding.
