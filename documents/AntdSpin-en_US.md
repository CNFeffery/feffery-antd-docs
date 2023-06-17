**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**wrapperClassName:** *string* or *dict* type

　　Used to set the CSS class name for the container of the current loading animation component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**size:** *string* type, default: `'middle'`

　　Used to set the size specification of the current loading animation. Available options are `'small'`, `'middle'`, and `'large'`.

**delay:** *int* type, default: `0`

　　Used to set the delay for displaying the loading animation, in milliseconds.

**text:** *string* type

　　Used to set the content of the accompanying text for the loading animation.

**debug:** *bool* type, default: `False`

　　Used to enable debug mode. When enabled, if the nested elements within the skeleton screen are assigned as callback function `Output` roles and are being executed, the `id` and `prop` information of the relevant components will be printed in the browser console.

**listenPropsMode:** *string* type, default: `'default'`

　　Used to set the listening mode for the callback behavior of the nested elements within the skeleton screen. Available options are `'default'` (default full listening mode), `'exclude'` (exclude mode), and `'include'` (include mode).

**excludeProps:** *list* type

　　When `listenPropsMode='exclude'`, used to specify the properties of the nested components that should be excluded from listening. Each element in the list defines the target to be excluded in the format of `component id.property name`, e.g., `'demo-input.value'`.

**includeProps:** *list* type

　　When `listenPropsMode='include'`, used to specify the properties of the nested components that should be included in listening. Each element in the list defines the target to be included in the format of `component id.property name`, e.g., `'demo-input.value'`.

**indicator:** *component type*

　　Used to customize the loading animation element, recommended to be used with `FefferyExtraSpinner` in the `fuc` function.