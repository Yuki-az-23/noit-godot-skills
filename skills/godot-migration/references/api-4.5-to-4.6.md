# Godot engine API changes (4.5-stable → 4.6-stable)

> Derived from the Godot Engine class reference (MIT License, © Godot Engine contributors, Juan Linietsky, Ariel Manzur). See `licenses/GODOT-LICENSE.txt` at the plugin root.

Generated from the engine's own class reference XML (doc/classes and modules/*/doc_classes) at each release tag. `+` added, `~` signature changed, `⚠` newly deprecated, `−` removed.

- 4.5-stable: 1006 classes
- 4.6-stable: 1058 classes

## 4.5-stable → 4.6-stable

### New classes (52)

- **BoneTwistDisperser3D** ← SkeletonModifier3D: A node that propagates and disperses the child bone's twist to the parent bones.
- **CCDIK3D** ← IterateIK3D: Rotation based cyclic coordinate descent inverse kinematics solver.
- **ChainIK3D** ← IKModifier3D: A [SkeletonModifier3D] to apply inverse kinematics to bone chains containing an arbitrary number of bones.
- **EditorDock** ← MarginContainer *(experimental)*: Dockable container for the editor.
- **FABRIK3D** ← IterateIK3D: Position based forward and backward reaching inverse kinematics solver.
- **GodotInstance** ← Object: Provides access to an embedded Godot instance.
- **IKModifier3D** ← SkeletonModifier3D: A node for inverse kinematics which may modify more than one bone.
- **IterateIK3D** ← ChainIK3D: A [SkeletonModifier3D] to approach the goal by repeating small rotations.
- **JacobianIK3D** ← IterateIK3D: Jacobian transpose based inverse kinematics solver.
- **JointLimitation3D** ← Resource: A base class of the limitation that interacts with [ChainIK3D].
- **JointLimitationCone3D** ← JointLimitation3D: A cone shape limitation that interacts with [ChainIK3D].
- **LimitAngularVelocityModifier3D** ← SkeletonModifier3D: Limit bone rotation angular velocity.
- **NavigationServer2DManager** ← Object: A singleton for managing [NavigationServer2D] implementations.
- **NavigationServer3DManager** ← Object: A singleton for managing [NavigationServer3D] implementations.
- **OpenXRAnchorTracker** ← OpenXRSpatialEntityTracker *(experimental)*: Positional tracker for our spatial entity anchor extension.
- **OpenXRAndroidThreadSettingsExtension** ← OpenXRExtensionWrapper: Wraps the [url=https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_KHR_android_thread_settings]XR_KHR_android_thread_settings[/url] extension.
- **OpenXRFrameSynthesisExtension** ← OpenXRExtensionWrapper: The OpenXR Frame synthesis extension allows for advanced reprojection at low(er) framerates.
- **OpenXRMarkerTracker** ← OpenXRSpatialEntityTracker *(experimental)*: Spatial entity tracker for our spatial entity marker tracking extension.
- **OpenXRPlaneTracker** ← OpenXRSpatialEntityTracker *(experimental)*: Spatial entity tracker for our spatial entity plane tracking extension.
- **OpenXRSpatialAnchorCapability** ← OpenXRExtensionWrapper *(experimental)*: Implementation for handling spatial entity anchor logic.
- **OpenXRSpatialCapabilityConfigurationAnchor** ← OpenXRSpatialCapabilityConfigurationBaseHeader *(experimental)*: Configuration header for spatial anchors.
- **OpenXRSpatialCapabilityConfigurationAprilTag** ← OpenXRSpatialCapabilityConfigurationBaseHeader *(experimental)*: Configuration header for April tag markers.
- **OpenXRSpatialCapabilityConfigurationAruco** ← OpenXRSpatialCapabilityConfigurationBaseHeader *(experimental)*: Configuration header for Aruco markers.
- **OpenXRSpatialCapabilityConfigurationBaseHeader** ← RefCounted *(experimental)*: Wrapper base class for OpenXR Spatial Capability Configuration headers.
- **OpenXRSpatialCapabilityConfigurationMicroQrCode** ← OpenXRSpatialCapabilityConfigurationBaseHeader *(experimental)*: Configuration header for QR code markers.
- **OpenXRSpatialCapabilityConfigurationPlaneTracking** ← OpenXRSpatialCapabilityConfigurationBaseHeader *(experimental)*: Configuration header for plane tracking.
- **OpenXRSpatialCapabilityConfigurationQrCode** ← OpenXRSpatialCapabilityConfigurationBaseHeader *(experimental)*: Configuration header for micro QR code markers.
- **OpenXRSpatialComponentAnchorList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries anchor result data.
- **OpenXRSpatialComponentBounded2DList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries bounded2d result data.
- **OpenXRSpatialComponentBounded3DList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries bounded3d result data.
- **OpenXRSpatialComponentData** ← RefCounted *(experimental)*: Object for storing OpenXR spatial entity component data.
- **OpenXRSpatialComponentMarkerList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries marker result data.
- **OpenXRSpatialComponentMesh2DList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries mesh2d result data.
- **OpenXRSpatialComponentMesh3DList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries mesh3d result data.
- **OpenXRSpatialComponentParentList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries parent result data.
- **OpenXRSpatialComponentPersistenceList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the query persistence result data.
- **OpenXRSpatialComponentPlaneAlignmentList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries plane alignment result data.
- **OpenXRSpatialComponentPlaneSemanticLabelList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries plane semantic label result data.
- **OpenXRSpatialComponentPolygon2DList** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the queries polygon2d result data.
- **OpenXRSpatialContextPersistenceConfig** ← OpenXRStructureBase *(experimental)*: Configuration header for spatial persistence.
- **OpenXRSpatialEntityExtension** ← OpenXRExtensionWrapper *(experimental)*: OpenXR extension that handles spatial entities.
- **OpenXRSpatialEntityTracker** ← XRPositionalTracker *(experimental)*: Base class for Positional trackers managed by OpenXR's spatial entity extensions.
- **OpenXRSpatialMarkerTrackingCapability** ← OpenXRExtensionWrapper *(experimental)*: Implementation for handling spatial entity marker tracking logic.
- **OpenXRSpatialPlaneTrackingCapability** ← OpenXRExtensionWrapper *(experimental)*: Implementation for handling spatial entity plane tracking logic.
- **OpenXRSpatialQueryResultData** ← OpenXRSpatialComponentData *(experimental)*: Object for storing the main query result data.
- **OpenXRStructureBase** ← RefCounted: Object for storing OpenXR structure data.
- **SocketServer** ← RefCounted: An abstract class for servers based on sockets.
- **SplineIK3D** ← ChainIK3D: A [SkeletonModifier3D] for aligning bones along a [Path3D].
- **StreamPeerSocket** ← StreamPeer: Abstract base class for interacting with socket streams.
- **StreamPeerUDS** ← StreamPeerSocket: A stream peer that handles UNIX Domain Socket (UDS) connections.
- **TwoBoneIK3D** ← IKModifier3D: Rotation based intersection of two circles inverse kinematics solver.
- **UDSServer** ← SocketServer: A Unix Domain Socket (UDS) server.

