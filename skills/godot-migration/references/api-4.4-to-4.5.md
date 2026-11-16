# Godot engine API changes (4.4-stable → 4.5-stable)

> Derived from the Godot Engine class reference (MIT License, © Godot Engine contributors, Juan Linietsky, Ariel Manzur). See `licenses/GODOT-LICENSE.txt` at the plugin root.

Generated from the engine's own class reference XML (doc/classes and modules/*/doc_classes) at each release tag. `+` added, `~` signature changed, `⚠` newly deprecated, `−` removed.

- 4.4-stable: 988 classes
- 4.5-stable: 1006 classes

## 4.4-stable → 4.5-stable

### New classes (18)

- **AimModifier3D** ← BoneConstraint3D: The [AimModifier3D] rotates a bone to look at a reference bone.
- **BoneConstraint3D** ← SkeletonModifier3D: A node that may modify Skeleton3D's bone with associating the two bones.
- **ConvertTransformModifier3D** ← BoneConstraint3D: A [SkeletonModifier3D] that apply transform to the bone which converted from reference.
- **CopyTransformModifier3D** ← BoneConstraint3D: A [SkeletonModifier3D] that apply transform to the bone which copied from reference.
- **DPITexture** ← Texture2D *(experimental)*: An automatically scalable [Texture2D] based on an SVG image.
- **EditorExportPlatformAppleEmbedded** ← EditorExportPlatform: Base class for the Apple embedded platform exporters (iOS and visionOS).
- **FoldableContainer** ← Container: A container that can be expanded/collapsed.
- **FoldableGroup** ← Resource: A group of foldable containers that doesn't allow more than one container to be expanded at a time.
- **Logger** ← RefCounted: Custom logger to receive messages from the internal error/warning stream.
- **ModifierBoneTarget3D** ← SkeletonModifier3D: А node that dynamically copies the 3D transform of a bone in its parent [Skeleton3D].
- **OpenXRExtensionWrapper** ← Object: Allows implementing OpenXR extensions with GDExtension.
- **OpenXRFutureExtension** ← OpenXRExtensionWrapper: The OpenXR Future extension allows for asynchronous APIs to be used.
- **OpenXRFutureResult** ← RefCounted: Result object tracking the asynchronous result of an OpenXR Future object.
- **OpenXRRenderModel** ← Node3D: This node will display an OpenXR render model.
- **OpenXRRenderModelExtension** ← OpenXRExtensionWrapper: This class implements the OpenXR Render Model Extension.
- **OpenXRRenderModelManager** ← Node3D: Helper node that will automatically manage displaying render models.
- **ResourceImporterSVG** ← ResourceImporter: Imports an SVG file as an automatically scalable texture for use in UI elements and 2D rendering.
- **ScriptBacktrace** ← RefCounted: A captured backtrace of a specific script language.

### Newly deprecated classes (5)

- OpenXRExtensionWrapperExtension
- PackedDataContainer
- PackedDataContainerRef
- ParallaxBackground
- ParallaxLayer

### Changed classes (146)

#### @GDScript
- + method `ord(char: String) -> int`
- + annotation `@abstract()`
- + annotation `@export_file_path(filter: String = "")`
- ~ method `char(char: int) -> String` → `char(code: int) -> String`

#### @GlobalScope
- + constant `PropertyHint.PROPERTY_HINT_FILE_PATH`
- + constant `PropertyHint.PROPERTY_HINT_GROUP_ENABLE`
- + constant `PropertyHint.PROPERTY_HINT_INPUT_NAME`

#### AStar2D
- + method `_filter_neighbor(from_id: int, neighbor_id: int) -> bool`
- + property `neighbor_filter_enabled: bool` (property)

#### AStar3D
- + method `_filter_neighbor(from_id: int, neighbor_id: int) -> bool`
- + property `neighbor_filter_enabled: bool` (property)

#### AcceptDialog
- + property `maximize_disabled: bool` (property)
- + property `minimize_disabled: bool` (property)

#### AnimationNodeBlendTree
- + method `get_node_list() -> StringName[]`

#### AnimationNodeStateMachine
- + method `get_node_list() -> StringName[]`

#### AnimationNodeStateMachinePlayback
- + signal `state_finished(state: StringName)`
- + signal `state_started(state: StringName)`

#### Array
- + method `duplicate_deep(deep_subresources_mode: int = 1) -> Array`

#### AudioListener3D
- + property `doppler_tracking: int` (property)
- + constant `DopplerTracking.DOPPLER_TRACKING_DISABLED`
- + constant `DopplerTracking.DOPPLER_TRACKING_IDLE_STEP`
- + constant `DopplerTracking.DOPPLER_TRACKING_PHYSICS_STEP`

#### AudioStream
- + method `_get_tags() -> Dictionary`

#### AudioStreamOggVorbis
- + property `tags: Dictionary` (property)

#### AudioStreamWAV
- + property `tags: Dictionary` (property)

#### BaseMaterial3D
- + property `bent_normal_enabled: bool` (property)
- + property `bent_normal_texture: Texture2D` (property)
- + property `depth_test: int` (property)
- + property `disable_specular_occlusion: bool` (property)
- + property `fov_override: float` (property)
- + property `stencil_color: Color` (property)
- + property `stencil_compare: int` (property)
- + property `stencil_flags: int` (property)
- + property `stencil_mode: int` (property)
- + property `stencil_outline_thickness: float` (property)
- + property `stencil_reference: int` (property)
- + property `use_fov_override: bool` (property)
- + property `use_z_clip_scale: bool` (property)
- + property `z_clip_scale: float` (property)
- + constant `DepthTest.DEPTH_TEST_DEFAULT`
- + constant `DepthTest.DEPTH_TEST_INVERTED`
- + constant `Feature.FEATURE_BENT_NORMAL_MAPPING`
- + constant `Flags.FLAG_DISABLE_SPECULAR_OCCLUSION`
- + constant `Flags.FLAG_USE_FOV_OVERRIDE`
- + constant `Flags.FLAG_USE_Z_CLIP_SCALE`
- + constant `StencilCompare.STENCIL_COMPARE_ALWAYS`
- + constant `StencilCompare.STENCIL_COMPARE_EQUAL`
- + constant `StencilCompare.STENCIL_COMPARE_GREATER`
- + constant `StencilCompare.STENCIL_COMPARE_GREATER_OR_EQUAL`
- + constant `StencilCompare.STENCIL_COMPARE_LESS`
- + constant `StencilCompare.STENCIL_COMPARE_LESS_OR_EQUAL`
- + constant `StencilCompare.STENCIL_COMPARE_NOT_EQUAL`
- + constant `StencilFlags.STENCIL_FLAG_READ`
- + constant `StencilFlags.STENCIL_FLAG_WRITE`
- + constant `StencilFlags.STENCIL_FLAG_WRITE_DEPTH_FAIL`
- + constant `StencilMode.STENCIL_MODE_CUSTOM`
- + constant `StencilMode.STENCIL_MODE_DISABLED`
- + constant `StencilMode.STENCIL_MODE_OUTLINE`
- + constant `StencilMode.STENCIL_MODE_XRAY`
- + constant `TextureParam.TEXTURE_BENT_NORMAL`

#### Basis
- + method `scaled_local(scale: Vector3) -> Basis`

#### BoneAttachment3D
- + property `external_skeleton: NodePath` (property)
- + property `physics_interpolation_mode: int` (property)
- + property `use_external_skeleton: bool` (property)
- − removed method `get_external_skeleton() -> NodePath`
- − removed method `get_use_external_skeleton() -> bool`
- − removed method `set_external_skeleton(external_skeleton: NodePath)`
- − removed method `set_use_external_skeleton(use_external_skeleton: bool)`

#### Button
- + property `autowrap_trim_flags: int` (property)

#### Camera2D
- + method `get_screen_rotation() -> float`
- + property `limit_enabled: bool` (property)

#### CameraServer
- + property `monitoring_feeds: bool` (property)
- + signal `camera_feeds_updated()`

#### CanvasItem
- ~ method `draw_char(font: Font, pos: Vector2, char: String, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1))` → `draw_char(font: Font, pos: Vector2, char: String, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_char_outline(font: Font, pos: Vector2, char: String, font_size: int = 16, size: int = -1, modulate: Color = Color(1, 1, 1, 1))` → `draw_char_outline(font: Font, pos: Vector2, char: String, font_size: int = 16, size: int = -1, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_multiline_string(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_multiline_string(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`
- ~ method `draw_multiline_string_outline(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, size: int = 1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_multiline_string_outline(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, size: int = 1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`
- ~ method `draw_string(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_string(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`
- ~ method `draw_string_outline(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, size: int = 1, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_string_outline(font: Font, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, size: int = 1, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`

#### CapsuleShape2D
- + property `mid_height: float` (property)

#### CapsuleShape3D
- + property `mid_height: float` (property)

#### ColorPicker
- + property `edit_intensity: bool` (property)
- + constant `ColorModeType.MODE_LINEAR`
- + constant `PickerShapeType.SHAPE_OK_HL_RECTANGLE`
- + constant `PickerShapeType.SHAPE_OK_HS_RECTANGLE`
- ⚠ deprecated constant `ColorModeType.MODE_RAW`

#### ColorPickerButton
- + property `edit_intensity: bool` (property)

#### Control
- + method `_accessibility_get_contextual_info() -> String`
- + method `_get_accessibility_container_name(node: Node) -> String`
- + method `accessibility_drag()`
- + method `accessibility_drop()`
- + method `get_focus_mode_with_override() -> int`
- + method `get_mouse_filter_with_override() -> int`
- + property `accessibility_controls_nodes: NodePath[]` (property)
- + property `accessibility_described_by_nodes: NodePath[]` (property)
- + property `accessibility_description: String` (property)
- + property `accessibility_flow_to_nodes: NodePath[]` (property)
- + property `accessibility_labeled_by_nodes: NodePath[]` (property)
- + property `accessibility_live: int` (property)
- + property `accessibility_name: String` (property)
- + property `focus_behavior_recursive: int` (property)
- + property `mouse_behavior_recursive: int` (property)
- + constant `FocusBehaviorRecursive.FOCUS_BEHAVIOR_DISABLED`
- + constant `FocusBehaviorRecursive.FOCUS_BEHAVIOR_ENABLED`
- + constant `FocusBehaviorRecursive.FOCUS_BEHAVIOR_INHERITED`
- + constant `FocusMode.FOCUS_ACCESSIBILITY`
- + constant `MouseBehaviorRecursive.MOUSE_BEHAVIOR_DISABLED`
- + constant `MouseBehaviorRecursive.MOUSE_BEHAVIOR_ENABLED`
- + constant `MouseBehaviorRecursive.MOUSE_BEHAVIOR_INHERITED`

