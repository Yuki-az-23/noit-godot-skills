# Godot engine API changes (4.3-stable → 4.4-stable)

> Derived from the Godot Engine class reference (MIT License, © Godot Engine contributors, Juan Linietsky, Ariel Manzur). See `licenses/GODOT-LICENSE.txt` at the plugin root.

Generated from the engine's own class reference XML (doc/classes and modules/*/doc_classes) at each release tag. `+` added, `~` signature changed, `⚠` newly deprecated, `−` removed.

- 4.3-stable: 956 classes
- 4.4-stable: 988 classes

## 4.3-stable → 4.4-stable

### New classes (32)

- **AnimationNodeExtension** ← AnimationNode *(experimental)*: Base class for extending [AnimationRootNode]s from GDScript, C#, or C++.
- **ColorPalette** ← Resource: A resource class for managing a palette of colors, which can be loaded and saved using [ColorPicker].
- **EditorContextMenuPlugin** ← RefCounted: Plugin for adding custom context menus in the editor.
- **EditorExportPlatformExtension** ← EditorExportPlatform: Base class for custom [EditorExportPlatform] implementations (plugins).
- **EditorExportPreset** ← RefCounted: Export preset configuration.
- **EditorToaster** ← HBoxContainer: Manages toast notifications within the editor.
- **ExternalTexture** ← Texture2D: Texture which displays the content of an external buffer.
- **GDScriptSyntaxHighlighter** ← EditorSyntaxHighlighter: A GDScript syntax highlighter that can be used with [TextEdit] and [CodeEdit] nodes.
- **GLTFObjectModelProperty** ← RefCounted: Describes how to access a property as defined in the glTF object model.
- **GridMapEditorPlugin** ← EditorPlugin: Editor for [GridMap] nodes.
- **JavaObject** ← RefCounted: Represents an object from the Java Native Interface.
- **LookAtModifier3D** ← SkeletonModifier3D: The [LookAtModifier3D] rotates a bone to look at a target.
- **OpenXRActionBindingModifier** ← OpenXRBindingModifier: Binding modifier that applies on individual actions related to an interaction profile.
- **OpenXRAnalogThresholdModifier** ← OpenXRActionBindingModifier: The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.
- **OpenXRBindingModifier** ← Resource: Binding modifier base class.
- **OpenXRBindingModifierEditor** ← PanelContainer: Binding modifier editor.
- **OpenXRDpadBindingModifier** ← OpenXRIPBindingModifier: The DPad binding modifier converts an axis input to a dpad output.
- **OpenXRHapticBase** ← Resource: OpenXR Haptic feedback base class.
- **OpenXRHapticVibration** ← OpenXRHapticBase: Vibration haptic feedback.
- **OpenXRIPBindingModifier** ← OpenXRBindingModifier: Binding modifier that applies directly on an interaction profile.
- **OpenXRInteractionProfileEditor** ← OpenXRInteractionProfileEditorBase: Default OpenXR interaction profile editor.
- **OpenXRInteractionProfileEditorBase** ← HBoxContainer: Base class for editing interaction profiles.
- **OpenXRVisibilityMask** ← VisualInstance3D: Draws a stereo correct visibility mask.
- **RetargetModifier3D** ← SkeletonModifier3D: A modifier to transfer parent skeleton poses (or global poses) to child skeletons in model space with different rests.
- **ShaderIncludeDB** ← Object: Internal database of built in shader include files.
- **SpringBoneCollision3D** ← Node3D: A base class of the collision that interacts with [SpringBoneSimulator3D].
- **SpringBoneCollisionCapsule3D** ← SpringBoneCollision3D: A capsule shape collision that interacts with [SpringBoneSimulator3D].
- **SpringBoneCollisionPlane3D** ← SpringBoneCollision3D: A infinite plane collision that interacts with [SpringBoneSimulator3D].
- **SpringBoneCollisionSphere3D** ← SpringBoneCollision3D: A sphere shape collision that interacts with [SpringBoneSimulator3D].
- **SpringBoneSimulator3D** ← SkeletonModifier3D: A [SkeletonModifier3D] to apply inertial wavering to bone chains.
- **SubtweenTweener** ← Tweener: Runs a [Tween] nested within another [Tween].
- **TranslationDomain** ← RefCounted: A self-contained collection of [Translation] resources.

### Changed classes (202)

#### @GDScript
- + annotation `@export_tool_button(text: String, icon: String = "")`
- + annotation `@warning_ignore_restore(warning: String)`
- + annotation `@warning_ignore_start(warning: String)`
- ⚠ deprecated method `Color8(r8: int, g8: int, b8: int, a8: int = 255) -> Color`
- ⚠ deprecated method `dict_to_inst(dictionary: Dictionary) -> Object`
- ⚠ deprecated method `inst_to_dict(instance: Object) -> Dictionary`

#### @GlobalScope
- + constant `MethodFlags.METHOD_FLAG_VIRTUAL_REQUIRED`
- + constant `PropertyHint.PROPERTY_HINT_DICTIONARY_TYPE`
- + constant `PropertyHint.PROPERTY_HINT_ONESHOT`
- + constant `PropertyHint.PROPERTY_HINT_TOOL_BUTTON`

#### AABB
- ~ method `get_support(dir: Vector3) -> Vector3` → `get_support(direction: Vector3) -> Vector3`

#### AStar2D
- ~ method `_estimate_cost(from_id: int, to_id: int) -> float` → `_estimate_cost(from_id: int, end_id: int) -> float`

#### AStar3D
- ~ method `_estimate_cost(from_id: int, to_id: int) -> float` → `_estimate_cost(from_id: int, end_id: int) -> float`

#### AStarGrid2D
- + method `get_point_data_in_region(region: Rect2i) -> Dictionary[]`
- ~ method `_estimate_cost(from_id: Vector2i, to_id: Vector2i) -> float` → `_estimate_cost(from_id: Vector2i, end_id: Vector2i) -> float`

#### Animation
- + method `add_marker(name: StringName, time: float)`
- + method `get_marker_at_time(time: float) -> StringName`
- + method `get_marker_color(name: StringName) -> Color`
- + method `get_marker_names() -> PackedStringArray`
- + method `get_marker_time(name: StringName) -> float`
- + method `get_next_marker(time: float) -> StringName`
- + method `get_prev_marker(time: float) -> StringName`
- + method `has_marker(name: StringName) -> bool`
- + method `optimize(allowed_velocity_err: float = 0.01, allowed_angular_err: float = 0.01, precision: int = 3)`
- + method `remove_marker(name: StringName)`
- + method `set_marker_color(name: StringName, color: Color)`

#### AnimationLibrary
- + method `get_animation_list_size() -> int`

#### AnimationMixer
- + property `root_motion_local: bool` (property)

#### AnimationNode
- + method `get_processing_animation_tree_instance_id() -> int`
- + method `is_process_testing() -> bool`

#### AnimationNodeAnimation
- + property `advance_on_start: bool` (property)

#### AnimationNodeTimeSeek
- + property `explicit_elapse: bool` (property)

#### AnimationPlayer
- + method `get_section_end_time() -> float`
- + method `get_section_start_time() -> float`
- + method `has_section() -> bool`
- + method `play_section(name: StringName = &"", start_time: float = -1, end_time: float = -1, custom_blend: float = -1, custom_speed: float = 1.0, from_end: bool = false)`
- + method `play_section_backwards(name: StringName = &"", start_time: float = -1, end_time: float = -1, custom_blend: float = -1)`
- + method `play_section_with_markers(name: StringName = &"", start_marker: StringName = &"", end_marker: StringName = &"", custom_blend: float = -1, custom_speed: float = 1.0, from_end: bool = false)`
- + method `play_section_with_markers_backwards(name: StringName = &"", start_marker: StringName = &"", end_marker: StringName = &"", custom_blend: float = -1)`
- + method `reset_section()`
- + method `set_section(start_time: float = -1, end_time: float = -1)`
- + method `set_section_with_markers(start_marker: StringName = &"", end_marker: StringName = &"")`

#### Array
- + method `find_custom(method: Callable, from: int = 0) -> int`
- + method `get(index: int) -> Variant`
- + method `rfind_custom(method: Callable, from: int = -1) -> int`
- + method `set(index: int, value: Variant)`

#### ArrayMesh
- + method `surface_remove(surf_idx: int)`

#### AudioEffectAmplify
- + property `volume_linear: float` (property)

#### AudioServer
- + method `get_bus_volume_linear(bus_idx: int) -> float`
- + method `get_driver_name() -> String`
- + method `get_input_mix_rate() -> float`
- + method `set_bus_volume_linear(bus_idx: int, volume_linear: float)`

#### AudioStream
- + method `_get_bar_beats() -> int`
- + method `_has_loop() -> bool`

#### AudioStreamGenerator
- + property `mix_rate_mode: int` (property)
- + constant `AudioStreamGeneratorMixRate.MIX_RATE_CUSTOM`
- + constant `AudioStreamGeneratorMixRate.MIX_RATE_INPUT`
- + constant `AudioStreamGeneratorMixRate.MIX_RATE_MAX`
- + constant `AudioStreamGeneratorMixRate.MIX_RATE_OUTPUT`

#### AudioStreamMP3
- + method `load_from_buffer(stream_data: PackedByteArray) -> AudioStreamMP3`
- + method `load_from_file(path: String) -> AudioStreamMP3`

#### AudioStreamOggVorbis
- ~ method `load_from_buffer(buffer: PackedByteArray) -> AudioStreamOggVorbis` → `load_from_buffer(stream_data: PackedByteArray) -> AudioStreamOggVorbis`

#### AudioStreamPlayback
- + method `get_loop_count() -> int`
- + method `get_playback_position() -> float`
- + method `is_playing() -> bool`
- + method `mix_audio(rate_scale: float, frames: int) -> PackedVector2Array`
- + method `seek(time: float = 0.0)`
- + method `start(from_pos: float = 0.0)`
- + method `stop()`

#### AudioStreamPlaybackInteractive
- + method `get_current_clip_index() -> int`

#### AudioStreamPlayer
- + property `volume_linear: float` (property)

#### AudioStreamPlayer2D
- + property `volume_linear: float` (property)

#### AudioStreamPlayer3D
- + property `volume_linear: float` (property)

