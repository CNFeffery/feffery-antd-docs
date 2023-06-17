**id:** *string* or *dict* type

　　Used to set the *unique id information* for the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which can force a redraw of the current component.

**style:** *dict* type

　　Used to set the *CSS styles* for the current component.

**className:** *string* or *dict* type

　　Used to set the *CSS class names* for the current component, supports [dynamic CSS](/advanced-classname).

**breakpoints:** `list[int]` type, required

　　Used to *set or listen to the breakpoints* for each segment.

**colors:** `list[string]` type, required

　　Used to *set the color values corresponding to each breakpoint*, the length of the `colors` array should be `len(breakpoints) - 1`.

**controls:** *bool* type, default is `True`

　　Used to *set whether to add auxiliary increment/decrement buttons inside each number input box*.

**keyboard:** *bool* type, default is `True`

　　Used to *set whether to allow adjusting the values of each number input box using the up and down keys on the keyboard*.

**min:** *int*, *float*, or *string* type

　　Used to *set the minimum valid value* for the number input box, with no limit by default.

**max:** *int*, *float*, or *string* type

　　Used to *set the maximum valid value* for the number input box, with no limit by default.

**step:** *int*, *float*, or *string* type

　　Used to *set the increment/decrement step* for the number input box.

**precision:** *int* type

　　Used to *set the precision* (number of decimal places) for the number input box.

**disabled:** *bool* type, default is `False`

　　Used to *set whether the current component is disabled*.

**size:** *string* type, default is `'middle'`

　　Used to *set the size specification* for the current component. Available options are `'small'`, `'middle'`, `'large'`.

**bordered:** *bool* type, default is `True`

　　Used to *set whether to render a border*.

**placeholder:** *string* type

　　Used to *set the placeholder text* for all input boxes.

**readOnly:** *bool* type

　　Used to *set whether to display in read-only mode*.

**pureLegend:** *bool* type, default is `False`

　　Used to *enable pure legend mode*.

**inputNumberStyle:** *dict* type

　　Used to *set CSS styles* for the number input box.

**colorBlockStyle:** *dict* type

　　Used to *set CSS styles* for the color block.

**colorBlockPosition:** *string* type

　　Used to *set the position of the color block relative to the number input box*. Available options are `'left'` and `'right'`.

**pureLegendLabelStyle:** *dict* type

　　When `pureLegend=True`, used to *set the CSS styles* for the legend text.