#### Dictionary
- + method `duplicate_deep(deep_subresources_mode: int = 1) -> Dictionary`

#### DirAccess
- + method `get_filesystem_type() -> String`
- + method `is_equivalent(path_a: String, path_b: String) -> bool`

#### DisplayServer
- + method `accessibility_create_element(window_id: int, role: int) -> RID`
- + method `accessibility_create_sub_element(parent_rid: RID, role: int, insert_pos: int = -1) -> RID`
- + method `accessibility_create_sub_text_edit_elements(parent_rid: RID, shaped_text: RID, min_height: float, insert_pos: int = -1) -> RID`
- + method `accessibility_element_get_meta(id: RID) -> Variant`
- + method `accessibility_element_set_meta(id: RID, meta: Variant)`
- + method `accessibility_free_element(id: RID)`
- + method `accessibility_get_window_root(window_id: int) -> RID`
- + method `accessibility_has_element(id: RID) -> bool`
- + method `accessibility_screen_reader_active() -> int`
- + method `accessibility_set_window_focused(window_id: int, focused: bool)`
- + method `accessibility_set_window_rect(window_id: int, rect_out: Rect2, rect_in: Rect2)`
- + method `accessibility_should_increase_contrast() -> int`
- + method `accessibility_should_reduce_animation() -> int`
- + method `accessibility_should_reduce_transparency() -> int`
- + method `accessibility_update_add_action(id: RID, action: int, callable: Callable)`
- + method `accessibility_update_add_child(id: RID, child_id: RID)`
- + method `accessibility_update_add_custom_action(id: RID, action_id: int, action_description: String)`
- + method `accessibility_update_add_related_controls(id: RID, related_id: RID)`
- + method `accessibility_update_add_related_described_by(id: RID, related_id: RID)`
- + method `accessibility_update_add_related_details(id: RID, related_id: RID)`
- + method `accessibility_update_add_related_flow_to(id: RID, related_id: RID)`
- + method `accessibility_update_add_related_labeled_by(id: RID, related_id: RID)`
- + method `accessibility_update_add_related_radio_group(id: RID, related_id: RID)`
- + method `accessibility_update_set_active_descendant(id: RID, other_id: RID)`
- + method `accessibility_update_set_background_color(id: RID, color: Color)`
- + method `accessibility_update_set_bounds(id: RID, p_rect: Rect2)`
- + method `accessibility_update_set_checked(id: RID, checekd: bool)`
- + method `accessibility_update_set_classname(id: RID, classname: String)`
- + method `accessibility_update_set_color_value(id: RID, color: Color)`
- + method `accessibility_update_set_description(id: RID, description: String)`
- + method `accessibility_update_set_error_message(id: RID, other_id: RID)`
- + method `accessibility_update_set_extra_info(id: RID, name: String)`
- + method `accessibility_update_set_flag(id: RID, flag: int, value: bool)`
- + method `accessibility_update_set_focus(id: RID)`
- + method `accessibility_update_set_foreground_color(id: RID, color: Color)`
- + method `accessibility_update_set_in_page_link_target(id: RID, other_id: RID)`
- + method `accessibility_update_set_language(id: RID, language: String)`
- + method `accessibility_update_set_list_item_count(id: RID, size: int)`
- + method `accessibility_update_set_list_item_expanded(id: RID, expanded: bool)`
- + method `accessibility_update_set_list_item_index(id: RID, index: int)`
- + method `accessibility_update_set_list_item_level(id: RID, level: int)`
- + method `accessibility_update_set_list_item_selected(id: RID, selected: bool)`
- + method `accessibility_update_set_list_orientation(id: RID, vertical: bool)`
- + method `accessibility_update_set_live(id: RID, live: int)`
- + method `accessibility_update_set_member_of(id: RID, group_id: RID)`
- + method `accessibility_update_set_name(id: RID, name: String)`
- + method `accessibility_update_set_next_on_line(id: RID, other_id: RID)`
- + method `accessibility_update_set_num_jump(id: RID, jump: float)`
- + method `accessibility_update_set_num_range(id: RID, min: float, max: float)`
- + method `accessibility_update_set_num_step(id: RID, step: float)`
- + method `accessibility_update_set_num_value(id: RID, position: float)`
- + method `accessibility_update_set_placeholder(id: RID, placeholder: String)`
- + method `accessibility_update_set_popup_type(id: RID, popup: int)`
- + method `accessibility_update_set_previous_on_line(id: RID, other_id: RID)`
- + method `accessibility_update_set_role(id: RID, role: int)`
- + method `accessibility_update_set_role_description(id: RID, description: String)`
- + method `accessibility_update_set_scroll_x(id: RID, position: float)`
- + method `accessibility_update_set_scroll_x_range(id: RID, min: float, max: float)`
- + method `accessibility_update_set_scroll_y(id: RID, position: float)`
- + method `accessibility_update_set_scroll_y_range(id: RID, min: float, max: float)`
- + method `accessibility_update_set_shortcut(id: RID, shortcut: String)`
- + method `accessibility_update_set_state_description(id: RID, description: String)`
- + method `accessibility_update_set_table_cell_position(id: RID, row_index: int, column_index: int)`
- + method `accessibility_update_set_table_cell_span(id: RID, row_span: int, column_span: int)`
- + method `accessibility_update_set_table_column_count(id: RID, count: int)`
- + method `accessibility_update_set_table_column_index(id: RID, index: int)`
- + method `accessibility_update_set_table_row_count(id: RID, count: int)`
- + method `accessibility_update_set_table_row_index(id: RID, index: int)`
- + method `accessibility_update_set_text_align(id: RID, align: int)`
- + method `accessibility_update_set_text_decorations(id: RID, underline: bool, strikethrough: bool, overline: bool)`
- + method `accessibility_update_set_text_orientation(id: RID, vertical: bool)`
- + method `accessibility_update_set_text_selection(id: RID, text_start_id: RID, start_char: int, text_end_id: RID, end_char: int)`
- + method `accessibility_update_set_tooltip(id: RID, tooltip: String)`
- + method `accessibility_update_set_transform(id: RID, transform: Transform2D)`
- + method `accessibility_update_set_url(id: RID, url: String)`
- + method `accessibility_update_set_value(id: RID, value: String)`
- + method `color_picker(callback: Callable) -> bool`
- + method `set_hardware_keyboard_connection_change_callback(callable: Callable)`
- + constant `AccessibilityAction.ACTION_BLUR`
- + constant `AccessibilityAction.ACTION_CLICK`
- + constant `AccessibilityAction.ACTION_COLLAPSE`
- + constant `AccessibilityAction.ACTION_CUSTOM`
- + constant `AccessibilityAction.ACTION_DECREMENT`
- + constant `AccessibilityAction.ACTION_EXPAND`
- + constant `AccessibilityAction.ACTION_FOCUS`
- + constant `AccessibilityAction.ACTION_HIDE_TOOLTIP`
- + constant `AccessibilityAction.ACTION_INCREMENT`
- + constant `AccessibilityAction.ACTION_REPLACE_SELECTED_TEXT`
- + constant `AccessibilityAction.ACTION_SCROLL_BACKWARD`
- + constant `AccessibilityAction.ACTION_SCROLL_DOWN`
- + constant `AccessibilityAction.ACTION_SCROLL_FORWARD`
- + constant `AccessibilityAction.ACTION_SCROLL_INTO_VIEW`
- + constant `AccessibilityAction.ACTION_SCROLL_LEFT`
- + constant `AccessibilityAction.ACTION_SCROLL_RIGHT`
- + constant `AccessibilityAction.ACTION_SCROLL_TO_POINT`
- + constant `AccessibilityAction.ACTION_SCROLL_UP`
- + constant `AccessibilityAction.ACTION_SET_SCROLL_OFFSET`
- + constant `AccessibilityAction.ACTION_SET_TEXT_SELECTION`
- + constant `AccessibilityAction.ACTION_SET_VALUE`
- + constant `AccessibilityAction.ACTION_SHOW_CONTEXT_MENU`
- + constant `AccessibilityAction.ACTION_SHOW_TOOLTIP`
- + constant `AccessibilityFlags.FLAG_BUSY`
- + constant `AccessibilityFlags.FLAG_CLIPS_CHILDREN`
- + constant `AccessibilityFlags.FLAG_DISABLED`
- + constant `AccessibilityFlags.FLAG_HIDDEN`
- + constant `AccessibilityFlags.FLAG_MODAL`
- + constant `AccessibilityFlags.FLAG_MULTISELECTABLE`
- + constant `AccessibilityFlags.FLAG_READONLY`
- + constant `AccessibilityFlags.FLAG_REQUIRED`
- + constant `AccessibilityFlags.FLAG_TOUCH_PASSTHROUGH`
- + constant `AccessibilityFlags.FLAG_VISITED`
- + constant `AccessibilityLiveMode.LIVE_ASSERTIVE`
- + constant `AccessibilityLiveMode.LIVE_OFF`
- + constant `AccessibilityLiveMode.LIVE_POLITE`
- + constant `AccessibilityPopupType.POPUP_DIALOG`
- + constant `AccessibilityPopupType.POPUP_LIST`
- + constant `AccessibilityPopupType.POPUP_MENU`
- + constant `AccessibilityPopupType.POPUP_TREE`
- + constant `AccessibilityRole.ROLE_AUDIO`
- + constant `AccessibilityRole.ROLE_BUTTON`
- + constant `AccessibilityRole.ROLE_CELL`
- + constant `AccessibilityRole.ROLE_CHECK_BOX`
- + constant `AccessibilityRole.ROLE_CHECK_BUTTON`
- + constant `AccessibilityRole.ROLE_COLOR_PICKER`
- + constant `AccessibilityRole.ROLE_COLUMN_HEADER`
- + constant `AccessibilityRole.ROLE_CONTAINER`
- + constant `AccessibilityRole.ROLE_DEFAULT_BUTTON`
- + constant `AccessibilityRole.ROLE_DIALOG`
- + constant `AccessibilityRole.ROLE_IMAGE`
- + constant `AccessibilityRole.ROLE_LINK`
- + constant `AccessibilityRole.ROLE_LIST`
- + constant `AccessibilityRole.ROLE_LIST_BOX`
- + constant `AccessibilityRole.ROLE_LIST_BOX_OPTION`
- + constant `AccessibilityRole.ROLE_LIST_ITEM`
- + constant `AccessibilityRole.ROLE_MENU`
- + constant `AccessibilityRole.ROLE_MENU_BAR`
- + constant `AccessibilityRole.ROLE_MENU_ITEM`
- + constant `AccessibilityRole.ROLE_MENU_ITEM_CHECK_BOX`
- + constant `AccessibilityRole.ROLE_MENU_ITEM_RADIO`
- + constant `AccessibilityRole.ROLE_MULTILINE_TEXT_FIELD`
- + constant `AccessibilityRole.ROLE_PANEL`
- + constant `AccessibilityRole.ROLE_PROGRESS_INDICATOR`
- + constant `AccessibilityRole.ROLE_RADIO_BUTTON`
- + constant `AccessibilityRole.ROLE_ROW`
- + constant `AccessibilityRole.ROLE_ROW_GROUP`
- + constant `AccessibilityRole.ROLE_ROW_HEADER`
- + constant `AccessibilityRole.ROLE_SCROLL_BAR`
- + constant `AccessibilityRole.ROLE_SCROLL_VIEW`
- + constant `AccessibilityRole.ROLE_SLIDER`
- + constant `AccessibilityRole.ROLE_SPIN_BUTTON`
- + constant `AccessibilityRole.ROLE_SPLITTER`
- + constant `AccessibilityRole.ROLE_STATIC_TEXT`
- + constant `AccessibilityRole.ROLE_TAB`
- + constant `AccessibilityRole.ROLE_TABLE`
- + constant `AccessibilityRole.ROLE_TAB_BAR`
- + constant `AccessibilityRole.ROLE_TAB_PANEL`
- + constant `AccessibilityRole.ROLE_TEXT_FIELD`
- + constant `AccessibilityRole.ROLE_TITLE_BAR`
- + constant `AccessibilityRole.ROLE_TOOLTIP`
- + constant `AccessibilityRole.ROLE_TREE`
- + constant `AccessibilityRole.ROLE_TREE_ITEM`
- + constant `AccessibilityRole.ROLE_UNKNOWN`
- + constant `AccessibilityRole.ROLE_VIDEO`
- + constant `AccessibilityRole.ROLE_WINDOW`
- + constant `AccessibilityScrollHint.SCROLL_HINT_BOTTOM_EDGE`
- + constant `AccessibilityScrollHint.SCROLL_HINT_BOTTOM_RIGHT`
- + constant `AccessibilityScrollHint.SCROLL_HINT_LEFT_EDGE`
- + constant `AccessibilityScrollHint.SCROLL_HINT_RIGHT_EDGE`
- + constant `AccessibilityScrollHint.SCROLL_HINT_TOP_EDGE`
- + constant `AccessibilityScrollHint.SCROLL_HINT_TOP_LEFT`
- + constant `AccessibilityScrollUnit.SCROLL_UNIT_ITEM`
- + constant `AccessibilityScrollUnit.SCROLL_UNIT_PAGE`
- + constant `Feature.FEATURE_ACCESSIBILITY_SCREEN_READER`
- + constant `Feature.FEATURE_NATIVE_COLOR_PICKER`
- + constant `Feature.FEATURE_SELF_FITTING_WINDOWS`
- + constant `INVALID_SCREEN`
- + constant `WindowEvent.WINDOW_EVENT_FORCE_CLOSE`
- + constant `WindowFlags.WINDOW_FLAG_MAXIMIZE_DISABLED`
- + constant `WindowFlags.WINDOW_FLAG_MINIMIZE_DISABLED`
- + constant `WindowFlags.WINDOW_FLAG_POPUP_WM_HINT`
- ~ method `file_dialog_show(title: String, current_directory: String, filename: String, show_hidden: bool, mode: int, filters: PackedStringArray, callback: Callable) -> int` → `file_dialog_show(title: String, current_directory: String, filename: String, show_hidden: bool, mode: int, filters: PackedStringArray, callback: Callable, parent_window_id: int = 0) -> int`
- ~ method `file_dialog_with_options_show(title: String, current_directory: String, root: String, filename: String, show_hidden: bool, mode: int, filters: PackedStringArray, options: Dictionary[], callback: Callable) -> int` → `file_dialog_with_options_show(title: String, current_directory: String, root: String, filename: String, show_hidden: bool, mode: int, filters: PackedStringArray, options: Dictionary[], callback: Callable, parent_window_id: int = 0) -> int`

