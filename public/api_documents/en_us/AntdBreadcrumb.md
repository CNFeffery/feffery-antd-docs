- id (string; optional):
    Unique identifier for the component.

- aria-* (string; optional):
    Wildcard for `aria-*` formatted attributes.

- className (string | dict; optional):
    The CSS class name for the current component, supporting [dynamic CSS](/advanced-classname).

- clickedItem (dict; optional):
    Listens for breadcrumb node click events.

    `clickedItem` is a dictionary with keys:

    - itemKey (string; optional):
        The key value of the clicked node.

    - itemTitle (string; optional):
        The title of the clicked node.

    - timestamp (number; optional):
        The timestamp of the click event.

- data-* (string; optional):
    Wildcard for `data-*` formatted attributes.

- items (list of dicts; optional):
    The data structure for breadcrumb nodes.

    `items` is a list of dictionaries with keys:

    - href (string; optional):
        The link address of the node.

    - icon (string; optional):
        The name of the prefix icon for the node, associated with the `iconRenderer` method. Under the `'AntdIcon'` method, it is the same as the icon parameter of AntdIcon, and under the `'fontawesome'` method, it represents the CSS class name of the icon.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        The rendering method for the prefix icon, with options `'AntdIcon'`, `'fontawesome'`. Default value: `'AntdIcon'`.

    - key (string; optional):
        The unique key value for the node.

    - menuItems (list of dicts; optional):
        The data structure required to set up a dropdown menu for the current node.

        `menuItems` is a list of dictionaries with keys:

        - disabled (boolean; optional):
            Whether to disable the current dropdown menu node.

        - href (string; optional):
            The link address of the dropdown menu node.

        - icon (string; optional):
            The name of the prefix icon for the dropdown menu node, associated with the `iconRenderer` method. Under the `'AntdIcon'` method, it is the same as the icon parameter of AntdIcon, and under the `'fontawesome'` method, it represents the CSS class name of the icon.

        - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
            The rendering method for the prefix icon, with options `'AntdIcon'`, `'fontawesome'`. Default value: `'AntdIcon'`.

        - target (string; optional):
            The link behavior for the dropdown menu node.

        - title (string; optional):
            The title of the dropdown menu node.

    - target (string; optional):
        The link behavior for the node.

    - title (string; optional):
        The title of the node.

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

- separator (a list of or a singular dash component, string or number; default '/'):
    Component type, separator. Default value: `'/'`.

- style (dict; optional):
    The CSS styles for the current component.
