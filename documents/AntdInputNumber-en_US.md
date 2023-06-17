**id:** *string* or *dict* type

　　Used to set the unique id information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-render of the component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**addonBefore:** *component type*

　　Used to set the additional element before the input box.

**addonAfter:** *component type*

　　Used to set the additional element after the input box.

**prefix:** *component type*

　　Used to set the embedded prefix element inside the input box.

**controls:** *bool* type, default: `True`

　　Used to determine whether to add auxiliary shortcut increase/decrease buttons inside the number input box.

**keyboard:** *bool* type, default: `True`

　　Used to determine whether to allow adjusting the value using the up and down arrow keys on the keyboard.

**min:** *int*, *float*, or *string* type

　　Used to set the lower bound of the valid values for the current number input box. Default is unlimited.

**max:** *int*, *float*, or *string* type

　　Used to set the upper bound of the valid values for the current number input box. Default is limited.

**step:** *int*, *float*, or *string* type

　　Used to set the increment/decrement step for the current number input box.

**precision:** *int* type

　　Used to set the number precision (decimal places) for the current number input box.

**stringMode:** *bool* type, default: `False`

　　Used to enable high precision mode, which allows accurate input of high precision numbers. When enabled, the parameters `min`, `max`, `step`, `value`, and `defaultValue` should be of *string* type.

**disabled:** *bool* type, default: `False`

　　Used to determine whether the current component is disabled.

**size:** *string* type, default: `'middle'`

　　Used to set the size specification of the current component. Options are `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool* type, default: `True`

　　Used to determine whether to render the border.

**placeholder:** *string* type

　　Used to set the fill-in instructions for blank input.

**value:** *list* type

　　Used to listen to or set the currently entered values.

**defaultValue:** *list* type

　　Used to listen to or set the initially entered values.

**debounceValue:** *string* type

　　Uses `debounceValue` instead of `value` to effectively debounce callbacks by setting a debounce delay.

**debounceWait:** *int* type, default: `200`

　　Used to set the debounce delay duration for updating `debounceValue`, in milliseconds.

**nSubmit:** *int* type, default: `0`

　　Used to listen to the number of times the Enter key is pressed while the cursor is inside the input box.

**status:** *string* type

　　Used to forcibly set the status of the component. Options are `'error'` and `'warning'`.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**persistence:** *bool* type

　　Used to enable attribute persistence for the current component.

**persisted_props:** *list* type, default: `['value']`

　　Used to specify which attributes of the current component should be persisted. Options include `'value'`.

**persistence_type:** *string* type, default: `'local'`

　　Used to set the storage type for attribute persistence of the current component. Options include `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).