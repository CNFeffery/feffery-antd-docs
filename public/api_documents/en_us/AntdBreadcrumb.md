- id (string; optional):
    Unique identifier for the component.

- key (string; optional):
    Update the component’s `key` to force it to remount.

- className (string | dict; optional):
    CSS class name of the component. Supports [dynamic CSS classes](/advanced-classname).

- items (list of dicts; optional):
    `items` is a list of dictionaries with keys:

    `items` is a list of dicts with keys:

    - title (string; optional):
        The title of the node.

    - key (string; optional):
        Unique key value of the node.

    - href (string; optional):
        Node link address.

    - target (string; optional):
        Node link jump behavior.

    - icon (string; optional):
        Node prefix icon name, associated with `iconRenderer` method, same as AntdIcon's icon parameter under `'AntdIcon'` method, represents the icon's CSS class name under `'fontawesome'` method.

    - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):
        The rendering method of the prefix icon, options include `'AntdIcon'`, `'fontawesome'`. Default value: `'AntdIcon'`.

    - menuItems (list of dicts; optional):
        `menuItems` is a list of dictionaries with keys:

        `menuItems` is a list of dicts with keys:

        - title (string; optional):

            The title of the dropdown menu node.

        - key (string; optional):

            Unique key of a dropdown menu node.

        - href (string; optional):

            The link address of the dropdown menu node.

        - target (string; optional):

            The link behavior for the dropdown menu node.

        - disabled (boolean; optional):

            Whether to disable the current dropdown menu node.

        - icon (string; optional):

            The name of the prefix icon for the dropdown menu node, associated with the `iconRenderer` method. Under the `'AntdIcon'` method, it is the same as the icon parameter of AntdIcon, and under the `'fontawesome'` method, it represents the CSS class name of the icon.

        - iconRenderer (a value equal to: 'AntdIcon', 'fontawesome'; optional):

            The rendering method of the prefix icon, options include `'AntdIcon'`, `'fontawesome'`. Default value: `'AntdIcon'`.

- separator (a list of or a singular dash component, string or number; default '/'):
    Component type, separator. Default value: `'/'`.

- clickedItem (dict; optional):
    Listens for breadcrumb node click events.

    `clickedItem` is a dict with keys:

    - itemTitle (string; optional):
        The title of the clicked node.

    - itemKey (string; optional):
        The key value of the clicked node.

    - menuItemTitle (string; optional):
        Title of the corresponding dropdown menu node.

    - menuItemKey (string; optional):
        Key of the corresponding dropdown menu node.

    - timestamp (number; optional):
        The timestamp of the click event.

- data-* (string; optional):
    Wildcard support for `data-*` attributes.

- aria-* (string; optional):
    Wildcard support for `aria-*` attributes.
