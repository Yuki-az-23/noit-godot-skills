---
name: godot-audio
description: Implements Godot 4.x audio - bus layouts and effects, AudioStreamPlayer/2D/3D setup, SFX pooling and polyphony, adaptive music with AudioStreamInteractive/Synchronized/Playlist, volume settings in linear or dB, ducking, and import settings. Use when adding sound effects, music systems, audio options menus, or debugging silent or clipping audio. Pairs with godot-mcp godot_audio_* tools.
---

# Godot Audio

## Bus Layout First

Create the buses before adding players, so every sound has a destination:

```
Master
├── Music      (Compressor optional)
├── SFX
│   └── UI     (optional sub-bus)
├── Voice
└── Ambience   (Reverb send optional)
```

| Task | godot-mcp tool |
|------|----------------|
| Create `default_bus_layout.tres` | `godot_audio_create_bus_layout` |
| Read, add or change buses, remove one | `godot_audio_read_bus_layout`, `godot_audio_set_bus`, `godot_audio_remove_bus` |
| Effect presets (reverb, compressor, low-pass) | `godot_audio_list_effect_presets`, `godot_audio_generate_effect_chain_script` |
| Apply a mix profile (for example "cinematic" or "retro") | `godot_audio_apply_mix_profile` |
| Configure an AudioStreamPlayer node in a scene | `godot_audio_configure_player` (scenePath, nodePath, stream, bus, volumeDb, pitchScale, autoplay) |
| List players in a scene | `godot_audio_list_players` |

Project Settings > Audio > Buses > Default Bus Layout must point at the layout file.

## Players

| Node | Use |
|------|-----|
| `AudioStreamPlayer` | Music, UI, non-positional SFX |
| `AudioStreamPlayer2D` | Positional 2D (attenuates with distance from the camera or `AudioListener2D`) |
| `AudioStreamPlayer3D` | Positional 3D (attenuation model, doppler, emission angle) |

- Always set `bus`. The default is Master, which bypasses the volume sliders.
- `max_polyphony > 1` lets one player overlap its own sound (rapid gunfire) without a pool.
- `volume_linear` (4.4+) is easier for sliders than `volume_db`.
- Randomize repetitive SFX with `AudioStreamRandomizer` (pitch and volume variation, several clips).
- Players in paused trees stop. Set `process_mode = ALWAYS` for UI and menu sounds.

## Volume Settings

```gdscript
func set_bus_volume(bus_name: StringName, linear: float) -> void:
    var idx := AudioServer.get_bus_index(bus_name)
    AudioServer.set_bus_volume_linear(idx, linear)      # 0.0–1.0, 4.4+
    # 4.3 and earlier: AudioServer.set_bus_volume_db(idx, linear_to_db(linear))
    AudioServer.set_bus_mute(idx, linear <= 0.001)
```
Sliders should be linear (0–1); the engine handles the dB conversion. Save the values to `user://settings.cfg` and apply them at startup in an autoload.

## SFX from Anywhere (AudioManager Autoload)

```gdscript
# autoload/audio_manager.gd
extends Node

const POOL_SIZE := 12
var _pool: Array[AudioStreamPlayer] = []

func _ready() -> void:
    process_mode = Node.PROCESS_MODE_ALWAYS
    for i in POOL_SIZE:
        var p := AudioStreamPlayer.new()
        p.bus = &"SFX"
        add_child(p)
        _pool.append(p)

func play_sfx(stream: AudioStream, pitch_jitter := 0.05) -> void:
    for p in _pool:
        if not p.playing:
            p.stream = stream
            p.pitch_scale = 1.0 + randf_range(-pitch_jitter, pitch_jitter)
            p.play()
            return
    # Pool exhausted: drop the sound rather than spawning nodes every frame.
```
For positional one-shots that outlive their source (enemy death sounds), reparent an `AudioStreamPlayer2D` to the level, or spawn one there, and `queue_free` it on `finished`.

## Music

- **Crossfade:** two `AudioStreamPlayer`s on the Music bus; tween one `volume_linear` 1→0 and the other 0→1.
- **Adaptive music (4.3+ built-ins):**
  - `AudioStreamInteractive`: clips plus a transition table (on beat, on bar, crossfade). Switch with `get_stream_playback().switch_to_clip_by_name(&"combat")`.
  - `AudioStreamSynchronized`: stems that play in sync. Fade individual layers (percussion in combat) by setting per-stream volume.
  - `AudioStreamPlaylist`: sequential or shuffled tracks with fades.
- Loop points: set loop in the Import dock (OGG/MP3 `loop`, `loop_offset`; WAV loop mode), not in code.
- `AudioStreamPolyphonic` + `AudioStreamPlaybackPolyphonic.play_stream()` plays many short sounds through one player, which is efficient for UI ticks.

## Ducking and Effects

- Duck music under dialogue: add a Compressor on Music with **sidechain** set to the Voice bus.
- Underwater or muffled: enable a LowPassFilter effect on SFX/Music with `AudioServer.set_bus_effect_enabled()`.
- Pause menu muffle: same idea, toggled on pause.

## Import Guidelines

| Type | Format |
|------|--------|
| Music, ambience (long) | OGG Vorbis (streams from disk, small) |
| Short SFX | WAV (fast decode; import as QOA or IMA-ADPCM compressed to save memory) |
| Voice | OGG |

Keep sample rates consistent (44.1 or 48 kHz) and normalize peaks below 0 dBFS. Watch the Master bus meter for clipping.

## Debug Checklist

1. No sound: wrong or muted bus, `volume_db` at -80, the player paused by tree pause, or a 2D player too far from the listener (`max_distance`).
2. Positional sound is wrong: there is no current `Camera2D/3D` or listener, or the attenuation is too aggressive.
3. Crackles or clicks: too many simultaneous voices (limit polyphony), or a missing fade on abrupt stops.
4. Web builds: audio starts only after the first user input (browser autoplay policy), so start music on a "Click to start" screen.
