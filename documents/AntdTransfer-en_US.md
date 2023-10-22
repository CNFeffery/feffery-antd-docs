**id:** *string* or *dict* type

　　Used to set the *unique ID information for the current component*.

**key:** *string* type

　　Updates the `key` value for the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS style for the current component*.

**className:** *string* or *dict* type

　　Used to set the *CSS class name for the current component*. Supports [dynamic CSS](/advanced-classname).

**locale:** *string* type, default: `'zh-cn'`

　　Used to *set the language for the functional text of the current component*. Options include `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**dataSource:** `list[dict]` type

　　Used to *define the options in the transfer box*. Each dictionary can have the following key-value pairs:

- **key:** *string* or *int* type, used to *set the unique identifier for the current option*.
- **title:** *component type*, used to *set the title content for the current option*.

**height:** *string* type

　　Used to *set the height of the current transfer box*. Accepts a valid `height` value in CSS.

**pagination:** *bool* or *dict* type, default: `False`

　　Used to *configure pagination for the options in the transfer box*. When passed as a *dict* type, the available key-value pairs are:

- **pageSize:** *int* type, used to *set the number of records per page*.

**operations:** `list[string]` type, default: `['', '']`

　　Used to *set the text content for the move item buttons on the left and right*.

**showSearch:** *bool* type, default: `False`

　　Used to *set whether to render the search box*.

**optionFilterMode:** *string* type, default: `'case-insensitive'`

　　Used to *set the matching mode for the input box search*. Options include `'case-insensitive'` (case-insensitive), `'case-sensitive'` (case-sensitive), and `'regex'` (regular expression).

**showSelectAll:** *bool* type, default: `True`

　　Used to *set whether to render the select all checkbox*.

**titles:** `list[component]` type

　　Used to *set the title content for the left and right transfer boxes*.

**targetKeys:** *list* type

　　Used to *set or listen to the key values of the options in the right area of the transfer box*.

**moveDirection:** *string* type

　　Used to *listen to the direction of the most recent move item operation*. Can be `'left'` or `'right'`.

**moveKeys:** *list* type

　　Used to *listen to the key values of the options involved in the most recent move item operation*.

**disabled:** *bool* type, default: `False`

　　Used to *set whether the current component is disabled*.

**status:** *string* type

　　Used to *force set the status of the component*. Options include `'error'` and `'warning'`.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**persistence:** *bool* type

　　Used to *set whether to enable property persistence for the current component*.

**persisted_props:** *list* type, default: `['targetKeys']`

　　Used to *set which properties of the current component to persist*. Options

 include `'targetKeys'`.

**persistence_type:** *string* type, default: `'local'`

　　Used to *set the storage type for property persistence of the current component*. Options include `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).