#### EditorExportPlatform
- ~ method `get_forced_export_files() -> PackedStringArray` → `get_forced_export_files(preset: EditorExportPreset = null) -> PackedStringArray`

#### EditorExportPlatformExtension
- ~ method `_get_option_icon(device: int) -> ImageTexture` → `_get_option_icon(device: int) -> Texture2D`

#### EditorExportPlugin
- + method `_update_android_prebuilt_manifest(platform: EditorExportPlatform, manifest_data: PackedByteArray) -> PackedByteArray`
- + method `add_apple_embedded_platform_bundle_file(path: String)`
- + method `add_apple_embedded_platform_cpp_code(code: String)`
- + method `add_apple_embedded_platform_embedded_framework(path: String)`
- + method `add_apple_embedded_platform_framework(path: String)`
- + method `add_apple_embedded_platform_linker_flags(flags: String)`
- + method `add_apple_embedded_platform_plist_content(plist_content: String)`
- + method `add_apple_embedded_platform_project_static_lib(path: String)`
- ⚠ deprecated method `add_ios_bundle_file(path: String)`
- ⚠ deprecated method `add_ios_cpp_code(code: String)`
- ⚠ deprecated method `add_ios_embedded_framework(path: String)`
- ⚠ deprecated method `add_ios_framework(path: String)`
- ⚠ deprecated method `add_ios_linker_flags(flags: String)`
- ⚠ deprecated method `add_ios_plist_content(plist_content: String)`
- ⚠ deprecated method `add_ios_project_static_lib(path: String)`

#### EditorExportPreset
- + method `get_project_setting(name: StringName) -> Variant`

#### EditorInspector
- + property `follow_focus: bool` (property)

#### EditorInterface
- + method `close_scene() -> int`
- + method `get_open_scene_roots() -> Node[]`

#### EditorProperty
- + property `focus_mode: int` (property)
- + signal `property_overridden()`

#### EditorSelection
- + method `get_top_selected_nodes() -> Node[]`
- ⚠ deprecated method `get_transformable_selected_nodes() -> Node[]`

#### EditorSettings
- + property `debugger/max_node_selection: int` (property)
- + property `docks/scene_tree/accessibility_warnings: bool` (property)
- + property `editors/2d/ruler_width: float` (property)
- + property `editors/3d/active_selection_box_color: Color` (property)
- + property `editors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size: float` (property)
- + property `editors/animation/default_animation_step: float` (property)
- + property `editors/animation/default_fps_compatibility: bool` (property)
- + property `editors/animation/default_fps_mode: int` (property)
- + property `editors/panning/zoom_style: int` (property)
- + property `interface/accessibility/accessibility_support: int` (property)
- + property `interface/editor/collapse_main_menu: bool` (property)
- + property `interface/editor/tablet_driver: int` (property)
- + property `interface/inspector/color_picker_show_intensity: bool` (property)
- + property `interface/touchscreen/enable_touch_optimizations: bool` (property)
- + property `interface/touchscreen/touch_actions_panel: int` (property)
- + property `network/connection/check_for_updates: int` (property)
- + property `text_editor/appearance/enable_inline_color_picker: bool` (property)
- + property `text_editor/behavior/files/drop_preload_resources_as_uid: bool` (property)
- + property `text_editor/theme/highlighting/comment_markers/critical_color: Color` (property)
- + property `text_editor/theme/highlighting/comment_markers/critical_list: String` (property)
- + property `text_editor/theme/highlighting/comment_markers/notice_color: Color` (property)
- + property `text_editor/theme/highlighting/comment_markers/notice_list: String` (property)
- + property `text_editor/theme/highlighting/comment_markers/warning_color: Color` (property)
- + property `text_editor/theme/highlighting/comment_markers/warning_list: String` (property)
- + property `text_editor/theme/highlighting/gdscript/annotation_color: Color` (property)
- + property `text_editor/theme/highlighting/gdscript/function_definition_color: Color` (property)
- + property `text_editor/theme/highlighting/gdscript/global_function_color: Color` (property)
- + property `text_editor/theme/highlighting/gdscript/node_path_color: Color` (property)
- + property `text_editor/theme/highlighting/gdscript/node_reference_color: Color` (property)
- + property `text_editor/theme/highlighting/gdscript/string_name_color: Color` (property)
- + property `text_editor/theme/highlighting/warning_color: Color` (property)
- − removed property `interface/touchscreen/increase_scrollbar_touch_area: bool`
- − removed property `network/connection/engine_version_update_mode: int`
- − removed property `text_editor/theme/line_spacing: int`

#### EditorSyntaxHighlighter
- + method `_create() -> EditorSyntaxHighlighter`

#### EditorUndoRedoManager
- ~ method `create_action(name: String, merge_mode: int = 0, custom_context: Object = null, backward_undo_ops: bool = false)` → `create_action(name: String, merge_mode: int = 0, custom_context: Object = null, backward_undo_ops: bool = false, mark_unsaved: bool = true)`

#### Engine
- + method `capture_script_backtraces(include_variables: bool = false) -> ScriptBacktrace[]`

#### FileAccess
- + method `get_access_time(file: String) -> int`
- + method `get_size(file: String) -> int`

