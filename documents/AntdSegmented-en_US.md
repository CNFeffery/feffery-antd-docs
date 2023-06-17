**id:** *string* or *dict* type

　　Used to set the *unique id information* for the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS styles* for the current component.

**className:** *string* or *dict* type

　　Used to set the *CSS class names* for the current component, supports [dynamic CSS](/advanced-classname).

**disabled:** *bool* type, default is `False`

　　Used to *set whether the current component is disabled*.

**options:** `list[dict]` type

　　Used to *define the options*, where each dictionary represents an option. Available key-value pairs are:

- **label:** *component type*, required. Used to *set the label content* for the current option.
- **value:** *int*, *float*, or *string* type, required. Used to *set the selected value* for the current option.
- **disabled:** *bool* type, default is `False`. Used to *set whether the current option is disabled*.
- **icon:** *string* type. Used to *set the prefix icon* for the current option, same as the corresponding parameter in `AntdIcon`.

**value:** *int*, *float*, or *string* type

　　Used to *listen to or set the currently selected value*.

**defaultValue:** *int*, *float*, or *string* type

　　Used to *set the initially selected value*.

**block:** *bool* type, default is `False`

　　Used to *set whether the current segment control spans the full width of its parent container*.

**size:** *string* type, default is `'middle'`

　　Used to *set the size specification* for the current component. Available options are `'small'`, `'middle'`, `'large'`.

**persistence:** *bool* type

　　Used to *set whether to enable attribute persistence* for the current component.

**persisted_props:** *list* type, default is `['value']`

　　Used to *set which attributes to persist* for the current component. Available option is `'value'`.

**persistence_type:** *string* type, default is `'local'`

　　Used to *set the storage type for attribute persistence* for the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).