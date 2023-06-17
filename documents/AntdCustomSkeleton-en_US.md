**id:** *string* or *dict* type

　　 Used to set the unique ID information of the current component.

**key:** *string* type

　　 Updates the `key` value of the current component, enabling the forced redraw of the current component.

**style:** *dict* type

　　 Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　 Used to set the CSS class name of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component type*

　　 Used to pass in nested child elements.

**skeletonContent:** *component type*

　　 Used to set the elements that serve as the content for the skeleton loading state.

**debug:** *bool* type, default: `False`

　　 Used to enable or disable debug mode. When enabled, the `id` and `prop` information of related components will be printed in the browser console when the nested elements inside the skeleton screen act as callback functions with the `Output` role and during the execution of callback functions.

**listenPropsMode:** *string* type, default: `'default'`

　　 Used to set the listening mode for the callback behavior of nested elements inside the skeleton screen. Available options are `'default'` (default full listening mode), `'exclude'` (exclude mode), and `'include'` (include mode).

**excludeProps:** *list* type

　　 When `listenPropsMode='exclude'`, used to specify the properties of the internal nested components that need to be excluded from listening. Each element in the list is used to define the target to be excluded in the format of `component_id.property_name`, for example, `'demo-input.value'`.

**includeProps:** *list* type

　　 When `listenPropsMode='include'`, used to specify the properties of the internal nested components that need to be included in listening. Each element in the list is used to define the target to be included in the format of `component_id.property_name`, for example, `'demo-input.value'`.