#### FileDialog
- + method `is_customization_flag_enabled(flag: int) -> bool`
- + method `set_customization_flag_enabled(flag: int, enabled: bool)`
- + property `display_mode: int` (property)
- + property `favorites_enabled: bool` (property)
- + property `file_filter_toggle_enabled: bool` (property)
- + property `file_sort_options_enabled: bool` (property)
- + property `folder_creation_enabled: bool` (property)
- + property `hidden_files_toggle_enabled: bool` (property)
- + property `layout_toggle_enabled: bool` (property)
- + property `recent_list_enabled: bool` (property)
- + constant `Customization.CUSTOMIZATION_CREATE_FOLDER`
- + constant `Customization.CUSTOMIZATION_FAVORITES`
- + constant `Customization.CUSTOMIZATION_FILE_FILTER`
- + constant `Customization.CUSTOMIZATION_FILE_SORT`
- + constant `Customization.CUSTOMIZATION_HIDDEN_FILES`
- + constant `Customization.CUSTOMIZATION_LAYOUT`
- + constant `Customization.CUSTOMIZATION_RECENT`
- + constant `DisplayMode.DISPLAY_LIST`
- + constant `DisplayMode.DISPLAY_THUMBNAILS`
- − removed property `ok_button_text: String`

#### Font
- ~ method `draw_char(canvas_item: RID, pos: Vector2, char: int, font_size: int, modulate: Color = Color(1, 1, 1, 1)) -> float` → `draw_char(canvas_item: RID, pos: Vector2, char: int, font_size: int, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) -> float`
- ~ method `draw_char_outline(canvas_item: RID, pos: Vector2, char: int, font_size: int, size: int = -1, modulate: Color = Color(1, 1, 1, 1)) -> float` → `draw_char_outline(canvas_item: RID, pos: Vector2, char: int, font_size: int, size: int = -1, modulate: Color = Color(1, 1, 1, 1), oversampling: float = 0.0) -> float`
- ~ method `draw_multiline_string(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_multiline_string(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`
- ~ method `draw_multiline_string_outline(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, size: int = 1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_multiline_string_outline(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, max_lines: int = -1, size: int = 1, modulate: Color = Color(1, 1, 1, 1), brk_flags: int = 3, justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`
- ~ method `draw_string(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_string(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`
- ~ method `draw_string_outline(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, size: int = 1, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0)` → `draw_string_outline(canvas_item: RID, pos: Vector2, text: String, alignment: int = 0, width: float = -1, font_size: int = 16, size: int = 1, modulate: Color = Color(1, 1, 1, 1), justification_flags: int = 3, direction: int = 0, orientation: int = 0, oversampling: float = 0.0)`

#### FontFile
- + property `modulate_color_glyphs: bool` (property)

#### GLTFDocument
- + property `fallback_image_format: String` (property)
- + property `fallback_image_quality: float` (property)
- + property `visibility_mode: int` (property)
- + constant `VisibilityMode.VISIBILITY_MODE_EXCLUDE`
- + constant `VisibilityMode.VISIBILITY_MODE_INCLUDE_OPTIONAL`
- + constant `VisibilityMode.VISIBILITY_MODE_INCLUDE_REQUIRED`

#### GLTFNode
- + property `visible: bool` (property)

#### GraphEdit
- + method `get_connection_list_from_node(node: StringName) -> Dictionary[]`
- + property `type_names: Dictionary` (property)

#### GraphNode
- + property `focus_mode: int` (property)
- + property `slots_focus_mode: int` (property)
- + signal `slot_sizes_changed()`

#### Image
- + method `load_dds_from_buffer(buffer: PackedByteArray) -> int`
- + method `save_dds(path: String) -> int`
- + method `save_dds_to_buffer() -> PackedByteArray`

#### Input
- + method `is_action_just_pressed_by_event(action: StringName, event: InputEvent, exact_match: bool = false) -> bool`
- + method `is_action_just_released_by_event(action: StringName, event: InputEvent, exact_match: bool = false) -> bool`

#### InputMap
- + method `get_action_description(action: StringName) -> String`

#### JSONRPC
- + method `set_method(name: String, callback: Callable)`
- − removed method `set_scope(scope: String, target: Object)`

#### Label
- + property `autowrap_trim_flags: int` (property)

#### Label3D
- + property `autowrap_trim_flags: int` (property)

#### LabelSettings
- + method `add_stacked_outline(index: int = -1)`
- + method `add_stacked_shadow(index: int = -1)`
- + method `get_stacked_outline_color(index: int) -> Color`
- + method `get_stacked_outline_size(index: int) -> int`
- + method `get_stacked_shadow_color(index: int) -> Color`
- + method `get_stacked_shadow_offset(index: int) -> Vector2`
- + method `get_stacked_shadow_outline_size(index: int) -> int`
- + method `move_stacked_outline(from_index: int, to_position: int)`
- + method `move_stacked_shadow(from_index: int, to_position: int)`
- + method `remove_stacked_outline(index: int)`
- + method `remove_stacked_shadow(index: int)`
- + method `set_stacked_outline_color(index: int, color: Color)`
- + method `set_stacked_outline_size(index: int, size: int)`
- + method `set_stacked_shadow_color(index: int, color: Color)`
- + method `set_stacked_shadow_offset(index: int, offset: Vector2)`
- + method `set_stacked_shadow_outline_size(index: int, size: int)`
- + property `stacked_outline_count: int` (property)
- + property `stacked_shadow_count: int` (property)

#### LineEdit
- + method `get_next_composite_character_column(column: int) -> int`
- + method `get_previous_composite_character_column(column: int) -> int`
- + property `backspace_deletes_composite_character_enabled: bool` (property)
- + property `virtual_keyboard_show_on_focus: bool` (property)

#### MenuBar
- + property `focus_mode: int` (property)

#### NavigationAgent2D
- + method `get_path_length() -> float`
- + property `path_return_max_length: float` (property)
- + property `path_return_max_radius: float` (property)
- + property `path_search_max_distance: float` (property)
- + property `path_search_max_polygons: int` (property)

#### NavigationAgent3D
- + method `get_path_length() -> float`
- + property `path_return_max_length: float` (property)
- + property `path_return_max_radius: float` (property)
- + property `path_search_max_distance: float` (property)
- + property `path_search_max_polygons: int` (property)

#### NavigationPathQueryParameters2D
- + property `excluded_regions: RID[]` (property)
- + property `included_regions: RID[]` (property)
- + property `path_return_max_length: float` (property)
- + property `path_return_max_radius: float` (property)
- + property `path_search_max_distance: float` (property)
- + property `path_search_max_polygons: int` (property)

#### NavigationPathQueryParameters3D
- + property `excluded_regions: RID[]` (property)
- + property `included_regions: RID[]` (property)
- + property `path_return_max_length: float` (property)
- + property `path_return_max_radius: float` (property)
- + property `path_search_max_distance: float` (property)
- + property `path_search_max_polygons: int` (property)

#### NavigationPathQueryResult2D
- + property `path_length: float` (property)

#### NavigationPathQueryResult3D
- + property `path_length: float` (property)

#### NavigationServer2D
- + method `get_process_info(process_info: int) -> int`
- + method `link_get_iteration_id(link: RID) -> int`
- + method `map_get_merge_rasterizer_cell_scale(map: RID) -> float`
- + method `map_set_merge_rasterizer_cell_scale(map: RID, scale: float)`
- + method `region_get_iteration_id(region: RID) -> int`
- + method `region_get_use_async_iterations(region: RID) -> bool`
- + method `region_set_use_async_iterations(region: RID, enabled: bool)`
- + method `set_active(active: bool)`
- + signal `avoidance_debug_changed()`
- + constant `ProcessInfo.INFO_ACTIVE_MAPS`
- + constant `ProcessInfo.INFO_AGENT_COUNT`
- + constant `ProcessInfo.INFO_EDGE_CONNECTION_COUNT`
- + constant `ProcessInfo.INFO_EDGE_COUNT`
- + constant `ProcessInfo.INFO_EDGE_FREE_COUNT`
- + constant `ProcessInfo.INFO_EDGE_MERGE_COUNT`
- + constant `ProcessInfo.INFO_LINK_COUNT`
- + constant `ProcessInfo.INFO_OBSTACLE_COUNT`
- + constant `ProcessInfo.INFO_POLYGON_COUNT`
- + constant `ProcessInfo.INFO_REGION_COUNT`
- ⚠ deprecated method `map_force_update(map: RID)`

#### NavigationServer3D
- + method `link_get_iteration_id(link: RID) -> int`
- + method `region_get_iteration_id(region: RID) -> int`
- + method `region_get_use_async_iterations(region: RID) -> bool`
- + method `region_set_use_async_iterations(region: RID, enabled: bool)`
- ⚠ deprecated method `map_force_update(map: RID)`

#### Node
- + method `_get_accessibility_configuration_warnings() -> PackedStringArray`
- + method `_get_focused_accessibility_element() -> RID`
- + method `can_auto_translate() -> bool`
- + method `get_accessibility_element() -> RID`
- + method `get_node_rpc_config() -> Variant`
- + method `get_orphan_node_ids() -> int[]`
- + method `queue_accessibility_update()`
- + constant `NOTIFICATION_ACCESSIBILITY_INVALIDATE`
- + constant `NOTIFICATION_ACCESSIBILITY_UPDATE`
- + constant `NOTIFICATION_WM_POSITION_CHANGED`
- − removed method `get_rpc_config() -> Variant`

#### OS
- + method `add_logger(logger: Logger)`
- + method `open_with_program(program_path: String, paths: PackedStringArray) -> int`
- + method `remove_logger(logger: Logger)`
- ~ method `read_buffer_from_stdin(buffer_size: int) -> PackedByteArray` → `read_buffer_from_stdin(buffer_size: int = 1024) -> PackedByteArray`
- ~ method `read_string_from_stdin(buffer_size: int) -> String` → `read_string_from_stdin(buffer_size: int = 1024) -> String`

#### Object
- + constant `ConnectFlags.CONNECT_APPEND_SOURCE_OBJECT`

#### OpenXRAPIExtension
- + method `register_frame_info_extension(extension: OpenXRExtensionWrapper)`
- + method `set_custom_play_space(space: const void*)`
- + method `unregister_frame_info_extension(extension: OpenXRExtensionWrapper)`
- ~ method `register_composition_layer_provider(extension: OpenXRExtensionWrapperExtension)` → `register_composition_layer_provider(extension: OpenXRExtensionWrapper)`
- ~ method `register_projection_views_extension(extension: OpenXRExtensionWrapperExtension)` → `register_projection_views_extension(extension: OpenXRExtensionWrapper)`
- ~ method `unregister_composition_layer_provider(extension: OpenXRExtensionWrapperExtension)` → `unregister_composition_layer_provider(extension: OpenXRExtensionWrapper)`
- ~ method `unregister_projection_views_extension(extension: OpenXRExtensionWrapperExtension)` → `unregister_projection_views_extension(extension: OpenXRExtensionWrapper)`

