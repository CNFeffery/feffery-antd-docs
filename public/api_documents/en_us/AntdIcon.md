- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- debounceWait (number; default 0):
    Debounce delay for the icon click event listener, in milliseconds. Default value: `0`.

- icon (string; optional):
    Name of the icon.

- key (string; optional):
    Updating the `key` value of the current component can force a redraw of the component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:
    - component_name (string; optional):
        Holds the name of the component that is loading.
    - is_loading (boolean; optional):
        Determines if the component is loading or not.
    - prop_name (string; optional):
        Holds which property is loading.

- nClicks (number; default 0):
    Number of times the icon has been clicked, used to monitor icon click behavior. Default value: `0`.

- style (dict; optional):
    CSS styles for the current component.
