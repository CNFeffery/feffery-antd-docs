- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    `AntdImage` components nested in the image group.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- locale (a value equal to: 'zh-cn', 'en-us', 'de-de', 'ru-ru', 'fr-fr'; default 'zh-cn'):
    Component language: `'zh-cn'` (Simplified Chinese), `'en-us'` (English), `'de-de'` (German), `'fr-fr'` (French), or `'ru-ru'` (Russian). Default: `'zh-cn'`.

- items (list of strings; optional):
    Array of image resource URLs displayed by the image group, in order.

- fallback (string; optional):
    Fallback image URL used when loading fails.

- preview (dict; default True):
    Image preview settings. Set to `False` to disable preview. Default: `True`.

    `preview` is a boolean | dict with keys:

    - src (string; optional):
        Custom preview image URL.

    - movable (boolean; optional):
        Whether the image can be moved in preview mode.

    - mask (a list of or a singular dash component, string or number; optional):
        Custom thumbnail mask element. Supports components.

    - maskClassName (string; optional):
        CSS class name for the thumbnail mask.

    - rootClassName (string; optional):
        CSS class name for the thumbnail root.

    - scaleStep (number; optional):
        Each zoom step multiplies the scale by `1+scaleStep`. Default: `0.5`.

    - minScale (number; optional):
        Minimum zoom factor. Default: `1`.

    - maxScale (number; optional):
        Maximum zoom factor. Default: `50`.

- visible (boolean; optional):
    Monitor or set whether the image group is in fullscreen preview mode.

- current (number; optional):
    Monitor or control the index of the image currently shown in the preview.

- disableCurrent (boolean; default True):
    Whether to disable controlled image indexing through `current`. Default: `True`.

- toolbarExtra (a list of or a singular dash component, string or number; optional):
    Custom tool icons appended to the image preview toolbar.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