#### OpenXRCompositionLayer
- + property `swapchain_state_alpha_swizzle: int` (property)
- + property `swapchain_state_blue_swizzle: int` (property)
- + property `swapchain_state_border_color: Color` (property)
- + property `swapchain_state_green_swizzle: int` (property)
- + property `swapchain_state_horizontal_wrap: int` (property)
- + property `swapchain_state_mag_filter: int` (property)
- + property `swapchain_state_max_anisotropy: float` (property)
- + property `swapchain_state_min_filter: int` (property)
- + property `swapchain_state_mipmap_mode: int` (property)
- + property `swapchain_state_red_swizzle: int` (property)
- + property `swapchain_state_vertical_wrap: int` (property)
- + constant `Filter.FILTER_CUBIC`
- + constant `Filter.FILTER_LINEAR`
- + constant `Filter.FILTER_NEAREST`
- + constant `MipmapMode.MIPMAP_MODE_DISABLED`
- + constant `MipmapMode.MIPMAP_MODE_LINEAR`
- + constant `MipmapMode.MIPMAP_MODE_NEAREST`
- + constant `Swizzle.SWIZZLE_ALPHA`
- + constant `Swizzle.SWIZZLE_BLUE`
- + constant `Swizzle.SWIZZLE_GREEN`
- + constant `Swizzle.SWIZZLE_ONE`
- + constant `Swizzle.SWIZZLE_RED`
- + constant `Swizzle.SWIZZLE_ZERO`
- + constant `Wrap.WRAP_CLAMP_TO_BORDER`
- + constant `Wrap.WRAP_CLAMP_TO_EDGE`
- + constant `Wrap.WRAP_MIRRORED_REPEAT`
- + constant `Wrap.WRAP_MIRROR_CLAMP_TO_EDGE`
- + constant `Wrap.WRAP_REPEAT`

#### OpenXRExtensionWrapperExtension
- − removed method `_get_composition_layer(index: int) -> int`
- − removed method `_get_composition_layer_count() -> int`
- − removed method `_get_composition_layer_order(index: int) -> int`
- − removed method `_get_requested_extensions() -> Dictionary`
- − removed method `_get_suggested_tracker_names() -> PackedStringArray`
- − removed method `_get_viewport_composition_layer_extension_properties() -> Dictionary[]`
- − removed method `_get_viewport_composition_layer_extension_property_defaults() -> Dictionary`
- − removed method `_on_before_instance_created()`
- − removed method `_on_event_polled(event: const void*) -> bool`
- − removed method `_on_instance_created(instance: int)`
- − removed method `_on_instance_destroyed()`
- − removed method `_on_main_swapchains_created()`
- − removed method `_on_post_draw_viewport(viewport: RID)`
- − removed method `_on_pre_draw_viewport(viewport: RID)`
- − removed method `_on_pre_render()`
- − removed method `_on_process()`
- − removed method `_on_register_metadata()`
- − removed method `_on_session_created(session: int)`
- − removed method `_on_session_destroyed()`
- − removed method `_on_state_exiting()`
- − removed method `_on_state_focused()`
- − removed method `_on_state_idle()`
- − removed method `_on_state_loss_pending()`
- − removed method `_on_state_ready()`
- − removed method `_on_state_stopping()`
- − removed method `_on_state_synchronized()`
- − removed method `_on_state_visible()`
- − removed method `_on_viewport_composition_layer_destroyed(layer: const void*)`
- − removed method `_set_android_surface_swapchain_create_info_and_get_next_pointer(property_values: Dictionary, next_pointer: void*) -> int`
- − removed method `_set_hand_joint_locations_and_get_next_pointer(hand_index: int, next_pointer: void*) -> int`
- − removed method `_set_instance_create_info_and_get_next_pointer(next_pointer: void*) -> int`
- − removed method `_set_projection_views_and_get_next_pointer(view_index: int, next_pointer: void*) -> int`
- − removed method `_set_session_create_and_get_next_pointer(next_pointer: void*) -> int`
- − removed method `_set_swapchain_create_info_and_get_next_pointer(next_pointer: void*) -> int`
- − removed method `_set_system_properties_and_get_next_pointer(next_pointer: void*) -> int`
- − removed method `_set_viewport_composition_layer_and_get_next_pointer(layer: const void*, property_values: Dictionary, next_pointer: void*) -> int`
- − removed method `get_openxr_api() -> OpenXRAPIExtension`
- − removed method `register_extension_wrapper()`

#### OpenXRInterface
- + method `get_session_state() -> int`
- + method `set_cpu_level(level: int)`
- + method `set_gpu_level(level: int)`
- + signal `cpu_level_changed(sub_domain: int, from_level: int, to_level: int)`
- + signal `gpu_level_changed(sub_domain: int, from_level: int, to_level: int)`
- + signal `session_synchronized()`
- + constant `PerfSettingsLevel.PERF_SETTINGS_LEVEL_BOOST`
- + constant `PerfSettingsLevel.PERF_SETTINGS_LEVEL_POWER_SAVINGS`
- + constant `PerfSettingsLevel.PERF_SETTINGS_LEVEL_SUSTAINED_HIGH`
- + constant `PerfSettingsLevel.PERF_SETTINGS_LEVEL_SUSTAINED_LOW`
- + constant `PerfSettingsNotificationLevel.PERF_SETTINGS_NOTIF_LEVEL_IMPAIRED`
- + constant `PerfSettingsNotificationLevel.PERF_SETTINGS_NOTIF_LEVEL_NORMAL`
- + constant `PerfSettingsNotificationLevel.PERF_SETTINGS_NOTIF_LEVEL_WARNING`
- + constant `PerfSettingsSubDomain.PERF_SETTINGS_SUB_DOMAIN_COMPOSITING`
- + constant `PerfSettingsSubDomain.PERF_SETTINGS_SUB_DOMAIN_RENDERING`
- + constant `PerfSettingsSubDomain.PERF_SETTINGS_SUB_DOMAIN_THERMAL`
- + constant `SessionState.SESSION_STATE_EXITING`
- + constant `SessionState.SESSION_STATE_FOCUSED`
- + constant `SessionState.SESSION_STATE_IDLE`
- + constant `SessionState.SESSION_STATE_LOSS_PENDING`
- + constant `SessionState.SESSION_STATE_READY`
- + constant `SessionState.SESSION_STATE_STOPPING`
- + constant `SessionState.SESSION_STATE_SYNCHRONIZED`
- + constant `SessionState.SESSION_STATE_UNKNOWN`
- + constant `SessionState.SESSION_STATE_VISIBLE`

#### OptionButton
- + method `get_item_auto_translate_mode(idx: int) -> int`
- + method `set_item_auto_translate_mode(idx: int, mode: int)`

#### PackedByteArray
- + method `bswap16(offset: int = 0, count: int = -1)`
- + method `bswap32(offset: int = 0, count: int = -1)`
- + method `bswap64(offset: int = 0, count: int = -1)`
- + method `erase(value: int) -> bool`
- + method `get_string_from_multibyte_char(encoding: String = "") -> String`
- + method `to_color_array() -> PackedColorArray`
- + method `to_vector2_array() -> PackedVector2Array`
- + method `to_vector3_array() -> PackedVector3Array`
- + method `to_vector4_array() -> PackedVector4Array`

#### PackedColorArray
- + method `erase(value: Color) -> bool`

#### PackedFloat32Array
- + method `erase(value: float) -> bool`

#### PackedFloat64Array
- + method `erase(value: float) -> bool`

#### PackedInt32Array
- + method `erase(value: int) -> bool`

#### PackedInt64Array
- + method `erase(value: int) -> bool`

#### PackedStringArray
- + method `erase(value: String) -> bool`

#### PackedVector2Array
- + method `erase(value: Vector2) -> bool`

#### PackedVector3Array
- + method `erase(value: Vector3) -> bool`

#### PackedVector4Array
- + method `erase(value: Vector4) -> bool`

#### Path3D
- + property `debug_custom_color: Color` (property)
- + signal `debug_color_changed()`

#### Performance
- + constant `Monitor.NAVIGATION_2D_ACTIVE_MAPS`
- + constant `Monitor.NAVIGATION_2D_AGENT_COUNT`
- + constant `Monitor.NAVIGATION_2D_EDGE_CONNECTION_COUNT`
- + constant `Monitor.NAVIGATION_2D_EDGE_COUNT`
- + constant `Monitor.NAVIGATION_2D_EDGE_FREE_COUNT`
- + constant `Monitor.NAVIGATION_2D_EDGE_MERGE_COUNT`
- + constant `Monitor.NAVIGATION_2D_LINK_COUNT`
- + constant `Monitor.NAVIGATION_2D_OBSTACLE_COUNT`
- + constant `Monitor.NAVIGATION_2D_POLYGON_COUNT`
- + constant `Monitor.NAVIGATION_2D_REGION_COUNT`
- + constant `Monitor.NAVIGATION_3D_ACTIVE_MAPS`
- + constant `Monitor.NAVIGATION_3D_AGENT_COUNT`
- + constant `Monitor.NAVIGATION_3D_EDGE_CONNECTION_COUNT`
- + constant `Monitor.NAVIGATION_3D_EDGE_COUNT`
- + constant `Monitor.NAVIGATION_3D_EDGE_FREE_COUNT`
- + constant `Monitor.NAVIGATION_3D_EDGE_MERGE_COUNT`
- + constant `Monitor.NAVIGATION_3D_LINK_COUNT`
- + constant `Monitor.NAVIGATION_3D_OBSTACLE_COUNT`
- + constant `Monitor.NAVIGATION_3D_POLYGON_COUNT`
- + constant `Monitor.NAVIGATION_3D_REGION_COUNT`

#### PhysicsDirectBodyState2D
- + property `collision_layer: int` (property)
- + property `collision_mask: int` (property)

#### PhysicsDirectBodyState2DExtension
- + method `_get_collision_layer() -> int`
- + method `_get_collision_mask() -> int`
- + method `_set_collision_layer(layer: int)`
- + method `_set_collision_mask(mask: int)`

#### PhysicsDirectBodyState3D
- + property `collision_layer: int` (property)
- + property `collision_mask: int` (property)

#### PhysicsDirectBodyState3DExtension
- + method `_get_collision_layer() -> int`
- + method `_get_collision_mask() -> int`
- + method `_set_collision_layer(layer: int)`
- + method `_set_collision_mask(mask: int)`

#### PhysicsServer3D
- + method `soft_body_apply_central_force(body: RID, force: Vector3)`
- + method `soft_body_apply_central_impulse(body: RID, impulse: Vector3)`
- + method `soft_body_apply_point_force(body: RID, point_index: int, force: Vector3)`
- + method `soft_body_apply_point_impulse(body: RID, point_index: int, impulse: Vector3)`
- + method `soft_body_get_shrinking_factor(body: RID) -> float`
- + method `soft_body_set_shrinking_factor(body: RID, shrinking_factor: float)`

#### PhysicsServer3DExtension
- + method `_soft_body_apply_central_force(body: RID, force: Vector3)`
- + method `_soft_body_apply_central_impulse(body: RID, impulse: Vector3)`
- + method `_soft_body_apply_point_force(body: RID, point_index: int, force: Vector3)`
- + method `_soft_body_apply_point_impulse(body: RID, point_index: int, impulse: Vector3)`
- + method `_soft_body_get_shrinking_factor(body: RID) -> float`
- + method `_soft_body_set_shrinking_factor(body: RID, shrinking_factor: float)`

#### Popup
- + property `maximize_disabled: bool` (property)
- + property `minimize_disabled: bool` (property)
- + property `popup_wm_hint: bool` (property)

#### PopupMenu
- + method `get_item_auto_translate_mode(index: int) -> int`
- + method `set_item_auto_translate_mode(index: int, mode: int)`

#### PortableCompressedTexture2D
- + method `set_basisu_compressor_params(uastc_level: int, rdo_quality_loss: float)`
- + constant `CompressionMode.COMPRESSION_MODE_ASTC`

#### ProjectSettings
- + method `get_setting_with_override_and_custom_features(name: StringName, features: PackedStringArray) -> Variant`
- + property `accessibility/general/accessibility_support: int` (property)
- + property `accessibility/general/updates_per_second: int` (property)
- + property `application/run/load_shell_environment: bool` (property)
- + property `debug/settings/gdscript/always_track_call_stacks: bool` (property)
- + property `debug/settings/gdscript/always_track_local_variables: bool` (property)
- + property `debug/shapes/avoidance/2d/agents_radius_color: Color` (property)
- + property `debug/shapes/avoidance/2d/enable_agents_radius: bool` (property)
- + property `debug/shapes/avoidance/2d/enable_obstacles_radius: bool` (property)
- + property `debug/shapes/avoidance/2d/enable_obstacles_static: bool` (property)
- + property `debug/shapes/avoidance/2d/obstacles_radius_color: Color` (property)
- + property `debug/shapes/avoidance/2d/obstacles_static_edge_pushin_color: Color` (property)
- + property `debug/shapes/avoidance/2d/obstacles_static_edge_pushout_color: Color` (property)
- + property `debug/shapes/avoidance/2d/obstacles_static_face_pushin_color: Color` (property)
- + property `debug/shapes/avoidance/2d/obstacles_static_face_pushout_color: Color` (property)
- + property `debug/shapes/avoidance/3d/agents_radius_color: Color` (property)
- + property `debug/shapes/avoidance/3d/enable_agents_radius: bool` (property)
- + property `debug/shapes/avoidance/3d/enable_obstacles_radius: bool` (property)
- + property `debug/shapes/avoidance/3d/enable_obstacles_static: bool` (property)
- + property `debug/shapes/avoidance/3d/obstacles_radius_color: Color` (property)
- + property `debug/shapes/avoidance/3d/obstacles_static_edge_pushin_color: Color` (property)
- + property `debug/shapes/avoidance/3d/obstacles_static_edge_pushout_color: Color` (property)
- + property `debug/shapes/avoidance/3d/obstacles_static_face_pushin_color: Color` (property)
- + property `debug/shapes/avoidance/3d/obstacles_static_face_pushout_color: Color` (property)
- + property `debug/shapes/navigation/2d/agent_path_color: Color` (property)
- + property `debug/shapes/navigation/2d/agent_path_point_size: float` (property)
- + property `debug/shapes/navigation/2d/edge_connection_color: Color` (property)
- + property `debug/shapes/navigation/2d/enable_agent_paths: bool` (property)
- + property `debug/shapes/navigation/2d/enable_edge_connections: bool` (property)
- + property `debug/shapes/navigation/2d/enable_edge_lines: bool` (property)
- + property `debug/shapes/navigation/2d/enable_geometry_face_random_color: bool` (property)
- + property `debug/shapes/navigation/2d/enable_link_connections: bool` (property)
- + property `debug/shapes/navigation/2d/geometry_edge_color: Color` (property)
- + property `debug/shapes/navigation/2d/geometry_edge_disabled_color: Color` (property)
- + property `debug/shapes/navigation/2d/geometry_face_color: Color` (property)
- + property `debug/shapes/navigation/2d/geometry_face_disabled_color: Color` (property)
- + property `debug/shapes/navigation/2d/link_connection_color: Color` (property)
- + property `debug/shapes/navigation/2d/link_connection_disabled_color: Color` (property)
- + property `debug/shapes/navigation/3d/agent_path_color: Color` (property)
- + property `debug/shapes/navigation/3d/agent_path_point_size: float` (property)
- + property `debug/shapes/navigation/3d/edge_connection_color: Color` (property)
- + property `debug/shapes/navigation/3d/enable_agent_paths: bool` (property)
- + property `debug/shapes/navigation/3d/enable_agent_paths_xray: bool` (property)
- + property `debug/shapes/navigation/3d/enable_edge_connections: bool` (property)
- + property `debug/shapes/navigation/3d/enable_edge_connections_xray: bool` (property)
- + property `debug/shapes/navigation/3d/enable_edge_lines: bool` (property)
- + property `debug/shapes/navigation/3d/enable_edge_lines_xray: bool` (property)
- + property `debug/shapes/navigation/3d/enable_geometry_face_random_color: bool` (property)
- + property `debug/shapes/navigation/3d/enable_link_connections: bool` (property)
- + property `debug/shapes/navigation/3d/enable_link_connections_xray: bool` (property)
- + property `debug/shapes/navigation/3d/geometry_edge_color: Color` (property)
- + property `debug/shapes/navigation/3d/geometry_edge_disabled_color: Color` (property)
- + property `debug/shapes/navigation/3d/geometry_face_color: Color` (property)
- + property `debug/shapes/navigation/3d/geometry_face_disabled_color: Color` (property)
- + property `debug/shapes/navigation/3d/link_connection_color: Color` (property)
- + property `debug/shapes/navigation/3d/link_connection_disabled_color: Color` (property)
- + property `display/display_server/driver.visionos: String` (property)
- + property `display/window/size/maximize_disabled: bool` (property)
- + property `display/window/size/minimize_disabled: bool` (property)
- + property `editor/movie_writer/ogv/audio_quality: float` (property)
- + property `editor/movie_writer/ogv/encoding_speed: int` (property)
- + property `editor/movie_writer/ogv/keyframe_interval: int` (property)
- + property `editor/movie_writer/video_quality: float` (property)
- + property `input/ui_accessibility_drag_and_drop: Dictionary` (property)
- + property `input/ui_colorpicker_delete_preset: Dictionary` (property)
- + property `input/ui_focus_mode: Dictionary` (property)
- + property `input/ui_graph_follow_left: Dictionary` (property)
- + property `input/ui_graph_follow_left.macos: Dictionary` (property)
- + property `input/ui_graph_follow_right: Dictionary` (property)
- + property `input/ui_graph_follow_right.macos: Dictionary` (property)
- + property `input_devices/pointing/android/disable_scroll_deadzone: bool` (property)
- + property `input_devices/pointing/android/override_volume_buttons: bool` (property)
- + property `internationalization/locale/line_breaking_strictness: int` (property)
- + property `navigation/2d/merge_rasterizer_cell_scale: float` (property)
- + property `navigation/world/region_use_async_iterations: bool` (property)
- + property `physics/3d/physics_interpolation/scene_traversal: String` (property)
- + property `rendering/anti_aliasing/quality/smaa_edge_detection_threshold: float` (property)
- + property `rendering/reflections/specular_occlusion/enabled: bool` (property)
- + property `rendering/rendering_device/driver.visionos: String` (property)
- + property `rendering/textures/basis_universal/rdo_dict_size: int` (property)
- + property `rendering/textures/basis_universal/zstd_supercompression: bool` (property)
- + property `rendering/textures/basis_universal/zstd_supercompression_level: int` (property)
- + property `xr/openxr/extensions/render_model: bool` (property)
- − removed property `debug/gdscript/warnings/constant_used_as_function: int`
- − removed property `debug/gdscript/warnings/function_used_as_property: int`
- − removed property `debug/gdscript/warnings/property_used_as_function: int`
- − removed property `debug/shapes/avoidance/agents_radius_color: Color`
- − removed property `debug/shapes/avoidance/enable_agents_radius: bool`
- − removed property `debug/shapes/avoidance/enable_obstacles_radius: bool`
- − removed property `debug/shapes/avoidance/enable_obstacles_static: bool`
- − removed property `debug/shapes/avoidance/obstacles_radius_color: Color`
- − removed property `debug/shapes/avoidance/obstacles_static_edge_pushin_color: Color`
- − removed property `debug/shapes/avoidance/obstacles_static_edge_pushout_color: Color`
- − removed property `debug/shapes/avoidance/obstacles_static_face_pushin_color: Color`
- − removed property `debug/shapes/avoidance/obstacles_static_face_pushout_color: Color`
- − removed property `debug/shapes/navigation/agent_path_color: Color`
- − removed property `debug/shapes/navigation/agent_path_point_size: float`
- − removed property `debug/shapes/navigation/edge_connection_color: Color`
- − removed property `debug/shapes/navigation/enable_agent_paths: bool`
- − removed property `debug/shapes/navigation/enable_agent_paths_xray: bool`
- − removed property `debug/shapes/navigation/enable_edge_connections: bool`
- − removed property `debug/shapes/navigation/enable_edge_connections_xray: bool`
- − removed property `debug/shapes/navigation/enable_edge_lines: bool`
- − removed property `debug/shapes/navigation/enable_edge_lines_xray: bool`
- − removed property `debug/shapes/navigation/enable_geometry_face_random_color: bool`
- − removed property `debug/shapes/navigation/enable_link_connections: bool`
- − removed property `debug/shapes/navigation/enable_link_connections_xray: bool`
- − removed property `debug/shapes/navigation/geometry_edge_color: Color`
- − removed property `debug/shapes/navigation/geometry_edge_disabled_color: Color`
- − removed property `debug/shapes/navigation/geometry_face_color: Color`
- − removed property `debug/shapes/navigation/geometry_face_disabled_color: Color`
- − removed property `debug/shapes/navigation/link_connection_color: Color`
- − removed property `debug/shapes/navigation/link_connection_disabled_color: Color`
- − removed property `editor/movie_writer/mjpeg_quality: float`
- − removed property `physics/jolt_physics_3d/simulation/areas_detect_static_bodies: bool`

