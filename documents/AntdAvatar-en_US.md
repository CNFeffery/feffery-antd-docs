**id:** *string* or *dict*

　　Used to set the unique ID information of the current component.

**key:** *string*

　　Updates the `key` value of the current component, allowing for forced re-rendering of the component.

**style:** *dict*

　　Used to set the CSS style of the current component.

**className:** *string* or *dict*

　　Used to set the CSS class name of the current component, supports [dynamic CSS](/advanced-classname).

**mode:** *string*, default: `'icon'`

　　Used to set the mode of the current avatar. Available options are `'text'`, `'icon'`, `'image'`.

**gap:** *int*, default: `4`

　　When `mode="text"`, sets the pixel gap between the text inside the avatar and the left and right sides.

**text:** *string*

　　When `mode="text"`, sets the text content inside the avatar.

**icon:** *string*

　　When `mode="icon"`, sets the icon displayed inside the avatar, same as the corresponding parameter in `AntdIcon`.

**iconRenderer:** *string* type, defaulting to `'AntdIcon'`

　　Used to specify the *rendering method for setting prefix icons for the current node*. Available options include `'AntdIcon'` (built-in icons) and `'fontawesome'` (rendered based on CSS class names).

**alt:** *string*

　　When `mode="image"`, sets the placeholder text when the avatar image fails to load.

**src:** *string*

　　When `mode="image"`, sets the URL address of the avatar image.

**srcSet:** *string*

　　When `mode="image"`, sets the base64 format address of the avatar image as an alternative to `src`.

**draggable:** *bool*, default: `False`

　　When `mode="image"`, sets whether the profile picture is allowed to be dragged.

**crossOrigin:** *string*

　　When `mode="image"`, sets the CORS attribute for the profile picture. The available options are `'anonymous'`, `'use-credentials'`, `''`. `'anonymous'` indicates that cross-origin requests should not send credentials, `'use-credentials'` indicates that cross-origin requests should send credentials, `''` indicates that the cross-origin resource should not be returned and errors should be reported in the console instead of loading the cross-origin resource.

**size:** *int*, *string*, or *dict*, default: `'default'`

　　Used to set the size of the avatar. When an *int* value is provided, it sets the pixel size of the avatar. When a *string* value is provided, it selects from the preset sizes, with options `'small'`, `'default'`, `'large'`. When a *dict* value is provided, it sets the pixel sizes for different responsive breakpoints. Available responsive breakpoints are `'xs'`, `'sm'`, `'md'`, `'lg'`, `'xl'`, `'xxl'`.

**shape:** *string*, default: `'circle'`

　　Used to set the shape of the avatar. Available options are `'circle'`, `'square'`.