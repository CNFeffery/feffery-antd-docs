- children (a list of or a singular dash component, string or number; optional):
    Component type, nested elements.

- id (string; optional):
    Unique ID for the component.

- align (a value equal to: 'top', 'middle', 'bottom'; default 'top'):
    Vertical alignment method, options include `'top'`, `'middle'`, `'bottom'`. Default value: `'top'`.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS class names](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- gutter (dict; default 0):
    Grid spacing, when passing a numeric value, it represents the horizontal pixel spacing. When passing an array, it sets the horizontal and vertical pixel spacing respectively. When passing a dictionary, you can set the horizontal pixel spacing for responsive breakpoints.

    `gutter` is a number | list of numbers | dict with keys:

    - lg (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 992px.

    - md (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 768px.

    - sm (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 567px.

    - xl (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 1200px.

    - xs (number; optional):
        Horizontal pixel spacing when the page width is less than 567px.

    - xxl (number; optional):
        Horizontal pixel spacing when the page width is greater than or equal to 1600px.

- justify (a value equal to: 'start', 'end', 'center', 'space-around', 'space-between'; default 'start'):
    Horizontal arrangement method, options include `'start'`, `'end'`, `'center'`, `'space-around'`, `'space-between'`.
    Default value: `'start'`.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- loading_state (dict; optional):

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    CSS styles for the current component.

- wrap (boolean; default True):
    Whether to allow automatic line wrapping. Default value: `True`.
