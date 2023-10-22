**id:** *string* or *dict*

   Used to set the unique ID information for the current component.

**key:** *string*

   Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict*

   Used to set the CSS style for the current component.

**className:** *string* or *dict*

   Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**disabled:** *bool*, default: `False`

   Used to enable or disable the current component.

**options:** `list[dict]`

   Used to define options, where each dictionary represents an option. Available key-value parameters are:

- **label:** *component*, used to set the label content for the current option.
- **value:** *string*, *int*, or *float*, used to set the selected value for the current option.
- **disabled:** *bool*, default: `False`, used to enable or disable the current option.

**value:** *list*

   Used to listen to or set the currently selected value.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**persistence:** *bool*

   Used to enable property persistence for the current component.

**persisted_props:** *list*, default: `['value']`

   Used to set which properties of the current component are persisted. Available options are `'value'`.

**persistence_type:** *string*, default: `'local'`

   Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).