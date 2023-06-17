**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**disabled:** *bool* type, default: `False`

　　Used to set whether the current component is disabled.

**checked:** *bool* type, default: `False`

　　Used to set or listen to the on/off state of the current switch.

**checkedChildren:** *component type*

　　Used to set the content of the label when the switch is in the on state.

**unCheckedChildren:** *component type*

　　Used to set the content of the label when the switch is in the off state.

**size:** *string* type, default: `'default'`

　　Used to set the size specification of the current component. Available options are `'default'` and `'small'`.

**loading:** *bool* type, default: `False`

　　Used to set whether to render the loading state.

**persistence:** *bool* type

　　Used to enable property persistence for the current component.

**persisted_props:** *list* type, default: `['checked']`

　　Used to set which properties of the current component are persisted. Available options are `'checked'`.

**persistence_type:** *string* type, default: `'local'`

　　Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).