#### AudioStreamWAV
- + method `load_from_buffer(stream_data: PackedByteArray, options: Dictionary = {}) -> AudioStreamWAV`
- + method `load_from_file(path: String, options: Dictionary = {}) -> AudioStreamWAV`

#### BoneAttachment3D
- + method `get_skeleton() -> Skeleton3D`

#### CPUParticles2D
- + method `request_particles_process(process_time: float)`
- + property `physics_interpolation_mode: int` (property)
- + property `seed: int` (property)
- + property `use_fixed_seed: bool` (property)
- ~ method `restart()` → `restart(keep_seed: bool = false)`

#### CPUParticles3D
- + method `capture_aabb() -> AABB`
- + method `request_particles_process(process_time: float)`
- + property `emission_ring_cone_angle: float` (property)
- + property `seed: int` (property)
- + property `use_fixed_seed: bool` (property)
- ~ method `restart()` → `restart(keep_seed: bool = false)`

#### CSGPolygon3D
- + property `path_rotation_accurate: bool` (property)

#### CSGShape3D
- + method `bake_collision_shape() -> ConcavePolygonShape3D`
- + method `bake_static_mesh() -> ArrayMesh`
- ⚠ deprecated property `snap: float`

#### Callable
- + method `get_unbound_arguments_count() -> int`

#### CameraFeed
- + method `_activate_feed() -> bool`
- + method `_deactivate_feed()`
- + method `get_texture_tex_id(feed_image_type: int) -> int`
- + method `set_external(width: int, height: int)`
- + method `set_format(index: int, parameters: Dictionary) -> bool`
- + method `set_name(name: String)`
- + method `set_position(position: int)`
- + method `set_rgb_image(rgb_image: Image)`
- + method `set_ycbcr_image(ycbcr_image: Image)`
- + property `formats: Array` (property)
- + signal `format_changed()`
- + signal `frame_changed()`
- + constant `FeedDataType.FEED_EXTERNAL`

#### CanvasItem
- + method `get_instance_shader_parameter(name: StringName) -> Variant`
- + method `set_instance_shader_parameter(name: StringName, value: Variant)`
- ~ method `make_canvas_position_local(screen_point: Vector2) -> Vector2` → `make_canvas_position_local(viewport_point: Vector2) -> Vector2`

#### ClassDB
- + method `class_call_static(class: StringName, method: StringName) -> Variant`
- + method `class_get_api_type(class: StringName) -> int`
- + method `class_get_property_getter(class: StringName, property: StringName) -> StringName`
- + method `class_get_property_setter(class: StringName, property: StringName) -> StringName`
- + constant `APIType.API_CORE`
- + constant `APIType.API_EDITOR`
- + constant `APIType.API_EDITOR_EXTENSION`
- + constant `APIType.API_EXTENSION`
- + constant `APIType.API_NONE`

#### CodeEdit
- + property `symbol_tooltip_on_hover: bool` (property)
- + signal `symbol_hovered(symbol: String, line: int, column: int)`

#### CollisionPolygon3D
- + property `debug_color: Color` (property)
- + property `debug_fill: bool` (property)

#### CollisionShape3D
- + property `debug_color: Color` (property)
- + property `debug_fill: bool` (property)

#### Color
- + method `from_rgba8(r8: int, g8: int, b8: int, a8: int = 255) -> Color`
- + property `ok_hsl_h: float` (property)
- + property `ok_hsl_l: float` (property)
- + property `ok_hsl_s: float` (property)

#### Control
- + property `tooltip_auto_translate_mode: int` (property)
- + constant `LayoutDirection.LAYOUT_DIRECTION_APPLICATION_LOCALE`
- + constant `LayoutDirection.LAYOUT_DIRECTION_MAX`
- + constant `LayoutDirection.LAYOUT_DIRECTION_SYSTEM_LOCALE`
- ⚠ deprecated constant `LayoutDirection.LAYOUT_DIRECTION_LOCALE`

#### Curve
- + method `get_domain_range() -> float`
- + method `get_value_range() -> float`
- + property `max_domain: float` (property)
- + property `min_domain: float` (property)
- + signal `domain_changed()`

#### Curve3D
- + property `closed: bool` (property)

#### Dictionary
- + method `assign(dictionary: Dictionary)`
- + method `get_typed_key_builtin() -> int`
- + method `get_typed_key_class_name() -> StringName`
- + method `get_typed_key_script() -> Variant`
- + method `get_typed_value_builtin() -> int`
- + method `get_typed_value_class_name() -> StringName`
- + method `get_typed_value_script() -> Variant`
- + method `is_same_typed(dictionary: Dictionary) -> bool`
- + method `is_same_typed_key(dictionary: Dictionary) -> bool`
- + method `is_same_typed_value(dictionary: Dictionary) -> bool`
- + method `is_typed() -> bool`
- + method `is_typed_key() -> bool`
- + method `is_typed_value() -> bool`
- + method `set(key: Variant, value: Variant) -> bool`
- + method `sort()`

#### DirAccess
- + method `create_temp(prefix: String = "", keep: bool = false) -> DirAccess`
- + method `is_bundle(path: String) -> bool`

#### DisplayServer
- + method `beep()`
- + method `has_hardware_keyboard() -> bool`
- + method `screen_get_image_rect(rect: Rect2i) -> Image`
- + method `show_emoji_and_symbol_picker()`
- + method `window_start_drag(window_id: int = 0)`
- + method `window_start_resize(edge: int, window_id: int = 0)`
- + constant `Feature.FEATURE_EMOJI_AND_SYMBOL_PICKER`
- + constant `Feature.FEATURE_NATIVE_DIALOG_FILE_EXTRA`
- + constant `Feature.FEATURE_NATIVE_DIALOG_FILE_MIME`
- + constant `Feature.FEATURE_SCREEN_EXCLUDE_FROM_CAPTURE`
- + constant `Feature.FEATURE_WINDOW_DRAG`
- + constant `Feature.FEATURE_WINDOW_EMBEDDING`
- + constant `HandleType.EGL_CONFIG`
- + constant `HandleType.EGL_DISPLAY`
- + constant `MouseMode.MOUSE_MODE_MAX`
- + constant `WindowFlags.WINDOW_FLAG_EXCLUDE_FROM_CAPTURE`
- + constant `WindowFlags.WINDOW_FLAG_SHARP_CORNERS`
- + constant `WindowResizeEdge.WINDOW_EDGE_BOTTOM`
- + constant `WindowResizeEdge.WINDOW_EDGE_BOTTOM_LEFT`
- + constant `WindowResizeEdge.WINDOW_EDGE_BOTTOM_RIGHT`
- + constant `WindowResizeEdge.WINDOW_EDGE_LEFT`
- + constant `WindowResizeEdge.WINDOW_EDGE_MAX`
- + constant `WindowResizeEdge.WINDOW_EDGE_RIGHT`
- + constant `WindowResizeEdge.WINDOW_EDGE_TOP`
- + constant `WindowResizeEdge.WINDOW_EDGE_TOP_LEFT`
- + constant `WindowResizeEdge.WINDOW_EDGE_TOP_RIGHT`

#### ENetPacketPeer
- + method `get_packet_flags() -> int`

#### EditorExportPlatform
- + method `add_message(type: int, category: String, message: String)`
- + method `clear_messages()`
- + method `create_preset() -> EditorExportPreset`
- + method `export_pack(preset: EditorExportPreset, debug: bool, path: String, flags: int = 0) -> int`
- + method `export_pack_patch(preset: EditorExportPreset, debug: bool, path: String, patches: PackedStringArray = PackedStringArray(), flags: int = 0) -> int`
- + method `export_project(preset: EditorExportPreset, debug: bool, path: String, flags: int = 0) -> int`
- + method `export_project_files(preset: EditorExportPreset, debug: bool, save_cb: Callable, shared_cb: Callable = Callable()) -> int`
- + method `export_zip(preset: EditorExportPreset, debug: bool, path: String, flags: int = 0) -> int`
- + method `export_zip_patch(preset: EditorExportPreset, debug: bool, path: String, patches: PackedStringArray = PackedStringArray(), flags: int = 0) -> int`
- + method `find_export_template(template_file_name: String) -> Dictionary`
- + method `gen_export_flags(flags: int) -> PackedStringArray`
- + method `get_current_presets() -> Array`
- + method `get_forced_export_files() -> PackedStringArray`
- + method `get_internal_export_files(preset: EditorExportPreset, debug: bool) -> Dictionary`
- + method `get_message_category(index: int) -> String`
- + method `get_message_count() -> int`
- + method `get_message_text(index: int) -> String`
- + method `get_message_type(index: int) -> int`
- + method `get_worst_message_type() -> int`
- + method `save_pack(preset: EditorExportPreset, debug: bool, path: String, embed: bool = false) -> Dictionary`
- + method `save_pack_patch(preset: EditorExportPreset, debug: bool, path: String) -> Dictionary`
- + method `save_zip(preset: EditorExportPreset, debug: bool, path: String) -> Dictionary`
- + method `save_zip_patch(preset: EditorExportPreset, debug: bool, path: String) -> Dictionary`
- + method `ssh_push_to_remote(host: String, port: String, scp_args: PackedStringArray, src_file: String, dst_file: String) -> int`
- + method `ssh_run_on_remote(host: String, port: String, ssh_arg: PackedStringArray, cmd_args: String, output: Array = [], port_fwd: int = -1) -> int`
- + method `ssh_run_on_remote_no_wait(host: String, port: String, ssh_args: PackedStringArray, cmd_args: String, port_fwd: int = -1) -> int`
- + constant `DebugFlags.DEBUG_FLAG_DUMB_CLIENT`
- + constant `DebugFlags.DEBUG_FLAG_REMOTE_DEBUG`
- + constant `DebugFlags.DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST`
- + constant `DebugFlags.DEBUG_FLAG_VIEW_COLLISIONS`
- + constant `DebugFlags.DEBUG_FLAG_VIEW_NAVIGATION`
- + constant `ExportMessageType.EXPORT_MESSAGE_ERROR`
- + constant `ExportMessageType.EXPORT_MESSAGE_INFO`
- + constant `ExportMessageType.EXPORT_MESSAGE_NONE`
- + constant `ExportMessageType.EXPORT_MESSAGE_WARNING`

