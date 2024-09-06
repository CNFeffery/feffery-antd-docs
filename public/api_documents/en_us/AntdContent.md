- children (a list of or a singular dash component, string or number; optional):
    Component type, for nested elements.

- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` attribute format.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` attribute format.

- key (string; optional):
    Updates the `key` value for the current component, which can force a re-render of the component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with the following keys:

    - component_name (string; optional):
        Holds the name of the component that is currently loading.

    - is_loading (boolean; optional):
        Indicates whether the component is in a loading state.

    - prop_name (string; optional):
        Specifies which property is currently loading.

- style (dict; optional):
    CSS styles for the current component.
