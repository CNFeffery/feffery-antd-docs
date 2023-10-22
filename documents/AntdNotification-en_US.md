**id:** *string* or *dict*

　　Used to set the unique id information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, which can force a re-render of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**message:** *string*

　　Used to set the main information content of the current notification.

**description:** *string*

　　Used to set the secondary information content of the current notification.

**type:** *string* (default: `'default'`)

　　Used to set the status type of the current notification. Available options are `'default'`, `'success'`, `'error'`, `'info'`, `'warning'`.

**placement:** *string* (default: `'topRight'`)

　　Used to set the popup position of the current notification. Available options are `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`.

**top:** *int* (default: `24`)

　　Used to set the pixel distance from the top when the notification pops up from the top of the page.

**bottom:** *int* (default: `24`)

　　Used to set the pixel distance from the bottom when the notification pops up from the bottom of the page.

**duration:** *int* or *float* (default: `4.5`)

　　Used to set the delay duration in seconds for the current notification from display to disappearance.

**closable:** *bool* (default: `True`)

　　Used to add a close button to the current notification.