#### EditorExportPlugin
- + method `_get_export_option_visibility(platform: EditorExportPlatform, option: String) -> bool`
- + method `get_export_platform() -> EditorExportPlatform`
- + method `get_export_preset() -> EditorExportPreset`

#### EditorFeatureProfile
- + constant `Feature.FEATURE_GAME`

#### EditorFileDialog
- + method `clear_filename_filter()`
- + method `get_filename_filter() -> String`
- + method `set_filename_filter(filter: String)`
- + signal `filename_filter_changed(filter: String)`

#### EditorImportPlugin
- + method `_get_format_version() -> int`

#### EditorInspector
- + method `edit(object: Object)`
- + method `instantiate_property_editor(object: Object, type: int, path: String, hint: int, hint_text: String, usage: int, wide: bool = false) -> EditorProperty`
- + property `draw_focus_border: bool` (property)
- + property `focus_mode: int` (property)

#### EditorInterface
- + method `get_editor_toaster() -> EditorToaster`
- + method `get_editor_undo_redo() -> EditorUndoRedoManager`
- + method `popup_create_dialog(callback: Callable, base_type: StringName = "", current_type: String = "", dialog_title: String = "", type_blocklist: StringName[] = [])`
- + method `popup_method_selector(object: Object, callback: Callable, current_value: String = "")`
- + method `popup_quick_open(callback: Callable, base_types: StringName[] = [])`
- ~ method `open_scene_from_path(scene_filepath: String)` → `open_scene_from_path(scene_filepath: String, set_inherited: bool = false)`
- ~ method `popup_node_selector(callback: Callable, valid_types: StringName[] = [])` → `popup_node_selector(callback: Callable, valid_types: StringName[] = [], current_value: Node = null)`
- ~ method `popup_property_selector(object: Object, callback: Callable, type_filter: PackedInt32Array = PackedInt32Array())` → `popup_property_selector(object: Object, callback: Callable, type_filter: PackedInt32Array = PackedInt32Array(), current_value: String = "")`

#### EditorPlugin
- + method `add_context_menu_plugin(slot: int, plugin: EditorContextMenuPlugin)`
- + method `add_export_platform(platform: EditorExportPlatform)`
- + method `remove_context_menu_plugin(plugin: EditorContextMenuPlugin)`
- + method `remove_export_platform(platform: EditorExportPlatform)`

#### EditorProperty
- + method `deselect()`
- + method `is_selected() -> bool`
- + method `select(focusable: int = -1)`
- + method `set_label_reference(control: Control)`
- + method `set_object_and_property(object: Object, property: StringName)`
- + property `draw_background: bool` (property)
- + property `draw_label: bool` (property)
- + property `name_split_ratio: float` (property)
- + property `selectable: bool` (property)
- + property `use_folding: bool` (property)
- + signal `property_favorited(property: StringName, favorited: bool)`

#### EditorSceneFormatImporter
- + method `add_import_option(name: String, value: Variant)`
- + method `add_import_option_advanced(type: int, name: String, default_value: Variant, hint: int = 0, hint_string: String = "", usage_flags: int = 6)`
- − removed method `_get_import_flags() -> int`

#### EditorSettings
- + property `asset_library/use_threads: bool` (property)
- + property `debugger/auto_switch_to_stack_trace: bool` (property)
- + property `debugger/profiler_target_fps: int` (property)
- + property `docks/filesystem/other_file_extensions: String` (property)
- + property `docks/scene_tree/ask_before_deleting_related_animation_tracks: bool` (property)
- + property `docks/scene_tree/ask_before_revoking_unique_name: bool` (property)
- + property `docks/scene_tree/hide_filtered_out_parents: bool` (property)
- + property `editors/2d/zoom_speed_factor: float` (property)
- + property `editors/3d/manipulator_gizmo_opacity: float` (property)
- + property `editors/3d/manipulator_gizmo_size: int` (property)
- + property `editors/3d/navigation/orbit_mouse_button: int` (property)
- + property `editors/3d/navigation/pan_mouse_button: int` (property)
- + property `editors/3d/navigation/show_viewport_navigation_gizmo: bool` (property)
- + property `editors/3d/navigation/show_viewport_rotation_gizmo: bool` (property)
- + property `editors/3d/navigation/zoom_mouse_button: int` (property)
- + property `editors/3d/navigation_feel/translation_sensitivity: float` (property)
- + property `editors/3d_gizmos/gizmo_colors/camera: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/csg: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/decal: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/fog_volume: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/gridmap_grid: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/joint_body_a: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/joint_body_b: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/lightmap_lines: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/lightprobe_lines: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/occluder: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/particle_attractor: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/particle_collision: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/particles: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/path_tilt: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/reflection_probe: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/selected_bone: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/skeleton: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/spring_bone_collision: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/spring_bone_inside_collision: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/spring_bone_joint: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/stream_player_3d: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/visibility_notifier: Color` (property)
- + property `editors/3d_gizmos/gizmo_colors/voxel_gi: Color` (property)
- + property `editors/3d_gizmos/gizmo_settings/bone_axis_length: float` (property)
- + property `editors/3d_gizmos/gizmo_settings/bone_shape: int` (property)
- + property `editors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size: float` (property)
- + property `editors/bone_mapper/handle_colors/error: Color` (property)
- + property `editors/bone_mapper/handle_colors/missing: Color` (property)
- + property `editors/bone_mapper/handle_colors/set: Color` (property)
- + property `editors/bone_mapper/handle_colors/unset: Color` (property)
- + property `editors/grid_map/palette_min_width: int` (property)
- + property `editors/grid_map/preview_size: int` (property)
- + property `export/ssh/scp: String` (property)
- + property `export/ssh/ssh: String` (property)
- + property `filesystem/file_server/password: String` (property)
- + property `filesystem/file_server/port: int` (property)
- + property `filesystem/quick_open_dialog/default_display_mode: int` (property)
- + property `filesystem/quick_open_dialog/enable_fuzzy_matching: bool` (property)
- + property `filesystem/quick_open_dialog/include_addons: bool` (property)
- + property `filesystem/quick_open_dialog/max_fuzzy_misses: int` (property)
- + property `filesystem/quick_open_dialog/max_results: int` (property)
- + property `filesystem/quick_open_dialog/show_search_highlight: bool` (property)
- + property `interface/editor/font_allow_msdf: bool` (property)
- + property `interface/editor/keep_screen_on: bool` (property)
- + property `interface/editors/derive_script_globals_by_name: bool` (property)
- + property `interface/editors/show_scene_tree_root_selection: bool` (property)
- + property `network/tls/enable_tls_v1.3: bool` (property)
- + property `run/window_placement/game_embed_mode: int` (property)
- + property `text_editor/behavior/documentation/enable_tooltips: bool` (property)
- + property `text_editor/behavior/files/auto_reload_and_parse_scripts_on_save: bool` (property)
- + property `text_editor/behavior/files/open_dominant_script_on_scene_change: bool` (property)
- + property `text_editor/behavior/general/empty_selection_clipboard: bool` (property)
- + property `text_editor/completion/idle_parse_delay_with_errors_found: float` (property)
- + property `text_editor/external/exec_flags: String` (property)
- + property `text_editor/external/exec_path: String` (property)
- + property `text_editor/external/use_external_editor: bool` (property)
- + property `text_editor/help/sort_functions_alphabetically: bool` (property)
- + property `text_editor/script_list/group_help_pages: bool` (property)
- + property `text_editor/script_list/highlight_scene_scripts: bool` (property)
- + property `text_editor/script_list/list_script_names_as: int` (property)
- + property `text_editor/script_list/script_temperature_enabled: bool` (property)
- + property `text_editor/script_list/script_temperature_history_size: int` (property)
- + property `text_editor/script_list/sort_scripts_by: int` (property)
- + property `text_editor/theme/line_spacing: int` (property)
- + property `version_control/ssh_private_key_path: String` (property)
- + property `version_control/ssh_public_key_path: String` (property)
- + property `version_control/username: String` (property)
- − removed property `editors/3d/navigation/orbit_modifier: int`
- − removed property `editors/3d/navigation/pan_modifier: int`
- − removed property `editors/3d/navigation/zoom_modifier: int`

#### EditorSpinSlider
- + property `editing_integer: bool` (property)
- + signal `updown_pressed()`

#### EditorTranslationParserPlugin
- ~ method `_parse_file(path: String, msgids: String[], msgids_context_plural: Array[])` → `_parse_file(path: String) -> PackedStringArray[]`

#### EditorUndoRedoManager
- + method `clear_history(id: int = -99, increase_version: bool = true)`

#### Engine
- + method `is_embedded_in_editor() -> bool`
- + property `print_to_stdout: bool` (property)

#### Environment
- + constant `ToneMapper.TONE_MAPPER_AGX`

#### FileAccess
- + method `create_temp(mode_flags: int, prefix: String = "", extension: String = "", keep: bool = false) -> FileAccess`
- + method `get_half() -> float`
- + method `store_half(value: float) -> bool`
- ~ method `open_encrypted(path: String, mode_flags: int, key: PackedByteArray) -> FileAccess` → `open_encrypted(path: String, mode_flags: int, key: PackedByteArray, iv: PackedByteArray = PackedByteArray()) -> FileAccess`
- ~ method `store_16(value: int)` → `store_16(value: int) -> bool`
- ~ method `store_32(value: int)` → `store_32(value: int) -> bool`
- ~ method `store_64(value: int)` → `store_64(value: int) -> bool`
- ~ method `store_8(value: int)` → `store_8(value: int) -> bool`
- ~ method `store_buffer(buffer: PackedByteArray)` → `store_buffer(buffer: PackedByteArray) -> bool`
- ~ method `store_csv_line(values: PackedStringArray, delim: String = ",")` → `store_csv_line(values: PackedStringArray, delim: String = ",") -> bool`
- ~ method `store_double(value: float)` → `store_double(value: float) -> bool`
- ~ method `store_float(value: float)` → `store_float(value: float) -> bool`
- ~ method `store_line(line: String)` → `store_line(line: String) -> bool`
- ~ method `store_pascal_string(string: String)` → `store_pascal_string(string: String) -> bool`
- ~ method `store_real(value: float)` → `store_real(value: float) -> bool`
- ~ method `store_string(string: String)` → `store_string(string: String) -> bool`
- ~ method `store_var(value: Variant, full_objects: bool = false)` → `store_var(value: Variant, full_objects: bool = false) -> bool`

