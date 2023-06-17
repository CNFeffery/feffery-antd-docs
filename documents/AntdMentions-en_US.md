**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which can force a redraw of the component.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**autoSize:** *bool* or *dict* type, default is `False`

　　Used to configure the input box's auto-sizing feature based on the input content. When passing a *dict* type input, the available key-value parameters are:

- **minRows:** *int* type, used to set the minimum number of rows.
- **maxRows:** *int* type, used to set the maximum number of rows.

**prefix:** *string* type, default is `'@'`

　　Used to set the keyword that triggers the submenu to pop up.

**value:** *list* type

　　Used to listen to or set the current input value.

**defaultValue:** *list* type

　　Used to listen to or set the initial input value.

**options:** `list[dict]` type, required

　　Used to define the options in the submenu. Each dictionary can have the following key-value parameters:

- **label:** *component* type, used to set the label content for the current option.
- **value:** *string* type, used to set the value corresponding to the current option.

**selectedOptions:** *list* type

　　Used to listen to the selected option values in the mentioned component.

**disabled:** *bool* type, default is `False`

　　Used to disable the current component.

**placement:** *str* type, default is `'bottom'`

　　Used to set the expansion direction of the submenu. The available options are `'bottom'` and `'top'`.

**status:** *string* type

　　Used to force set the status of the component. The available options are `'error'` and `'warning'`.

**popupContainer:** *string* type, default is `'body'`

　　Used to set the reference container type for the floating layer elements involved in the current component. The available options are `'body'` (with the page root node as the reference) and `'parent'` (with the parent container of the current element as the reference). When the component is located inside a scrollable container, setting `popupContainer='parent'` can solve the problem of the floating layer not scrolling along.