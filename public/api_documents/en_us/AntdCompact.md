- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- id (string; optional):
    Unique ID for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- block (boolean; default False):
    Whether to render as a block-level element (width fills the parent container) Default value: `False`.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS class names](/advanced-classname).

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- direction (a value equal to: 'vertical', 'horizontal'; default 'horizontal'):
    Direction of arrangement, options include `'vertical'`, `'horizontal'`. Default value: `'horizontal'`.

- key (string; optional):
    Updates the `key` value for the current component, which can force a redraw of the current component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is currently loading.

    - prop_name (string; optional):
        Holds which property is being loaded.

- style (dict; optional):
    The CSS styles for the current component.
