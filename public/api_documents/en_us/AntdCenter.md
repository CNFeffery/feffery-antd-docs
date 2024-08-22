- children (a list of or a singular dash component, string or number; optional):
    Component type, nested elements.

- id (string; optional):
    Unique ID for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS class names](/advanced-classname).

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- inline (boolean; default False):
    Whether to render as an inline element. Default value: `False`.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- style (dict; optional):
    CSS styles for the current component.
