- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- active (boolean; default False):
    Whether to show animation. Default: `False`.

- shape (a value equal to: 'circle', 'square'; default 'circle'):
    Avatar placeholder shape. Supported values: `'circle'`, `'square'`. Default: `'circle'`.

- size (number | a value equal to: 'large', 'small', 'default'; default 'default'):
    Avatar placeholder size. Use a number for pixels or a preset size. Supported values: `'large'`, `'small'`, `'default'`. Default: `'default'`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
