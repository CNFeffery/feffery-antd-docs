**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in multiple nested avatars.

**maxCount:** *int*

　　Used to set the maximum number of avatars to be displayed. The exceeding avatars will be omitted. By default, there is no limit.

**maxPopoverPlacement:** *string*, default: `'top'`

　　Used to set the placement of the popover card for the omitted avatars. Available options are `'top'`, `'bottom'`.

**maxPopoverTrigger:** *string*, default: `'hover'`

　　Used to set the triggering action for the popover card of the omitted avatars. Available options are `'hover'`, `'click'`.

**maxStyle:** *dict*

　　Used to set the CSS style of the omitted avatars.

**size:** *int*, *string*, or *dict*, default: `'default'`

　　Used to uniformly set the size of the nested avatars. When an *int* value is provided, it sets the pixel size of the avatars. When a *string* value is provided, it selects from the preset sizes, with options `'small'`, `'default'`, `'large'`. When a *dict* value is provided, it sets the pixel sizes for different responsive breakpoints. Available responsive breakpoints are `'xs'`, `'sm'`, `'md'`, `'lg'`, `'xl'`, `'xxl'`.