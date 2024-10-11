
- id (string; optional):
    The unique identifier for the component.

- key (string; optional):
    Updates the `key` value of the current component, which can force a redraw of the current component.

- style (dict; optional):
    The CSS styles for the current component.

- className (string | dict; optional):
    The CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

- layout (a value equal to: 'horizontal', 'vertical'; default 'horizontal'):
    The layout direction, options include `'horizontal'`, `'vertical'`. Default value: `'horizontal'`.

- items (list of dicts; required):
    Configures the subitems of the split panel, with higher priority than `children`.

    `items` is a list of dictionaries with keys:

    - key (string; optional):
        The key for the panel.

    - children (a list of or a singular dash component, string or number; optional):
        The component type, embedded elements.

    - style (dict; optional):
        The CSS styles for the current component.

    - className (string or dict; optional):
        The CSS class name for the current component, supports [dynamic CSS](/advanced-classname).

    - defaultSize (number | string; optional):
        The initial panel size, supports numeric `px` or textual `'percentage%'` types.

    - min (number | string; optional):
        The minimum threshold, supports numeric `px` or textual `'percentage%'` types.

    - max (number | string; optional):
        The maximum threshold, supports numeric `px` or textual `'percentage%'` types.

    - size (number | string; optional):
        The panel size, supports numeric `px` or textual `'percentage%'` types.

    - collapsible (dict; optional):
        Whether it is collapsible. Default value: `False`.

        `collapsible` is a boolean | dict with keys:

        - start (boolean; optional)

        - end (boolean; optional)

    - resizable (boolean; optional):
        Whether to enable drag-to-resize. Default value: `True`.

- currentSizes (list of dicts; optional):
    Listens for changes in the current panel size information.

    `currentSizes` is a list of dictionaries with keys:

    - key (string; optional):
        The key for the panel.

    - size (number | string; optional):
        The size of the panel.

- data-* (string; optional):
    A wildcard for `data-*` format attributes.

- aria-* (string; optional):
    A wildcard for `aria-*` format attributes.

- loading_state (dict; optional)

    `loading_state` is a dictionary with keys:

    - is_loading (boolean; optional):
        Determines whether the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading.