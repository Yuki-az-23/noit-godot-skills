# Godot engine API changes (4.6-stable → 4.7.2-stable)

> Derived from the Godot Engine class reference (MIT License, © Godot Engine contributors, Juan Linietsky, Ariel Manzur). See `licenses/GODOT-LICENSE.txt` at the plugin root.

Generated from the engine's own class reference XML (doc/classes and modules/*/doc_classes) at each release tag. `+` added, `~` signature changed, `⚠` newly deprecated, `−` removed.

- 4.6-stable: 1058 classes
- 4.7.2-stable: 1071 classes

## 4.6-stable → 4.7.2-stable

### New classes (13)

- **AccessibilityServer** ← Object: A server interface for screen reader support.
- **AreaLight3D** ← Light3D: An area light, such as a neon light tube or a screen.
- **AwaitTweener** ← Tweener: Awaits a specified signal.
- **BlitMaterial** ← Material: A material that processes blit calls to a DrawableTexture.
- **DrawableTexture2D** ← Texture2D: A 2D texture that supports drawing to itself via Blit calls.
- **GDScriptLanguageProtocol** ← JSONRPC *(experimental)*: GDScript language server.
- **GDScriptTextDocument** ← RefCounted: Document related language server functionality.
- **GDScriptWorkspace** ← RefCounted *(experimental)*: Workspace related language server functionality.
- **RDAccelerationStructureGeometry** ← RefCounted *(experimental)*: Acceleration structure geometry (used by [RenderingDevice]).
- **RDAccelerationStructureInstance** ← RefCounted *(experimental)*: Acceleration structure instance (used by [RenderingDevice]).
- **RDHitGroup** ← RefCounted *(experimental)*: Hit group (used by [RenderingDevice]).
- **RDPipelineShader** ← RefCounted *(experimental)*: Pipeline shader (used by [RenderingDevice]).
- **VirtualJoystick** ← Control: A virtual joystick control for touchscreen devices.

### Changed classes (138)

#### @GDScript
- ⚠ deprecated method `type_exists(type: StringName) -> bool`

#### @GlobalScope
- + property `AccessibilityServer: AccessibilityServer` (property)
- + property `GDScriptLanguageProtocol: GDScriptLanguageProtocol` (property)
- + constant `INT16_MAX`
- + constant `INT16_MIN`
- + constant `INT32_MAX`
- + constant `INT32_MIN`
- + constant `INT64_MAX`
- + constant `INT64_MIN`
- + constant `INT8_MAX`
- + constant `INT8_MIN`
- + constant `JoyButton.JOY_BUTTON_MISC2`
- + constant `JoyButton.JOY_BUTTON_MISC3`
- + constant `JoyButton.JOY_BUTTON_MISC4`
- + constant `JoyButton.JOY_BUTTON_MISC5`
- + constant `JoyButton.JOY_BUTTON_MISC6`
- + constant `UINT16_MAX`
- + constant `UINT32_MAX`
- + constant `UINT8_MAX`

#### AnimationLibrary
- ~ signal `animation_added(name: StringName)` → `animation_added(anim_name: StringName)`
- ~ signal `animation_changed(name: StringName)` → `animation_changed(anim_name: StringName)`
- ~ signal `animation_removed(name: StringName)` → `animation_removed(anim_name: StringName)`
- ~ signal `animation_renamed(name: StringName, to_name: StringName)` → `animation_renamed(old_name: StringName, new_name: StringName)`

#### AnimationNode
- + signal `node_updated(object_id: int)`
- ~ signal `animation_node_removed(object_id: int, name: String)` → `animation_node_removed(object_id: int, node_name: String)`

#### AnimationNodeBlendSpace1D
- + method `find_blend_point_by_name(name: StringName) -> int`
- + method `get_blend_point_name(point: int) -> StringName`
- + method `reorder_blend_point(from_index: int, to_index: int)`
- + method `set_blend_point_name(point: int, name: StringName)`
- + property `cyclic_length: float` (property)
- + property `sync_mode: int` (property)
- + constant `SyncMode.SYNC_MODE_CYCLIC_CONSTANT`
- + constant `SyncMode.SYNC_MODE_CYCLIC_MUTABLE`
- + constant `SyncMode.SYNC_MODE_INDEPENDENT`
- + constant `SyncMode.SYNC_MODE_NONE`
- ~ method `add_blend_point(node: AnimationRootNode, pos: float, at_index: int = -1)` → `add_blend_point(node: AnimationRootNode, pos: float, at_index: int = -1, name: StringName = &"")`
- ⚠ deprecated property `sync: bool`

#### AnimationNodeBlendSpace2D
- + method `find_blend_point_by_name(name: StringName) -> int`
- + method `get_blend_point_name(point: int) -> StringName`
- + method `reorder_blend_point(from_index: int, to_index: int)`
- + method `set_blend_point_name(point: int, name: StringName)`
- + property `cyclic_length: float` (property)
- + property `sync_mode: int` (property)
- + constant `SyncMode.SYNC_MODE_CYCLIC_CONSTANT`
- + constant `SyncMode.SYNC_MODE_CYCLIC_MUTABLE`
- + constant `SyncMode.SYNC_MODE_INDEPENDENT`
- + constant `SyncMode.SYNC_MODE_NONE`
- ~ method `add_blend_point(node: AnimationRootNode, pos: Vector2, at_index: int = -1)` → `add_blend_point(node: AnimationRootNode, pos: Vector2, at_index: int = -1, name: StringName = &"")`
- ⚠ deprecated property `sync: bool`

#### AnimationPlayer
- ~ signal `current_animation_changed(name: StringName)` → `current_animation_changed(anim_name: StringName)`

#### AudioEffectInstance
- ~ method `_process(src_buffer: const void*, dst_buffer: AudioFrame*, frame_count: int)` → `_process(src_buffer: const void*, r_dst_buffer: AudioFrame*, frame_count: int)`

#### AudioEffectSpectrumAnalyzer
- − removed property `tap_back_pos: float`

#### AudioStreamInteractive
- + constant `TransitionToTime.TRANSITION_TO_TIME_PREVIOUS_POSITION`

#### AudioStreamRandomizer
- + property `stream_{index}/stream: AudioStream` (property)
- + property `stream_{index}/weight: float` (property)

#### Basis
- + method `is_orthonormal() -> bool`

#### CPUParticles2D
- ~ method `request_particles_process(process_time: float)` → `request_particles_process(process_time: float, process_time_residual: float = 0.0)`

#### CPUParticles3D
- ~ method `request_particles_process(process_time: float)` → `request_particles_process(process_time: float, process_time_residual: float = 0.0)`

#### CSGShape3D
- + property `autosmooth: bool` (property)
- + property `smoothing_angle: float` (property)

#### CameraFeed
- + method `_get_formats() -> Array`
- + method `_set_format(index: int, parameters: Dictionary) -> bool`

#### CanvasItem
- + property `oversampling_with_scale: int` (property)
- + constant `OversamplingWithScale.OVERSAMPLING_WITH_SCALE_DISABLED`
- + constant `OversamplingWithScale.OVERSAMPLING_WITH_SCALE_ENABLED`
- + constant `OversamplingWithScale.OVERSAMPLING_WITH_SCALE_MAX`
- + constant `OversamplingWithScale.OVERSAMPLING_WITH_SCALE_PARENT_NODE`

#### CodeEdit
- + method `join_lines(line_ending: String = " ")`
- + constant `CodeCompletionKind.KIND_KEYWORD`

#### CollisionObject2D
- + method `get_shape_owner_one_way_collision_direction(owner_id: int) -> Vector2`
- + method `shape_owner_set_one_way_collision_direction(owner_id: int, direction: Vector2)`

#### CollisionPolygon2D
- + property `one_way_collision_direction: Vector2` (property)

#### CollisionShape2D
- + property `one_way_collision_direction: Vector2` (property)

#### Container
- + property `accessibility_region: bool` (property)
- + property `propagate_maximum_size: bool` (property)

#### Control
- + method `_get_cursor_shape(at_position: Vector2) -> int`
- + method `_get_maximum_size() -> Vector2`
- + method `_get_tooltip_auto_translate_mode_at(at_position: Vector2) -> int`
- + method `get_bound_minimum_size() -> Vector2`
- + method `get_combined_maximum_size() -> Vector2`
- + method `get_maximum_size() -> Vector2`
- + method `update_maximum_size()`
- + property `custom_maximum_size: Vector2` (property)
- + property `offset_transform_enabled: bool` (property)
- + property `offset_transform_pivot: Vector2` (property)
- + property `offset_transform_pivot_ratio: Vector2` (property)
- + property `offset_transform_position: Vector2` (property)
- + property `offset_transform_position_ratio: Vector2` (property)
- + property `offset_transform_rotation: float` (property)
- + property `offset_transform_scale: Vector2` (property)
- + property `offset_transform_visual_only: bool` (property)
- + property `propagate_maximum_size: bool` (property)
- + property `translation_context: StringName` (property)
- + signal `maximum_size_changed()`
- ~ method `get_cursor_shape(position: Vector2 = Vector2(0, 0)) -> int` → `get_cursor_shape(at_position: Vector2 = Vector2(0, 0)) -> int`

#### Curve
- + property `point_{index}/left_mode: int` (property)
- + property `point_{index}/left_tangent: float` (property)
- + property `point_{index}/position: Vector2` (property)
- + property `point_{index}/right_mode: int` (property)
- + property `point_{index}/right_tangent: float` (property)

#### Curve2D
- + property `point_{index}/in: Vector2` (property)
- + property `point_{index}/out: Vector2` (property)
- + property `point_{index}/position: Vector2` (property)

#### Curve3D
- + property `point_{index}/in: Vector3` (property)
- + property `point_{index}/out: Vector3` (property)
- + property `point_{index}/position: Vector3` (property)
- + property `point_{index}/tilt: float` (property)

