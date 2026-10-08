- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Floating buttons contained in this group.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- icon (a list of or a singular dash component, string or number; optional):
    Icon component.

- description (a list of or a singular dash component, string or number; optional):
    Description content.

- tooltip (dict; optional):
    Popover content.

    `tooltip` is a list of or a singular dash component, string or
    number | dict with keys:

    - title (a list of or a singular dash component, string or number; optional):
        Popover content.

    - color (string; optional):
        Popover background color.

    - placement (a value equal to: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight', 'leftTop', 'leftBottom', 'rightTop', 'rightBottom'; optional):
        Popover placement. Supported values: `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, `'bottomRight'`, `'leftTop'`, `'leftBottom'`, `'rightTop'`, `'rightBottom'`.

- type (a value equal to: 'default', 'primary'; default 'default'):
    Type of the button, options include `'default'`, `'primary'`. Default value: `'default'`.

- shape (a value equal to: 'circle', 'square'; default 'circle'):
    Shape of the nested floating buttons. Supported values: `'circle'`, `'square'`. Default: `'circle'`.

- trigger (a value equal to: 'click', 'hover'; optional):
    Trigger for expanding the menu. Supported values: `'click'`, `'hover'`.

- placement (a value equal to: 'top', 'right', 'bottom', 'left'; optional):
    Menu placement. Supported values: `'top'`, `'right'`, `'bottom'`, `'left'`.

- open (boolean; optional):
    Set or monitor whether the floating button group is expanded.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
