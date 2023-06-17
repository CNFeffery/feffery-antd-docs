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

**title:** *component type*

　　Used to set the content of the title part for the current card.

**extraLink:** *dict*

　　Used to configure additional link-related features in the top-right corner of the card. Available key-value parameters are:

- **content:** *string* type, used to set the link text content.
- **href:** *string* type, used to set the link address.
- **target:** *string*, default: `'_blank'`, used to set the link behavior.
- **className:** *string*, used to set the CSS class name of the link.
- **style:** *dict*, used to set the CSS style of the link.

**coverImg:** *dict*

　　Used to configure the card's cover image-related features. Available key-value parameters are:

- **src:** *string* type, used to set the address of the cover image.
- **alt:** *string* type, used as placeholder text when the cover image fails to load.
- **className:** *string*, used to set the CSS class name of the cover image.
- **style:** *dict*, used to set the CSS style of the cover image.

**bodyStyle:** *dict*

　　Used to set the CSS style of the card's content area.

**headStyle:** *dict*

　　Used to set the CSS style of the card's title area.

**bordered:** *bool*, default: `True`

　　Used to determine whether to render a border for the current card.

**hoverable:** *bool*, default: `False`

　　Used to enable mouse hover shadow effect for the current card.

**size:** *string*, default: `'default'`

　　Used to set the size specification of the current card. Available options are `'default'` and `'small'`.