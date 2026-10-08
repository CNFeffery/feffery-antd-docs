- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- direction (a value equal to: 'vertical', 'horizontal'; default 'horizontal'):
    Direction of arrangement, options include `'vertical'`, `'horizontal'`. Default value: `'horizontal'`.

- block (boolean; default False):
    Whether to render as a block-level element (width fills the parent container) Default value: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
