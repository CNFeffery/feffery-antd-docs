- children (a list of or a singular dash component, string or number; optional):
    Component type, child elements within the divider.

- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` formatted attributes.

- className (string | dict; optional):
    Current component CSS class name, supports [dynamic CSS class names](/advanced-classname).

- data-* (string; optional):
    Wildcard for `data-*` formatted attributes.

- direction (a value equal to: "horizontal", "vertical"; default 'horizontal'):
    Direction of the divider, options include `'horizontal'`, `'vertical'`. Default value: `'horizontal'`.

- fontColor (string; optional):
    Font color of the child elements.

- fontFamily (string; optional):
    Font of the child elements.

- fontSize (string | number; optional):
    Font size of the child elements.

- fontStyle (string; optional):
    Font style of the child elements.

- fontWeight (string; optional):
    Font weight of the child elements.

- innerTextOrientation (a value equal to: "left", "center", "right"; default 'center'):
    Alignment of the child elements, options include `'left'`, `'center'`, `'right'`. Default value: `'center'`.

- isDashed (boolean; default False):
    Whether to render as a dashed line. Default value: `False`.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- lineColor (string; optional):
    Color of the divider line.

- loading_state (dict; optional):

    `loading_state` is a dictionary with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is currently loading.

    - prop_name (string; optional):
        Holds which property is currently loading.

- style (dict; optional):
    CSS styles for the current component.

- variant (a value equal to: 'dashed', 'dotted', 'solid'; default 'solid'):
    Variant of the divider, options include `'dashed'` (dashed line), `'dotted'` (dotted line), `'solid'` (solid line).
    Default value: `'solid'`.
