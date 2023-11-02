**id:** *string* or *dict* type

　　Used to set the *unique ID information for the current component*.

**key:** *string* type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS style for the current component*.

**className:** *string* or *dict* type

　　Used to set the *CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Options include `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**format:** *string* type

　　Used to set the *date parsing format for the current date picker*. Refer to the [documentation](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/) for specific formats.

**disabled:** *bool* type, default: `False`

　　Used to set whether to disable the current component.

**hourStep:** *int* type, default: `1`

　　Used to set the interval between options in the hour selection.

**minuteStep:** *int* type, default: `1`

　　Used to set the interval between options in the minute selection.

**secondStep:** *int* type, default: `1`

　　Used to set the interval between options in the second selection.

**use12Hours:** *bool* type, default: `False`

　　Used to set whether to use the 12-hour format.

**size:** *string* type, default: `'middle'`

　　Used to set the size specification for the current component. Options include `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool* type, default: `True`

　　Used to set whether to render a border.

**placeholder:** *string* type

　　Used to set the explanatory text for the blank input.

**placement:** *str* type, default: `'bottomLeft'`

　　Used to set the expansion direction of the dropdown menu. Options include `'bottomLeft'`, `'bottomRight'`, `'topLeft'`, and `'topRight'`.

**value:** *string* type

　　Used to listen to or set the currently selected value.

**defaultValue:** *string* type

　　Used to listen to or set the initially selected value.

**status:** *string* type

　　Used to forcefully set the status of the component. Options include `'error'` and `'warning'`.

**allowClear:** *bool* type, default: `True`

　　Used to set whether users are allowed to clear the selected option.

**autoFocus:** *bool* type, default: `False`

　　Used to set whether to automatically focus.

**readOnly:** *bool* type

　　Used to set whether to display the component in read-only mode.

**showNow:** *bool* type, default: `True`

　　Used to *determine whether to render the "Now" shortcut button.*

**extraFooter:** *Component*

　　Used to *set additional elements at the bottom of the selection panel.*

**popupContainer:** *string* type, default: `'body'`

　　Used to set the reference container type for the floating layer elements associated with the current component. Options include `'body'` (root node of the page) and `'parent'` (parent container of the current element). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling with it.

**persistence:** *bool* type

　　Used to enable property persistence for the current component.

**persisted_props:** *list* type, default: `['value']`

　　Used to set which properties of the current

 component are persisted. Options include `'value'`.

**persistence_type:** *string* type, default: `'local'`

　　Used to set the storage type for property persistence of the current component. Options include `'local'` (browser local cache), `'session'` (current tab session cache), and `'memory'` (temporary memory cache).