#### FileDialog
- + method `clear_filename_filter()`
- + property `filename_filter: String` (property)
- + property `ok_button_text: String` (property)
- + property `size: Vector2i` (property)
- + signal `filename_filter_changed(filter: String)`

#### FontFile
- + property `keep_rounding_remainders: bool` (property)

#### GDExtensionManager
- + signal `extension_loaded(extension: GDExtension)`
- + signal `extension_unloading(extension: GDExtension)`

#### GLTFAccessor
- + constant `GLTFComponentType.COMPONENT_TYPE_DOUBLE_FLOAT`
- + constant `GLTFComponentType.COMPONENT_TYPE_HALF_FLOAT`
- + constant `GLTFComponentType.COMPONENT_TYPE_NONE`
- + constant `GLTFComponentType.COMPONENT_TYPE_SIGNED_BYTE`
- + constant `GLTFComponentType.COMPONENT_TYPE_SIGNED_INT`
- + constant `GLTFComponentType.COMPONENT_TYPE_SIGNED_LONG`
- + constant `GLTFComponentType.COMPONENT_TYPE_SIGNED_SHORT`
- + constant `GLTFComponentType.COMPONENT_TYPE_SINGLE_FLOAT`
- + constant `GLTFComponentType.COMPONENT_TYPE_UNSIGNED_BYTE`
- + constant `GLTFComponentType.COMPONENT_TYPE_UNSIGNED_INT`
- + constant `GLTFComponentType.COMPONENT_TYPE_UNSIGNED_LONG`
- + constant `GLTFComponentType.COMPONENT_TYPE_UNSIGNED_SHORT`

#### GLTFDocument
- + method `export_object_model_property(state: GLTFState, node_path: NodePath, godot_node: Node, gltf_node_index: int) -> GLTFObjectModelProperty`
- + method `get_supported_gltf_extensions() -> PackedStringArray`
- + method `import_object_model_property(state: GLTFState, json_pointer: String) -> GLTFObjectModelProperty`

#### GLTFDocumentExtension
- + method `_export_object_model_property(state: GLTFState, node_path: NodePath, godot_node: Node, gltf_node_index: int, target_object: Object, target_depth: int) -> GLTFObjectModelProperty`
- + method `_export_post_convert(state: GLTFState, root: Node) -> int`
- + method `_import_object_model_property(state: GLTFState, split_json_pointer: PackedStringArray, partial_paths: NodePath[]) -> GLTFObjectModelProperty`
- + method `_import_pre_generate(state: GLTFState) -> int`

#### GLTFNode
- + method `append_child_index(child_index: int)`
- + method `get_scene_node_path(gltf_state: GLTFState, handle_skeletons: bool = true) -> NodePath`

#### GLTFState
- + method `append_gltf_node(gltf_node: GLTFNode, godot_scene_node: Node, parent_node_index: int) -> int`

#### GPUParticles2D
- + method `request_particles_process(process_time: float)`
- + property `seed: int` (property)
- + property `use_fixed_seed: bool` (property)
- ~ method `restart()` → `restart(keep_seed: bool = false)`

#### GPUParticles3D
- + method `request_particles_process(process_time: float)`
- + property `seed: int` (property)
- + property `use_fixed_seed: bool` (property)
- ~ method `restart()` → `restart(keep_seed: bool = false)`

#### GPUParticlesCollisionHeightField3D
- + method `get_heightfield_mask_value(layer_number: int) -> bool`
- + method `set_heightfield_mask_value(layer_number: int, value: bool)`
- + property `heightfield_mask: int` (property)

#### Geometry2D
- + method `bresenham_line(from: Vector2i, to: Vector2i) -> Vector2i[]`

#### GeometryInstance3D
- + property `gi_lightmap_texel_scale: float` (property)
- ⚠ deprecated property `gi_lightmap_scale: int`
- ⚠ deprecated constant `LightmapScale.LIGHTMAP_SCALE_1X`
- ⚠ deprecated constant `LightmapScale.LIGHTMAP_SCALE_2X`
- ⚠ deprecated constant `LightmapScale.LIGHTMAP_SCALE_4X`
- ⚠ deprecated constant `LightmapScale.LIGHTMAP_SCALE_8X`
- ⚠ deprecated constant `LightmapScale.LIGHTMAP_SCALE_MAX`

#### GraphEdit
- + method `get_connection_count(from_node: StringName, from_port: int) -> int`
- + property `connections: Dictionary[]` (property)
- + signal `cut_nodes_request()`
- ~ method `connect_node(from_node: StringName, from_port: int, to_node: StringName, to_port: int) -> int` → `connect_node(from_node: StringName, from_port: int, to_node: StringName, to_port: int, keep_alive: bool = false) -> int`
- ~ signal `frame_rect_changed(frame: GraphFrame, new_rect: Vector2)` → `frame_rect_changed(frame: GraphFrame, new_rect: Rect2)`
- − removed method `get_connection_list() -> Dictionary[]`

#### Image
- + method `linear_to_srgb()`

#### ImporterMesh
- − removed property `_data: Dictionary`

#### Input
- + constant `MouseMode.MOUSE_MODE_MAX`

#### InputMap
- ~ method `add_action(action: StringName, deadzone: float = 0.5)` → `add_action(action: StringName, deadzone: float = 0.2)`

#### ItemList
- + method `get_h_scroll_bar() -> HScrollBar`
- + method `get_item_auto_translate_mode(idx: int) -> int`
- + method `set_item_auto_translate_mode(idx: int, mode: int)`
- + property `auto_width: bool` (property)
- + property `wraparound_items: bool` (property)
- + constant `SelectMode.SELECT_TOGGLE`

#### JSON
- + method `from_native(variant: Variant, full_objects: bool = false) -> Variant`
- + method `to_native(json: Variant, allow_objects: bool = false) -> Variant`

#### JavaClass
- + method `get_java_class_name() -> String`
- + method `get_java_method_list() -> Dictionary[]`
- + method `get_java_parent_class() -> JavaClass`

#### JavaClassWrapper
- + method `get_exception() -> JavaObject`

#### JavaScriptBridge
- + method `is_js_buffer(javascript_object: JavaScriptObject) -> bool`
- + method `js_buffer_to_packed_byte_array(javascript_buffer: JavaScriptObject) -> PackedByteArray`

#### Label
- + property `paragraph_separator: String` (property)

#### LabelSettings
- + property `paragraph_spacing: float` (property)

#### Light3D
- + property `shadow_caster_mask: int` (property)

#### LightmapGI
- + property `shadowmask_mode: int` (property)
- + property `supersampling: bool` (property)
- + property `supersampling_factor: float` (property)

#### LightmapGIData
- + property `shadowmask_textures: TextureLayered[]` (property)
- + constant `ShadowmaskMode.SHADOWMASK_MODE_NONE`
- + constant `ShadowmaskMode.SHADOWMASK_MODE_OVERLAY`
- + constant `ShadowmaskMode.SHADOWMASK_MODE_REPLACE`

#### LineEdit
- + method `apply_ime()`
- + method `cancel_ime()`
- + method `edit()`
- + method `has_ime_text() -> bool`
- + method `has_redo() -> bool`
- + method `has_undo() -> bool`
- + method `is_editing() -> bool`
- + method `unedit()`
- + property `emoji_menu_enabled: bool` (property)
- + property `keep_editing_on_text_submit: bool` (property)
- + signal `editing_toggled(toggled_on: bool)`
- + constant `MenuItems.MENU_EMOJI_AND_SYMBOL`

#### MeshInstance3D
- + method `bake_mesh_from_current_skeleton_pose(existing: ArrayMesh = null) -> ArrayMesh`

#### MeshLibrary
- + method `get_item_mesh_cast_shadow(id: int) -> int`
- + method `set_item_mesh_cast_shadow(id: int, shadow_casting_setting: int)`

#### MultiMesh
- + method `reset_instance_physics_interpolation(instance: int)`
- + method `set_buffer_interpolated(buffer_curr: PackedFloat32Array, buffer_prev: PackedFloat32Array)`
- + property `physics_interpolation_quality: int` (property)
- + constant `PhysicsInterpolationQuality.INTERP_QUALITY_FAST`
- + constant `PhysicsInterpolationQuality.INTERP_QUALITY_HIGH`

#### NavigationLink2D
- + method `get_navigation_map() -> RID`
- + method `set_navigation_map(navigation_map: RID)`

#### NavigationLink3D
- + method `get_navigation_map() -> RID`
- + method `set_navigation_map(navigation_map: RID)`

#### NavigationMeshSourceGeometryData2D
- + method `get_bounds() -> Rect2`

#### NavigationMeshSourceGeometryData3D
- + method `get_bounds() -> AABB`

#### NavigationPathQueryParameters2D
- + constant `PathPostProcessing.PATH_POSTPROCESSING_NONE`

#### NavigationPathQueryParameters3D
- + constant `PathPostProcessing.PATH_POSTPROCESSING_NONE`

#### NavigationPolygon
- + property `sample_partition_type: int` (property)
- + constant `SamplePartitionType.SAMPLE_PARTITION_CONVEX_PARTITION`
- + constant `SamplePartitionType.SAMPLE_PARTITION_MAX`
- + constant `SamplePartitionType.SAMPLE_PARTITION_TRIANGULATE`

#### NavigationRegion2D
- + method `get_bounds() -> Rect2`

#### NavigationRegion3D
- + method `get_bounds() -> AABB`

#### NavigationServer2D
- + method `map_get_use_async_iterations(map: RID) -> bool`
- + method `map_set_use_async_iterations(map: RID, enabled: bool)`
- + method `region_get_bounds(region: RID) -> Rect2`
- + method `region_get_closest_point(region: RID, to_point: Vector2) -> Vector2`
- ~ method `query_path(parameters: NavigationPathQueryParameters2D, result: NavigationPathQueryResult2D)` → `query_path(parameters: NavigationPathQueryParameters2D, result: NavigationPathQueryResult2D, callback: Callable = Callable())`