### Changed classes (82)

#### @GlobalScope
- + property `NavigationServer2DManager: NavigationServer2DManager` (property)
- + property `NavigationServer3DManager: NavigationServer3DManager` (property)

#### AimModifier3D
- + method `is_relative(index: int) -> bool`
- + method `set_relative(index: int, enabled: bool)`

#### AnimationNodeOneShot
- + property `abort_on_reset: bool` (property)

#### AnimationNodeStateMachinePlayback
- + method `get_fading_from_length() -> float`
- + method `get_fading_from_play_position() -> float`
- + method `get_fading_length() -> float`
- + method `get_fading_position() -> float`

#### AnimationPlayer
- + method `is_animation_active() -> bool`
- ~ method `get_queue() -> PackedStringArray` → `get_queue() -> StringName[]`
- ~ signal `current_animation_changed(name: String)` → `current_animation_changed(name: StringName)`

#### AudioServer
- + method `get_input_buffer_length_frames() -> int`
- + method `get_input_frames(frames: int) -> PackedVector2Array`
- + method `get_input_frames_available() -> int`
- + method `set_input_device_active(active: bool) -> int`

#### AudioStreamRandomizer
- + property `random_pitch_semitones: float` (property)

#### BoneConstraint3D
- + method `get_reference_node(index: int) -> NodePath`
- + method `get_reference_type(index: int) -> int`
- + method `set_reference_node(index: int, node: NodePath)`
- + method `set_reference_type(index: int, type: int)`
- + constant `ReferenceType.REFERENCE_TYPE_BONE`
- + constant `ReferenceType.REFERENCE_TYPE_NODE`

#### CPUParticles2D
- + property `emission_ring_inner_radius: float` (property)
- + property `emission_ring_radius: float` (property)
- + constant `EmissionShape.EMISSION_SHAPE_RING`

#### CameraFeed
- + method `set_ycbcr_images(y_image: Image, cbcr_image: Image)`

#### CanvasItem
- + method `draw_ellipse(position: Vector2, major: float, minor: float, color: Color, filled: bool = true, width: float = -1.0, antialiased: bool = false)`
- + method `draw_ellipse_arc(center: Vector2, major: float, minor: float, start_angle: float, end_angle: float, point_count: int, color: Color, width: float = -1.0, antialiased: bool = false)`

