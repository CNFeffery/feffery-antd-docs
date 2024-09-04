- children (a list of or a singular dash component, string or number; optional):
    Component type, child elements.

- id (string; optional):
    Unique identifier for the component.

- align (string; default 'normal'):
    Alignment of child elements in the cross axis, equivalent to the CSS `align-items` property. Default value: `'normal'`.

- aria-* (string; optional):
    Wildcard for `aria-*` formatted attributes.

- className (string | dict; optional):
    Current component CSS class name, supports [dynamic CSS](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` formatted attributes.

- flex (string; default 'normal'):
    Equivalent to the CSS `flex` property. Default value: `'normal'`.

- gap (string | number | a value equal to: 'small', 'middle', 'large'; optional):
    Spacing between child elements, options include `'small'`, `'middle'`, `'large'`, or a string CSS width, or a numeric pixel width.

- justify (string; default 'normal'):
    Alignment of child elements in the main axis, equivalent to the CSS `justify-content` property. Default value: `'normal'`.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

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

- vertical (boolean; default False):
    Whether to use a vertical main axis. Default value: `False`.

- wrap (string | boolean; default 'nowrap'):
    Behavior of child element wrapping, equivalent to the CSS `flex-wrap` property, or can directly pass a boolean value to set whether to wrap automatically. Default value: `'nowrap'`.
