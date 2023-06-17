**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, enabling forced re-rendering of the component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component* type

　　Used to pass in nested description list items.

**title:** *component* type

　　Used to set the title content for the current description list.

**column:** *int* or *dict* type, default: `3`

　　Used to set the unit width of each row in the current description list. When passing a *dict* type input, it is used to set the unit width for different responsive breakpoints. Available responsive breakpoints are `'xs'`, `'sm'`, `'md'`, `'lg'`, `'xl'`, `'xxl'`.

**bordered:** *bool* type, default: `False`

　　Used to set whether to render borders.

**size:** *string* type, default: `'default'`

　　Used to set the size specification of the current component. Available options are `'small'`, `'default'`, and `'large'`.

**layout:** *string* type, default: `'horizontal'`

　　Used to set the layout of the current description list. Available options are `'horizontal'` and `'vertical'`.

**labelStyle:** *dict* type

　　Used to set the CSS style for the titles of each description list item.

**contentStyle:** *dict* type

　　Used to set the CSS style for the content area of each description list item.