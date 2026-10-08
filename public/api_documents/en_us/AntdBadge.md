- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Target element for the badge. Supports components.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- styles (dict; optional):
    Fine-grained CSS styles for child elements.

    `styles` is a dict with keys:

    - root (dict; optional):
        CSS styles for the root element.

    - indicator (dict; optional):
        CSS styles for the badge element.

- classNames (dict; optional):
    Fine-grained control over the CSS classes of child elements.

    `classNames` is a dict with keys:

    - root (string; optional):
        CSS class name for the root element.

    - indicator (string; optional):
        CSS class name for the badge element.

- color (string; optional):
    Badge color.

- count (number; optional):
    Number shown in the badge.

- dot (boolean; default False):
    Whether to show a dot instead of a number. Default: `False`.

- showZero (boolean; default False):
    Whether to show the badge number when `count=0`. Default: `False`.

- overflowCount (number; default 99):
    Maximum displayed badge number. Larger values show a `+` suffix. Default: `99`.

- offset (list of numbers; optional):
    Badge offset in pixels, in the form `[水平偏移, 竖直偏移]` (horizontal and vertical offsets).

- status (a value equal to: 'success', 'processing', 'default', 'error', 'warning'; optional):
    Badge status. Supported values: `'success'`, `'processing'`, `'default'`, `'error'`, `'warning'`.

- text (string; optional):
    Badge text when the `status` property is set.

- title (string; optional):
    Badge hover tooltip text.

- size (a value equal to: 'default', 'small'; default 'default'):
    Badge size. Supported values: `'default'`, `'small'`.

- nClicks (number; default 0):
    Cumulative number of badge clicks. Default: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