#### RenderingDevice
- + constant `DataFormat.DATA_FORMAT_ASTC_10x10_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_10x5_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_10x6_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_10x8_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_12x10_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_12x12_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_4x4_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_5x4_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_5x5_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_6x5_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_6x6_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_8x5_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_8x6_SFLOAT_BLOCK`
- + constant `DataFormat.DATA_FORMAT_ASTC_8x8_SFLOAT_BLOCK`
- + constant `Features.SUPPORTS_IMAGE_ATOMIC_32_BIT`
- + constant `Features.SUPPORTS_METALFX_SPATIAL`
- + constant `Features.SUPPORTS_METALFX_TEMPORAL`
- ~ method `texture_create_from_extension(type: int, format: int, samples: int, usage_flags: int, image: int, width: int, height: int, depth: int, layers: int) -> RID` → `texture_create_from_extension(type: int, format: int, samples: int, usage_flags: int, image: int, width: int, height: int, depth: int, layers: int, mipmaps: int = 1) -> RID`

#### RenderingServer
- + method `environment_set_fog_depth(env: RID, curve: float, begin: float, end: float)`
- + method `instance_teleport(instance: RID)`
- + method `mesh_surface_get_format_index_stride(format: int, vertex_count: int) -> int`
- + method `mesh_surface_update_index_region(mesh: RID, surface: int, offset: int, data: PackedByteArray)`
- + constant `CANVAS_LAYER_MAX`
- + constant `CANVAS_LAYER_MIN`
- + constant `ViewportScreenSpaceAA.VIEWPORT_SCREEN_SPACE_AA_SMAA`
- − removed method `instance_reset_physics_interpolation(instance: RID)`
- − removed method `instance_set_interpolated(instance: RID, interpolated: bool)`

#### Resource
- + method `duplicate_deep(deep_subresources_mode: int = 1) -> Resource`
- + constant `DeepDuplicateMode.DEEP_DUPLICATE_ALL`
- + constant `DeepDuplicateMode.DEEP_DUPLICATE_INTERNAL`
- + constant `DeepDuplicateMode.DEEP_DUPLICATE_NONE`
- ~ method `duplicate(subresources: bool = false) -> Resource` → `duplicate(deep: bool = false) -> Resource`

#### ResourceImporter
- + method `_get_build_dependencies(path: String) -> PackedStringArray`

#### ResourceImporterDynamicFont
- + property `modulate_color_glyphs: bool` (property)

#### ResourceImporterLayeredTexture
- + property `compress/rdo_quality_loss: float` (property)
- + property `compress/uastc_level: int` (property)

#### ResourceImporterScene
- + property `materials/extract: int` (property)
- + property `materials/extract_format: int` (property)
- + property `materials/extract_path: String` (property)
- + property `nodes/root_script: Script` (property)
- + property `nodes/use_name_suffixes: bool` (property)

#### ResourceImporterTexture
- + property `compress/rdo_quality_loss: float` (property)
- + property `compress/uastc_level: int` (property)
- + property `process/channel_remap/alpha: int` (property)
- + property `process/channel_remap/blue: int` (property)
- + property `process/channel_remap/green: int` (property)
- + property `process/channel_remap/red: int` (property)
- ⚠ deprecated property `process/normal_map_invert_y: bool`

#### ResourceSaver
- + method `set_uid(resource: String, uid: int) -> int`

#### ResourceUID
- + method `create_id_for_path(path: String) -> int`
- + method `ensure_path(path_or_uid: String) -> String`
- + method `path_to_uid(path: String) -> String`
- + method `uid_to_path(uid: String) -> String`

#### RichTextLabel
- + method `add_hr(width: int = 90, height: int = 2, color: Color = Color(1, 1, 1, 1), alignment: int = 1, width_in_percent: bool = true, height_in_percent: bool = false)`
- + method `get_line_height(line: int) -> int`
- + method `get_line_width(line: int) -> int`
- + method `get_visible_content_rect() -> Rect2i`
- + method `reload_effects()`
- + method `set_table_column_name(column: int, name: String)`
- + property `autowrap_trim_flags: int` (property)
- + property `focus_mode: int` (property)
- + property `scroll_following_visible_characters: bool` (property)
- ~ method `add_image(image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), key: Variant = null, pad: bool = false, tooltip: String = "", size_in_percent: bool = false)` → `add_image(image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), key: Variant = null, pad: bool = false, tooltip: String = "", width_in_percent: bool = false, height_in_percent: bool = false, alt_text: String = "")`
- ~ method `push_strikethrough()` → `push_strikethrough(color: Color = Color(0, 0, 0, 0))`
- ~ method `push_table(columns: int, inline_align: int = 0, align_to_row: int = -1)` → `push_table(columns: int, inline_align: int = 0, align_to_row: int = -1, name: String = "")`
- ~ method `push_underline()` → `push_underline(color: Color = Color(0, 0, 0, 0))`
- ~ method `update_image(key: Variant, mask: int, image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), pad: bool = false, tooltip: String = "", size_in_percent: bool = false)` → `update_image(key: Variant, mask: int, image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), pad: bool = false, tooltip: String = "", width_in_percent: bool = false, height_in_percent: bool = false)`

#### SceneState
- + method `get_base_scene_state() -> SceneState`
- + method `get_path() -> String`

#### SceneTree
- + method `is_accessibility_enabled() -> bool`
- + method `is_accessibility_supported() -> bool`
- + signal `scene_changed()`

#### ScriptEditor
- + method `clear_docs_from_script(script: Script)`

#### ScriptLanguage
- + constant `ScriptNameCasing.SCRIPT_NAME_CASING_CAMEL_CASE`

#### ScrollBar
- + property `focus_mode: int` (property)

#### Skeleton3D
- + method `advance(delta: float)`
- + constant `ModifierCallbackModeProcess.MODIFIER_CALLBACK_MODE_PROCESS_MANUAL`

#### SkeletonModifier3D
- + method `_process_modification_with_delta(delta: float)`
- + method `_skeleton_changed(old_skeleton: Skeleton3D, new_skeleton: Skeleton3D)`
- + method `_validate_bone_names()`
- ⚠ deprecated method `_process_modification()`

#### Slider
- + property `ticks_position: int` (property)
- + constant `TickPosition.TICK_POSITION_BOTH`
- + constant `TickPosition.TICK_POSITION_BOTTOM_RIGHT`
- + constant `TickPosition.TICK_POSITION_CENTER`
- + constant `TickPosition.TICK_POSITION_TOP_LEFT`

#### SoftBody3D
- + method `apply_central_force(force: Vector3)`
- + method `apply_central_impulse(impulse: Vector3)`
- + method `apply_force(point_index: int, force: Vector3)`
- + method `apply_impulse(point_index: int, impulse: Vector3)`
- + property `shrinking_factor: float` (property)

#### SplitContainer
- + property `touch_dragger_enabled: bool` (property)

#### SpringBoneCollisionCapsule3D
- + property `mid_height: float` (property)

#### SpringBoneSimulator3D
- + method `get_joint_rotation_axis_vector(index: int, joint: int) -> Vector3`
- + method `get_rotation_axis_vector(index: int) -> Vector3`
- + method `set_joint_rotation_axis_vector(index: int, joint: int, vector: Vector3)`
- + method `set_rotation_axis_vector(index: int, vector: Vector3)`
- + property `external_force: Vector3` (property)
- + constant `RotationAxis.ROTATION_AXIS_CUSTOM`

#### String
- + method `remove_char(what: int) -> String`
- + method `remove_chars(chars: String) -> String`
- + method `replace_char(key: int, with: int) -> String`
- + method `replace_chars(keys: String, with: int) -> String`
- + method `to_kebab_case() -> String`
- + method `to_multibyte_char_buffer(encoding: String = "") -> PackedByteArray`
- + method `uri_file_decode() -> String`
- ~ method `chr(char: int) -> String` → `chr(code: int) -> String`
- ~ method `path_join(file: String) -> String` → `path_join(path: String) -> String`

#### StringName
- + method `remove_char(what: int) -> String`
- + method `remove_chars(chars: String) -> String`
- + method `replace_char(key: int, with: int) -> String`
- + method `replace_chars(keys: String, with: int) -> String`
- + method `to_kebab_case() -> String`
- + method `to_multibyte_char_buffer(encoding: String = "") -> PackedByteArray`
- + method `uri_file_decode() -> String`
- ~ method `path_join(file: String) -> String` → `path_join(path: String) -> String`

#### SystemFont
- + property `modulate_color_glyphs: bool` (property)

#### TabBar
- + property `close_with_middle_mouse: bool` (property)

#### TextEdit
- + method `get_next_composite_character_column(line: int, column: int) -> int`
- + method `get_previous_composite_character_column(line: int, column: int) -> int`
- + property `backspace_deletes_composite_character_enabled: bool` (property)
- + property `tab_input_mode: bool` (property)
- + property `virtual_keyboard_show_on_focus: bool` (property)

