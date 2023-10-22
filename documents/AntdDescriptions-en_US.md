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

**items:** `list[dict]` type

　　Used to *set the data-driven approach for nested description list items*. Each dictionary element represents an item, and the available key-value pairs are:

- **label:** *component*, used to *set the current sub-item's title content*.
- **span:** *int*, default is `1`, used to *set the number of width units allocated to the current sub-item*.
- **children:** *component*, used to *set the internal elements of the current sub-item*.
- **labelStyle:** *dict*, used to *set the CSS style for the current sub-item's label*.
- **contentStyle:** *dict*, used to *set the CSS style for the current sub-item's content container*.
- **style:** *dict*, used to *set the CSS style for the current sub-item*.
- **className:** *string*, used to *set the CSS class for the current sub-item*.

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