#### NavigationServer3D
- + method `map_get_use_async_iterations(map: RID) -> bool`
- + method `map_set_use_async_iterations(map: RID, enabled: bool)`
- + method `region_get_bounds(region: RID) -> AABB`
- + method `region_get_closest_point(region: RID, to_point: Vector3) -> Vector3`
- + method `region_get_closest_point_normal(region: RID, to_point: Vector3) -> Vector3`
- + method `region_get_closest_point_to_segment(region: RID, start: Vector3, end: Vector3, use_collision: bool = false) -> Vector3`
- + constant `ProcessInfo.INFO_OBSTACLE_COUNT`
- ~ method `query_path(parameters: NavigationPathQueryParameters3D, result: NavigationPathQueryResult3D)` → `query_path(parameters: NavigationPathQueryParameters3D, result: NavigationPathQueryResult3D, callback: Callable = Callable())`

#### Node
- + method `get_rpc_config() -> Variant`
- + method `set_translation_domain_inherited()`
- + signal `editor_state_changed()`

#### Node3D
- + method `get_global_transform_interpolated() -> Transform3D`

#### OS
- + method `get_stderr_type() -> int`
- + method `get_stdin_type() -> int`
- + method `get_stdout_type() -> int`
- + method `get_temp_dir() -> String`
- + method `get_version_alias() -> String`
- + method `read_buffer_from_stdin(buffer_size: int) -> PackedByteArray`
- + constant `RenderingDriver.RENDERING_DRIVER_METAL`
- + constant `StdHandleType.STD_HANDLE_CONSOLE`
- + constant `StdHandleType.STD_HANDLE_FILE`
- + constant `StdHandleType.STD_HANDLE_INVALID`
- + constant `StdHandleType.STD_HANDLE_PIPE`
- + constant `StdHandleType.STD_HANDLE_UNKNOWN`
- ~ method `execute_with_pipe(path: String, arguments: PackedStringArray) -> Dictionary` → `execute_with_pipe(path: String, arguments: PackedStringArray, blocking: bool = true) -> Dictionary`
- ~ method `read_string_from_stdin() -> String` → `read_string_from_stdin(buffer_size: int) -> String`

#### Object
- + method `_iter_get(iter: Variant) -> Variant`
- + method `_iter_init(iter: Array) -> bool`
- + method `_iter_next(iter: Array) -> bool`
- + method `get_translation_domain() -> StringName`
- + method `has_connections(signal: StringName) -> bool`
- + method `set_translation_domain(domain: StringName)`

#### OmniLight3D
- + property `light_specular: float` (property)

#### OpenXRAPIExtension
- + method `action_get_handle(action: RID) -> int`
- + method `begin_debug_label_region(label_name: String)`
- + method `end_debug_label_region()`
- + method `find_action(name: String, action_set: RID) -> RID`
- + method `get_projection_layer() -> int`
- + method `get_render_state_z_far() -> float`
- + method `get_render_state_z_near() -> float`
- + method `get_supported_swapchain_formats() -> PackedInt64Array`
- + method `insert_debug_label(label_name: String)`
- + method `openxr_swapchain_acquire(swapchain: int)`
- + method `openxr_swapchain_create(create_flags: int, usage_flags: int, swapchain_format: int, width: int, height: int, sample_count: int, array_size: int) -> int`
- + method `openxr_swapchain_free(swapchain: int)`
- + method `openxr_swapchain_get_image(swapchain: int) -> RID`
- + method `openxr_swapchain_get_swapchain(swapchain: int) -> int`
- + method `openxr_swapchain_release(swapchain: int)`
- + method `register_projection_views_extension(extension: OpenXRExtensionWrapperExtension)`
- + method `set_object_name(object_type: int, object_handle: int, object_name: String)`
- + method `set_render_region(render_region: Rect2i)`
- + method `set_velocity_depth_texture(render_target: RID)`
- + method `set_velocity_target_size(target_size: Vector2i)`
- + method `set_velocity_texture(render_target: RID)`
- + method `unregister_projection_views_extension(extension: OpenXRExtensionWrapperExtension)`

#### OpenXRCompositionLayer
- + method `get_android_surface() -> JavaObject`
- + property `android_surface_size: Vector2i` (property)
- + property `use_android_surface: bool` (property)

#### OpenXRExtensionWrapperExtension
- + method `_on_post_draw_viewport(viewport: RID)`
- + method `_on_pre_draw_viewport(viewport: RID)`
- + method `_set_android_surface_swapchain_create_info_and_get_next_pointer(property_values: Dictionary, next_pointer: void*) -> int`
- + method `_set_projection_views_and_get_next_pointer(view_index: int, next_pointer: void*) -> int`

#### OpenXRIPBinding
- + method `get_binding_modifier(index: int) -> OpenXRActionBindingModifier`
- + method `get_binding_modifier_count() -> int`
- + property `binding_modifiers: Array` (property)
- + property `binding_path: String` (property)
- ⚠ deprecated method `add_path(path: String)`
- ⚠ deprecated method `get_path_count() -> int`
- ⚠ deprecated method `has_path(path: String) -> bool`
- ⚠ deprecated method `remove_path(path: String)`
- ⚠ deprecated property `paths: PackedStringArray`

#### OpenXRInteractionProfile
- + method `get_binding_modifier(index: int) -> OpenXRIPBindingModifier`
- + method `get_binding_modifier_count() -> int`
- + property `binding_modifiers: Array` (property)

#### PCKPacker
- + method `add_file_removal(target_path: String) -> int`
- ~ method `add_file(pck_path: String, source_path: String, encrypt: bool = false) -> int` → `add_file(target_path: String, source_path: String, encrypt: bool = false) -> int`
- ~ method `pck_start(pck_name: String, alignment: int = 32, key: String = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory: bool = false) -> int` → `pck_start(pck_path: String, alignment: int = 32, key: String = "0000000000000000000000000000000000000000000000000000000000000000", encrypt_directory: bool = false) -> int`

#### PackedByteArray
- + method `get(index: int) -> int`

#### PackedColorArray
- + method `get(index: int) -> Color`

#### PackedFloat32Array
- + method `get(index: int) -> float`

#### PackedFloat64Array
- + method `get(index: int) -> float`

#### PackedInt32Array
- + method `get(index: int) -> int`

#### PackedInt64Array
- + method `get(index: int) -> int`

#### PackedScene
- − removed property `_bundled: Dictionary`

#### PackedStringArray
- + method `get(index: int) -> String`

#### PackedVector2Array
- + method `get(index: int) -> Vector2`

#### PackedVector3Array
- + method `get(index: int) -> Vector3`

#### PackedVector4Array
- + method `get(index: int) -> Vector4`

#### ParticleProcessMaterial
- + property `emission_ring_cone_angle: float` (property)
- + property `sub_emitter_amount_at_start: int` (property)
- + signal `emission_shape_changed()`
- + constant `SubEmitterMode.SUB_EMITTER_AT_START`

#### Performance
- + constant `Monitor.NAVIGATION_OBSTACLE_COUNT`
- + constant `Monitor.PIPELINE_COMPILATIONS_CANVAS`
- + constant `Monitor.PIPELINE_COMPILATIONS_DRAW`
- + constant `Monitor.PIPELINE_COMPILATIONS_MESH`
- + constant `Monitor.PIPELINE_COMPILATIONS_SPECIALIZATION`
- + constant `Monitor.PIPELINE_COMPILATIONS_SURFACE`

#### Polygon2D
- − removed property `bones: Array`

#### PopupMenu
- + property `transparent: bool` (property)
- + property `transparent_bg: bool` (property)

#### PopupPanel
- + property `transparent: bool` (property)
- + property `transparent_bg: bool` (property)

#### PortableCompressedTexture2D
- − removed property `_data: PackedByteArray`

#### ProjectSettings
- + property `debug/gdscript/warnings/missing_tool: int` (property)
- + property `debug/settings/physics_interpolation/enable_warnings: bool` (property)
- + property `display/window/frame_pacing/android/enable_frame_pacing: bool` (property)
- + property `display/window/frame_pacing/android/swappy_mode: int` (property)
- + property `display/window/size/sharp_corners: bool` (property)
- + property `input/ui_unicode_start: Dictionary` (property)
- + property `input_devices/sensors/enable_accelerometer: bool` (property)
- + property `input_devices/sensors/enable_gravity: bool` (property)
- + property `input_devices/sensors/enable_gyroscope: bool` (property)
- + property `input_devices/sensors/enable_magnetometer: bool` (property)
- + property `navigation/pathfinding/max_threads: int` (property)
- + property `navigation/world/map_use_async_iterations: bool` (property)
- + property `network/tls/enable_tls_v1.3: bool` (property)
- + property `physics/jolt_physics_3d/collisions/active_edge_threshold: float` (property)
- + property `physics/jolt_physics_3d/collisions/collision_margin_fraction: float` (property)
- + property `physics/jolt_physics_3d/joints/world_node: int` (property)
- + property `physics/jolt_physics_3d/limits/max_angular_velocity: float` (property)
- + property `physics/jolt_physics_3d/limits/max_bodies: int` (property)
- + property `physics/jolt_physics_3d/limits/max_body_pairs: int` (property)
- + property `physics/jolt_physics_3d/limits/max_contact_constraints: int` (property)
- + property `physics/jolt_physics_3d/limits/max_linear_velocity: float` (property)
- + property `physics/jolt_physics_3d/limits/temporary_memory_buffer_size: int` (property)
- + property `physics/jolt_physics_3d/limits/world_boundary_shape_size: float` (property)
- + property `physics/jolt_physics_3d/motion_queries/recovery_amount: float` (property)
- + property `physics/jolt_physics_3d/motion_queries/recovery_iterations: int` (property)
- + property `physics/jolt_physics_3d/motion_queries/use_enhanced_internal_edge_removal: bool` (property)
- + property `physics/jolt_physics_3d/queries/enable_ray_cast_face_index: bool` (property)
- + property `physics/jolt_physics_3d/queries/use_enhanced_internal_edge_removal: bool` (property)
- + property `physics/jolt_physics_3d/simulation/allow_sleep: bool` (property)
- + property `physics/jolt_physics_3d/simulation/areas_detect_static_bodies: bool` (property)
- + property `physics/jolt_physics_3d/simulation/baumgarte_stabilization_factor: float` (property)
- + property `physics/jolt_physics_3d/simulation/body_pair_contact_cache_angle_threshold: float` (property)
- + property `physics/jolt_physics_3d/simulation/body_pair_contact_cache_distance_threshold: float` (property)
- + property `physics/jolt_physics_3d/simulation/body_pair_contact_cache_enabled: bool` (property)
- + property `physics/jolt_physics_3d/simulation/bounce_velocity_threshold: float` (property)
- + property `physics/jolt_physics_3d/simulation/continuous_cd_max_penetration: float` (property)
- + property `physics/jolt_physics_3d/simulation/continuous_cd_movement_threshold: float` (property)
- + property `physics/jolt_physics_3d/simulation/generate_all_kinematic_contacts: bool` (property)
- + property `physics/jolt_physics_3d/simulation/penetration_slop: float` (property)
- + property `physics/jolt_physics_3d/simulation/position_steps: int` (property)
- + property `physics/jolt_physics_3d/simulation/sleep_time_threshold: float` (property)
- + property `physics/jolt_physics_3d/simulation/sleep_velocity_threshold: float` (property)
- + property `physics/jolt_physics_3d/simulation/soft_body_point_radius: float` (property)
- + property `physics/jolt_physics_3d/simulation/speculative_contact_distance: float` (property)
- + property `physics/jolt_physics_3d/simulation/use_enhanced_internal_edge_removal: bool` (property)
- + property `physics/jolt_physics_3d/simulation/velocity_steps: int` (property)
- + property `rendering/2d/batching/item_buffer_size: int` (property)
- + property `rendering/2d/batching/uniform_set_cache_size: int` (property)
- + property `rendering/lightmapping/bake_performance/max_transparency_rays: int` (property)
- + property `rendering/lightmapping/lightmap_gi/use_bicubic_filter: bool` (property)
- + property `rendering/rendering_device/fallback_to_opengl3: bool` (property)
- + property `rendering/rendering_device/staging_buffer/texture_download_region_size_px: int` (property)
- + property `rendering/scaling_3d/mode.ios: int` (property)
- + property `rendering/scaling_3d/mode.macos: int` (property)
- + property `rendering/textures/vram_compression/cache_gpu_compressor: bool` (property)
- + property `rendering/textures/vram_compression/compress_with_gpu: bool` (property)
- + property `xr/openxr/binding_modifiers/analog_threshold: bool` (property)
- + property `xr/openxr/binding_modifiers/dpad_binding: bool` (property)
- + property `xr/openxr/extensions/debug_message_types: int` (property)
- + property `xr/openxr/extensions/debug_utils: int` (property)
- + property `xr/openxr/extensions/hand_tracking_controller_data_source: bool` (property)
- + property `xr/openxr/extensions/hand_tracking_unobstructed_data_source: bool` (property)
- − removed property `display/window/energy_saving/keep_screen_on.editor_hint: bool`
- − removed property `rendering/shading/overrides/force_vertex_shading.mobile: bool`

