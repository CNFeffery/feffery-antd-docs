- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- id (string; optional):
    Unique ID for the component.

- aria-* (string; optional):
    Wildcard for attributes in the `aria-*` format.

- backClicks (number; default 0):
    Number of times the back button has been clicked, used to monitor the behavior of back button clicks. Default value: `0`.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS class names](/advanced-classname).

- data-* (string; optional):
    Wildcard for attributes in the `data-*` format.

- ghost (boolean; default False):
    Whether to enable the transparent background mode. Default value: `False`.

- historyBackDisabled (boolean; default False):
    Whether to disable the function of going back to the previous address by clicking the back button. Default value: `False`.

- key (string; optional):
    Update the `key` value of the current component to force a redraw of the current component.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- showBackIcon (boolean; default True):
    Whether to render the back button. Default value: `True`.

- style (dict; optional):
    The CSS style for the current component.

- subTitle (a list of or a singular dash component, string or number; optional):
    Component type, content for the page header subtitle.

- title (a list of or a singular dash component, string or number; optional):
    Component type, content for the page header title.
