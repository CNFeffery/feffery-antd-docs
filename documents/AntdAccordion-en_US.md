**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**items:** `list[dict]`

　　Used to define the current accordion list, where each dictionary can have the following key-value parameters:

- **children:** *component type*, used to set the inner elements of the current accordion item.
- **className:** *string* or *dict*, used to set the CSS class name of the current accordion item, supports [dynamic CSS](/advanced-classname).
- **style:** *dict*, used to set the CSS style of the current accordion item.
- **key:** *int* or *string*, required, used to set the unique identifier for the current accordion item.
- **collapsible:** *string*, used to set the collapse trigger mode of the current accordion item, with options `'header'` and `'disabled'`.
- **title:** *component type*, used to set the title content of the current accordion item.
- **extra:** *component type*, used to set additional content for the current accordion item.
- **showArrow:** *bool*, default: `True`, used to set whether to display the arrow icon for the current accordion item.
- **forceRender:** *bool*, default: `False`, used to set whether to force render the inner elements during initialization.

**accordion:** *bool*, default: `True`

　　Used to enable or disable the accordion mode.

**activeKey:** *int*, *string*, or *list*

　　Used to set or listen to the key value of the currently expanded accordion item.

**defaultActiveKey:** *int*, *string*, or *list*

　　Used to set the key value of the accordion item that is initially expanded.

**bordered:** *bool*, default: `True`

　　Used to set whether to render borders for the current accordion.

**collapsible:** *string*

　　Used to set the collapse trigger mode for all accordion items, with options `'header'`, `'disabled'`, `'icon'`.

**expandIconPosition:** *string*, default: `'left'`

　　Used to set the position of the collapse icon, with options `'left'` or `'right'`.

**ghost:** *bool*, default: `False`

　　Used to enable or disable the transparent panel mode.