#### DPITexture
- + property `fix_alpha_border: bool` (property)
- + property `premult_alpha: bool` (property)

#### DirAccess
- + method `get_drive_label(idx: int) -> String`

#### DisplayServer
- + method `is_in_pip_mode(window_id: int = 0) -> bool`
- + method `pip_mode_enter(window_id: int = 0)`
- + method `pip_mode_set_aspect_ratio(numerator: int, denominator: int, window_id: int = 0)`
- + method `pip_mode_set_auto_enter_on_background(auto_enter_on_background: bool, window_id: int = 0)`
- + method `window_get_hdr_output_current_max_luminance(window_id: int = 0) -> float`
- + method `window_get_hdr_output_current_reference_luminance(window_id: int = 0) -> float`
- + method `window_get_hdr_output_max_luminance(window_id: int = 0) -> float`
- + method `window_get_hdr_output_reference_luminance(window_id: int = 0) -> float`
- + method `window_get_output_max_linear_value(window_id: int = 0) -> float`
- + method `window_is_hdr_output_enabled(window_id: int = 0) -> bool`
- + method `window_is_hdr_output_requested(window_id: int = 0) -> bool`
- + method `window_is_hdr_output_supported(window_id: int = 0) -> bool`
- + method `window_request_hdr_output(enable: bool, window_id: int = 0)`
- + method `window_set_hdr_output_max_luminance(max_luminance: float, window_id: int = 0)`
- + method `window_set_hdr_output_reference_luminance(reference_luminance: float, window_id: int = 0)`
- + method `window_set_icon(icon: Image, window_id: int = 0)`
- + method `window_set_taskbar_progress_state(state: int, window_id: int = 0)`
- + method `window_set_taskbar_progress_value(value: float, window_id: int = 0)`
- + signal `orientation_changed(orientation: int)`
- + constant `AccessibilityRole.ROLE_REGION`
- + constant `AccessibilityRole.ROLE_TEXT_RUN`
- + constant `Feature.FEATURE_HDR_OUTPUT`
- + constant `Feature.FEATURE_PIP_MODE`
- + constant `HandleType.GLX_FBCONFIG`
- + constant `HandleType.GLX_VISUALID`
- + constant `ProgressState.PROGRESS_STATE_ERROR`
- + constant `ProgressState.PROGRESS_STATE_INDETERMINATE`
- + constant `ProgressState.PROGRESS_STATE_NOPROGRESS`
- + constant `ProgressState.PROGRESS_STATE_NORMAL`
- + constant `ProgressState.PROGRESS_STATE_PAUSED`
- + constant `WindowEvent.WINDOW_EVENT_OUTPUT_MAX_LINEAR_VALUE_CHANGED`
- ~ method `accessibility_update_set_bounds(id: RID, p_rect: Rect2)` → `accessibility_update_set_bounds(id: RID, rect: Rect2)`
- ⚠ deprecated method `accessibility_create_element(window_id: int, role: int) -> RID`
- ⚠ deprecated method `accessibility_create_sub_element(parent_rid: RID, role: int, insert_pos: int = -1) -> RID`
- ⚠ deprecated method `accessibility_create_sub_text_edit_elements(parent_rid: RID, shaped_text: RID, min_height: float, insert_pos: int = -1, is_last_line: bool = false) -> RID`
- ⚠ deprecated method `accessibility_element_get_meta(id: RID) -> Variant`
- ⚠ deprecated method `accessibility_element_set_meta(id: RID, meta: Variant)`
- ⚠ deprecated method `accessibility_free_element(id: RID)`
- ⚠ deprecated method `accessibility_get_window_root(window_id: int) -> RID`
- ⚠ deprecated method `accessibility_has_element(id: RID) -> bool`
- ⚠ deprecated method `accessibility_set_window_focused(window_id: int, focused: bool)`
- ⚠ deprecated method `accessibility_set_window_rect(window_id: int, rect_out: Rect2, rect_in: Rect2)`
- ⚠ deprecated method `accessibility_update_add_action(id: RID, action: int, callable: Callable)`
- ⚠ deprecated method `accessibility_update_add_child(id: RID, child_id: RID)`
- ⚠ deprecated method `accessibility_update_add_custom_action(id: RID, action_id: int, action_description: String)`
- ⚠ deprecated method `accessibility_update_add_related_controls(id: RID, related_id: RID)`
- ⚠ deprecated method `accessibility_update_add_related_described_by(id: RID, related_id: RID)`
- ⚠ deprecated method `accessibility_update_add_related_details(id: RID, related_id: RID)`
- ⚠ deprecated method `accessibility_update_add_related_flow_to(id: RID, related_id: RID)`
- ⚠ deprecated method `accessibility_update_add_related_labeled_by(id: RID, related_id: RID)`
- ⚠ deprecated method `accessibility_update_add_related_radio_group(id: RID, related_id: RID)`
- ⚠ deprecated method `accessibility_update_set_active_descendant(id: RID, other_id: RID)`
- ⚠ deprecated method `accessibility_update_set_background_color(id: RID, color: Color)`
- ⚠ deprecated method `accessibility_update_set_bounds(id: RID, rect: Rect2)`
- ⚠ deprecated method `accessibility_update_set_checked(id: RID, checekd: bool)`
- ⚠ deprecated method `accessibility_update_set_classname(id: RID, classname: String)`
- ⚠ deprecated method `accessibility_update_set_color_value(id: RID, color: Color)`
- ⚠ deprecated method `accessibility_update_set_description(id: RID, description: String)`
- ⚠ deprecated method `accessibility_update_set_error_message(id: RID, other_id: RID)`
- ⚠ deprecated method `accessibility_update_set_extra_info(id: RID, name: String)`
- ⚠ deprecated method `accessibility_update_set_flag(id: RID, flag: int, value: bool)`
- ⚠ deprecated method `accessibility_update_set_focus(id: RID)`
- ⚠ deprecated method `accessibility_update_set_foreground_color(id: RID, color: Color)`
- ⚠ deprecated method `accessibility_update_set_in_page_link_target(id: RID, other_id: RID)`
- ⚠ deprecated method `accessibility_update_set_language(id: RID, language: String)`
- ⚠ deprecated method `accessibility_update_set_list_item_count(id: RID, size: int)`
- ⚠ deprecated method `accessibility_update_set_list_item_expanded(id: RID, expanded: bool)`
- ⚠ deprecated method `accessibility_update_set_list_item_index(id: RID, index: int)`
- ⚠ deprecated method `accessibility_update_set_list_item_level(id: RID, level: int)`
- ⚠ deprecated method `accessibility_update_set_list_item_selected(id: RID, selected: bool)`
- ⚠ deprecated method `accessibility_update_set_list_orientation(id: RID, vertical: bool)`
- ⚠ deprecated method `accessibility_update_set_live(id: RID, live: int)`
- ⚠ deprecated method `accessibility_update_set_member_of(id: RID, group_id: RID)`
- ⚠ deprecated method `accessibility_update_set_name(id: RID, name: String)`
- ⚠ deprecated method `accessibility_update_set_next_on_line(id: RID, other_id: RID)`
- ⚠ deprecated method `accessibility_update_set_num_jump(id: RID, jump: float)`
- ⚠ deprecated method `accessibility_update_set_num_range(id: RID, min: float, max: float)`
- ⚠ deprecated method `accessibility_update_set_num_step(id: RID, step: float)`
- ⚠ deprecated method `accessibility_update_set_num_value(id: RID, position: float)`
- ⚠ deprecated method `accessibility_update_set_placeholder(id: RID, placeholder: String)`
- ⚠ deprecated method `accessibility_update_set_popup_type(id: RID, popup: int)`
- ⚠ deprecated method `accessibility_update_set_previous_on_line(id: RID, other_id: RID)`
- ⚠ deprecated method `accessibility_update_set_role(id: RID, role: int)`
- ⚠ deprecated method `accessibility_update_set_role_description(id: RID, description: String)`
- ⚠ deprecated method `accessibility_update_set_scroll_x(id: RID, position: float)`
- ⚠ deprecated method `accessibility_update_set_scroll_x_range(id: RID, min: float, max: float)`
- ⚠ deprecated method `accessibility_update_set_scroll_y(id: RID, position: float)`
- ⚠ deprecated method `accessibility_update_set_scroll_y_range(id: RID, min: float, max: float)`
- ⚠ deprecated method `accessibility_update_set_shortcut(id: RID, shortcut: String)`
- ⚠ deprecated method `accessibility_update_set_state_description(id: RID, description: String)`
- ⚠ deprecated method `accessibility_update_set_table_cell_position(id: RID, row_index: int, column_index: int)`
- ⚠ deprecated method `accessibility_update_set_table_cell_span(id: RID, row_span: int, column_span: int)`
- ⚠ deprecated method `accessibility_update_set_table_column_count(id: RID, count: int)`
- ⚠ deprecated method `accessibility_update_set_table_column_index(id: RID, index: int)`
- ⚠ deprecated method `accessibility_update_set_table_row_count(id: RID, count: int)`
- ⚠ deprecated method `accessibility_update_set_table_row_index(id: RID, index: int)`
- ⚠ deprecated method `accessibility_update_set_text_align(id: RID, align: int)`
- ⚠ deprecated method `accessibility_update_set_text_decorations(id: RID, underline: bool, strikethrough: bool, overline: bool)`
- ⚠ deprecated method `accessibility_update_set_text_orientation(id: RID, vertical: bool)`
- ⚠ deprecated method `accessibility_update_set_text_selection(id: RID, text_start_id: RID, start_char: int, text_end_id: RID, end_char: int)`
- ⚠ deprecated method `accessibility_update_set_tooltip(id: RID, tooltip: String)`
- ⚠ deprecated method `accessibility_update_set_transform(id: RID, transform: Transform2D)`
- ⚠ deprecated method `accessibility_update_set_url(id: RID, url: String)`
- ⚠ deprecated method `accessibility_update_set_value(id: RID, value: String)`
- ⚠ deprecated constant `AccessibilityAction.ACTION_BLUR`
- ⚠ deprecated constant `AccessibilityAction.ACTION_CLICK`
- ⚠ deprecated constant `AccessibilityAction.ACTION_COLLAPSE`
- ⚠ deprecated constant `AccessibilityAction.ACTION_CUSTOM`
- ⚠ deprecated constant `AccessibilityAction.ACTION_DECREMENT`
- ⚠ deprecated constant `AccessibilityAction.ACTION_EXPAND`
- ⚠ deprecated constant `AccessibilityAction.ACTION_FOCUS`
- ⚠ deprecated constant `AccessibilityAction.ACTION_HIDE_TOOLTIP`
- ⚠ deprecated constant `AccessibilityAction.ACTION_INCREMENT`
- ⚠ deprecated constant `AccessibilityAction.ACTION_REPLACE_SELECTED_TEXT`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_BACKWARD`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_DOWN`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_FORWARD`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_INTO_VIEW`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_LEFT`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_RIGHT`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_TO_POINT`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SCROLL_UP`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SET_SCROLL_OFFSET`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SET_TEXT_SELECTION`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SET_VALUE`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SHOW_CONTEXT_MENU`
- ⚠ deprecated constant `AccessibilityAction.ACTION_SHOW_TOOLTIP`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_BUSY`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_CLIPS_CHILDREN`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_DISABLED`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_HIDDEN`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_MODAL`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_MULTISELECTABLE`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_READONLY`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_REQUIRED`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_TOUCH_PASSTHROUGH`
- ⚠ deprecated constant `AccessibilityFlags.FLAG_VISITED`
- ⚠ deprecated constant `AccessibilityLiveMode.LIVE_ASSERTIVE`
- ⚠ deprecated constant `AccessibilityLiveMode.LIVE_OFF`
- ⚠ deprecated constant `AccessibilityLiveMode.LIVE_POLITE`
- ⚠ deprecated constant `AccessibilityPopupType.POPUP_DIALOG`
- ⚠ deprecated constant `AccessibilityPopupType.POPUP_LIST`
- ⚠ deprecated constant `AccessibilityPopupType.POPUP_MENU`
- ⚠ deprecated constant `AccessibilityPopupType.POPUP_TREE`
- ⚠ deprecated constant `AccessibilityRole.ROLE_AUDIO`
- ⚠ deprecated constant `AccessibilityRole.ROLE_BUTTON`
- ⚠ deprecated constant `AccessibilityRole.ROLE_CELL`
- ⚠ deprecated constant `AccessibilityRole.ROLE_CHECK_BOX`
- ⚠ deprecated constant `AccessibilityRole.ROLE_CHECK_BUTTON`
- ⚠ deprecated constant `AccessibilityRole.ROLE_COLOR_PICKER`
- ⚠ deprecated constant `AccessibilityRole.ROLE_COLUMN_HEADER`
- ⚠ deprecated constant `AccessibilityRole.ROLE_CONTAINER`
- ⚠ deprecated constant `AccessibilityRole.ROLE_DEFAULT_BUTTON`
- ⚠ deprecated constant `AccessibilityRole.ROLE_DIALOG`
- ⚠ deprecated constant `AccessibilityRole.ROLE_IMAGE`
- ⚠ deprecated constant `AccessibilityRole.ROLE_LINK`
- ⚠ deprecated constant `AccessibilityRole.ROLE_LIST`
- ⚠ deprecated constant `AccessibilityRole.ROLE_LIST_BOX`
- ⚠ deprecated constant `AccessibilityRole.ROLE_LIST_BOX_OPTION`
- ⚠ deprecated constant `AccessibilityRole.ROLE_LIST_ITEM`
- ⚠ deprecated constant `AccessibilityRole.ROLE_MENU`
- ⚠ deprecated constant `AccessibilityRole.ROLE_MENU_BAR`
- ⚠ deprecated constant `AccessibilityRole.ROLE_MENU_ITEM`
- ⚠ deprecated constant `AccessibilityRole.ROLE_MENU_ITEM_CHECK_BOX`
- ⚠ deprecated constant `AccessibilityRole.ROLE_MENU_ITEM_RADIO`
- ⚠ deprecated constant `AccessibilityRole.ROLE_MULTILINE_TEXT_FIELD`
- ⚠ deprecated constant `AccessibilityRole.ROLE_PANEL`
- ⚠ deprecated constant `AccessibilityRole.ROLE_PROGRESS_INDICATOR`
- ⚠ deprecated constant `AccessibilityRole.ROLE_RADIO_BUTTON`
- ⚠ deprecated constant `AccessibilityRole.ROLE_ROW`
- ⚠ deprecated constant `AccessibilityRole.ROLE_ROW_GROUP`
- ⚠ deprecated constant `AccessibilityRole.ROLE_ROW_HEADER`
- ⚠ deprecated constant `AccessibilityRole.ROLE_SCROLL_BAR`
- ⚠ deprecated constant `AccessibilityRole.ROLE_SCROLL_VIEW`
- ⚠ deprecated constant `AccessibilityRole.ROLE_SLIDER`
- ⚠ deprecated constant `AccessibilityRole.ROLE_SPIN_BUTTON`
- ⚠ deprecated constant `AccessibilityRole.ROLE_SPLITTER`
- ⚠ deprecated constant `AccessibilityRole.ROLE_STATIC_TEXT`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TAB`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TABLE`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TAB_BAR`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TAB_PANEL`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TEXT_FIELD`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TITLE_BAR`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TOOLTIP`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TREE`
- ⚠ deprecated constant `AccessibilityRole.ROLE_TREE_ITEM`
- ⚠ deprecated constant `AccessibilityRole.ROLE_UNKNOWN`
- ⚠ deprecated constant `AccessibilityRole.ROLE_VIDEO`
- ⚠ deprecated constant `AccessibilityRole.ROLE_WINDOW`
- ⚠ deprecated constant `AccessibilityScrollHint.SCROLL_HINT_BOTTOM_EDGE`
- ⚠ deprecated constant `AccessibilityScrollHint.SCROLL_HINT_BOTTOM_RIGHT`
- ⚠ deprecated constant `AccessibilityScrollHint.SCROLL_HINT_LEFT_EDGE`
- ⚠ deprecated constant `AccessibilityScrollHint.SCROLL_HINT_RIGHT_EDGE`
- ⚠ deprecated constant `AccessibilityScrollHint.SCROLL_HINT_TOP_EDGE`
- ⚠ deprecated constant `AccessibilityScrollHint.SCROLL_HINT_TOP_LEFT`
- ⚠ deprecated constant `AccessibilityScrollUnit.SCROLL_UNIT_ITEM`
- ⚠ deprecated constant `AccessibilityScrollUnit.SCROLL_UNIT_PAGE`

#### EditorCommandPalette
- − removed property `dialog_hide_on_ok: bool`

#### EditorContextMenuPlugin
- + constant `ContextMenuSlot.CONTEXT_SLOT_INSPECTOR_PROPERTY`

#### EditorDock
- + property `accessibility_region: bool` (property)
- + signal `opened()`
- + constant `DockSlot.DOCK_SLOT_BOTTOM_L`
- + constant `DockSlot.DOCK_SLOT_BOTTOM_R`

#### EditorExportPlatform
- ~ method `export_project(preset: EditorExportPreset, debug: bool, path: String, flags: int = 0) -> int` → `export_project(preset: EditorExportPreset, debug: bool, path: String, flags: int = 0, notify: bool = true) -> int`

#### EditorExportPlugin
- + method `_end_generate_apple_embedded_project(path: String, will_build_archive: bool)`

#### EditorFileSystem
- + method `is_importing() -> bool`

#### EditorInspector
- + method `collapse_all_folding()`
- + method `create_default_inspector(filter_line_edit: LineEdit = null) -> EditorInspector`
- + method `expand_all_folding()`
- + method `expand_revertable()`

#### EditorInterface
- + method `get_unsaved_scenes() -> PackedStringArray`

#### EditorNode3DGizmoPlugin
- + method `_can_commit_handle_on_click() -> bool`

#### EditorSceneFormatImporter
- + constant `ImportFlags.IMPORT_ANIMATION`
- + constant `ImportFlags.IMPORT_DISCARD_MESHES_AND_MATERIALS`
- + constant `ImportFlags.IMPORT_FAIL_ON_MISSING_DEPENDENCIES`
- + constant `ImportFlags.IMPORT_FORCE_DISABLE_MESH_COMPRESSION`
- + constant `ImportFlags.IMPORT_GENERATE_TANGENT_ARRAYS`
- + constant `ImportFlags.IMPORT_SCENE`
- + constant `ImportFlags.IMPORT_USE_NAMED_SKIN_BINDS`
- − removed constant `IMPORT_ANIMATION`
- − removed constant `IMPORT_DISCARD_MESHES_AND_MATERIALS`
- − removed constant `IMPORT_FAIL_ON_MISSING_DEPENDENCIES`
- − removed constant `IMPORT_FORCE_DISABLE_MESH_COMPRESSION`
- − removed constant `IMPORT_GENERATE_TANGENT_ARRAYS`
- − removed constant `IMPORT_SCENE`
- − removed constant `IMPORT_USE_NAMED_SKIN_BINDS`

#### EditorSettings
- + property `asset_store/available_urls: Dictionary` (property)
- + property `asset_store/use_threads: bool` (property)
- + property `docks/filesystem/ask_before_moving_files: bool` (property)
- + property `docks/filesystem/automatically_open_created_scripts: bool` (property)
- + property `editors/2d/locked_selection_rectangle_color: Color` (property)
- + property `editors/2d/selection_rectangle_color: Color` (property)
- + property `editors/3d/freelook/freelook_invert_y_axis: bool` (property)
- + property `editors/3d/view_plane_rotation_gizmo_scale: float` (property)
- + property `editors/3d_gizmos/gizmo_settings/show_collision_shapes_only_when_selected: bool` (property)
- + property `editors/audio_buses/active_max_db_color: Color` (property)
- + property `editors/audio_buses/active_min_db_color: Color` (property)
- + property `editors/audio_buses/active_normalized_db_color: Color` (property)
- + property `editors/audio_buses/inactive_max_db_color: Color` (property)
- + property `editors/audio_buses/inactive_min_db_color: Color` (property)
- + property `editors/audio_buses/inactive_normalized_db_color: Color` (property)
- + property `editors/audio_buses/tint_over_color: Color` (property)
- + property `editors/audio_buses/tint_under_color: Color` (property)
- + property `interface/accessibility/property_descriptions: bool` (property)
- + property `interface/editor/appearance/accept_dialog_cancel_ok_buttons: int` (property)
- + property `interface/editor/appearance/collapse_main_menu: bool` (property)
- + property `interface/editor/appearance/custom_display_scale: float` (property)
- + property `interface/editor/appearance/display_scale: int` (property)
- + property `interface/editor/appearance/editor_screen: int` (property)
- + property `interface/editor/appearance/expand_to_title: bool` (property)
- + property `interface/editor/appearance/project_manager_screen: int` (property)
- + property `interface/editor/appearance/show_renderer_selector: bool` (property)
- + property `interface/editor/appearance/show_update_spinner: int` (property)
- + property `interface/editor/appearance/use_embedded_menu: bool` (property)
- + property `interface/editor/appearance/use_native_file_dialogs: bool` (property)
- + property `interface/editor/behavior/automatically_open_screenshots: bool` (property)
- + property `interface/editor/behavior/import_resources_when_unfocused: bool` (property)
- + property `interface/editor/behavior/save_each_scene_on_quit: bool` (property)
- + property `interface/editor/behavior/save_on_focus_loss: bool` (property)
- + property `interface/editor/behavior/separate_distraction_mode: bool` (property)
- + property `interface/editor/behavior/show_internal_errors_in_toast_notifications: int` (property)
- + property `interface/editor/display/keep_screen_on: bool` (property)
- + property `interface/editor/display/single_window_mode: bool` (property)
- + property `interface/editor/display/update_continuously: bool` (property)
- + property `interface/editor/display/vsync_mode: int` (property)
- + property `interface/editor/docks/bottom_dock_tab_style: int` (property)
- + property `interface/editor/docks/dock_tab_style: int` (property)
- + property `interface/editor/fonts/code_font: String` (property)
- + property `interface/editor/fonts/code_font_contextual_ligatures: int` (property)
- + property `interface/editor/fonts/code_font_custom_opentype_features: String` (property)
- + property `interface/editor/fonts/code_font_custom_variations: String` (property)
- + property `interface/editor/fonts/code_font_size: int` (property)
- + property `interface/editor/fonts/font_allow_msdf: bool` (property)
- + property `interface/editor/fonts/font_antialiasing: int` (property)
- + property `interface/editor/fonts/font_disable_embedded_bitmaps: bool` (property)
- + property `interface/editor/fonts/font_hinting: int` (property)
- + property `interface/editor/fonts/font_subpixel_positioning: int` (property)
- + property `interface/editor/fonts/main_font: String` (property)
- + property `interface/editor/fonts/main_font_bold: String` (property)
- + property `interface/editor/fonts/main_font_custom_opentype_features: String` (property)
- + property `interface/editor/fonts/main_font_size: int` (property)
- + property `interface/editor/input/mouse_extra_buttons_navigate_history: bool` (property)
- + property `interface/editor/input/tablet_driver: int` (property)
- + property `interface/editor/localization/editor_language: String` (property)
- + property `interface/editor/localization/localize_settings: bool` (property)
- + property `interface/editor/localization/ui_layout_direction: int` (property)
- + property `interface/editor/timers/dragging_hover_wait_seconds: float` (property)
- + property `interface/editor/timers/low_processor_mode_sleep_usec: int` (property)
- + property `interface/editor/timers/unfocused_low_processor_mode_sleep_usec: int` (property)
- + property `interface/theme/use_monospace_font_for_editor_symbols: bool` (property)
- + property `interface/touchscreen/haptic_on_long_press: bool` (property)
- + property `network/language_server/enable_smart_resolve: bool` (property)
- + property `network/language_server/poll_limit_usec: int` (property)
- + property `network/language_server/remote_host: String` (property)
- + property `network/language_server/remote_port: int` (property)
- + property `network/language_server/show_native_symbols_in_editor: bool` (property)
- + property `network/language_server/use_thread: bool` (property)
- + property `text_editor/appearance/drag_and_drop_info/show_drag_and_drop_info: bool` (property)
- − removed property `asset_library/use_threads: bool`
- − removed property `interface/editor/accept_dialog_cancel_ok_buttons: int`
- − removed property `interface/editor/automatically_open_screenshots: bool`
- − removed property `interface/editor/bottom_dock_tab_style: int`
- − removed property `interface/editor/code_font: String`
- − removed property `interface/editor/code_font_contextual_ligatures: int`
- − removed property `interface/editor/code_font_custom_opentype_features: String`
- − removed property `interface/editor/code_font_custom_variations: String`
- − removed property `interface/editor/code_font_size: int`
- − removed property `interface/editor/collapse_main_menu: bool`
- − removed property `interface/editor/custom_display_scale: float`
- − removed property `interface/editor/display_scale: int`
- − removed property `interface/editor/dock_tab_style: int`
- − removed property `interface/editor/dragging_hover_wait_seconds: float`
- − removed property `interface/editor/editor_language: String`
- − removed property `interface/editor/editor_screen: int`
- − removed property `interface/editor/expand_to_title: bool`
- − removed property `interface/editor/font_allow_msdf: bool`
- − removed property `interface/editor/font_antialiasing: int`
- − removed property `interface/editor/font_disable_embedded_bitmaps: bool`
- − removed property `interface/editor/font_hinting: int`
- − removed property `interface/editor/font_subpixel_positioning: int`
- − removed property `interface/editor/import_resources_when_unfocused: bool`
- − removed property `interface/editor/keep_screen_on: bool`
- − removed property `interface/editor/localize_settings: bool`
- − removed property `interface/editor/low_processor_mode_sleep_usec: int`
- − removed property `interface/editor/main_font: String`
- − removed property `interface/editor/main_font_bold: String`
- − removed property `interface/editor/main_font_custom_opentype_features: String`
- − removed property `interface/editor/main_font_size: int`
- − removed property `interface/editor/mouse_extra_buttons_navigate_history: bool`
- − removed property `interface/editor/project_manager_screen: int`
- − removed property `interface/editor/save_each_scene_on_quit: bool`
- − removed property `interface/editor/save_on_focus_loss: bool`
- − removed property `interface/editor/separate_distraction_mode: bool`
- − removed property `interface/editor/show_internal_errors_in_toast_notifications: int`
- − removed property `interface/editor/show_update_spinner: int`
- − removed property `interface/editor/single_window_mode: bool`
- − removed property `interface/editor/tablet_driver: int`
- − removed property `interface/editor/ui_layout_direction: int`
- − removed property `interface/editor/unfocused_low_processor_mode_sleep_usec: int`
- − removed property `interface/editor/update_continuously: bool`
- − removed property `interface/editor/use_embedded_menu: bool`
- − removed property `interface/editor/use_native_file_dialogs: bool`
- − removed property `interface/editor/vsync_mode: int`
- − removed property `interface/editors/show_scene_tree_root_selection: bool`

#### EditorSpinSlider
- + property `deferred_drag_mode: bool` (property)

#### EditorTranslationParserPlugin
- + method `_customize_strings(strings: PackedStringArray[]) -> PackedStringArray[]`

#### EditorVCSInterface
- + method `_allow_amends() -> bool`
- ~ method `_commit(msg: String)` → `_commit(msg: String, amend: bool)`

#### FileDialog
- + property `option_{index}/default: int` (property)
- + property `option_{index}/name: String` (property)
- + property `option_{index}/values: PackedStringArray` (property)

#### Font
- + method `get_palette_colors(index: int) -> PackedColorArray`
- + method `get_palette_count() -> int`
- + method `get_palette_name(index: int) -> String`
- ~ method `find_variation(variation_coordinates: Dictionary, face_index: int = 0, strength: float = 0.0, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: int = 0, spacing_bottom: int = 0, spacing_space: int = 0, spacing_glyph: int = 0, baseline_offset: float = 0.0) -> RID` → `find_variation(variation_coordinates: Dictionary, face_index: int = 0, strength: float = 0.0, transform: Transform2D = Transform2D(1, 0, 0, 1, 0, 0), spacing_top: int = 0, spacing_bottom: int = 0, spacing_space: int = 0, spacing_glyph: int = 0, baseline_offset: float = 0.0, palette_index: int = 0, custom_colors: PackedColorArray = PackedColorArray()) -> RID`

#### FontVariation
- + property `palette_custom_colors: PackedColorArray` (property)
- + property `palette_index: int` (property)

#### GLTFDocument
- + property `texture_map_mode: int` (property)
- + constant `ImportFlags.IMPORT_FLAG_DISCARD_MESHES_AND_MATERIALS`
- + constant `ImportFlags.IMPORT_FLAG_FORCE_DISABLE_MESH_COMPRESSION`
- + constant `ImportFlags.IMPORT_FLAG_GENERATE_TANGENT_ARRAYS`
- + constant `ImportFlags.IMPORT_FLAG_USE_NAMED_SKIN_BINDS`
- + constant `TextureMapMode.TEXTURE_MAP_MODE_DO_NOT_REMAP`
- + constant `TextureMapMode.TEXTURE_MAP_MODE_REMAP_TO_STANDARD_MATERIAL`

#### GLTFDocumentExtension
- + method `_export_get_property_list(root_node: Node) -> Dictionary[]`

#### GPUParticles2D
- ~ method `request_particles_process(process_time: float)` → `request_particles_process(process_time: float, process_time_residual: float = 0)`

#### GPUParticles3D
- + property `transform_align_axis: int` (property)
- + property `transform_align_channel_filter: int` (property)
- + constant `TransformAlign.TRANSFORM_ALIGN_LOCAL_BILLBOARD`
- ~ method `request_particles_process(process_time: float)` → `request_particles_process(process_time: float, process_time_residual: float = 0.0)`

#### GradientTexture2D
- + constant `Fill.FILL_CONIC`

#### GridMap
- + method `get_octant_coords_from_cell_coords(cell_coords: Vector3i) -> Vector3i`
- + method `get_octants_in_bounds(bounds: AABB) -> Vector3i[]`
- + method `get_used_cells_in_octant(octant_coords: Vector3i) -> Vector3i[]`
- + method `get_used_cells_in_octant_by_item(octant_coords: Vector3i, item: int) -> Vector3i[]`
- + method `get_used_octants() -> Vector3i[]`
- + method `get_used_octants_by_item(item: int) -> Vector3i[]`
- + method `get_used_octants_in_bounds(bounds: AABB) -> Vector3i[]`
- + property `collision_visibility_mode: int` (property)
- + constant `DebugVisibilityMode.DEBUG_VISIBILITY_MODE_DEFAULT`
- + constant `DebugVisibilityMode.DEBUG_VISIBILITY_MODE_FORCE_HIDE`
- + constant `DebugVisibilityMode.DEBUG_VISIBILITY_MODE_FORCE_SHOW`

#### Image
- ~ method `save_exr(path: String, grayscale: bool = false) -> int` → `save_exr(path: String, grayscale: bool = false, color_image: bool = false, max_linear_value: float = -1.0) -> int`
- ~ method `save_exr_to_buffer(grayscale: bool = false) -> PackedByteArray` → `save_exr_to_buffer(grayscale: bool = false, color_image: bool = false, max_linear_value: float = -1.0) -> PackedByteArray`

#### ImageTexture
- − removed method `get_format() -> int`

#### ImporterMesh
- + method `merge_importer_meshes(importer_meshes: ImporterMesh[], relative_transforms: Transform3D[], deduplicate_surfaces: bool = true) -> ImporterMesh`

#### Input
- + method `clear_joy_motion_sensors_calibration(device: int)`
- + method `get_joy_accelerometer(device: int) -> Vector3`
- + method `get_joy_gravity(device: int) -> Vector3`
- + method `get_joy_gyroscope(device: int) -> Vector3`
- + method `get_joy_motion_sensors_calibration(device: int) -> Dictionary`
- + method `get_joy_motion_sensors_rate(device: int) -> float`
- + method `get_joy_vibration_remaining_duration(device: int) -> float`
- + method `has_joy_motion_sensors(device: int) -> bool`
- + method `has_joy_vibration(device: int) -> bool`
- + method `is_joy_motion_sensors_calibrated(device: int) -> bool`
- + method `is_joy_motion_sensors_calibrating(device: int) -> bool`
- + method `is_joy_motion_sensors_enabled(device: int) -> bool`
- + method `is_joy_vibrating(device: int) -> bool`
- + method `set_joy_motion_sensors_calibration(device: int, calibration_info: Dictionary)`
- + method `set_joy_motion_sensors_enabled(device: int, enable: bool)`
- + method `start_joy_motion_sensors_calibration(device: int)`
- + method `stop_joy_motion_sensors_calibration(device: int)`
- + property `ignore_joypad_on_unfocused_application: bool` (property)

#### InputEvent
- + constant `DEVICE_ID_KEYBOARD`
- + constant `DEVICE_ID_MOUSE`

#### InputEventGesture
- + property `device: int` (property)

#### InputEventMouse
- + property `device: int` (property)

#### InputEventWithModifiers
- + property `device: int` (property)

#### InputMap
- + signal `project_settings_loaded()`

#### ItemList
- + method `center_on_current(center_verically: bool = true, center_horizontally: bool = true)`
- + property `item_{index}/disabled: bool` (property)
- + property `item_{index}/icon: Texture2D` (property)
- + property `item_{index}/selectable: bool` (property)
- + property `item_{index}/text: String` (property)

#### JavaClassWrapper
- + method `create_proxy(object: Object, interfaces: PackedStringArray) -> JavaObject`
- + method `create_sam_callback(sam_interface: String, callable: Callable) -> JavaObject`

#### LabelSettings
- + property `stacked_outline_{index}/color: Color` (property)
- + property `stacked_outline_{index}/size: int` (property)
- + property `stacked_shadow_{index}/color: Color` (property)
- + property `stacked_shadow_{index}/offset: Vector2` (property)
- + property `stacked_shadow_{index}/outline_size: int` (property)

#### MainLoop
- + constant `NOTIFICATION_APPLICATION_PIP_MODE_ENTERED`
- + constant `NOTIFICATION_APPLICATION_PIP_MODE_EXITED`

#### MenuButton
- + property `popup/item_{index}/checkable: int` (property)
- + property `popup/item_{index}/checked: bool` (property)
- + property `popup/item_{index}/disabled: bool` (property)
- + property `popup/item_{index}/icon: Texture2D` (property)
- + property `popup/item_{index}/id: int` (property)
- + property `popup/item_{index}/separator: bool` (property)
- + property `popup/item_{index}/text: String` (property)

#### MeshLibrary
- + method `get_item_count() -> int`

#### MovieWriter
- + method `_get_supported_extensions() -> PackedStringArray`

#### MultiplayerPeerExtension
- ~ method `_disconnect_peer(p_peer: int, p_force: bool)` → `_disconnect_peer(peer: int, force: bool)`
- ~ method `_put_packet(p_buffer: const uint8_t*, p_buffer_size: int) -> int` → `_put_packet(buffer: const uint8_t*, buffer_size: int) -> int`
- ~ method `_put_packet_script(p_buffer: PackedByteArray) -> int` → `_put_packet_script(buffer: PackedByteArray) -> int`
- ~ method `_set_refuse_new_connections(p_enable: bool)` → `_set_refuse_new_connections(enable: bool)`
- ~ method `_set_target_peer(p_peer: int)` → `_set_target_peer(peer: int)`
- ~ method `_set_transfer_channel(p_channel: int)` → `_set_transfer_channel(channel: int)`
- ~ method `_set_transfer_mode(p_mode: int)` → `_set_transfer_mode(mode: int)`

#### NativeMenu
- + method `set_item_index(rid: RID, idx: int, target_idx: int) -> int`

#### Node
- + constant `NOTIFICATION_APPLICATION_PIP_MODE_ENTERED`
- + constant `NOTIFICATION_APPLICATION_PIP_MODE_EXITED`
- + constant `NOTIFICATION_WM_OUTPUT_MAX_LINEAR_VALUE_CHANGED`

#### Object
- ~ method `is_class(class: String) -> bool` → `is_class(class: StringName) -> bool`

#### OpenXRAPIExtension
- + method `get_view_configuration() -> int`
- + method `get_view_count() -> int`
- + method `register_projection_layer_extension(extension: OpenXRExtensionWrapper)`
- + method `unregister_projection_layer_extension(extension: OpenXRExtensionWrapper)`

#### OpenXRBindingModifierEditor
- − removed property `size_flags_horizontal: int`

#### OpenXRCompositionLayer
- + property `eye_visibility: int` (property)
- + constant `EyeVisibility.EYE_VISIBILITY_BOTH`
- + constant `EyeVisibility.EYE_VISIBILITY_LEFT`
- + constant `EyeVisibility.EYE_VISIBILITY_RIGHT`

#### OpenXRExtensionWrapper
- + method `_set_projection_layer_and_get_next_pointer(next_pointer: void*) -> int`
- ~ method `_on_register_metadata()` → `_on_register_metadata(interaction_profile_metadata: OpenXRInteractionProfileMetadata)`

#### OpenXRInteractionProfileEditorBase
- − removed property `size_flags_horizontal: int`
- − removed property `size_flags_vertical: int`

#### OpenXRInterface
- + method `is_user_presence_supported() -> bool`
- + method `is_user_present() -> bool`
- + property `foveation_with_subsampled_images: bool` (property)
- + signal `user_presence_changed(is_user_present: bool)`

#### OpenXRSpatialAnchorCapability
- + method `create_default_persistence_context(user_callback: Callable = Callable()) -> OpenXRFutureResult`
- + method `do_entity_update(spatial_context: RID, component_data: OpenXRSpatialComponentData[], next_snapshot_create: OpenXRStructureBase = null, next_snapshot_query: OpenXRStructureBase = null)`
- + method `start_entity_discovery(spatial_context: RID, component_data: OpenXRSpatialComponentData[], next_snapshot_create: OpenXRStructureBase = null, next_snapshot_query: OpenXRStructureBase = null, user_callback: Callable = Callable()) -> OpenXRFutureResult`
- ~ method `create_new_anchor(transform: Transform3D, spatial_context: RID = RID()) -> OpenXRAnchorTracker` → `create_new_anchor(transform: Transform3D, spatial_context: RID = RID(), next: OpenXRStructureBase = null) -> OpenXRAnchorTracker`

#### OpenXRSpatialCapabilityConfigurationBaseHeader
- + method `get_configuration() -> int`

#### OpenXRSpatialComponentData
- + method `get_component_type() -> int`

#### OpenXRSpatialContextPersistenceConfig
- + method `get_persistence_contexts() -> Array`

#### OpenXRSpatialEntityExtension
- + method `discover_spatial_entities_with_component_data(spatial_context: RID, component_data: OpenXRSpatialComponentData[], next: OpenXRStructureBase = null, user_callback: Callable = Callable()) -> OpenXRFutureResult`

#### OpenXRSpatialEntityTracker
- + method `add_next(next: OpenXRStructureBase)`
- + method `get_next() -> OpenXRStructureBase`
- + method `get_spatial_context() -> RID`
- + method `remove_next(next: OpenXRStructureBase)`
- + method `set_spatial_context(spatial_context: RID)`
- + signal `next_changed()`

#### OpenXRSpatialMarkerTrackingCapability
- + method `do_entity_update(spatial_context: RID, component_data: OpenXRSpatialComponentData[], next_snapshot_create: OpenXRStructureBase = null, next_snapshot_query: OpenXRStructureBase = null)`
- + method `start_entity_discovery(spatial_context: RID, component_data: OpenXRSpatialComponentData[], next_snapshot_create: OpenXRStructureBase = null, next_snapshot_query: OpenXRStructureBase = null, user_callback: Callable = Callable()) -> OpenXRFutureResult`

#### OpenXRSpatialPlaneTrackingCapability
- + method `start_entity_discovery(spatial_context: RID, component_data: OpenXRSpatialComponentData[], next_snapshot_create: OpenXRStructureBase = null, next_snapshot_query: OpenXRStructureBase = null, user_callback: Callable = Callable()) -> OpenXRFutureResult`

#### OptimizedTranslation
- ~ method `generate(from: Translation)` → `generate(from: Translation) -> bool`

#### OptionButton
- + property `popup/item_{index}/disabled: bool` (property)
- + property `popup/item_{index}/icon: Texture2D` (property)
- + property `popup/item_{index}/id: int` (property)
- + property `popup/item_{index}/separator: bool` (property)
- + property `popup/item_{index}/text: String` (property)
- + property `search_bar_enabled: bool` (property)
- + property `search_bar_fuzzy_search_enabled: bool` (property)
- + property `search_bar_fuzzy_search_max_misses: int` (property)
- + property `search_bar_min_item_count: int` (property)

#### PCKPacker
- + method `add_file_from_buffer(target_path: String, data: PackedByteArray, encrypt: bool = false) -> int`

#### PacketPeerExtension
- ~ method `_put_packet(p_buffer: const uint8_t*, p_buffer_size: int) -> int` → `_put_packet(buffer: const uint8_t*, buffer_size: int) -> int`

#### ParticleProcessMaterial
- + property `particle_flag_inherit_emitter_scale: bool` (property)
- + property `rotation_3d_max: Vector3` (property)
- + property `rotation_3d_min: Vector3` (property)
- + property `rotation_velocity_3d_curve: Texture2D` (property)
- + property `rotation_velocity_3d_max: Vector3` (property)
- + property `rotation_velocity_3d_min: Vector3` (property)
- + property `scale_3d_max: Vector3` (property)
- + property `scale_3d_min: Vector3` (property)
- + property `use_rotation_3d: bool` (property)
- + property `use_rotation_velocity_3d: bool` (property)
- + property `use_scale_3d: bool` (property)
- + constant `ParticleFlags.PARTICLE_FLAG_INHERIT_EMITTER_SCALE`

#### PhysicsDirectSpaceState2DExtension
- ~ method `_cast_motion(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, closest_safe: float*, closest_unsafe: float*) -> bool` → `_cast_motion(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_closest_safe: float*, r_closest_unsafe: float*) -> bool`
- ~ method `_collide_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: void*, max_results: int, result_count: int32_t*) -> bool` → `_collide_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_results: void*, max_results: int, r_result_count: int32_t*) -> bool`
- ~ method `_intersect_point(position: Vector2, canvas_instance_id: int, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: PhysicsServer2DExtensionShapeResult*, max_results: int) -> int` → `_intersect_point(position: Vector2, canvas_instance_id: int, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_results: PhysicsServer2DExtensionShapeResult*, max_results: int) -> int`
- ~ method `_intersect_ray(from: Vector2, to: Vector2, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, result: PhysicsServer2DExtensionRayResult*) -> bool` → `_intersect_ray(from: Vector2, to: Vector2, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, r_result: PhysicsServer2DExtensionRayResult*) -> bool`
- ~ method `_intersect_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, result: PhysicsServer2DExtensionShapeResult*, max_results: int) -> int` → `_intersect_shape(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_result: PhysicsServer2DExtensionShapeResult*, max_results: int) -> int`
- ~ method `_rest_info(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, rest_info: PhysicsServer2DExtensionShapeRestInfo*) -> bool` → `_rest_info(shape_rid: RID, transform: Transform2D, motion: Vector2, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_rest_info: PhysicsServer2DExtensionShapeRestInfo*) -> bool`

#### PhysicsDirectSpaceState3DExtension
- ~ method `_cast_motion(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, closest_safe: float*, closest_unsafe: float*, info: PhysicsServer3DExtensionShapeRestInfo*) -> bool` → `_cast_motion(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_closest_safe: float*, r_closest_unsafe: float*, r_info: PhysicsServer3DExtensionShapeRestInfo*) -> bool`
- ~ method `_collide_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: void*, max_results: int, result_count: int32_t*) -> bool` → `_collide_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_results: void*, max_results: int, r_result_count: int32_t*) -> bool`
- ~ method `_intersect_point(position: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, results: PhysicsServer3DExtensionShapeResult*, max_results: int) -> int` → `_intersect_point(position: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_results: PhysicsServer3DExtensionShapeResult*, max_results: int) -> int`
- ~ method `_intersect_ray(from: Vector3, to: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, hit_back_faces: bool, pick_ray: bool, result: PhysicsServer3DExtensionRayResult*) -> bool` → `_intersect_ray(from: Vector3, to: Vector3, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, hit_from_inside: bool, hit_back_faces: bool, pick_ray: bool, r_result: PhysicsServer3DExtensionRayResult*) -> bool`
- ~ method `_intersect_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, result_count: PhysicsServer3DExtensionShapeResult*, max_results: int) -> int` → `_intersect_shape(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_result_count: PhysicsServer3DExtensionShapeResult*, max_results: int) -> int`
- ~ method `_rest_info(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, rest_info: PhysicsServer3DExtensionShapeRestInfo*) -> bool` → `_rest_info(shape_rid: RID, transform: Transform3D, motion: Vector3, margin: float, collision_mask: int, collide_with_bodies: bool, collide_with_areas: bool, r_rest_info: PhysicsServer3DExtensionShapeRestInfo*) -> bool`

#### PhysicsServer2D
- ~ method `body_set_shape_as_one_way_collision(body: RID, shape_idx: int, enable: bool, margin: float)` → `body_set_shape_as_one_way_collision(body: RID, shape_idx: int, enable: bool, margin: float, direction: Vector2 = Vector2(0, 1))`

#### PhysicsServer2DExtension
- ~ method `_body_collide_shape(body: RID, body_shape: int, shape: RID, shape_xform: Transform2D, motion: Vector2, results: void*, result_max: int, result_count: int32_t*) -> bool` → `_body_collide_shape(body: RID, body_shape: int, shape: RID, shape_xform: Transform2D, motion: Vector2, r_results: void*, result_max: int, r_result_count: int32_t*) -> bool`
- ~ method `_body_set_shape_as_one_way_collision(body: RID, shape_idx: int, enable: bool, margin: float)` → `_body_set_shape_as_one_way_collision(body: RID, shape_idx: int, enable: bool, margin: float, direction: Vector2)`
- ~ method `_body_test_motion(body: RID, from: Transform2D, motion: Vector2, margin: float, collide_separation_ray: bool, recovery_as_collision: bool, result: PhysicsServer2DExtensionMotionResult*) -> bool` → `_body_test_motion(body: RID, from: Transform2D, motion: Vector2, margin: float, collide_separation_ray: bool, recovery_as_collision: bool, r_result: PhysicsServer2DExtensionMotionResult*) -> bool`
- ~ method `_shape_collide(shape_A: RID, xform_A: Transform2D, motion_A: Vector2, shape_B: RID, xform_B: Transform2D, motion_B: Vector2, results: void*, result_max: int, result_count: int32_t*) -> bool` → `_shape_collide(shape_A: RID, xform_A: Transform2D, motion_A: Vector2, shape_B: RID, xform_B: Transform2D, motion_B: Vector2, r_results: void*, result_max: int, r_result_count: int32_t*) -> bool`

#### PhysicsServer3DExtension
- ~ method `_body_test_motion(body: RID, from: Transform3D, motion: Vector3, margin: float, max_collisions: int, collide_separation_ray: bool, recovery_as_collision: bool, result: PhysicsServer3DExtensionMotionResult*) -> bool` → `_body_test_motion(body: RID, from: Transform3D, motion: Vector3, margin: float, max_collisions: int, collide_separation_ray: bool, recovery_as_collision: bool, r_result: PhysicsServer3DExtensionMotionResult*) -> bool`

#### PopupMenu
- + method `set_item_index(index: int, target_index: int)`
- + property `canvas_item_default_texture_filter: int` (property)
- + property `canvas_item_default_texture_repeat: int` (property)
- + property `item_{index}/checkable: int` (property)
- + property `item_{index}/checked: bool` (property)
- + property `item_{index}/disabled: bool` (property)
- + property `item_{index}/icon: Texture2D` (property)
- + property `item_{index}/id: int` (property)
- + property `item_{index}/separator: bool` (property)
- + property `item_{index}/text: String` (property)
- + property `search_bar_enabled: bool` (property)
- + property `search_bar_fuzzy_search_enabled: bool` (property)
- + property `search_bar_fuzzy_search_max_misses: int` (property)
- + property `search_bar_min_item_count: int` (property)

#### PopupPanel
- + property `canvas_item_default_texture_filter: int` (property)
- + property `canvas_item_default_texture_repeat: int` (property)

#### PortableCompressedTexture2D
- − removed method `get_format() -> int`

#### ProjectSettings
- + property `accessibility/general/accessibility_driver: String` (property)
- + property `animation/warnings/check_invalid_skeleton_modifier_node_paths: bool` (property)
- + property `debug/gdscript/warnings/confusable_temporary_modification: int` (property)
- + property `display/window/hdr/request_hdr_output: bool` (property)
- + property `input_devices/joypads/ignore_joypad_on_unfocused_application: bool` (property)
- + property `rendering/environment/fog/use_legacy_blending: bool` (property)
- + property `xr/openxr/extensions/user_presence: bool` (property)
- + property `xr/openxr/foveation_eye_tracked: bool` (property)
- + property `xr/openxr/foveation_with_subsampled_images: bool` (property)

#### RDShaderSPIRV
- + property `bytecode_any_hit: PackedByteArray` (property)
- + property `bytecode_closest_hit: PackedByteArray` (property)
- + property `bytecode_intersection: PackedByteArray` (property)
- + property `bytecode_miss: PackedByteArray` (property)
- + property `bytecode_raygen: PackedByteArray` (property)
- + property `compile_error_any_hit: String` (property)
- + property `compile_error_closest_hit: String` (property)
- + property `compile_error_intersection: String` (property)
- + property `compile_error_miss: String` (property)
- + property `compile_error_raygen: String` (property)

#### RDShaderSource
- + property `source_any_hit: String` (property)
- + property `source_closest_hit: String` (property)
- + property `source_intersection: String` (property)
- + property `source_miss: String` (property)
- + property `source_raygen: String` (property)

#### RenderingDevice
- + method `blas_build(blas: RID) -> int`
- + method `blas_create(geometries: RDAccelerationStructureGeometry[], flags: int) -> RID`
- + method `hit_sbt_create(raytracing_pipeline: RID, initial_hit_group_capacity: int) -> RID`
- + method `hit_sbt_range_alloc(hit_sbt: RID, hit_group_count: int) -> int`
- + method `hit_sbt_range_free(hit_sbt: RID, range: int) -> int`
- + method `hit_sbt_range_update(hit_sbt: RID, range: int, offset: int, hit_group_indices: PackedInt32Array) -> int`
- + method `hit_sbt_set_pipeline(hit_sbt: RID, raytracing_pipeline: RID) -> int`
- + method `raytracing_list_begin() -> int`
- + method `raytracing_list_bind_raytracing_pipeline(raytracing_list: int, raytracing_pipeline: RID)`
- + method `raytracing_list_bind_uniform_set(raytracing_list: int, uniform_set: RID, set_index: int)`
- + method `raytracing_list_end()`
- + method `raytracing_list_set_push_constant(raytracing_list: int, buffer: PackedByteArray, size_bytes: int)`
- + method `raytracing_list_trace_rays(raytracing_list: int, raygen_shader_index: int, hit_sbt: RID, width: int, height: int, depth: int)`
- + method `raytracing_pipeline_create(raygen_shaders: RDPipelineShader[], miss_shaders: RDPipelineShader[], hit_groups: RDHitGroup[], max_trace_recursion_depth: int) -> RID`
- + method `raytracing_pipeline_is_valid(raytracing_pipeline: RID) -> bool`
- + method `tlas_build(tlas: RID, instances: RDAccelerationStructureInstance[]) -> int`
- + method `tlas_create(max_instance_count: int, flags: int) -> RID`
- + constant `AccelerationStructureFlagBits.ACCELERATION_STRUCTURE_ALLOW_COMPACTION_BIT`
- + constant `AccelerationStructureFlagBits.ACCELERATION_STRUCTURE_ALLOW_UPDATE_BIT`
- + constant `AccelerationStructureFlagBits.ACCELERATION_STRUCTURE_LOW_MEMORY_BIT`
- + constant `AccelerationStructureFlagBits.ACCELERATION_STRUCTURE_PREFER_FAST_BUILD_BIT`
- + constant `AccelerationStructureFlagBits.ACCELERATION_STRUCTURE_PREFER_FAST_TRACE_BIT`
- + constant `AccelerationStructureGeometryFlagBits.ACCELERATION_STRUCTURE_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT`
- + constant `AccelerationStructureGeometryFlagBits.ACCELERATION_STRUCTURE_GEOMETRY_OPAQUE_BIT`
- + constant `AccelerationStructureInstanceFlagBits.ACCELERATION_STRUCTURE_INSTANCE_FORCE_NO_OPAQUE_BIT`
- + constant `AccelerationStructureInstanceFlagBits.ACCELERATION_STRUCTURE_INSTANCE_FORCE_OPAQUE_BIT`
- + constant `AccelerationStructureInstanceFlagBits.ACCELERATION_STRUCTURE_INSTANCE_TRIANGLE_FACING_CULL_DISABLE_BIT`
- + constant `AccelerationStructureInstanceFlagBits.ACCELERATION_STRUCTURE_INSTANCE_TRIANGLE_FLIP_FACING_BIT`
- + constant `BufferCreationBits.BUFFER_CREATION_ACCELERATION_STRUCTURE_BUILD_INPUT_READ_ONLY_BIT`
- + constant `Features.SUPPORTS_HDR_OUTPUT`
- + constant `Features.SUPPORTS_RAYTRACING_PIPELINE`
- + constant `Features.SUPPORTS_RAY_QUERY`
- + constant `ShaderStage.SHADER_STAGE_ANY_HIT`
- + constant `ShaderStage.SHADER_STAGE_ANY_HIT_BIT`
- + constant `ShaderStage.SHADER_STAGE_CLOSEST_HIT`
- + constant `ShaderStage.SHADER_STAGE_CLOSEST_HIT_BIT`
- + constant `ShaderStage.SHADER_STAGE_INTERSECTION`
- + constant `ShaderStage.SHADER_STAGE_INTERSECTION_BIT`
- + constant `ShaderStage.SHADER_STAGE_MISS`
- + constant `ShaderStage.SHADER_STAGE_MISS_BIT`
- + constant `ShaderStage.SHADER_STAGE_RAYGEN`
- + constant `ShaderStage.SHADER_STAGE_RAYGEN_BIT`
- + constant `UniformType.UNIFORM_TYPE_ACCELERATION_STRUCTURE`

#### RenderingServer
- + method `area_light_create() -> RID`
- + method `light_area_set_normalize_energy(light: RID, enable: bool)`
- + method `light_area_set_size(light: RID, size: Vector2)`
- + method `particles_set_transform_align_axis(particles: RID, rotation_axis: int)`
- + method `particles_set_transform_align_channel_filter(particles: RID, channel_filter: int)`
- + method `texture_drawable_blit_rect(textures: RID[], rect: Rect2i, material: RID, modulate: Color, source_textures: RID[], to_mipmap: int = 0)`
- + method `texture_drawable_create(width: int, height: int, format: int, color: Color = Color(1, 1, 1, 1), with_mipmaps: bool = false) -> RID`
- + method `texture_drawable_generate_mipmaps(texture: RID)`
- + method `texture_drawable_get_default_material() -> RID`
- + constant `LightType.LIGHT_AREA`
- + constant `ParticlesTransformAlign.PARTICLES_TRANSFORM_ALIGN_LOCAL_BILLBOARD`
- + constant `ParticlesTransformAlignAxis.PARTICLES_ALIGN_AXIS_X`
- + constant `ParticlesTransformAlignAxis.PARTICLES_ALIGN_AXIS_Y`
- + constant `ParticlesTransformAlignCustomSrc.PARTICLES_ALIGN_CHANNEL_FILTER_DISABLED`
- + constant `ParticlesTransformAlignCustomSrc.PARTICLES_ALIGN_CHANNEL_FILTER_W`
- + constant `ParticlesTransformAlignCustomSrc.PARTICLES_ALIGN_CHANNEL_FILTER_X`
- + constant `ParticlesTransformAlignCustomSrc.PARTICLES_ALIGN_CHANNEL_FILTER_Y`
- + constant `ParticlesTransformAlignCustomSrc.PARTICLES_ALIGN_CHANNEL_FILTER_Z`
- + constant `ShaderMode.SHADER_TEXTURE_BLIT`
- + constant `TextureDrawableFormat.TEXTURE_DRAWABLE_FORMAT_RGBA8`
- + constant `TextureDrawableFormat.TEXTURE_DRAWABLE_FORMAT_RGBA8_SRGB`
- + constant `TextureDrawableFormat.TEXTURE_DRAWABLE_FORMAT_RGBAF`
- + constant `TextureDrawableFormat.TEXTURE_DRAWABLE_FORMAT_RGBAH`
- + constant `ViewportScaling3DMode.VIEWPORT_SCALING_3D_MODE_NEAREST`
- ~ method `environment_set_volumetric_fog(env: RID, enable: bool, density: float, albedo: Color, emission: Color, emission_energy: float, anisotropy: float, length: float, p_detail_spread: float, gi_inject: float, temporal_reprojection: bool, temporal_reprojection_amount: float, ambient_inject: float, sky_affect: float)` → `environment_set_volumetric_fog(env: RID, enable: bool, density: float, albedo: Color, emission: Color, emission_energy: float, anisotropy: float, length: float, detail_spread: float, gi_inject: float, temporal_reprojection: bool, temporal_reprojection_amount: float, ambient_inject: float, sky_affect: float)`
- ~ method `particles_request_process_time(particles: RID, time: float)` → `particles_request_process_time(particles: RID, process_time: float, process_time_residual: float = 0.0)`
- ~ method `viewport_set_size(viewport: RID, width: int, height: int)` → `viewport_set_size(viewport: RID, width: int, height: int, view_count: int = 1)`

#### Resource
- + method `copy_from_resource(resource: Resource) -> int`

#### ResourceImporterSVG
- + property `fix_alpha_border: bool` (property)
- + property `premult_alpha: bool` (property)

#### ResourceImporterScene
- + property `array_mesh/deduplicate_surfaces: bool` (property)
- + property `mesh_library/use_node_names_as_mesh_names: bool` (property)

#### RichTextLabel
- + constant `ImageUnit.IMAGE_UNIT_EM`
- + constant `ImageUnit.IMAGE_UNIT_PERCENT`
- + constant `ImageUnit.IMAGE_UNIT_PIXEL`
- + constant `ImageUpdateMask.UPDATE_WIDTH_UNIT`
- ~ method `add_image(image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), key: Variant = null, pad: bool = false, tooltip: String = "", width_in_percent: bool = false, height_in_percent: bool = false, alt_text: String = "")` → `add_image(image: Texture2D, width: float = 0, height: float = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), key: Variant = null, pad: bool = false, tooltip: String = "", width_unit: int = 0, height_unit: int = 0, alt_text: String = "")`
- ~ method `update_image(key: Variant, mask: int, image: Texture2D, width: int = 0, height: int = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), pad: bool = false, tooltip: String = "", width_in_percent: bool = false, height_in_percent: bool = false)` → `update_image(key: Variant, mask: int, image: Texture2D, width: float = 0, height: float = 0, color: Color = Color(1, 1, 1, 1), inline_align: int = 5, region: Rect2 = Rect2(0, 0, 0, 0), pad: bool = false, tooltip: String = "", width_unit: int = 0, height_unit: int = 0)`
- − removed constant `ImageUpdateMask.UPDATE_WIDTH_IN_PERCENT`

#### Script
- + method `has_script_method(method_name: StringName) -> bool`
- ⚠ deprecated method `instance_has(base_object: Object) -> bool`

#### ScriptEditor
- + method `close_file(path: String) -> int`
- + method `get_unsaved_files() -> PackedStringArray`
- + method `reload_open_files()`
- + method `save_all_scripts()`

#### ScriptExtension
- ⚠ deprecated method `_instance_has(object: Object) -> bool`

#### ScriptLanguageExtension
- + constant `CodeCompletionKind.CODE_COMPLETION_KIND_KEYWORD`
- ⚠ deprecated method `_create_script() -> Object`

#### ScrollContainer
- + property `propagate_maximum_size: bool` (property)
- + property `scroll_horizontal_by_default: bool` (property)
- + constant `ScrollMode.SCROLL_MODE_MAXIMIZE_FIRST`

#### Shader
- + constant `Mode.MODE_TEXTURE_BLIT`

#### SkeletonModification2DJiggle
- + method `reset()`

#### SplitContainer
- + property `drag_nested_intersections: bool` (property)

#### SpriteFrames
- + method `get_animation_loop_mode(anim: StringName) -> int`
- + method `set_animation_loop_mode(anim: StringName, loop_mode: int)`
- + constant `LoopMode.LOOP_LINEAR`
- + constant `LoopMode.LOOP_NONE`
- + constant `LoopMode.LOOP_PINGPONG`
- ⚠ deprecated method `get_animation_loop(anim: StringName) -> bool`
- ⚠ deprecated method `set_animation_loop(anim: StringName, loop: bool)`

#### StreamPeerExtension
- ~ method `_put_data(p_data: const uint8_t*, p_bytes: int, r_sent: int32_t*) -> int` → `_put_data(data: const uint8_t*, bytes: int, r_sent: int32_t*) -> int`
- ~ method `_put_partial_data(p_data: const uint8_t*, p_bytes: int, r_sent: int32_t*) -> int` → `_put_partial_data(data: const uint8_t*, bytes: int, r_sent: int32_t*) -> int`

#### SubViewport
- + property `view_count: int` (property)

#### TabBar
- + property `tab_{index}/disabled: bool` (property)
- + property `tab_{index}/icon: Texture2D` (property)
- + property `tab_{index}/title: String` (property)
- + property `tab_{index}/tooltip: String` (property)

#### TabContainer
- + property `tab_{index}/disabled: bool` (property)
- + property `tab_{index}/hidden: bool` (property)
- + property `tab_{index}/icon: Texture2D` (property)
- + property `tab_{index}/title: String` (property)
- ⚠ deprecated property `all_tabs_in_front: bool`

#### TextEdit
- + method `is_line_in_viewport(line: int) -> bool`

#### TextServer
- + method `font_get_palette_colors(font_rid: RID, index: int) -> PackedColorArray`
- + method `font_get_palette_count(font_rid: RID) -> int`
- + method `font_get_palette_custom_colors(font_rid: RID) -> PackedColorArray`
- + method `font_get_palette_name(font_rid: RID, index: int) -> String`
- + method `font_get_used_palette(font_rid: RID) -> int`
- + method `font_set_palette_custom_colors(font_rid: RID, colors: PackedColorArray)`
- + method `font_set_used_palette(font_rid: RID, index: int)`
- + method `shaped_get_run_glyph_range(shaped: RID, index: int) -> Vector2i`
- ~ method `font_set_modulate_color_glyphs(font_rid: RID, force_autohinter: bool)` → `font_set_modulate_color_glyphs(font_rid: RID, modulate: bool)`

#### TextServerExtension
- + method `_font_get_palette_colors(font_rid: RID, index: int) -> PackedColorArray`
- + method `_font_get_palette_count(font_rid: RID) -> int`
- + method `_font_get_palette_custom_colors(font_rid: RID) -> PackedColorArray`
- + method `_font_get_palette_name(font_rid: RID, index: int) -> String`
- + method `_font_get_used_palette(font_rid: RID) -> int`
- + method `_font_set_palette_custom_colors(font_rid: RID, colors: PackedColorArray)`
- + method `_font_set_used_palette(font_rid: RID, index: int)`
- + method `_shaped_get_run_glyph_range(shaped: RID, index: int) -> Vector2i`
- ~ method `_shaped_text_get_carets(shaped: RID, position: int, caret: CaretInfo*)` → `_shaped_text_get_carets(shaped: RID, position: int, r_caret: CaretInfo*)`

#### Texture2D
- + method `_get_format() -> int`
- + method `_get_image() -> Image`
- + method `_get_mipmap_count() -> int`
- + method `_has_mipmaps() -> bool`
- + method `get_format() -> int`
- + method `get_mipmap_count() -> int`
- + method `has_mipmaps() -> bool`

#### TileSet
- + method `clear_terrains(terrain_set: int)`
- ~ method `set_coords_level_tile_proxy(p_source_from: int, coords_from: Vector2i, source_to: int, coords_to: Vector2i)` → `set_coords_level_tile_proxy(source_from: int, coords_from: Vector2i, source_to: int, coords_to: Vector2i)`

#### Tree
- + method `get_custom_drawing_canvas_item() -> RID`

#### TreeItem
- + method `get_autowrap_trim_flags(column: int) -> int`
- + method `is_accepting_children() -> bool`
- + method `set_accept_children(allowed: bool)`
- + method `set_autowrap_trim_flags(column: int, flags: int)`
- ~ method `select(column: int)` → `select(column: int, set_as_cursor: bool = true)`

#### Tween
- + method `has_tweeners() -> bool`
- + method `tween_await(signal: Signal) -> AwaitTweener`

#### Viewport
- + constant `DebugDraw.DEBUG_DRAW_AREA_LIGHT_ATLAS`
- + constant `DebugDraw.DEBUG_DRAW_CLUSTER_AREA_LIGHTS`
- + constant `DefaultCanvasItemTextureFilter.DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_PARENT_NODE`
- + constant `DefaultCanvasItemTextureRepeat.DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_PARENT_NODE`
- + constant `Scaling3DMode.SCALING_3D_MODE_NEAREST`

#### VisualShader
- + constant `Type.TYPE_TEXTURE_BLIT`

#### WebRTCDataChannelExtension
- ~ method `_put_packet(p_buffer: const uint8_t*, p_buffer_size: int) -> int` → `_put_packet(buffer: const uint8_t*, buffer_size: int) -> int`
- ~ method `_set_write_mode(p_write_mode: int)` → `_set_write_mode(write_mode: int)`

#### WebRTCPeerConnectionExtension
- ~ method `_add_ice_candidate(p_sdp_mid_name: String, p_sdp_mline_index: int, p_sdp_name: String) -> int` → `_add_ice_candidate(sdp_mid_name: String, sdp_mline_index: int, sdp_name: String) -> int`
- ~ method `_create_data_channel(p_label: String, p_config: Dictionary) -> WebRTCDataChannel` → `_create_data_channel(label: String, config: Dictionary) -> WebRTCDataChannel`
- ~ method `_initialize(p_config: Dictionary) -> int` → `_initialize(config: Dictionary) -> int`
- ~ method `_set_local_description(p_type: String, p_sdp: String) -> int` → `_set_local_description(type: String, sdp: String) -> int`
- ~ method `_set_remote_description(p_type: String, p_sdp: String) -> int` → `_set_remote_description(type: String, sdp: String) -> int`

#### Window
- + method `get_output_max_linear_value() -> float`
- + method `set_taskbar_progress_state(state: int)`
- + method `set_taskbar_progress_value(value: float)`
- + property `hdr_output_requested: bool` (property)
- + signal `output_max_linear_value_changed(output_max_linear_value: float)`

#### XRController3D
- ~ signal `button_pressed(name: String)` → `button_pressed(action_name: String)`
- ~ signal `button_released(name: String)` → `button_released(action_name: String)`
- ~ signal `input_float_changed(name: String, value: float)` → `input_float_changed(action_name: String, value: float)`
- ~ signal `input_vector2_changed(name: String, value: Vector2)` → `input_vector2_changed(action_name: String, value: Vector2)`

#### XRPositionalTracker
- ~ signal `button_pressed(name: String)` → `button_pressed(action_name: String)`
- ~ signal `button_released(name: String)` → `button_released(action_name: String)`
- ~ signal `input_float_changed(name: String, value: float)` → `input_float_changed(action_name: String, value: float)`
- ~ signal `input_vector2_changed(name: String, vector: Vector2)` → `input_vector2_changed(action_name: String, vector: Vector2)`

#### XRServer
- + signal `world_origin_changed()`

#### ZIPPacker
- + method `add_directory(path: String, permissions: int = 493, modified_time: int = 0) -> int`
- ~ method `start_file(path: String) -> int` → `start_file(path: String, permissions: int = 420, modified_time: int = 0) -> int`
