- children (a list of or a singular dash component, string or number; optional):
    Component type, nested elements.

- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` format attributes.

- className (string | dict; optional):
    The CSS class name of the current component, supports [dynamic CSS class names](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` format attributes.

- flex (string | number; optional):
    The same as the flex in CSS.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- lg (dict; optional):
    Configures the layout parameters of the column when the page width is greater than or equal to 992px. When a numeric value is passed, it represents the span parameter. When a dictionary is passed, it sets the layout parameters individually.

    `lg` is a number | dict with keys:

    - offset (number; optional):
        The same as the offset parameter.

    - order (number; optional):
        The same as the order parameter.

    - pull (number; optional):
        The same as the pull parameter.

    - push (number; optional):
        The same as the push parameter.

    - span (number; optional):
        The same as the span parameter.

- loading_state (dict; optional):
    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- md (dict; optional):
    Configures the layout parameters of the column when the page width is greater than or equal to 768px. When a numeric value is passed, it represents the span parameter. When a dictionary is passed, it sets the layout parameters individually.

    `md` is a number | dict with keys:

    - offset (number; optional):
        The same as the offset parameter.

    - order (number; optional):
        The same as the order parameter.

    - pull (number; optional):
        The same as the pull parameter.

    - push (number; optional):
        The same as the push parameter.

    - span (number; optional):
        The same as the span parameter.

- offset (number; default 0):
    The number of fractions of the width of the gap to the left of the column. Default value: `0`.

- order (number; default 0):
    The order of the column. Default value: `0`.

- pull (number; default 0):
    The number of fractions of the width that the column moves to the left. Default value: `0`.

- push (number; default 0):
    The number of fractions of the width that the column moves to the right. Default value: `0`.

- sm (dict; optional):
    Configures the layout parameters of the column when the page width is greater than or equal to 567px. When a numeric value is passed, it represents the span parameter. When a dictionary is passed, it sets the layout parameters individually.

    `sm` is a number | dict with keys:

    - offset (number; optional):
        The same as the offset parameter.

    - order (number; optional):
        The same as the order parameter.

    - pull (number; optional):
        The same as the pull parameter.

    - push (number; optional):
        The same as the push parameter.

    - span (number; optional):
        The same as the span parameter.

- span (number; optional):
    The number of fractions of the width that the column occupies.

- style (dict; optional):
    The CSS style of the current component.

- xl (dict; optional):
    Configures the layout parameters of the column when the page width is greater than or equal to 1200px. When a numeric value is passed, it represents the span parameter. When a dictionary is passed, it sets the layout parameters individually.

    `xl` is a number | dict with keys:

    - offset (number; optional):
        The same as the offset parameter.

    - order (number; optional):
        The same as the order parameter.

    - pull (number; optional):
        The same as the pull parameter.

    - push (number; optional):
        The same as the push parameter.

    - span (number; optional):
        The same as the span parameter.

- xs (dict; optional):
    Configures the layout parameters of the column when the page width is less than 567px. When a numeric value is passed, it represents the span parameter. When a dictionary is passed, it sets the layout parameters individually.

    `xs` is a number | dict with keys:

    - offset (number; optional):
        The same as the offset parameter.

    - order (number; optional):
        The same as the order parameter.

    - pull (number; optional):
        The same as the pull parameter.

    - push (number; optional):
        The same as the push parameter.

    - span (number; optional):
        The same as the span parameter.

- xxl (dict; optional):
    Configures the layout parameters of the column when the page width is greater than or equal to 1600px. When a numeric value is passed, it represents the span parameter. When a dictionary is passed, it sets the layout parameters individually.

    `xxl` is a number | dict with keys:

    - offset (number; optional):
        The same as the offset parameter.

    - order (number; optional):
        The same as the order parameter.

    - pull (number; optional):
        The same as the pull parameter.

    - push (number; optional):
        The same as the push parameter.

    - span (number; optional):
        The same as the span parameter.
