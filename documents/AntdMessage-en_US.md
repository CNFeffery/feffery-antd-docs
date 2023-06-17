**id:** *string* or *dict*

　　Used to set the unique ID information for the current component.

**key:** *string*

　　Updates the `key` value of the current component, which can force the component to be redrawn.

**style:** *dict*

　　Used to set the CSS styles for the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name(s) for the current component, supports [dynamic CSS](/advanced-classname).

**content:** *string*

　　Used to set the text content inside the message prompt.

**type:** *string* (default: `'default'`)

　　Used to set the type of the message prompt. Available options are `'default'`, `'success'`, `'error'`, `'info'`, and `'warning'`.

**duration:** *int* or *float* (default: `3`)

　　Used to set the duration in seconds for the message prompt to display before automatically disappearing.

**top:** *int* (default: `8`)

　　Used to set the default distance in pixels of the message prompt from the top.

**maxCount:** *int*

　　Used to set the maximum number of message boxes allowed to be displayed simultaneously globally. By default, there is no limit.

**icon:** *string*

　　Used to customize the prefix icon for the message prompt, same as the corresponding parameter in `AntdIcon`.