#### Projection
- + constant `Planes.PLANE_BOTTOM`
- + constant `Planes.PLANE_FAR`
- + constant `Planes.PLANE_LEFT`
- + constant `Planes.PLANE_NEAR`
- + constant `Planes.PLANE_RIGHT`
- + constant `Planes.PLANE_TOP`
- − removed constant `PLANE_BOTTOM`
- − removed constant `PLANE_FAR`
- − removed constant `PLANE_LEFT`
- − removed constant `PLANE_NEAR`
- − removed constant `PLANE_RIGHT`
- − removed constant `PLANE_TOP`

#### RDTextureFormat
- + property `is_discardable: bool` (property)
- + property `is_resolve_buffer: bool` (property)

#### Rect2
- + method `get_support(direction: Vector2) -> Vector2`

#### ReflectionProbe
- + property `blend_distance: float` (property)

#### RegEx
- ~ method `compile(pattern: String) -> int` → `compile(pattern: String, show_error: bool = true) -> int`
- ~ method `create_from_string(pattern: String) -> RegEx` → `create_from_string(pattern: String, show_error: bool = true) -> RegEx`

#### RenderSceneBuffersConfiguration
- + property `anisotropic_filtering_level: int` (property)

#### RenderSceneBuffersExtension
- + method `_set_anisotropic_filtering_level(anisotropic_filtering_level: int)`

#### RenderSceneBuffersRD
- ~ method `create_texture(context: StringName, name: StringName, data_format: int, usage_bits: int, texture_samples: int, size: Vector2i, layers: int, mipmaps: int, unique: bool) -> RID` → `create_texture(context: StringName, name: StringName, data_format: int, usage_bits: int, texture_samples: int, size: Vector2i, layers: int, mipmaps: int, unique: bool, discardable: bool) -> RID`

#### RenderingDevice
- + method `buffer_get_data_async(buffer: RID, callback: Callable, offset_bytes: int = 0, size_bytes: int = 0) -> int`
- + method `buffer_get_device_address(buffer: RID) -> int`
- + method `draw_list_draw_indirect(draw_list: int, use_indices: bool, buffer: RID, offset: int = 0, draw_count: int = 1, stride: int = 0)`
- + method `get_device_allocation_count() -> int`
- + method `get_device_allocs_by_object_type(type: int) -> int`
- + method `get_device_memory_by_object_type(type: int) -> int`
- + method `get_device_total_memory() -> int`
- + method `get_driver_allocation_count() -> int`
- + method `get_driver_allocs_by_object_type(type: int) -> int`
- + method `get_driver_and_device_memory_report() -> String`
- + method `get_driver_memory_by_object_type(type: int) -> int`
- + method `get_driver_total_memory() -> int`
- + method `get_perf_report() -> String`
- + method `get_tracked_object_name(type_index: int) -> String`
- + method `get_tracked_object_type_count() -> int`
- + method `has_feature(feature: int) -> bool`
- + method `texture_get_data_async(texture: RID, layer: int, callback: Callable) -> int`
- + method `texture_is_discardable(texture: RID) -> bool`
- + method `texture_set_discardable(texture: RID, discardable: bool)`
- + constant `BreadcrumbMarker.ALPHA_PASS`
- + constant `BreadcrumbMarker.BLIT_PASS`
- + constant `BreadcrumbMarker.DEBUG_PASS`
- + constant `BreadcrumbMarker.LIGHTMAPPER_PASS`
- + constant `BreadcrumbMarker.NONE`
- + constant `BreadcrumbMarker.OPAQUE_PASS`
- + constant `BreadcrumbMarker.POST_PROCESSING_PASS`
- + constant `BreadcrumbMarker.REFLECTION_PROBES`
- + constant `BreadcrumbMarker.SHADOW_PASS_CUBE`
- + constant `BreadcrumbMarker.SHADOW_PASS_DIRECTIONAL`
- + constant `BreadcrumbMarker.SKY_PASS`
- + constant `BreadcrumbMarker.TRANSPARENT_PASS`
- + constant `BreadcrumbMarker.UI_PASS`
- + constant `BufferCreationBits.BUFFER_CREATION_AS_STORAGE_BIT`
- + constant `BufferCreationBits.BUFFER_CREATION_DEVICE_ADDRESS_BIT`
- + constant `DrawFlags.DRAW_CLEAR_ALL`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_0`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_1`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_2`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_3`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_4`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_5`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_6`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_7`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_ALL`
- + constant `DrawFlags.DRAW_CLEAR_COLOR_MASK`
- + constant `DrawFlags.DRAW_CLEAR_DEPTH`
- + constant `DrawFlags.DRAW_CLEAR_STENCIL`
- + constant `DrawFlags.DRAW_DEFAULT_ALL`
- + constant `DrawFlags.DRAW_IGNORE_ALL`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_0`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_1`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_2`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_3`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_4`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_5`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_6`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_7`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_ALL`
- + constant `DrawFlags.DRAW_IGNORE_COLOR_MASK`
- + constant `DrawFlags.DRAW_IGNORE_DEPTH`
- + constant `DrawFlags.DRAW_IGNORE_STENCIL`
- + constant `Features.SUPPORTS_BUFFER_DEVICE_ADDRESS`
- + constant `Limit.LIMIT_METALFX_TEMPORAL_SCALER_MAX_SCALE`
- + constant `Limit.LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE`
- ~ method `draw_list_begin(framebuffer: RID, initial_color_action: int, final_color_action: int, initial_depth_action: int, final_depth_action: int, clear_color_values: PackedColorArray = PackedColorArray(), clear_depth: float = 1.0, clear_stencil: int = 0, region: Rect2 = Rect2(0, 0, 0, 0)) -> int` → `draw_list_begin(framebuffer: RID, draw_flags: int = 0, clear_color_values: PackedColorArray = PackedColorArray(), clear_depth_value: float = 1.0, clear_stencil_value: int = 0, region: Rect2 = Rect2(0, 0, 0, 0), breadcrumb: int = 0) -> int`
- ~ method `index_buffer_create(size_indices: int, format: int, data: PackedByteArray = PackedByteArray(), use_restart_indices: bool = false) -> RID` → `index_buffer_create(size_indices: int, format: int, data: PackedByteArray = PackedByteArray(), use_restart_indices: bool = false, creation_bits: int = 0) -> RID`
- ~ method `storage_buffer_create(size_bytes: int, data: PackedByteArray = PackedByteArray(), usage: int = 0) -> RID` → `storage_buffer_create(size_bytes: int, data: PackedByteArray = PackedByteArray(), usage: int = 0, creation_bits: int = 0) -> RID`
- ~ method `uniform_buffer_create(size_bytes: int, data: PackedByteArray = PackedByteArray()) -> RID` → `uniform_buffer_create(size_bytes: int, data: PackedByteArray = PackedByteArray(), creation_bits: int = 0) -> RID`
- ~ method `vertex_buffer_create(size_bytes: int, data: PackedByteArray = PackedByteArray(), use_as_storage: bool = false) -> RID` → `vertex_buffer_create(size_bytes: int, data: PackedByteArray = PackedByteArray(), creation_bits: int = 0) -> RID`
- ⚠ deprecated constant `FinalAction.FINAL_ACTION_DISCARD`
- ⚠ deprecated constant `FinalAction.FINAL_ACTION_MAX`
- ⚠ deprecated constant `FinalAction.FINAL_ACTION_STORE`
- ⚠ deprecated constant `InitialAction.INITIAL_ACTION_CLEAR`
- ⚠ deprecated constant `InitialAction.INITIAL_ACTION_DISCARD`
- ⚠ deprecated constant `InitialAction.INITIAL_ACTION_LOAD`
- ⚠ deprecated constant `InitialAction.INITIAL_ACTION_MAX`

