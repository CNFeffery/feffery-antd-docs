**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**loadingChildren:** *component type*

　　Used to set the nested child elements of the button when it is in the loading state.

**type:** *string*, default: `'default'`

　　Used to set the button style. Available options are `'primary'`, `'ghost'`, `'dashed'`, `'link'`, `'text'`, and `'default'`.

**href:** *string*

　　When a valid URL is passed, the `AntdButton` can function as a webpage redirect button.

**target:** *string*

　　When the `href` parameter has a valid URL passed, it is used to set the type of action for the redirect. [Reference](https://www.w3schools.com/tags/att_a_target.asp)

**block:** *bool*, default: `False`

　　Used to set whether the button's width should span the full width of its parent element.

**danger:** *bool*, default: `False`

　　Used to render the button in a dangerous warning state.

**disabled:** *bool*, default: `False`

　　Used to disable the current component.

**ghost:** *bool*, default: `False`

　　Used to set the current button background transparent.

**shape:** *string* or *None*, default: `None`

　　Used to set the button shape. Available options are `'circle'` (circle) and `'round'` (rounded rectangle).

**size:** *string*, default: `'middle'`

　　Used to set the size of the current component. Available options are `'small'`, `'middle'`, and `'large'`.

**nClicks:** *int*, default: `0`

　　Used to record the number of times the button is clicked in the callback.

**debounceWait:** *int*, default: `200`

　　Used to set the debounce delay for updating `nClicks` in the listener, in milliseconds.

**icon:** *component type*

　　Used to set the embedded prefix subelement for the current button.

**loading:** *bool*, default: `False`

　　Used to render the button in the loading state.

**autoSpin:** *bool*, default: `False`

　　Used to automatically switch the button to the loading state after being clicked.