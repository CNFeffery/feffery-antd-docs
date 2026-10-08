- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- icon (a list of or a singular dash component, string or number; optional):
    Component type, prefix icon element nested within the button.

- description (a list of or a singular dash component, string or number; optional):
    Component type, nested element within the button, available only when `shape='square'`.

- tooltip (dict; optional):
    Component type, additional tooltip content for the button.

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
    Shape of the button, options include `'circle'`, `'square'`. Default value: `'circle'`.

- href (string; optional):
    URL to redirect to when the button is clicked.

- target (string; default '_blank'):
    Method of opening the link when the button is clicked. Default value: `'_blank'`.

- nClicks (number; default 0):
    Number of times the button has been clicked, used to monitor button click behavior. Default value: `0`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
