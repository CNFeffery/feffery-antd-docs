- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` formatted attributes.

- className (string | dict; optional):
    CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` formatted attributes.

- description (a list of or a singular dash component, string or number; optional):
    Component type, nested element within the button, available only when `shape='square'`.

- href (string; optional):
    URL to redirect to when the button is clicked.

- icon (a list of or a singular dash component, string or number; optional):
    Component type, prefix icon element nested within the button.

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
    Number of times the button has been clicked, used to monitor button click behavior. Default value: `0`.

- shape (a value equal to: 'circle', 'square'; default 'circle'):
    Shape of the button, options include `'circle'`, `'square'`. Default value: `'circle'`.

- style (dict; optional):
    CSS styles for the current component.

- target (string; default '_blank'):
    Method of opening the link when the button is clicked. Default value: `'_blank'`.

- tooltip (a list of or a singular dash component, string or number; optional):
    Component type, additional tooltip content for the button.

- type (a value equal to: 'default', 'primary'; default 'default'):
    Type of the button, options include `'default'`, `'primary'`. Default value: `'default'`.
