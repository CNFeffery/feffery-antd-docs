- children (a list of or a singular dash component, string or number; optional):
    Component type, embedded elements.

- id (string; optional):
    Unique ID for the component.

- addSplitLine (boolean; default False):
    Whether to add a separator line. Default value: `False`.

- align (a value equal to: 'start', 'end', 'center', 'baseline'; optional):
    Alignment method, with options `start`, `end`, `center`, `baseline`.

- aria-* (string; optional):
    Wildcard for `aria-*` attribute format.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS class names](/advanced-classname).

- classNames (dict; optional):
    Fine-grained control over the CSS classes of child elements.

    `classNames` is a dict with keys:

    - item (string; optional):
        CSS class for the child item container element.

- customSplit (a list of or a singular dash component, string or number; optional):
    Custom separator line element.

- data-* (string; optional):
    Wildcard for `data-*` attribute format.

- direction (a value equal to: 'vertical', 'horizontal'; default 'horizontal'):
    Layout direction, with options `vertical`, `horizontal`. Default value: `horizontal`.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- loading_state (dict; optional):

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is currently loading.

    - prop_name (string; optional):
        Holds which property is currently loading.

- size (a value equal to: 'small', 'middle', 'large' | number; default 'small'):
    Spacing between child elements, with options `small`, `middle`, `large`, or a numeric value representing pixel spacing.
    Default value: `small`.

- style (dict; optional):
    The CSS style for the current component.

- styles (dict; optional):
    Fine-grained control over the CSS styles of child elements.

    `styles` is a dict with keys:

    - item (dict; optional):
        CSS style for the child item container element.

- wrap (boolean; default False):
    Whether child elements automatically wrap to the next line, only effective when `direction='horizontal'`. Default value: `False`.
