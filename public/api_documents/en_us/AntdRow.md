- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- align (a value equal to: 'top', 'middle', 'bottom'; default 'top'):
    Vertical alignment method, options include `'top'`, `'middle'`, `'bottom'`. Default value: `'top'`.

- gutter (dict; default 0):
    `gutter` is a number | list of numbers | dict with keys:

    `gutter` is a number | list of numbers | dict with keys:

    - xs (number; optional):
        Horizontal pixel spacing when the page width is less than 567px.

    - sm (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 567px.

    - md (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 768px.

    - lg (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 992px.

    - xl (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 1200px.

    - xxl (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 1600px.

- justify (a value equal to: 'start', 'end', 'center', 'space-around', 'space-between'; default 'start'):
    Horizontal arrangement method, options include `'start'`, `'end'`, `'center'`, `'space-around'`, `'space-between'`. Default value: `'start'`.

- wrap (boolean; default True):
    Whether to allow automatic line wrapping. Default value: `True`.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
