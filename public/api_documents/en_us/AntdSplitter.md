- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    The layout direction, options include `'horizontal'`, `'vertical'`. Default value: `'horizontal'`.

- items (list of dicts; required):
    `items` is a list of dictionaries with keys:

    `items` is a list of dicts with keys:

    - key (string; optional):
        Unique child item `key`.

    - children (a list of or a singular dash component, string or number; optional):
        Component type, embedded elements.

    - style (dict; optional):
        `css` styles for this child item.

    - className (string; optional):
        `css` class name for this child item.

    - defaultSize (number

            Or string; optional): Initial panel size, specified in pixels (`px`) or as a percentage.

    - size (number | string; optional):
        Panel size, specified in `px` or as a `'百分比%'` percentage.

    - min (number | string; optional):
        Minimum size, specified in `px` or as a `'百分比%'` percentage.

    - max (number | string; optional):
        Maximum size, specified in `px` or as a `'百分比%'` percentage.

    - collapsible (dict; optional):
        Whether the component can be collapsed. Default: `False`.

        `collapsible` is a boolean | dict with keys:

        - start (boolean; optional)

        - end (boolean; optional)

    - resizable (boolean; optional):
        Whether to enable drag-to-resize. Default value: `True`.

- lazy (boolean; default False):
    Whether panel rendering is deferred until dragging finishes. Default: `False`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
