**id：** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key：** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style：** *dict* type

　　Used to set the CSS style for the current component.

**className：** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**children：** *component type*

　　Used to pass in nested child elements.

**active：** *bool* type, default to `False`

　　Used to set whether the current skeleton screen enables the scanning animation effect.

**avatar：** *bool* or *dict* type, default to `False`

　　Used to set whether to add an avatar placeholder in the skeleton screen. When passing a *dict* type, you can configure the avatar placeholder. Available key-value parameters include:

- **active：** *bool* type, default to `False`, used to set whether the avatar placeholder enables the scanning animation effect.
- **shape：** *string* type, optional values are `'circle'` and `'square'`.
- **size：** *int* or *string* type, default to `'default'`, used to set the size of the avatar placeholder. For *int* type input, it sets the pixel size. For *string* type, optional values are `'large'`, `'small'`, and `'default'`.

**paragraph：** *bool* or *dict* type, default to `True`

　　Used to set whether to add a paragraph placeholder in the skeleton screen. When passing a *dict* type, you can configure the paragraph placeholder. Available key-value parameters include:

- **rows：** *int* type, used to set the actual number of rows in the paragraph placeholder.
- **width：** *int*, *string*, or *list* type. When passing *int* or *string* type, it sets the width of the last line of the paragraph placeholder. When passing *list* type, it sets the width line by line.

**title：** *bool* or *dict* type, default to `True`

　　Used to set whether to add a title placeholder in the skeleton screen. When passing a *dict* type, you can configure the title placeholder. Available key-value parameters include:

- **width：** *int* or *string* type, used to set the width of the title placeholder.

**round：** *bool* type, default to `False`

　　Used to set whether to enable rounded corners for the paragraph and title placeholders.

**debug：** *bool* type, default to `False`

　　Used to enable debugging mode. When enabled, the `id` and `prop` information of the relevant components will be printed in the browser console when the nested elements inside the skeleton screen act as callback function `Output` roles and during the execution of the callback function.

**listenPropsMode：** *string* type, default to `'default'`

　　Used to set the listening mode for the callback behavior of the nested elements inside the skeleton screen. Available options are `'default'` (default full listening mode), `'exclude'` (exclude mode), and `'include'` (include mode).

**excludeProps：** *list* type

　　When `listenPropsMode='exclude'`, used to set the properties of the internal nested components that need to be excluded from listening. Each element in the list is used to define the target to be

 excluded, and the format is `component_id.property_name`, such as `'demo-input.value'`.

**includeProps：** *list* type

　　When `listenPropsMode='include'`, used to set the properties of the internal nested components that need to be included in listening. Each element in the list is used to define the target to be included, and the format is `component_id.property_name`, such as `'demo-input.value'`.