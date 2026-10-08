- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- items (list of dicts; required):
    Required. Timeline node definitions.

    `items` is a list of dicts with keys:

    - content (a list of or a singular dash component, string or number; optional):
        Node body content. Supports components.

    - color (string; optional):
        Node color. Common choices: `'blue'` for current/default, `'green'` for completed, `'red'` for warning/error, and `'grey'` for incomplete/inactive.

    - icon (a list of or a singular dash component, string or number; optional):
        Custom icon element. Supports components.

    - label (a list of or a singular dash component, string or number; optional):
        Node label content. Supports components.

    - position (a value equal to: 'left', 'right'; optional):
        Node position. Supported values: `'left'`, `'right'`.

- mode (a value equal to: 'left', 'alternate', 'right'; default 'left'):
    Position of the timeline relative to its content. Supported values: `'left'`, `'alternate'`, `'right'`.

- pending (a list of or a singular dash component, string or number; optional):
    Title of an additional pending node at the end of the timeline. Supports components; no pending node by default.

- pendingDot (a list of or a singular dash component, string or number; optional):
    Custom pending node icon. Supports components.

- reverse (boolean; default False):
    Whether timeline items appear in reverse order. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
