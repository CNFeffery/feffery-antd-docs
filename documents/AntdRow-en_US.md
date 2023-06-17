**id:** *string* or *dict* type

　　Used to set the *unique id information* for the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS styles* for the current component.

**className:** *string* or *dict* type

　　Used to set the *CSS class names* for the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in *nested child elements*.

**align:** *string* type, default is `'top'`

　　Used to *set the vertical alignment* of the columns. Available options are `'top'`, `'middle'`, and `'bottom'`.

**gutter:** *int*, *list*, or *dict* type, default is `0`

　　Used to set the pixel spacing between rows and columns. When an *int* value is passed, it sets the horizontal spacing between the included columns. It can also be passed as a list `[horizontal spacing, vertical spacing]` to set the pixel spacing between column components in both directions. Alternatively, it can be passed as a dictionary with responsive breakpoints such as `'xs'` as keys to set the horizontal spacing between columns individually for each breakpoint.

**justify:** *string* type, default is `'start'`

　　Used to *set the overall horizontal layout* of all internal column components. Available options are `'start'`, `'end'`, `'center'`, `'space-around'`, `'space-between'`.

**wrap:** *bool* type, default is `True`

　　Used to *set whether the internal column elements automatically wrap to the next line when the unit width of the columns exceeds*.