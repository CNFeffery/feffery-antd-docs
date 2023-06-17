**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supporting [dynamic CSS](/advanced-classname).

**children:** *component type*

　　Used to pass in nested child elements.

**direction:** *string*, default: `'horizontal'`

　　Used to set the arrangement direction of internal elements. Options include `'vertical'` (vertical arrangement) and `'horizontal'` (horizontal arrangement).

**block:** *bool*, default: `False`

　　Used to determine whether the component stretches to fill the width of its parent container.