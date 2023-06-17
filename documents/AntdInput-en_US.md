**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which allows for forcefully redrawing the current component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**mode:** *string* type, default: `'default'`

　　Used to set the functional mode of the current input box. Options are `'default'` (regular input box), `'search'` (search input box with search functionality), `'text-area'` (text area input box), `'password'` (password input box).

**autoComplete:** *string* type, default: `'on'`

　　Used to set the browser's built-in autocomplete feature for the input box. Options are `'on'` (enabled) and `'off'` (disabled).

**disabled:** *bool* type, default: `False`

　　Used to set whether the current component is disabled.

**size:** *string* type, default: `'middle'`

　　Used to set the size specification of the current component. Options are `'small'`, `'middle'`, and `'large'`.

**bordered:** *bool* type, default: `True`

　　Used to set whether to render the border.

**placeholder:** *string* type

　　Used to set the placeholder text for the empty input.

**value:** *list* type

　　Used to listen to or set the currently inputted value.

**defaultValue:** *list* type

　　Used to listen to or set the initially inputted value.

**md5Value:** *string* type

　　When `passwordUseMd5=True`, used to listen to the MD5 encrypted information of the currently inputted value.

**debounceValue:** *string* type

　　Use `debounceValue` instead of `value` to effectively set debounce delay and achieve debounce effect.

**passwordUseMd5:** *bool* type, default: `False`

　　Used to enable MD5 encryption in password input box mode.

**debounceWait:** *int* type, default: `200`

　　Used to set the debounce delay for updating `debounceValue`, in milliseconds.

**addonBefore:** *component type*

　　Used to set the additional element before the input box.

**addonAfter:** *component type*

　　Used to set the additional element after the input box.

**prefix:** *component type*

　　Used to set the embedded prefix element inside the input box.

**suffix:** *component type*

　　Used to set the embedded suffix element inside the input box.

**maxLength:** *int* type

　　Used to set the maximum number of characters allowed in the input box, no limit by default.

**showCount:** *bool* type, default: `False`

　　Used to set whether to display the current character count.

**autoSize:** *bool* or *dict* type, default: `False`

　　Used to configure the auto-adjustment of the input box height for the text area input box mode. When a *dict* type input is passed, the available key-value pairs are:

- **minRows:** *int* type, used to set the minimum number of rows.
- **maxRows:** *int* type, used to set the maximum number of rows.

**nSubmit:** *int* type, default: `0`

　　Used to listen to the number of times the Enter key is pressed while the cursor is inside the input box.

**nClicksSearch:** *int* type, default: `0`

　　Used to listen to the number of times the search button is clicked in search input box mode.

**status:** *string* type

　　Used to forcefully set the status of the component. Options are `'error'` and `'warning'`.

**allowClear:** *bool* type, default: `True`

　　Used to set whether to allow the user to clear the selected option.

**readOnly:** *bool* type

　　Used to display the component in read-only mode.

**emptyAsNone:** *bool* type, default: `False`

　　When there is no valid content in the input box, used to set whether to update `value` and `debounceValue` to None instead of an empty string.

**persistence:** *bool* type

　　Used to enable property persistence for the current component.

**persisted_props:** *list* type, default: `['value', 'md5Value']`

　　Used to set which properties of the current component to persist. Options are `'value'` and `'md5Value'`.

**persistence_type:** *string* type, default: `'local'`

　　Used to set the storage type for property persistence of the current component. Options are `'local'` (browser local storage), `'session'` (current tab session storage), and `'memory'` (temporary memory cache).