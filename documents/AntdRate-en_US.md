**id:** *string* or *dict* type

　　 Used to set the *unique id information* for the current component.

**key:** *string* type

　　 Updates the `key` value of the current component, which can force a redraw of the current component.

**style:** *dict* type

　　 Used to set the *CSS styles* for the current component.

**className:** *string* or *dict* type

　　 Used to set the *CSS class names* for the current component, supports [dynamic CSS](/advanced-classname).

**allowClear:** *bool* type, default is `True`

　　 Used to *set whether to allow users to clear the rating by clicking again*.

**allowHalf:** *bool* type, default is `False`

　　 Used to *set whether to allow half-star selection*.

**count:** *int* type, default is `5`

　　 Used to *set the total number of stars*.

**tooltips:** `list[string]` type

　　 Used to *set the mouse hover tooltip text for each star rating*.

**disabled:** *bool* type, default is `False`

　　 Used to *set whether the current component is disabled*.

**value:** *int* or *float* type

　　 Used to *listen to or set the currently selected value*.

**defaultValue:** *int* or *float* type

　　 Used to *listen to or set the initially selected value*.

**persistence:** *bool* type

　　 Used to *set whether to enable attribute persistence* for the current component.

**persisted_props:** *list* type, default is `['value']`

　　 Used to *set which attributes of the current component are persisted*. Available options are `'value'`.

**persistence_type:** *string* type, default is `'local'`

　　 Used to *set the storage type for attribute persistence* of the current component. Available options are `'local'` (browser local storage), `'session'` (current tab session storage), `'memory'` (temporary memory cache).