#### CodeEdit
- + property `gutters_line_numbers_min_digits: int` (property)

#### Control
- + method `get_combined_pivot_offset() -> Vector2`
- + property `pivot_offset_ratio: Vector2` (property)
- ~ method `grab_focus()` → `grab_focus(hide_focus: bool = false)`
- ~ method `has_focus() -> bool` → `has_focus(ignore_hidden_focus: bool = false) -> bool`

#### DisplayServer
- + method `window_set_color(color: Color)`
- ~ method `accessibility_create_sub_text_edit_elements(parent_rid: RID, shaped_text: RID, min_height: float, insert_pos: int = -1) -> RID` → `accessibility_create_sub_text_edit_elements(parent_rid: RID, shaped_text: RID, min_height: float, insert_pos: int = -1, is_last_line: bool = false) -> RID`

#### EditorExportPlatformExtension
- + method `_initialize()`

#### EditorFeatureProfile
- + constant `Feature.FEATURE_GROUPS_DOCK`
- + constant `Feature.FEATURE_SIGNALS_DOCK`
- ⚠ deprecated constant `Feature.FEATURE_NODE_DOCK`

#### EditorFileDialog
- ⚠ deprecated method `add_side_menu(menu: Control, title: String = "")`
- ⚠ deprecated property `disable_overwrite_warning: bool`
- − removed method `add_filter(filter: String, description: String = "")`
- − removed method `add_option(name: String, values: PackedStringArray, default_value_index: int)`
- − removed method `clear_filename_filter()`
- − removed method `clear_filters()`
- − removed method `get_filename_filter() -> String`
- − removed method `get_line_edit() -> LineEdit`
- − removed method `get_option_default(option: int) -> int`
- − removed method `get_option_name(option: int) -> String`
- − removed method `get_option_values(option: int) -> PackedStringArray`
- − removed method `get_selected_options() -> Dictionary`
- − removed method `get_vbox() -> VBoxContainer`
- − removed method `invalidate()`
- − removed method `popup_file_dialog()`
- − removed method `set_filename_filter(filter: String)`
- − removed method `set_option_default(option: int, default_value_index: int)`
- − removed method `set_option_name(option: int, name: String)`
- − removed method `set_option_values(option: int, values: PackedStringArray)`
- − removed property `access: int`
- − removed property `current_dir: String`
- − removed property `current_file: String`
- − removed property `current_path: String`
- − removed property `dialog_hide_on_ok: bool`
- − removed property `display_mode: int`
- − removed property `file_mode: int`
- − removed property `filters: PackedStringArray`
- − removed property `option_count: int`
- − removed property `show_hidden_files: bool`
- − removed property `title: String`
- − removed signal `dir_selected(dir: String)`
- − removed signal `file_selected(path: String)`
- − removed signal `filename_filter_changed(filter: String)`
- − removed signal `files_selected(paths: PackedStringArray)`
- − removed constant `Access.ACCESS_FILESYSTEM`
- − removed constant `Access.ACCESS_RESOURCES`
- − removed constant `Access.ACCESS_USERDATA`
- − removed constant `DisplayMode.DISPLAY_LIST`
- − removed constant `DisplayMode.DISPLAY_THUMBNAILS`
- − removed constant `FileMode.FILE_MODE_OPEN_ANY`
- − removed constant `FileMode.FILE_MODE_OPEN_DIR`
- − removed constant `FileMode.FILE_MODE_OPEN_FILE`
- − removed constant `FileMode.FILE_MODE_OPEN_FILES`
- − removed constant `FileMode.FILE_MODE_SAVE_FILE`

#### EditorInterface
- + method `add_root_node(node: Node)`
- + method `get_editor_language() -> String`
- + method `get_node_3d_rotate_snap() -> float`
- + method `get_node_3d_scale_snap() -> float`
- + method `get_node_3d_translate_snap() -> float`
- + method `is_node_3d_snap_enabled() -> bool`
- + method `is_object_edited(object: Object) -> bool`
- + method `set_object_edited(object: Object, edited: bool)`

#### EditorPlugin
- + method `_run_scene(scene: String, args: PackedStringArray) -> PackedStringArray`
- + method `add_dock(dock: EditorDock)`
- + method `remove_dock(dock: EditorDock)`
- + constant `DockSlot.DOCK_SLOT_BOTTOM`
- + constant `DockSlot.DOCK_SLOT_NONE`
- ⚠ deprecated method `add_control_to_bottom_panel(control: Control, title: String, shortcut: Shortcut = null) -> Button`
- ⚠ deprecated method `add_control_to_dock(slot: int, control: Control, shortcut: Shortcut = null)`
- ⚠ deprecated method `remove_control_from_bottom_panel(control: Control)`
- ⚠ deprecated method `remove_control_from_docks(control: Control)`
- ⚠ deprecated method `set_dock_tab_icon(control: Control, icon: Texture2D)`

