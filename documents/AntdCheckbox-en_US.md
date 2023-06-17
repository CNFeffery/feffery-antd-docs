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

**label:** *component*

   Used to set the label content for the current checkbox.

**checked:** *bool*, default: `False`

   Used to set or listen to the checked state of the current checkbox.

**indeterminate:** *bool*, default: `False`

   Used to control whether the current checkbox should be styled as indeterminate. This parameter only affects the style and is independent of the checked state.

**persistence:** *bool*

   Used to enable property persistence for the current component.

**persisted_props:** *list*, default: `['checked']`

   Used to set which properties of the current component are persisted. Available options are `'checked'`.

**persistence_type:** *string*, default: `'local'`

   Used to set the storage type for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).