#### TextLine
- + method `get_inferred_direction() -> int`
- ~ method `draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1))` → `draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1))` → `draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`

#### TextParagraph
- + method `get_inferred_direction() -> int`
- + method `get_range() -> Vector2i`
- ~ method `draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), dc_color: Color = Color(1, 1, 1, 1))` → `draw(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), dc_color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_dropcap(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1))` → `draw_dropcap(canvas: RID, pos: Vector2, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_dropcap_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1))` → `draw_dropcap_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_line(canvas: RID, pos: Vector2, line: int, color: Color = Color(1, 1, 1, 1))` → `draw_line(canvas: RID, pos: Vector2, line: int, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_line_outline(canvas: RID, pos: Vector2, line: int, outline_size: int = 1, color: Color = Color(1, 1, 1, 1))` → `draw_line_outline(canvas: RID, pos: Vector2, line: int, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), dc_color: Color = Color(1, 1, 1, 1))` → `draw_outline(canvas: RID, pos: Vector2, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), dc_color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`

#### TextServer
- + method `font_clear_system_fallback_cache()`
- + method `font_get_size_cache_info(font_rid: RID) -> Dictionary[]`
- + method `font_is_modulate_color_glyphs(font_rid: RID) -> bool`
- + method `font_set_modulate_color_glyphs(font_rid: RID, force_autohinter: bool)`
- + method `shaped_get_run_count(shaped: RID) -> int`
- + method `shaped_get_run_direction(shaped: RID, index: int) -> int`
- + method `shaped_get_run_font_rid(shaped: RID, index: int) -> RID`
- + method `shaped_get_run_font_size(shaped: RID, index: int) -> int`
- + method `shaped_get_run_language(shaped: RID, index: int) -> String`
- + method `shaped_get_run_object(shaped: RID, index: int) -> Variant`
- + method `shaped_get_run_range(shaped: RID, index: int) -> Vector2i`
- + method `shaped_get_run_text(shaped: RID, index: int) -> String`
- + method `shaped_get_span_object(shaped: RID, index: int) -> Variant`
- + method `shaped_get_span_text(shaped: RID, index: int) -> String`
- + method `shaped_get_text(shaped: RID) -> String`
- + constant `LineBreakFlag.BREAK_TRIM_END_EDGE_SPACES`
- + constant `LineBreakFlag.BREAK_TRIM_START_EDGE_SPACES`
- + constant `OverrunBehavior.OVERRUN_TRIM_ELLIPSIS_FORCE`
- + constant `OverrunBehavior.OVERRUN_TRIM_WORD_ELLIPSIS_FORCE`
- ~ method `font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color = Color(1, 1, 1, 1))` → `font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color = Color(1, 1, 1, 1))` → `font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `shaped_text_draw(shaped: RID, canvas: RID, pos: Vector2, clip_l: float = -1, clip_r: float = -1, color: Color = Color(1, 1, 1, 1))` → `shaped_text_draw(shaped: RID, canvas: RID, pos: Vector2, clip_l: float = -1, clip_r: float = -1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ~ method `shaped_text_draw_outline(shaped: RID, canvas: RID, pos: Vector2, clip_l: float = -1, clip_r: float = -1, outline_size: int = 1, color: Color = Color(1, 1, 1, 1))` → `shaped_text_draw_outline(shaped: RID, canvas: RID, pos: Vector2, clip_l: float = -1, clip_r: float = -1, outline_size: int = 1, color: Color = Color(1, 1, 1, 1), oversampling: float = 0.0)`
- ⚠ deprecated method `font_get_global_oversampling() -> float`
- ⚠ deprecated method `font_set_global_oversampling(oversampling: float)`
- ⚠ deprecated constant `LineBreakFlag.BREAK_TRIM_EDGE_SPACES`

#### TextServerExtension
- + method `_font_clear_system_fallback_cache()`
- + method `_font_get_size_cache_info(font_rid: RID) -> Dictionary[]`
- + method `_font_is_modulate_color_glyphs(font_rid: RID) -> bool`
- + method `_font_set_modulate_color_glyphs(font_rid: RID, modulate: bool)`
- + method `_reference_oversampling_level(oversampling: float)`
- + method `_shaped_get_run_count(shaped: RID) -> int`
- + method `_shaped_get_run_direction(shaped: RID, index: int) -> int`
- + method `_shaped_get_run_font_rid(shaped: RID, index: int) -> RID`
- + method `_shaped_get_run_font_size(shaped: RID, index: int) -> int`
- + method `_shaped_get_run_language(shaped: RID, index: int) -> String`
- + method `_shaped_get_run_object(shaped: RID, index: int) -> Variant`
- + method `_shaped_get_run_range(shaped: RID, index: int) -> Vector2i`
- + method `_shaped_get_run_text(shaped: RID, index: int) -> String`
- + method `_shaped_get_span_object(shaped: RID, index: int) -> Variant`
- + method `_shaped_get_span_text(shaped: RID, index: int) -> String`
- + method `_shaped_get_text(shaped: RID) -> String`
- + method `_unreference_oversampling_level(oversampling: float)`
- ~ method `_font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color)` → `_font_draw_glyph(font_rid: RID, canvas: RID, size: int, pos: Vector2, index: int, color: Color, oversampling: float)`
- ~ method `_font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color)` → `_font_draw_glyph_outline(font_rid: RID, canvas: RID, size: int, outline_size: int, pos: Vector2, index: int, color: Color, oversampling: float)`
- ~ method `_shaped_text_draw(shaped: RID, canvas: RID, pos: Vector2, clip_l: float, clip_r: float, color: Color)` → `_shaped_text_draw(shaped: RID, canvas: RID, pos: Vector2, clip_l: float, clip_r: float, color: Color, oversampling: float)`
- ~ method `_shaped_text_draw_outline(shaped: RID, canvas: RID, pos: Vector2, clip_l: float, clip_r: float, outline_size: int, color: Color)` → `_shaped_text_draw_outline(shaped: RID, canvas: RID, pos: Vector2, clip_l: float, clip_r: float, outline_size: int, color: Color, oversampling: float)`

#### Theme
- + method `rename_type(old_theme_type: StringName, theme_type: StringName)`

#### TileMapLayer
- + property `physics_quadrant_size: int` (property)

#### TranslationDomain
- + method `get_locale_override() -> String`
- + method `set_locale_override(locale: String)`
- + property `enabled: bool` (property)

#### TreeItem
- + method `get_description(column: int) -> String`
- + method `set_button_description(column: int, button_index: int, description: String)`
- + method `set_description(column: int, description: String)`
- ~ method `add_button(column: int, button: Texture2D, id: int = -1, disabled: bool = false, tooltip_text: String = "")` → `add_button(column: int, button: Texture2D, id: int = -1, disabled: bool = false, tooltip_text: String = "", description: String = "")`

#### TriangleMesh
- + method `create_from_faces(faces: PackedVector3Array) -> bool`
- + method `get_faces() -> PackedVector3Array`
- + method `intersect_ray(begin: Vector3, dir: Vector3) -> Dictionary`
- + method `intersect_segment(begin: Vector3, end: Vector3) -> Dictionary`

#### VehicleWheel3D
- + property `physics_interpolation_mode: int` (property)

#### VideoStreamPlayer
- + property `speed_scale: float` (property)

#### Viewport
- + method `get_oversampling() -> float`
- + method `gui_get_drag_description() -> String`
- + method `gui_set_drag_description(description: String)`
- + property `oversampling: bool` (property)
- + property `oversampling_override: float` (property)
- + constant `ScreenSpaceAA.SCREEN_SPACE_AA_SMAA`

#### VisibleOnScreenNotifier2D
- + property `show_rect: bool` (property)

#### VisualShader
- ⚠ deprecated property `graph_offset: Vector2`

#### Window
- + method `get_focused_window() -> Window`
- + property `accessibility_description: String` (property)
- + property `accessibility_name: String` (property)
- + property `maximize_disabled: bool` (property)
- + property `minimize_disabled: bool` (property)
- + property `popup_wm_hint: bool` (property)
- + constant `Flags.FLAG_MAXIMIZE_DISABLED`
- + constant `Flags.FLAG_MINIMIZE_DISABLED`
- + constant `Flags.FLAG_POPUP_WM_HINT`

#### WorkerThreadPool
- + method `get_caller_group_id() -> int`
- + method `get_caller_task_id() -> int`

#### XRBodyTracker
- + constant `Joint.JOINT_LEFT_FOOT_TWIST`
- + constant `Joint.JOINT_LEFT_HEEL`
- + constant `Joint.JOINT_LEFT_MIDDLE_FOOT`
- + constant `Joint.JOINT_LEFT_SCAPULA`
- + constant `Joint.JOINT_LEFT_WRIST_TWIST`
- + constant `Joint.JOINT_LOWER_CHEST`
- + constant `Joint.JOINT_RIGHT_FOOT_TWIST`
- + constant `Joint.JOINT_RIGHT_HEEL`
- + constant `Joint.JOINT_RIGHT_MIDDLE_FOOT`
- + constant `Joint.JOINT_RIGHT_SCAPULA`
- + constant `Joint.JOINT_RIGHT_WRIST_TWIST`

#### XRCamera3D
- + property `physics_interpolation_mode: int` (property)

#### XRInterface
- + constant `PlayAreaMode.XR_PLAY_AREA_CUSTOM`
- + constant `VRSTextureFormat.XR_VRS_TEXTURE_FORMAT_FRAGMENT_DENSITY_MAP`
- + constant `VRSTextureFormat.XR_VRS_TEXTURE_FORMAT_FRAGMENT_SHADING_RATE`
- + constant `VRSTextureFormat.XR_VRS_TEXTURE_FORMAT_UNIFIED`

#### XRInterfaceExtension
- + method `_get_vrs_texture_format() -> int`

#### XRNode3D
- + property `physics_interpolation_mode: int` (property)

#### ZIPPacker
- + property `compression_level: int` (property)
- + constant `CompressionLevel.COMPRESSION_BEST`
- + constant `CompressionLevel.COMPRESSION_DEFAULT`
- + constant `CompressionLevel.COMPRESSION_FAST`
- + constant `CompressionLevel.COMPRESSION_NONE`

#### ZIPReader
- + method `get_compression_level(path: String, case_sensitive: bool = true) -> int`
