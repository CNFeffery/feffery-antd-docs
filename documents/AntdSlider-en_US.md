**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* type

　　Used to set the CSS class name for the current component.

**vertical:** *bool* type, default: `False`

　　Used to set whether to display the slider vertically.

**range:** *bool* type, default: `False`

　　Used to enable range selection.

**min:** *int* or *float* type, required

　　Specifies the minimum value of the adjustable range.

**max:** *int* or *float* type, required

　　Specifies the maximum value of the adjustable range.

**step:** *int* or *float* type, default: `1`

　　Specifies the sliding adjustment step.

**marks:** *dict* type

　　Specifies the scale labels corresponding to specific values.

**tooltipVisible:** *bool* type

　　Specifies the visibility strategy of the tooltip. Set to `True` to always display the tooltip, `False` to hide it. By default, the tooltip is only displayed when the user drags the slider.

**tooltipPrefix:** *string* type, default: `''`

　　Specifies additional prefix text content for the tooltip.

**tooltipSuffix:** *string* type, default: `''`

　　Specifies additional suffix text content for the tooltip.

**disabled:** *bool* type, default: `False`

　　Specifies whether the current component is disabled.

**value:** *int*, *float*, or *list* type

　　Listens to or sets the current slider value.

**defaultValue:** *int*, *float*, or *list* type

　　Listens to or sets the initial slider value.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**popupContainer:** *string* type, default: `'body'`

　　Specifies the reference container type for the floating layer elements associated with the current component. Available options are `'body'` (uses the root node of the page as the reference) and `'parent'` (uses the parent container of the current element as the reference). When the component is inside a scrollable container, setting `popupContainer='parent'` can solve the issue of the floating layer not scrolling with the container.

**persistence:** *bool* type

　　Specifies whether to enable property persistence for the current component.

**persisted_props:** *list* type, default: `['value']`

　　Specifies which properties of the current component to persist. Available options are `'value'`.

**persistence_type:** *string* type, default: `'local'`

　　Specifies the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).