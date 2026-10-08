- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- extra (a list of or a singular dash component, string or number; optional):
    Action area. Supports components.

- status (a value equal to: 'success', 'error', 'info', 'warning', '404', '403', '500', 'loading'; default 'info'):
    Status. Supported values: `'success'`, `'error'`, `'info'`, `'warning'`, `'404'`, `'403'`, `'500'`. Default: `'info'`.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- subTitle (a list of or a singular dash component, string or number; optional):
    Subtitle content. Supports components.

- icon (a list of or a singular dash component, string or number; optional):
    Icon content. Supports components.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
