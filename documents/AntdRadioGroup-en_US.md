**id:** *string* or *dict* type

　　 Used to set the *unique id information* for the current component.

**key:** *string* type

　　 Updates the `key` value of the current component, which can force a redraw of the current component.

**style:** *dict* type

　　 Used to set the *CSS styles* for the current component.

**className:** *string* or *dict* type

　　 Used to set the *CSS class names* for the current component, supports [dynamic CSS](/advanced-classname).

**direction:** *string* type, default is `'horizontal'`

　　 Used to *set the direction of option arrangement* for the radio group, available options are `'horizontal'` and `'vertical'`.

**options:** `list[dict]` type

　　 Used to *define the options*, where each dictionary represents an option. Available key-value parameters include:

- **label:** *component type*, used to *set the label content* for the current option.
- **value:** *string*, *int*, or *float* type, used to *set the selected value* for the current option.
- **disabled:** *bool* type, default is `False`, used to *set whether the current option is disabled*.

**disabled:** *bool* type, default is `False`

　　 Used to *set whether the current component is disabled*.

**size:** *string* type, default is `'middle'`

　　 When `optionType='button'`, used to *set the size specification* for the current component. Available options are `'small'`, `'middle'`, and `'large'`.

**value:** *string*, *int*, or *float* type

　　 Used to *listen to or set the currently selected value*.

**defaultValue:** *string*, *int*, or *float* type

　　 Used to *listen to or set the initially selected value*.

**optionType:** *string* type, default is `'default'`

　　 Used to *set the style type* for the options. Available options are `'default'` and `'button'`.

**buttonStyle:** *string* type, default is `'outline'`

　　 When `optionType='button'`, used to *set the style of the buttons*. Available options are `'outline'` and `'solid'`.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**persistence:** *bool* type

　　 Used to *set whether to enable attribute persistence* for the current component.

**persisted_props:** *list* type, default is `['value']`

　　 Used to *set which attributes of the current component are persisted*. Available options are `'value'`.

**persistence_type:** *string* type, default is `'local'`

　　 Used to *set the storage type for attribute persistence* of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).