#### EditorResourcePreviewGenerator
- + method `request_draw_and_wait(viewport: RID)`

#### EditorScript
- ⚠ deprecated method `add_root_node(node: Node)`
- ⚠ deprecated method `get_scene() -> Node`

#### EditorSettings
- + method `add_shortcut(path: String, shortcut: Shortcut)`
- + method `get_shortcut(path: String) -> Shortcut`
- + method `get_shortcut_list() -> PackedStringArray`
- + method `has_shortcut(path: String) -> bool`
- + method `is_shortcut(path: String, event: InputEvent) -> bool`
- + method `remove_shortcut(path: String)`
- + property `editors/2d/auto_resample_delay: float` (property)
- + property `editors/3d/navigation_feel/angle_snap_threshold: float` (property)
- + property `editors/3d/show_gizmo_during_rotation: int` (property)
- + property `editors/3d_gizmos/gizmo_colors/ik_chain: Color` (property)
- + property `editors/animation/insert_at_current_time: bool` (property)
- + property `filesystem/on_save/warn_on_saving_large_text_resources: bool` (property)
- + property `filesystem/quick_open_dialog/instant_preview: bool` (property)
- + property `interface/editor/bottom_dock_tab_style: int` (property)
- + property `interface/editor/dragging_hover_wait_seconds: float` (property)
- + property `interface/editor/main_font_custom_opentype_features: String` (property)
- + property `interface/inspector/integer_drag_speed: float` (property)
- + property `interface/scene_tabs/auto_select_current_scene_file: bool` (property)
- + property `interface/theme/color_preset: String` (property)
- + property `interface/theme/draw_relationship_lines: int` (property)
- + property `interface/theme/style: String` (property)
- + property `text_editor/theme/highlighting/string_placeholder_color: Color` (property)
- − removed property `editors/grid_map/palette_min_width: int`
- − removed property `interface/theme/preset: String`

#### EditorSpinSlider
- + property `control_state: int` (property)
- + constant `ControlState.CONTROL_STATE_DEFAULT`
- + constant `ControlState.CONTROL_STATE_HIDE`
- + constant `ControlState.CONTROL_STATE_PREFER_SLIDER`
- ⚠ deprecated property `hide_slider: bool`

#### Environment
- + property `tonemap_agx_contrast: float` (property)
- + property `tonemap_agx_white: float` (property)

#### FileAccess
- + method `get_extended_attribute(file: String, attribute_name: String) -> PackedByteArray`
- + method `get_extended_attribute_string(file: String, attribute_name: String) -> String`
- + method `get_extended_attributes_list(file: String) -> PackedStringArray`
- + method `remove_extended_attribute(file: String, attribute_name: String) -> int`
- + method `set_extended_attribute(file: String, attribute_name: String, data: PackedByteArray) -> int`
- + method `set_extended_attribute_string(file: String, attribute_name: String, data: String) -> int`
- ~ method `get_as_text(skip_cr: bool = false) -> String` → `get_as_text() -> String`

#### FileDialog
- + method `get_favorite_list() -> PackedStringArray`
- + method `get_recent_list() -> PackedStringArray`
- + method `popup_file_dialog()`
- + method `set_favorite_list(favorites: PackedStringArray)`
- + method `set_get_icon_callback(callback: Callable)`
- + method `set_get_thumbnail_callback(callback: Callable)`
- + method `set_recent_list(recents: PackedStringArray)`
- + property `deleting_enabled: bool` (property)
- + property `overwrite_warning_enabled: bool` (property)
- + constant `Customization.CUSTOMIZATION_DELETE`
- + constant `Customization.CUSTOMIZATION_OVERWRITE_WARNING`
- ~ method `add_filter(filter: String, description: String = "")` → `add_filter(filter: String, description: String = "", mime_type: String = "")`

#### FileSystemDock
- + signal `selection_changed()`

#### GDExtensionManager
- + method `load_extension_from_function(path: String, init_func: const GDExtensionInitializationFunction*) -> int`

#### GLTFAccessor
- + method `from_dictionary(dictionary: Dictionary) -> GLTFAccessor`
- + method `to_dictionary() -> Dictionary`

#### GLTFBufferView
- + method `from_dictionary(dictionary: Dictionary) -> GLTFBufferView`
- + method `to_dictionary() -> Dictionary`

