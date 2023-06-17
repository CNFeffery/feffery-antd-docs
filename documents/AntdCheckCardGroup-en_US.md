**id:** *string* or *dict*

　　Used to set the *unique id information* of the current component.

**key:** *string*

　　Updates the `key` value of the current component to force a re-render.

**style:** *dict*

　　Used to set the *CSS style* of the current component.

**className:** *string* or *dict*

　　Used to set the *CSS class name* of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass *nested individual check cards*.

**multiple:** *bool*, default is `False`

　　Used to *determine whether multiple selections are allowed*.

**bordered:** *bool*, default is `True`

　　Used to *determine whether to render an outline* for the individual check cards.

**value:** *int*, *float*, *string*, or *list*

　　Used to *set or listen to the values* of the currently selected check cards.

**defaultValue:** *int*, *float*, *string*, or *list*

　　Used to *set the initial values* of the pre-selected check cards.

**disabled:** *bool*, default is `False`

　　Used to *disable the entire check card group*.

**size:** *string*, default is `'default'`

　　Used to *set the overall size* of the check card group. Available options are `'small'`, `'default'`, `'large'`.

**persistence:** *bool*

　　Used to *enable property persistence* for the current component.

**persisted_props:** *list*, default is `['value']`

　　Used to *specify which properties* of the current component should be persisted. Options include `'value'`.

**persistence_type:** *string*, default is `'local'`

　　Used to *specify the storage type* for property persistence of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).