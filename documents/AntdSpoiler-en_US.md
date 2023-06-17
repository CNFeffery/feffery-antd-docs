**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Available options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**contentClassName:** *string* or *dict* type

　　Used to set the CSS class name for the content area of the current expand/collapse component, supports [dynamic CSS](/advanced-classname).

**contentStyle:** *dict* type

　　Used to set the CSS style for the content area of the current expand/collapse component.

**hideLabel:** *component type*

　　Used to set the label information for the collapse button when the current expand/collapse component is in the collapsed state.

**showLabel:** *component type*

　　Used to set the label information for the expand button when the current expand/collapse component is in the expanded state.

**labelPosition:** *string* type, default: `'left'`

　　Used to set the position of the expand/collapse button. Available options are `'left'` and `'right'`.

**open:** *bool* type, default: `False`

　　Used to set or listen to whether the current expand/collapse component is in the expanded state.

**maxHeight:** *int* type, default: `50`

　　Used to set the maximum pixel height of the content area of the current expand/collapse component in the collapsed state.

**transitionDuration:** *int* or *float* type, default: `0.1`

　　Used to set the duration of the transition animation when the state of the current expand/collapse component changes, in seconds.