- id (string; optional):
    Unique identifier for the component.

- affix (boolean; default True):
    Whether to enable the affix mode. Default value: `True`.

- align (a value equal to: 'left', 'right'; default 'right'):
    The position of the anchor point, with options `left` or `right`. Default value: `right`.

- aria-* (string; optional):
    Wildcard for `aria-*` formatted attributes.

- bounds (number; default 5):
    The pixel margin for the anchor point. Default value: `5`.

- className (string | dict; optional):
    The CSS class name for the current component, supporting [dynamic CSS class names](/advanced-classname).

- clickedLink (dict; optional):
    Listens for click events on the anchor point node.

- containerId (string; optional):
    The ID of the target container for the anchor point.

- data-* (string; optional):
    Wildcard for `data-*` formatted attributes.

- key (string; optional):
    Updates the `key` value for the current component, which can force a redraw of the component.

- linkDict (optional):
    Hierarchical data structure for the directory.

- loading_state (dict; optional):
    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is currently loading.

    - prop_name (string; optional):
        Holds which property is currently loading.

- offsetTop (number; optional):
    Sets the specified pixel offset from the top of the window to trigger the anchoring effect.

- style (dict; optional):
    The CSS styles for the current component.

- targetOffset (number; optional):
    The offset for the anchor point. Default is the same as the parameter offsetTop.
