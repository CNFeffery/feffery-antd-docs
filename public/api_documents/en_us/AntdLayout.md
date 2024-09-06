- children (a list of or a singular dash component, string or number; optional):
    Component type, for embedded elements.

- id (string; optional):
    The unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` attribute format.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` attribute format.

- key (string; optional):
    Updates the `key` value of the current component, which can force a re-rendering of the component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with the following keys:

    - component_name (string; optional):
        Holds the name of the component that is currently loading.

    - is_loading (boolean; optional):
        Indicates whether the component is in a loading state or not.

    - prop_name (string; optional):
        Indicates which property of the component is currently loading.

- style (dict; optional):
    The CSS styles for the current component.