#### GLTFState
- + property `handle_binary_image_mode: int` (property)
- + constant `HandleBinaryImageMode.HANDLE_BINARY_IMAGE_MODE_DISCARD_TEXTURES`
- + constant `HandleBinaryImageMode.HANDLE_BINARY_IMAGE_MODE_EMBED_AS_BASISU`
- + constant `HandleBinaryImageMode.HANDLE_BINARY_IMAGE_MODE_EMBED_AS_UNCOMPRESSED`
- + constant `HandleBinaryImageMode.HANDLE_BINARY_IMAGE_MODE_EXTRACT_TEXTURES`
- ~ method `get_animation_player(idx: int) -> AnimationPlayer` → `get_animation_player(anim_player_index: int) -> AnimationPlayer`
- ~ method `get_animation_players_count(idx: int) -> int` → `get_animation_players_count(anim_player_index: int) -> int`
- ~ method `get_scene_node(idx: int) -> Node` → `get_scene_node(gltf_node_index: int) -> Node`
- ⚠ deprecated method `get_handle_binary_image() -> int`
- ⚠ deprecated method `set_handle_binary_image(method: int)`
- ⚠ deprecated constant `HANDLE_BINARY_DISCARD_TEXTURES`
- ⚠ deprecated constant `HANDLE_BINARY_EMBED_AS_BASISU`
- ⚠ deprecated constant `HANDLE_BINARY_EMBED_AS_UNCOMPRESSED`
- ⚠ deprecated constant `HANDLE_BINARY_EXTRACT_TEXTURES`

#### GraphElement
- + property `scaling_menus: bool` (property)

#### GraphNode
- + method `get_slot_metadata_left(slot_index: int) -> Variant`
- + method `get_slot_metadata_right(slot_index: int) -> Variant`
- + method `set_slot_metadata_left(slot_index: int, value: Variant)`
- + method `set_slot_metadata_right(slot_index: int, value: Variant)`

#### Image
- + method `load_exr_from_buffer(buffer: PackedByteArray) -> int`
- + constant `Format.FORMAT_R16`
- + constant `Format.FORMAT_R16I`
- + constant `Format.FORMAT_RG16`
- + constant `Format.FORMAT_RG16I`
- + constant `Format.FORMAT_RGB16`
- + constant `Format.FORMAT_RGB16I`
- + constant `Format.FORMAT_RGBA16`
- + constant `Format.FORMAT_RGBA16I`

#### ImporterMesh
- + method `from_mesh(mesh: Mesh) -> ImporterMesh`

#### Input
- + method `has_joy_light(device: int) -> bool`
- + method `set_joy_light(device: int, color: Color)`