#### RenderingServer
- + method `canvas_item_attach_skeleton(item: RID, skeleton: RID)`
- + method `canvas_item_get_instance_shader_parameter(instance: RID, parameter: StringName) -> Variant`
- + method `canvas_item_get_instance_shader_parameter_default_value(instance: RID, parameter: StringName) -> Variant`
- + method `canvas_item_get_instance_shader_parameter_list(instance: RID) -> Dictionary[]`
- + method `canvas_item_set_instance_shader_parameter(instance: RID, parameter: StringName, value: Variant)`
- + method `environment_set_camera_id(env: RID, id: int)`
- + method `get_current_rendering_driver_name() -> String`
- + method `get_current_rendering_method() -> String`
- + method `instance_reset_physics_interpolation(instance: RID)`
- + method `instance_set_interpolated(instance: RID, interpolated: bool)`
- + method `light_set_shadow_caster_mask(light: RID, mask: int)`
- + method `lightmaps_set_bicubic_filter(enable: bool)`
- + method `mesh_surface_remove(mesh: RID, surface: int)`
- + method `multimesh_get_buffer_rd_rid(multimesh: RID) -> RID`
- + method `multimesh_get_command_buffer_rd_rid(multimesh: RID) -> RID`
- + method `multimesh_instance_reset_physics_interpolation(multimesh: RID, index: int)`
- + method `multimesh_set_buffer_interpolated(multimesh: RID, buffer: PackedFloat32Array, buffer_previous: PackedFloat32Array)`
- + method `multimesh_set_physics_interpolated(multimesh: RID, interpolated: bool)`
- + method `multimesh_set_physics_interpolation_quality(multimesh: RID, quality: int)`
- + method `particles_collision_set_height_field_mask(particles_collision: RID, mask: int)`
- + method `particles_request_process_time(particles: RID, time: float)`
- + method `reflection_probe_set_blend_distance(probe: RID, blend_distance: float)`
- + method `texture_create_from_native_handle(type: int, format: int, native_handle: int, width: int, height: int, depth: int, layers: int = 1, layered_type: int = 0) -> RID`
- + method `viewport_set_anisotropic_filtering_level(viewport: RID, anisotropic_filtering_level: int)`
- + constant `EnvironmentToneMapper.ENV_TONE_MAPPER_AGX`
- + constant `GlobalShaderParameterType.GLOBAL_VAR_TYPE_SAMPLEREXT`
- + constant `MultimeshPhysicsInterpolationQuality.MULTIMESH_INTERP_QUALITY_FAST`
- + constant `MultimeshPhysicsInterpolationQuality.MULTIMESH_INTERP_QUALITY_HIGH`
- + constant `PipelineSource.PIPELINE_SOURCE_CANVAS`
- + constant `PipelineSource.PIPELINE_SOURCE_DRAW`
- + constant `PipelineSource.PIPELINE_SOURCE_MAX`
- + constant `PipelineSource.PIPELINE_SOURCE_MESH`
- + constant `PipelineSource.PIPELINE_SOURCE_SPECIALIZATION`
- + constant `PipelineSource.PIPELINE_SOURCE_SURFACE`
- + constant `RenderingInfo.RENDERING_INFO_PIPELINE_COMPILATIONS_CANVAS`
- + constant `RenderingInfo.RENDERING_INFO_PIPELINE_COMPILATIONS_DRAW`
- + constant `RenderingInfo.RENDERING_INFO_PIPELINE_COMPILATIONS_MESH`
- + constant `RenderingInfo.RENDERING_INFO_PIPELINE_COMPILATIONS_SPECIALIZATION`
- + constant `RenderingInfo.RENDERING_INFO_PIPELINE_COMPILATIONS_SURFACE`
- + constant `TextureType.TEXTURE_TYPE_2D`
- + constant `TextureType.TEXTURE_TYPE_3D`
- + constant `TextureType.TEXTURE_TYPE_LAYERED`
- + constant `ViewportAnisotropicFiltering.VIEWPORT_ANISOTROPY_16X`
- + constant `ViewportAnisotropicFiltering.VIEWPORT_ANISOTROPY_2X`
- + constant `ViewportAnisotropicFiltering.VIEWPORT_ANISOTROPY_4X`
- + constant `ViewportAnisotropicFiltering.VIEWPORT_ANISOTROPY_8X`
- + constant `ViewportAnisotropicFiltering.VIEWPORT_ANISOTROPY_DISABLED`
- + constant `ViewportAnisotropicFiltering.VIEWPORT_ANISOTROPY_MAX`
- + constant `ViewportScaling3DMode.VIEWPORT_SCALING_3D_MODE_METALFX_SPATIAL`
- + constant `ViewportScaling3DMode.VIEWPORT_SCALING_3D_MODE_METALFX_TEMPORAL`
- ~ method `environment_set_ambient_light(env: RID, color: Color, ambient: int = 0, energy: float = 1.0, sky_contibution: float = 0.0, reflection_source: int = 0)` → `environment_set_ambient_light(env: RID, color: Color, ambient: int = 0, energy: float = 1.0, sky_contribution: float = 0.0, reflection_source: int = 0)`
- ~ method `multimesh_allocate_data(multimesh: RID, instances: int, transform_format: int, color_format: bool = false, custom_data_format: bool = false)` → `multimesh_allocate_data(multimesh: RID, instances: int, transform_format: int, color_format: bool = false, custom_data_format: bool = false, use_indirect: bool = false)`

#### Resource
- + method `_reset_state()`
- + method `_set_path_cache(path: String)`
- + method `get_id_for_path(path: String) -> String`
- + method `is_built_in() -> bool`
- + method `reset_state()`
- + method `set_id_for_path(path: String, id: String)`
- + method `set_path_cache(path: String)`

#### ResourceImporterDynamicFont
- + property `keep_rounding_remainders: bool` (property)

#### ResourceImporterOBJ
- + property `generate_lightmap_uv2: bool` (property)
- + property `generate_lightmap_uv2_texel_size: float` (property)
- + property `generate_lods: bool` (property)
- + property `generate_shadow_mesh: bool` (property)
- − removed property `optimize_mesh: bool`

#### ResourceImporterOggVorbis
- ~ method `load_from_buffer(buffer: PackedByteArray) -> AudioStreamOggVorbis` → `load_from_buffer(stream_data: PackedByteArray) -> AudioStreamOggVorbis`
- ⚠ deprecated method `load_from_buffer(stream_data: PackedByteArray) -> AudioStreamOggVorbis`
- ⚠ deprecated method `load_from_file(path: String) -> AudioStreamOggVorbis`

#### ResourceImporterScene
- + property `nodes/use_node_type_suffixes: bool` (property)

#### ResourceLoader
- + method `get_cached_ref(path: String) -> Resource`
- + method `list_directory(directory_path: String) -> PackedStringArray`

#### ResourceSaver
- + method `get_resource_id_for_path(path: String, generate: bool = false) -> int`

#### RichTextLabel
- + method `get_line_range(line: int) -> Vector2i`
- + method `get_selection_line_offset() -> float`
- + method `is_finished() -> bool`
- + property `horizontal_alignment: int` (property)
- + property `justification_flags: int` (property)
- + property `tab_stops: PackedFloat32Array` (property)
- + property `vertical_alignment: int` (property)
- ~ method `push_meta(data: Variant, underline_mode: int = 1)` → `push_meta(data: Variant, underline_mode: int = 1, tooltip: String = "")`
- ~ method `set_table_column_expand(column: int, expand: bool, ratio: int = 1)` → `set_table_column_expand(column: int, expand: bool, ratio: int = 1, shrink: bool = true)`
- ⚠ deprecated method `is_ready() -> bool`

#### Script
- + method `get_rpc_config() -> Variant`

#### ScriptEditor
- + method `get_breakpoints() -> PackedStringArray`
- + method `update_docs_from_script(script: Script)`

#### ScriptExtension
- + method `_get_doc_class_name() -> StringName`

#### ScriptLanguageExtension
- + method `_reload_scripts(scripts: Array, soft_reload: bool)`
- + constant `LookupResultType.LOOKUP_RESULT_LOCAL_CONSTANT`
- + constant `LookupResultType.LOOKUP_RESULT_LOCAL_VARIABLE`
- ⚠ deprecated constant `LookupResultType.LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE`

#### ScrollContainer
- + property `draw_focus_border: bool` (property)
- + constant `ScrollMode.SCROLL_MODE_RESERVE`

#### Semaphore
- ~ method `post()` → `post(count: int = 1)`

#### Shader
- + method `inspect_native_shader_code()`
- ~ method `get_default_texture_parameter(name: StringName, index: int = 0) -> Texture2D` → `get_default_texture_parameter(name: StringName, index: int = 0) -> Texture`
- ~ method `set_default_texture_parameter(name: StringName, texture: Texture2D, index: int = 0)` → `set_default_texture_parameter(name: StringName, texture: Texture, index: int = 0)`

#### Signal
- + method `has_connections() -> bool`

#### Skeleton3D
- + method `get_bone_meta(bone_idx: int, key: StringName) -> Variant`
- + method `get_bone_meta_list(bone_idx: int) -> StringName[]`
- + method `has_bone_meta(bone_idx: int, key: StringName) -> bool`
- + method `set_bone_meta(bone_idx: int, key: StringName, value: Variant)`
- + signal `rest_updated()`

#### SkeletonModifier3D
- + constant `BoneAxis.BONE_AXIS_MINUS_X`
- + constant `BoneAxis.BONE_AXIS_MINUS_Y`
- + constant `BoneAxis.BONE_AXIS_MINUS_Z`
- + constant `BoneAxis.BONE_AXIS_PLUS_X`
- + constant `BoneAxis.BONE_AXIS_PLUS_Y`
- + constant `BoneAxis.BONE_AXIS_PLUS_Z`

#### SoftBody3D
- ~ method `set_point_pinned(point_index: int, pinned: bool, attachment_path: NodePath = NodePath(""))` → `set_point_pinned(point_index: int, pinned: bool, attachment_path: NodePath = NodePath(""), insert_at: int = -1)`

