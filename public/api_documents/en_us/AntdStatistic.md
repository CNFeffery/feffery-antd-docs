- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- value (number | string | a list of or a singular dash component, string or number; optional):
    Value to display. Supports components.

- showGroupSeparator (boolean; default True):
    Whether numeric `value` uses thousands separators. Default: `True`.

- precision (number; optional):
    Precision of numeric `value`.

- prefix (a list of or a singular dash component, string or number; optional):
    Value prefix. Supports components.

- suffix (a list of or a singular dash component, string or number; optional):
    Value suffix. Supports components.

- title (a list of or a singular dash component, string or number; optional):
    Title content. Supports components.

- titleTooltip (string; optional):
    Additional tooltip for the title.

- valueStyle (dict; optional):
    CSS styles for the displayed value.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.