#### ItemList
- + property `scroll_hint_mode: int` (property)
- + property `tile_scroll_hint: bool` (property)
- + constant `ScrollHintMode.SCROLL_HINT_MODE_BOTH`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_BOTTOM`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_DISABLED`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_TOP`

#### JNISingleton
- + method `has_java_method(method: StringName) -> bool`

#### JavaClass
- + method `has_java_method(method: StringName) -> bool`

#### JavaObject
- + method `has_java_method(method: StringName) -> bool`

#### LineEdit
- + property `icon_expand_mode: int` (property)
- + property `right_icon_scale: float` (property)
- + constant `ExpandMode.EXPAND_MODE_FIT_TO_LINE_EDIT`
- + constant `ExpandMode.EXPAND_MODE_FIT_TO_TEXT`
- + constant `ExpandMode.EXPAND_MODE_ORIGINAL_SIZE`
- ~ method `edit()` → `edit(hide_focus: bool = false)`

#### LinkButton
- + property `ellipsis_char: String` (property)
- + property `text_overrun_behavior: int` (property)

#### LookAtModifier3D
- + property `relative: bool` (property)

#### MissingNode
- + property `recording_signals: bool` (property)

#### MultiMesh
- + method `reset_instances_physics_interpolation()`

#### NativeMenu
- + method `get_system_menu_text(menu_id: int) -> String`
- + method `set_system_menu_text(menu_id: int, name: String)`

#### Node
- + constant `DuplicateFlags.DUPLICATE_DEFAULT`
- + constant `DuplicateFlags.DUPLICATE_INTERNAL_STATE`

#### OpenXRAPIExtension
- + method `get_openxr_version() -> int`
- + method `update_main_swapchain_size()`

#### OpenXRCompositionLayer
- + property `protected_content: bool` (property)

#### OpenXRExtensionWrapper
- + method `_prepare_view_configuration(view_count: int)`
- + method `_print_view_configuration_info(view: int)`
- + method `_set_view_configuration_and_get_next_pointer(view: int, next_pointer: void*) -> int`
- ~ method `_get_requested_extensions() -> Dictionary` → `_get_requested_extensions(xr_version: int) -> Dictionary`
- ~ method `_set_instance_create_info_and_get_next_pointer(next_pointer: void*) -> int` → `_set_instance_create_info_and_get_next_pointer(xr_version: int, next_pointer: void*) -> int`

#### OpenXRInteractionProfileMetadata
- + method `register_path_rename(old_name: String, new_name: String)`
- ~ method `register_interaction_profile(display_name: String, openxr_path: String, openxr_extension_name: String)` → `register_interaction_profile(display_name: String, openxr_path: String, openxr_extension_names: String)`
- ~ method `register_io_path(interaction_profile: String, display_name: String, toplevel_path: String, openxr_path: String, openxr_extension_name: String, action_type: int)` → `register_io_path(interaction_profile: String, display_name: String, toplevel_path: String, openxr_path: String, openxr_extension_names: String, action_type: int)`
- ~ method `register_top_level_path(display_name: String, openxr_path: String, openxr_extension_name: String)` → `register_top_level_path(display_name: String, openxr_path: String, openxr_extension_names: String)`

#### Performance
- + method `get_custom_monitor_types() -> PackedInt32Array`
- + constant `MonitorType.MONITOR_TYPE_MEMORY`
- + constant `MonitorType.MONITOR_TYPE_PERCENTAGE`
- + constant `MonitorType.MONITOR_TYPE_QUANTITY`
- + constant `MonitorType.MONITOR_TYPE_TIME`
- ~ method `add_custom_monitor(id: StringName, callable: Callable, arguments: Array = [])` → `add_custom_monitor(id: StringName, callable: Callable, arguments: Array = [], type: int = 0)`

#### PopupMenu
- + property `shrink_height: bool` (property)
- + property `shrink_width: bool` (property)

#### ProjectSettings
- + method `check_changed_settings_in_group(setting_prefix: String) -> bool`
- + method `get_changed_settings() -> PackedStringArray`
- + property `animation/compatibility/default_parent_skeleton_in_mesh_instance_3d: bool` (property)
- + property `application/boot_splash/stretch_mode: int` (property)
- + property `application/config/disable_project_settings_override: bool` (property)
- + property `debug/gdscript/warnings/directory_rules: Dictionary` (property)
- + property `debug/gdscript/warnings/missing_await: int` (property)
- + property `editor/movie_writer/audio_bit_depth: int` (property)
- + property `gui/common/drag_threshold: int` (property)
- + property `gui/common/show_focus_state_on_pointer_event: int` (property)
- + property `input/ui_close_dialog: Dictionary` (property)
- + property `input/ui_close_dialog.macos: Dictionary` (property)
- + property `input/ui_filedialog_delete: Dictionary` (property)
- + property `input/ui_filedialog_find: Dictionary` (property)
- + property `input/ui_filedialog_focus_path: Dictionary` (property)
- + property `input/ui_filedialog_focus_path.macos: Dictionary` (property)
- + property `navigation/2d/navigation_engine: String` (property)
- + property `navigation/2d/warnings/navmesh_cell_size_mismatch: bool` (property)
- + property `navigation/2d/warnings/navmesh_edge_merge_errors: bool` (property)
- + property `navigation/3d/navigation_engine: String` (property)
- + property `navigation/3d/warnings/navmesh_cell_size_mismatch: bool` (property)
- + property `navigation/3d/warnings/navmesh_edge_merge_errors: bool` (property)
- + property `network/limits/unix/connect_timeout_seconds: int` (property)
- + property `rendering/environment/screen_space_reflection/half_size: bool` (property)
- + property `rendering/rendering_device/d3d12/max_resource_descriptors: int` (property)
- + property `rendering/rendering_device/d3d12/max_sampler_descriptors: int` (property)
- + property `xr/openxr/extensions/frame_synthesis: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/april_tag_dict: int` (property)
- + property `xr/openxr/extensions/spatial_entity/aruco_dict: int` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_builtin_marker_tracking: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_builtin_plane_detection: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_marker_tracking: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_persistent_anchors: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_plane_tracking: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enable_spatial_anchors: bool` (property)
- + property `xr/openxr/extensions/spatial_entity/enabled: bool` (property)
- + property `xr/openxr/target_api_version: String` (property)
- − removed property `application/boot_splash/fullsize: bool`
- − removed property `debug/gdscript/warnings/exclude_addons: bool`
- − removed property `rendering/environment/screen_space_reflection/roughness_quality: int`
- − removed property `rendering/rendering_device/d3d12/max_misc_descriptors_per_frame: int`
- − removed property `rendering/rendering_device/d3d12/max_resource_descriptors_per_frame: int`
- − removed property `rendering/rendering_device/d3d12/max_sampler_descriptors_per_frame: int`

