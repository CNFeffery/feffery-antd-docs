- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- message (a list of or a singular dash component, string or number; optional):
    Main message content.

- description (a list of or a singular dash component, string or number; optional):
    Additional hint content.

- type (a value equal to: 'success', 'info', 'warning', 'error'; default 'info'):
    Message type. Supported values: `'success'`, `'info'`, `'warning'`, `'error'`. Default: `'info'`.

- showIcon (boolean; default False):
    Whether to show an additional icon. Default: `False`.

- icon (a list of or a singular dash component, string or number; optional):
    Custom icon element when `showIcon=True`. Supports components.

- closable (boolean; default False):
    Whether the component can be closed. Default: `False`.

- messageRenderMode (a value equal to: 'default', 'loop-text', 'marquee'; default 'default'):
    Rendering mode. Supported values: `'default'`, `'loop-text'`, `'marquee'`. Default: `'default'`.

- action (a list of or a singular dash component, string or number; optional):
    Additional upper-right action area elements. Supports components.

- banner (boolean; default False):
    Whether to use the alert as a top banner. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
