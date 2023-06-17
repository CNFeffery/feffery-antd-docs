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

**color:** *string*

　　Used to set the color of the badge.

**count:** *int*

　　Used to set the count value to be displayed in the badge. Can be used in conjunction with the `showZero` and `overflowCount` parameters for additional display functionality.

**dot:** *bool*, default: `False`

　　Used to determine whether to display a numerical count or just a small dot in the badge.

**showZero:** *bool*, default: `False`

　　By default, the badge does not display a count value when `count` is 0. Setting `showZero=True` will force the display of the count value as 0.

**overflowCount:** *int*, default: `99`

　　Used to set the upper limit of the count value in the badge. When the `count` exceeds this limit, it will be displayed as `overflowCount+`, for example, `99+`.

**offset:** *list*

　　Used to set the offset distance of the badge from the right and bottom edges in pixels. The format is `[offset from right, offset from bottom]`.

**status:** *string*

　　Used to set the status of the badge. Available options are `'success'`, `'processing'`, `'default'`, `'error'`, and `'warning'`.

**text:** *string*

　　When the `status` parameter is set, this parameter can be used to set the text content of the status badge.

**title:** *string*

　　Used to set the text content displayed when hovering over the status badge.

**size:** *string*, default: `'default'`

　　Used to set the size of the current component. Available options are `'default'` and `'small'`.

**nClicks:** *int*, default: `0`

　　Used to listen to the click event of the badge.