#### RDVertexAttribute
- + property `binding: int` (property)

#### RenderingDevice
- + method `draw_list_bind_vertex_buffers_format(draw_list: int, vertex_format: int, vertex_count: int, vertex_buffers: RID[], offsets: PackedInt64Array = PackedInt64Array())`
- + constant `TextureUsageBits.TEXTURE_USAGE_DEPTH_RESOLVE_ATTACHMENT_BIT`
- + constant `UniformType.UNIFORM_TYPE_STORAGE_BUFFER_DYNAMIC`
- + constant `UniformType.UNIFORM_TYPE_UNIFORM_BUFFER_DYNAMIC`

#### RenderingServer
- + method `canvas_item_add_ellipse(item: RID, pos: Vector2, major: float, minor: float, color: Color, antialiased: bool = false)`
- + method `environment_set_ssr_half_size(half_size: bool)`
- + method `environment_set_tonemap_agx_contrast(env: RID, agx_contrast: float)`
- + method `material_set_use_debanding(enable: bool)`
- + method `multimesh_instances_reset_physics_interpolation(multimesh: RID)`
- + method `set_boot_image_with_stretch(image: Image, color: Color, stretch_mode: int, use_filter: bool = true)`
- + constant `SplashStretchMode.SPLASH_STRETCH_MODE_COVER`
- + constant `SplashStretchMode.SPLASH_STRETCH_MODE_DISABLED`
- + constant `SplashStretchMode.SPLASH_STRETCH_MODE_IGNORE`
- + constant `SplashStretchMode.SPLASH_STRETCH_MODE_KEEP`
- + constant `SplashStretchMode.SPLASH_STRETCH_MODE_KEEP_HEIGHT`
- + constant `SplashStretchMode.SPLASH_STRETCH_MODE_KEEP_WIDTH`
- ⚠ deprecated method `environment_set_ssr_roughness_quality(quality: int)`
- ⚠ deprecated method `reflection_probe_set_resolution(probe: RID, resolution: int)`
- ⚠ deprecated method `set_boot_image(image: Image, color: Color, scale: bool, use_filter: bool = true)`

#### ResourceImporterCSVTranslation
- + property `unescape_keys: bool` (property)
- + property `unescape_translations: bool` (property)

#### SceneTree
- + method `change_scene_to_node(node: Node) -> int`

#### ScrollContainer
- + property `scroll_hint_mode: int` (property)
- + property `tile_scroll_hint: bool` (property)
- + constant `ScrollHintMode.SCROLL_HINT_MODE_ALL`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_BOTTOM_AND_RIGHT`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_DISABLED`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_TOP_AND_LEFT`

#### SkeletonModifier3D
- + constant `BoneDirection.BONE_DIRECTION_FROM_PARENT`
- + constant `BoneDirection.BONE_DIRECTION_MINUS_X`
- + constant `BoneDirection.BONE_DIRECTION_MINUS_Y`
- + constant `BoneDirection.BONE_DIRECTION_MINUS_Z`
- + constant `BoneDirection.BONE_DIRECTION_PLUS_X`
- + constant `BoneDirection.BONE_DIRECTION_PLUS_Y`
- + constant `BoneDirection.BONE_DIRECTION_PLUS_Z`
- + constant `RotationAxis.ROTATION_AXIS_ALL`
- + constant `RotationAxis.ROTATION_AXIS_CUSTOM`
- + constant `RotationAxis.ROTATION_AXIS_X`
- + constant `RotationAxis.ROTATION_AXIS_Y`
- + constant `RotationAxis.ROTATION_AXIS_Z`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_CUSTOM`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_MINUS_X`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_MINUS_Y`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_MINUS_Z`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_NONE`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_PLUS_X`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_PLUS_Y`
- + constant `SecondaryDirection.SECONDARY_DIRECTION_PLUS_Z`

#### SpinBox
- + property `custom_arrow_round: bool` (property)

#### SplitContainer
- + method `get_drag_area_controls() -> Control[]`
- + property `split_offsets: PackedInt32Array` (property)
- ~ method `clamp_split_offset()` → `clamp_split_offset(priority_index: int = 0)`
- ⚠ deprecated method `get_drag_area_control() -> Control`
- ⚠ deprecated property `split_offset: int`

