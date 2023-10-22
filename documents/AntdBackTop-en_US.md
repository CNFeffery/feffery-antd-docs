**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**duration:** *int* or *float*, default: `0.45`

　　Used to set the duration of the scroll-to-top animation in seconds.

**visibilityHeight:** *int*, default: `400`

　　Used to set the pixel threshold for the scroll distance before the back-to-top button becomes visible.

**containerId:** *string*

　　Used to set the ID of the container to which the back-to-top button is bound.

**containerSelector:** *string* type

　　Lower priority than `containerId`, used for *passing a JavaScript code string to configure the target local container*.