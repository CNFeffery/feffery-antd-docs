**id:** *string* or *dict*

　　Used to set the *unique id information* of the current component.

**key:** *string*

　　Updates the `key` value of the current component to force a re-render.

**style:** *dict*

　　Used to set the *CSS style* of the current component.

**className:** *string* or *dict*

　　Used to set the *CSS class name* of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass *nested child elements*.

**checked:** *bool*

　　Used to *set or listen to the state* of the current check card.

**defaultChecked:** *bool*

　　Used to *set the initial state* of the current check card.

**bordered:** *bool*, default is `True`

　　Used to *determine whether to render an outline* for the current check card.

**disabled:** *bool*, default is `False`

　　Used to *disable the current check card*.

**size:** *string*, default is `'default'`

　　Used to *set the size* of the current check card. Available options are `'small'`, `'default'`, `'large'`.

**value:** *int*, *float*, or *string*

　　Used in conjunction with `AntdCheckCardGroup` to *set the value* associated with the current check card.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**persistence:** *bool*

　　Used to *enable property persistence* for the current component.

**persisted_props:** *list*, default is `['checked']`

　　Used to *specify which properties* of the current component should be persisted. Options include `'checked'`.

**persistence_type:** *string*, default is `'local'`

　　Used to *specify the storage type* for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).