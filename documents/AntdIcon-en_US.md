**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**icon:** *string*

　　Used to set the name of the icon to be rendered.

**nClicks:** *int*, default: `0`

　　Used to record the number of times the icon is clicked in the callback.

**debounceWait:** *int*, default: `200`

　　Used to set the debounce delay for updating `nClicks` in milliseconds.