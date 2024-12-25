In the default mode, the `menuItems` parameter is freely nested through the `children` field to construct any tree-shaped menu structure. The legal parameters for each node are described as follows:

- component (options include: 'Item', 'SubMenu', 'ItemGroup', 'Divider'; required):

  The type of the current menu node. Options include `'Item'` (menu item), `'SubMenu'` (submenu), `'ItemGroup'` (menu item group), and `'Divider'` (divider line).

- props (dict; optional):

  Configure the attribute values related to the current node.

  - key (string; required):

    The unique identifier for the current node.

  - title (string; optional):

    The title of the current node.

  - disabled (boolean; default False):

    Whether the current node is disabled.

  - danger (boolean; default False):

    Whether the current node is displayed in a danger state.

  - href (string; optional):

    The link address for the current node.

  - target (string; optional):

    The opening method for the link of the current node.

  - icon (string; optional):

    The type of prefix icon for the current node. When `iconRenderer` is `'AntdIcon'`, it corresponds to the same parameter in `AntdIcon`. When `iconRenderer` is `'fontawesome'`, it is the CSS class name.

  - iconRenderer (options include: 'AntdIcon', 'fontawesome'; optional):

    The rendering method for the prefix icon of the current node. Options include `'AntdIcon'` and `'fontawesome'`.

  - dashed (boolean; default False):

    If the current node is a divider, set whether to display it as a dashed line.

  - name (string; optional):

    A unique auxiliary identifier for the current node.