- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- mode (a value equal to: 'text', 'icon', 'image'; default 'icon'):
    Avatar rendering mode. Supported values: `'text'`, `'icon'`, `'image'`. Default: `'icon'`.

- gap (number; default 4):
    Gap in pixels between the text and the left/right edges when `mode='text'`. Default: `4`.

- text (string; optional):
    Text content when `mode='text'`.

- icon (string; optional):
    Icon name when `mode='icon'`, equivalent to the **AntdIcon** `icon` property.

- iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; default 'AntdIcon'):
    Icon renderer when `mode='icon'`. Supported values: `'AntdIcon'`, `'fontawesome'`.

- alt (string; optional):
    Fallback text when an image cannot be displayed in `mode='image'`.

- src (string; optional):
    Image URL when `mode='image'`.

- srcSet (string; optional):
    Base64 image URL when `mode='image'`.

- draggable (boolean | a value equal to: 'true', 'false'; optional):
    Whether the image can be dragged when `mode='image'`.

- crossOrigin (a value equal to: 'anonymous', 'use-credentials', ''; optional):
    Image CORS setting when `mode='image'`. Supported values: `'anonymous'`, `'use-credentials'`, `''`.

- size (dict; optional):
    Avatar size. Use a number for pixels, including responsive settings, or a preset size. Supported values: `'large'`, `'small'`, `'default'`.

    `size` is a number | a value equal to: 'large', 'small', 'default'
    | dict with keys:

    - xs (number; optional)

    - sm (number; optional)

    - md (number; optional)

    - lg (number; optional)

    - xl (number; optional)

    - xxl (number; optional)

- shape (a value equal to: 'circle', 'square'; default 'circle'):
    Avatar shape. Supported values: `'circle'`, `'square'`. Default: `'circle'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