#### SpringBoneSimulator3D
- + property `mutable_bone_axes: bool` (property)
- − removed constant `BoneDirection.BONE_DIRECTION_FROM_PARENT`
- − removed constant `BoneDirection.BONE_DIRECTION_MINUS_X`
- − removed constant `BoneDirection.BONE_DIRECTION_MINUS_Y`
- − removed constant `BoneDirection.BONE_DIRECTION_MINUS_Z`
- − removed constant `BoneDirection.BONE_DIRECTION_PLUS_X`
- − removed constant `BoneDirection.BONE_DIRECTION_PLUS_Y`
- − removed constant `BoneDirection.BONE_DIRECTION_PLUS_Z`
- − removed constant `RotationAxis.ROTATION_AXIS_ALL`
- − removed constant `RotationAxis.ROTATION_AXIS_CUSTOM`
- − removed constant `RotationAxis.ROTATION_AXIS_X`
- − removed constant `RotationAxis.ROTATION_AXIS_Y`
- − removed constant `RotationAxis.ROTATION_AXIS_Z`

#### StreamPeerTCP
- − removed method `disconnect_from_host()`
- − removed method `get_status() -> int`
- − removed method `poll() -> int`
- − removed constant `Status.STATUS_CONNECTED`
- − removed constant `Status.STATUS_CONNECTING`
- − removed constant `Status.STATUS_ERROR`
- − removed constant `Status.STATUS_NONE`

#### TCPServer
- − removed method `is_connection_available() -> bool`
- − removed method `is_listening() -> bool`
- − removed method `stop()`

#### TabBar
- + property `switch_on_drag_hover: bool` (property)

#### TabContainer
- + property `switch_on_drag_hover: bool` (property)

#### TextEdit
- − removed property `clip_contents: bool`

#### TextLine
- + method `duplicate() -> TextLine`
- + method `has_object(key: Variant) -> bool`

#### TextParagraph
- + method `duplicate() -> TextParagraph`
- + method `has_object(key: Variant) -> bool`

#### TextServer
- + method `is_locale_using_support_data(locale: String) -> bool`
- + method `shaped_text_duplicate(rid: RID) -> RID`
- + method `shaped_text_has_object(shaped: RID, key: Variant) -> bool`
- + constant `TextOverrunFlag.OVERRUN_SHORT_STRING_ELLIPSIS`
- ⚠ deprecated method `format_number(number: String, language: String = "") -> String`
- ⚠ deprecated method `parse_number(number: String, language: String = "") -> String`
- ⚠ deprecated method `percent_sign(language: String = "") -> String`

#### TextServerExtension
- + method `_is_locale_using_support_data(locale: String) -> bool`
- + method `_shaped_text_duplicate(shaped: RID) -> RID`
- + method `_shaped_text_has_object(shaped: RID, key: Variant) -> bool`
- ⚠ deprecated method `_format_number(number: String, language: String) -> String`
- ⚠ deprecated method `_parse_number(number: String, language: String) -> String`
- ⚠ deprecated method `_percent_sign(language: String) -> String`

#### Thread
- + method `is_main_thread() -> bool`

#### Translation
- + property `plural_rules_override: String` (property)

#### TranslationDomain
- + method `find_translations(locale: String, exact: bool) -> Translation[]`
- + method `get_translations() -> Translation[]`
- + method `has_translation(translation: Translation) -> bool`
- + method `has_translation_for_locale(locale: String, exact: bool) -> bool`
- ⚠ deprecated method `get_translation_object(locale: String) -> Translation`

#### TranslationServer
- + method `find_translations(locale: String, exact: bool) -> Translation[]`
- + method `format_number(number: String, locale: String) -> String`
- + method `get_percent_sign(locale: String) -> String`
- + method `get_plural_rules(locale: String) -> String`
- + method `get_translations() -> Translation[]`
- + method `has_translation(translation: Translation) -> bool`
- + method `has_translation_for_locale(locale: String, exact: bool) -> bool`
- + method `parse_number(number: String, locale: String) -> String`
- ⚠ deprecated method `get_translation_object(locale: String) -> Translation`

#### Tree
- + method `get_column_title_tooltip_text(column: int) -> String`
- + method `set_column_title_tooltip_text(column: int, tooltip_text: String)`
- + property `enable_drag_unfolding: bool` (property)
- + property `scroll_hint_mode: int` (property)
- + property `tile_scroll_hint: bool` (property)
- + constant `ScrollHintMode.SCROLL_HINT_MODE_BOTH`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_BOTTOM`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_DISABLED`
- + constant `ScrollHintMode.SCROLL_HINT_MODE_TOP`

#### TreeItem
- + method `get_custom_stylebox(column: int) -> StyleBox`
- + method `set_custom_stylebox(column: int, stylebox: StyleBox)`

#### Viewport
- + property `gui_drag_threshold: int` (property)

#### VisualShaderNodeParameter
- + property `instance_index: int` (property)
- + constant `Qualifier.QUAL_INSTANCE_INDEX`

#### Window
- + property `nonclient_area: Rect2i` (property)
- + signal `nonclient_window_input(event: InputEvent)`
