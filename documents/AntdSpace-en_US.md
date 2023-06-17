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

**align:** *string* type

　　Used to set the alignment of nested internal elements. Available options are `'start'`, `'end'`, `'center'`, `'baseline'`.

**direction:** *string* type, default: `'horizontal'`

　　Used to set the arrangement direction of internal elements. Available options are `'vertical'` (vertical arrangement) and `'horizontal'` (horizontal arrangement).

**size:** *string* or *int* type, default: `'small'`

　　Used to set the spacing size between internal elements. Available options are `'small'`, `'middle'`, `'large'`, or an *int* value representing the pixel unit spacing.

**customSplit:** *component type*

　　Used to customize the split element.

**addSplitLine:** *bool* type, default: `False`

　　Used to determine whether to add a split line between the internal elements. This option ignores the settings of `customSplit`.

**wrap:** *bool* type, default: `False`

　　Only available in **horizontal arrangement mode**. Determines whether to wrap the internal horizontally arranged elements when they overflow their width.