**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**message:** *component type*

　　Used to set the main information content for the current alert message.

**description:** *component type*

　　Used to set the secondary information content for the current alert message.

**type:** *string*, default: `'info'`

　　Used to set the status type for the current alert message, with options `'success'`, `'info'`, `'warning'`, `'error'`.

**showIcon:** *bool*, default: `False`

　　Used to set whether to add a status icon to the current alert message.

**closable:** *bool*, default: `False`

　　Used to set whether the current alert message can be closed.

**messageRenderMode:** *string*, default: `'default'`

　　Used to set the rendering mode for the current alert message, with options `'default'`, `'loop-text'`, `'marquee'`. For `'loop-text'` mode, the `message` parameter should be in an array format.

**action:** *component type*

　　Used to set additional content for the top right corner of the current alert message.

**banner:** *component type*, default: `False`

　　Used to enable or disable the top banner mode.