#### SplitContainer
- + method `get_drag_area_control() -> Control`
- + property `drag_area_highlight_in_editor: bool` (property)
- + property `drag_area_margin_begin: int` (property)
- + property `drag_area_margin_end: int` (property)
- + property `drag_area_offset: int` (property)
- + property `dragging_enabled: bool` (property)
- + signal `drag_ended()`
- + signal `drag_started()`

#### SpotLight3D
- + property `light_specular: float` (property)

#### SpriteFrames
- + method `duplicate_animation(anim_from: StringName, anim_to: StringName)`

#### StreamPeer
- + method `get_half() -> float`
- + method `put_half(value: float)`

#### String
- + method `is_valid_ascii_identifier() -> bool`
- + method `is_valid_unicode_identifier() -> bool`
- ⚠ deprecated method `is_valid_identifier() -> bool`

#### StringName
- + method `is_valid_ascii_identifier() -> bool`
- + method `is_valid_unicode_identifier() -> bool`
- ⚠ deprecated method `is_valid_identifier() -> bool`

#### SubViewportContainer
- + property `mouse_target: bool` (property)

#### SystemFont
- + property `keep_rounding_remainders: bool` (property)

#### TextEdit
- + method `get_line_with_ime(line: int) -> String`
- + property `emoji_menu_enabled: bool` (property)
- + property `empty_selection_clipboard_enabled: bool` (property)
- + property `scroll_fit_content_width: bool` (property)
- + constant `MenuItems.MENU_EMOJI_AND_SYMBOL`
- ~ method `get_line_column_at_pos(position: Vector2i, allow_out_of_bounds: bool = true) -> Vector2i` → `get_line_column_at_pos(position: Vector2i, clamp_line: bool = true, clamp_column: bool = true) -> Vector2i`

#### TextParagraph
- + property `line_spacing: float` (property)

#### TextServer
- + method `font_get_keep_rounding_remainders(font_rid: RID) -> bool`
- + method `font_get_supported_glyphs(font_rid: RID) -> PackedInt32Array`
- + method `font_set_keep_rounding_remainders(font_rid: RID, keep_rounding_remainders: bool)`
- + method `get_support_data() -> PackedByteArray`
- + method `shaped_get_span_embedded_object(shaped: RID, index: int) -> Variant`

#### TextServerExtension
- + method `_font_get_keep_rounding_remainders(font_rid: RID) -> bool`
- + method `_font_get_supported_glyphs(font_rid: RID) -> PackedInt32Array`
- + method `_font_set_keep_rounding_remainders(font_rid: RID, keep_rounding_remainders: bool)`
- + method `_get_support_data() -> PackedByteArray`
- + method `_shaped_get_span_embedded_object(shaped: RID, index: int) -> Variant`

#### TileData
- + method `add_occluder_polygon(layer_id: int)`
- + method `get_occluder_polygon(layer_id: int, polygon_index: int, flip_h: bool = false, flip_v: bool = false, transpose: bool = false) -> OccluderPolygon2D`
- + method `get_occluder_polygons_count(layer_id: int) -> int`
- + method `has_custom_data(layer_name: String) -> bool`
- + method `remove_occluder_polygon(layer_id: int, polygon_index: int)`
- + method `set_occluder_polygon(layer_id: int, polygon_index: int, polygon: OccluderPolygon2D)`
- + method `set_occluder_polygons_count(layer_id: int, polygons_count: int)`
- ⚠ deprecated method `get_occluder(layer_id: int, flip_h: bool = false, flip_v: bool = false, transpose: bool = false) -> OccluderPolygon2D`
- ⚠ deprecated method `set_occluder(layer_id: int, occluder_polygon: OccluderPolygon2D)`

#### TileMap
- + method `is_cell_flipped_h(layer: int, coords: Vector2i, use_proxies: bool = false) -> bool`
- + method `is_cell_flipped_v(layer: int, coords: Vector2i, use_proxies: bool = false) -> bool`
- + method `is_cell_transposed(layer: int, coords: Vector2i, use_proxies: bool = false) -> bool`

#### TileMapLayer
- + method `_update_cells(coords: Vector2i[], forced_cleanup: bool)`
- + method `is_cell_flipped_h(coords: Vector2i) -> bool`
- + method `is_cell_flipped_v(coords: Vector2i) -> bool`
- + method `is_cell_transposed(coords: Vector2i) -> bool`
- + property `occlusion_enabled: bool` (property)

#### TileSet
- + method `get_physics_layer_collision_priority(layer_index: int) -> float`
- + method `has_custom_data_layer_by_name(layer_name: String) -> bool`
- + method `set_physics_layer_collision_priority(layer_index: int, priority: float)`

#### Timer
- + property `ignore_time_scale: bool` (property)

#### TranslationServer
- + method `get_or_add_domain(domain: StringName) -> TranslationDomain`
- + method `has_domain(domain: StringName) -> bool`
- + method `remove_domain(domain: StringName)`
- ~ method `standardize_locale(locale: String) -> String` → `standardize_locale(locale: String, add_defaults: bool = false) -> String`

#### Tree
- + property `auto_tooltip: bool` (property)

#### TreeItem
- + method `clear_buttons()`
- + method `get_auto_translate_mode(column: int) -> int`
- + method `get_icon_overlay(column: int) -> Texture2D`
- + method `set_auto_translate_mode(column: int, mode: int)`
- + method `set_icon_overlay(column: int, texture: Texture2D)`

#### Tween
- + method `set_ignore_time_scale(ignore: bool = true) -> Tween`
- + method `tween_subtween(subtween: Tween) -> SubtweenTweener`

#### Vector2
- + constant `Axis.AXIS_X`
- + constant `Axis.AXIS_Y`
- − removed constant `AXIS_X`
- − removed constant `AXIS_Y`

#### Vector2i
- + constant `Axis.AXIS_X`
- + constant `Axis.AXIS_Y`
- − removed constant `AXIS_X`
- − removed constant `AXIS_Y`

#### Vector3
- + constant `Axis.AXIS_X`
- + constant `Axis.AXIS_Y`
- + constant `Axis.AXIS_Z`
- − removed constant `AXIS_X`
- − removed constant `AXIS_Y`
- − removed constant `AXIS_Z`

#### Vector3i
- + constant `Axis.AXIS_X`
- + constant `Axis.AXIS_Y`
- + constant `Axis.AXIS_Z`
- − removed constant `AXIS_X`
- − removed constant `AXIS_Y`
- − removed constant `AXIS_Z`

#### Vector4
- + constant `Axis.AXIS_W`
- + constant `Axis.AXIS_X`
- + constant `Axis.AXIS_Y`
- + constant `Axis.AXIS_Z`
- − removed constant `AXIS_W`
- − removed constant `AXIS_X`
- − removed constant `AXIS_Y`
- − removed constant `AXIS_Z`

#### Vector4i
- + constant `Axis.AXIS_W`
- + constant `Axis.AXIS_X`
- + constant `Axis.AXIS_Y`
- + constant `Axis.AXIS_Z`
- − removed constant `AXIS_W`
- − removed constant `AXIS_X`
- − removed constant `AXIS_Y`
- − removed constant `AXIS_Z`

#### VehicleWheel3D
- + method `get_contact_normal() -> Vector3`
- + method `get_contact_point() -> Vector3`

#### Viewport
- + method `get_audio_listener_2d() -> AudioListener2D`
- + method `get_audio_listener_3d() -> AudioListener3D`
- + method `get_stretch_transform() -> Transform2D`
- + method `gui_cancel_drag()`
- + method `notify_mouse_entered()`
- + method `notify_mouse_exited()`
- + property `anisotropic_filtering_level: int` (property)
- + property `physics_interpolation_mode: int` (property)
- + constant `AnisotropicFiltering.ANISOTROPY_16X`
- + constant `AnisotropicFiltering.ANISOTROPY_2X`
- + constant `AnisotropicFiltering.ANISOTROPY_4X`
- + constant `AnisotropicFiltering.ANISOTROPY_8X`
- + constant `AnisotropicFiltering.ANISOTROPY_DISABLED`
- + constant `AnisotropicFiltering.ANISOTROPY_MAX`
- + constant `Scaling3DMode.SCALING_3D_MODE_METALFX_SPATIAL`
- + constant `Scaling3DMode.SCALING_3D_MODE_METALFX_TEMPORAL`

#### VisualShaderNodeColorFunc
- + constant `Function.FUNC_LINEAR_TO_SRGB`
- + constant `Function.FUNC_SRGB_TO_LINEAR`

#### VisualShaderNodeIntParameter
- + property `enum_names: PackedStringArray` (property)
- + constant `Hint.HINT_ENUM`

#### VisualShaderNodeRemap
- + property `op_type: int` (property)
- + constant `OpType.OP_TYPE_MAX`
- + constant `OpType.OP_TYPE_SCALAR`
- + constant `OpType.OP_TYPE_VECTOR_2D`
- + constant `OpType.OP_TYPE_VECTOR_2D_SCALAR`
- + constant `OpType.OP_TYPE_VECTOR_3D`
- + constant `OpType.OP_TYPE_VECTOR_3D_SCALAR`
- + constant `OpType.OP_TYPE_VECTOR_4D`
- + constant `OpType.OP_TYPE_VECTOR_4D_SCALAR`

#### WebSocketPeer
- + property `heartbeat_interval: float` (property)

#### Window
- + method `start_drag()`
- + method `start_resize(edge: int)`
- + property `exclude_from_capture: bool` (property)
- + property `sharp_corners: bool` (property)
- + signal `title_changed()`
- + constant `Flags.FLAG_EXCLUDE_FROM_CAPTURE`
- + constant `Flags.FLAG_SHARP_CORNERS`
- + constant `LayoutDirection.LAYOUT_DIRECTION_APPLICATION_LOCALE`
- + constant `LayoutDirection.LAYOUT_DIRECTION_MAX`
- + constant `LayoutDirection.LAYOUT_DIRECTION_SYSTEM_LOCALE`
- ⚠ deprecated constant `LayoutDirection.LAYOUT_DIRECTION_LOCALE`

#### XRHandTracker
- + constant `HandTrackingSource.HAND_TRACKING_SOURCE_NOT_TRACKED`

#### XRServer
- + property `camera_locked_to_origin: bool` (property)

#### XRVRS
- + property `vrs_render_region: Rect2i` (property)
