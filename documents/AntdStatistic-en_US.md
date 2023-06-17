**id:** *string* or *dict* type

　　Used to set the unique id information for the current component.

**key:** *string* type

　　Updates the `key` value of the current component to force a re-rendering effect.

**style:** *dict* type

　　Used to set the CSS style for the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**value:** *int*, *float*, or *component type*

　　Used to set the value to be displayed, can also directly pass other elements as content. Typical use cases include passing `fuc.FefferyCountUp()` to achieve a number increment animation.

**showGroupSeparator:** *bool* type, default: `True`

　　Used to set whether to display thousands separator for numeric `value` input.

**precision:** *int* type

　　Used to set the precision limit for numeric `value` input.

**prefix:** *component type*

　　Used to add a prefix content to the numeric value.

**suffix:** *component type*

　　Used to add a suffix content to the numeric value.

**title:** *component type*

　　Used to set the title content.

**titleTooltip:** *string* type

　　Used to set the tooltip information for the title suffix.

**valueStyle:** *dict* type

　　Used to set the CSS style for the value information.