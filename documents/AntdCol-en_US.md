**id:** *string* or *dict*

　　Used to set the *unique id information* of the current component.

**key:** *string*

　　Updates the `key` value of the current component to force a re-render.

**style:** *dict*

　　Used to set the *CSS style* of the current component.

**className:** *string* or *dict*

　　Used to set the *CSS class name* of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component*

　　Used to pass *nested child elements*.

**span:** *int*

　　In the `fac` grid system, each `AntdRow` is divided into 24 parts. The `span` parameter is used to set the number of units occupied by the corresponding `AntdCol` within the parent `AntdRow`.

**offset:** *int*, default is `0`

　　Used to *set the number of offset units on the left side of the current column*.

**order:** *int*, default is `0`

　　Used to *set the order of the current column*.

**pull:** *int*, default is `0`

　　Used to *move the current column to the left by a certain number of units*.

**push:** *int*, default is `0`

　　Used to *move the current column to the right by a certain number of units*.

**flex:** *string* or *int*

　　For developers familiar with the `flex` layout in CSS, this parameter is equivalent to the `flex` parameter in CSS, allowing for more flexible customizations of column widths.

**xs, sm, md, lg, xl, xxl:** *int* or *dict*

　　Used for *configuring responsive layouts*. When passing an *int* value, it represents the `span` value at the corresponding breakpoint. When passing a *dict* value, you can set `span`, `offset`, `order`, `pull`, and `push` parameters for the corresponding breakpoint using key-value pairs.