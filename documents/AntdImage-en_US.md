**id:** *string* or *dict* type

　　Used to set the unique ID information of the current component.

**key:** *string* type

　　Updates the `key` value of the current component, which allows for forcefully redrawing the current component.

**style:** *dict* type

　　Used to set the CSS style of the current component.

**className:** *string* or *dict* type

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**locale:** *string* type, default: `'zh-cn'`

　　Used to set the language for the functional text of the current component. Options are `'zh-cn'` (Simplified Chinese) and `'en-us'` (English).

**alt:** *string* type

　　Used to set the description text when the image fails to load.

**width:** *int* or *string* type

　　Used to set the width of the image.

**height:** *int* or *string* type

　　Used to set the height of the image.

**src:** *string* or *list* type

　　Used to set the URL address of the image. When passed as a *list*, it is treated as a combination of multiple images to be displayed.

**fallback:** *string* type

　　Used to set the placeholder image when the image fails to load. By default, it uses the built-in placeholder image.

**multiImageMode:** *string* type, default: `'fold'`

　　Used to set the specific form of displaying multiple images. Options are `'fold'` and `'unfold'`.

**preview:** *bool* type, default: `True`

　　Used to enable or disable the interactive preview functionality.