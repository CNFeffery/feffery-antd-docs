**id：** *string* or *dict* type

　　Used to set the unique id information of the current component.

**key：** *string* type

　　Updates the `key` value of the current component, enabling the effect of forced redraw of the current component.

**style：** *dict* type

　　Used to set the CSS style of the current component.

**className：** *string* or *dict* type

　　Used to set the CSS class name of the current component, supporting [dynamic CSS](/advanced-classname).

**locale：** *string* type, default to `'zh-cn'`

　　Used to set the language for the functional text of the current component, optional values are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**options：** `list[dict]` type, required

　　Used to construct the option structure for the dropdown selection. Each dictionary in the list can have the following key-value pairs:

- **label：** *component type*, used to set the label content of the current option.
- **value：** *string*, *int*, or *float* type, used to set the value of the current option.
- **disabled：** *bool* type, default to `False`, used to set whether the current option is disabled.
- **colors：** `list[string]` type, used to define the color value sequence of the current option in special color rendering mode.
- **group：** *string* type, used to set the label content of the current group.
- **options：** `list[dict]` type, used to define the option configuration dictionary array nested under the current group.

**listHeight：** *int* type, default to `256`

　　Used to set the pixel height of the dropdown selection menu.

**colorsMode：** *string* type

　　Used to set the color rendering mode when color rendering is needed. Optional values are `'sequential'` (sequential color scheme) and `'diverging'` (discrete color scheme).

**colorsNameWidth：** *int* type, default to `40`

　　Used to set the pixel width of the color name part in color rendering mode.

**mode：** *string* type

　　Used to set the selection mode, optional values are `'multiple'` (multiple selection) and `'tags'` (freely adding tags), not setting this will default to single selection.

**disabled：** *bool* type, default to `False`

　　Used to set whether the current component is disabled.

**size：** *string* type, default to `'middle'`

　　Used to set the size specification of the current component, optional values are `'small'`, `'middle'`, and `'large'`.

**bordered：** *bool* type, default to `True`

　　Used to set whether to render the border.

**placeholder：** *string* type

　　Used to set the filling explanatory text for the blank selection.

**placement：** *str* type, default to `'bottomLeft'`

　　Used to set the expansion direction of the dropdown menu, optional values are `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.

**value：** *string*, *int*, *float*, or *list* type

　　Used to listen to or set the currently selected value.

**defaultValue：** *string*, *int*, *float*, or *list* type

　　Used to listen to or set the initially selected value.

**maxTagCount：** *int

* or *str* type

　　Used to set the maximum number of selected items displayed in the selection box in multiple selection mode. It can also be set to `'responsive'` to enable responsive mode for adaptive adjustment.

**status：** *string* type

　　Used to forcibly set the status of the component, optional values are `'error'` and `'warning'`.

**optionFilterProp：** *string* type, default to `'value'`

　　Used to set the matching field of the search content with each option. Optional values are `'value'` and `'label'`.

**searchValue：** *string* type

　　Used to listen to the currently entered search content.

**optionFilterMode：** *string* type, default to `'case-insensitive'`

　　Used to set the matching mode for the search input box. Optional values are `'case-insensitive'` (case-insensitive), `'case-sensitive'` (case-sensitive), and `'regex'` (regular expression).

**debounceSearchValue：** *string* type

　　Used for debounced listening of the currently entered search content.

**debounceWait：** *int* type, default to `200`

　　Used to set the debounce delay duration for updating `debounceSearchValue`, in milliseconds.

**autoSpin：** *bool* type, default to `False`

　　Used to set whether to display a loading spinner animation when any parameter in the current dropdown selection acts as a callback output.

**autoClearSearchValue：** *bool* type, default to `True`

　　When `mode='multiple'` or `mode='tags'`, used to set whether to automatically clear the search content in the input box after a new option is selected.

**emptyContent：** *component type*

　　Used to customize the prompt content displayed in the dropdown menu when there are no options available.

**loadingEmptyContent：** *component type*

　　When `autoSpin=True` and any parameter in the current dropdown selection acts as a callback output, used to customize the prompt content displayed in the dropdown menu when there are no options available.

**dropdownBefore：** *component type*

　　Used to add additional custom content at the beginning of the dropdown menu.

**dropdownAfter：** *component type*

　　Used to add additional custom content at the end of the dropdown menu.

**allowClear：** *bool* type, default to `True`

　　Used to set whether to allow the user to clear the selected option.

**autoFocus：** *bool* type, default: `False`

　　Used to set whether to automatically focus.

**readOnly：** *bool* type

　　Used to display the component in read-only mode.

**popupContainer：** *string* type, default to `'body'`

　　Used to set the reference container type for the floating layer elements involved in the current component. Optional values are `'body'` (referencing the root node of the page) and `'parent'` (referencing the parent container of the current element). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling along.

**persistence：** *bool* type

　　Used to enable property persistence for the current component.

**persisted_props：** *list* type, default to `['value']`

　　Used to specify which properties of the current component should be persisted. Optional values are `'value'`.

**persistence_type：** *string* type, default to `'local'`

　　Used to set the storage type for property persistence of the current component. Optional values are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (in-memory temporary storage).