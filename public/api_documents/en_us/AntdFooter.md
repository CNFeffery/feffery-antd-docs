- children (a list of or a singular dash component, string or number; optional):
    Component type for embedded elements.

- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- className (string | dict; optional):
    CSS class name for the current component, supporting [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- key (string; optional):
    Updates the `key` value of the current component to force a re-render.

- loading_state (dict; optional):
    The `loading_state` is a dictionary with the following keys:
    - component_name (string; optional):
        Holds the name of the component that is loading.
    - is_loading (boolean; optional):
        Determines whether the component is currently loading.
    - prop_name (string; optional):
        Indicates which property is currently loading.

- style (dict; optional):
    CSS styles for the current component.
