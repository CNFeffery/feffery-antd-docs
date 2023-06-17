**id:** *string* or *dict* type

　　Used to set the unique id information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, allowing for a forced redraw of the component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**description:** *component type* or *bool* type

　　Used to set the description information. When set to `False`, the description information will be hidden.

**image:** *string* type, default: `'default'`

　　Used to set the placeholder image for the empty state. Options are `'default'` and `'simple'`. You can also directly pass the image URL address to customize the placeholder image.

**imageStyle:** *dict* type

　　Used to set the CSS style of the placeholder image.