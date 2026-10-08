- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- vertical (boolean; default False):
    Whether to use a vertical main axis. Default value: `False`.

- wrap (string | boolean; default 'nowrap'):
    Behavior of child element wrapping, equivalent to the CSS `flex-wrap` property, or can directly pass a boolean value to set whether to wrap automatically. Default value: `'nowrap'`.

- justify (string; default 'normal'):
    Alignment of child elements in the main axis, equivalent to the CSS `justify-content` property. Default value: `'normal'`.

- align (string; default 'normal'):
    Alignment of child elements in the cross axis, equivalent to the CSS `align-items` property. Default value: `'normal'`.

- flex (string; default 'normal'):
    Equivalent to the CSS `flex` property. Default value: `'normal'`.

- gap (string | number | a value equal to: 'small', 'middle', 'large'; optional):
    Spacing between child elements, options include `'small'`, `'middle'`, `'large'`, or a string CSS width, or a numeric pixel width.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
