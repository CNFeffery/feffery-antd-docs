In the default mode, the `treeData` parameter is freely nested through the `children` field to construct any tree structure, where the valid parameters for each node are as follows:

- title (string; required):

  The title of the current node.

- key (string; required):

  The unique identifier for the current node.

- children (list; optional):

  Defines the child nodes for the current node.

- disabled (boolean; default False):

  Whether the current node is disabled.

- icon (string; optional):

  The prefix icon type for the current node. When `iconRenderer` is `'AntdIcon'`, it corresponds to the same parameter in `AntdIcon`. When `iconRenderer` is `'fontawesome'`, it is the CSS class name.

- iconRenderer (options: 'AntdIcon', 'fontawesome'; optional):

  The rendering method for the prefix icon of the current node. Options include `'AntdIcon'` and `'fontawesome'`.

- checkable (boolean; optional):

  When the overall `checkable=True` for the tree component, it controls whether the checkbox is rendered for the current node.

- disableCheckbox (boolean; optional):

  When the overall `checkable=True` for the tree component, it controls whether the checkbox for the current node is disabled.

- selectable (boolean; optional):

  Whether the current node is clickable for selection.

- enableFavorites (boolean; optional):

  When the overall `enableNodeFavorites=True` for the tree component, it controls whether the current node can be favorited.

- style (dict; optional):

  The CSS style for the current node.

- className (string; optional):

  The CSS class name for the current node.

- tooltipProps (dict; optional):

  Configures the tooltip-related parameters for the current node.

  - title (string; optional):

    The content of the tooltip for the current node.

  - placement (options: 'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; default 'top'):

    The direction in which the tooltip for the current node expands. Options include `'top'`, `'left'`, `'right'`, `'bottom'`, `'topLeft'`, `'topRight'`, `'bottomLeft'`, and `'bottomRight'`.

- contextMenu (dict; optional):

  Configures the context menu-related parameters for the current node.

  - key (string; optional):

    The unique identifier for the current context menu item.

  - label (string; optional):

    The title content of the current context menu item.

  - icon (string; optional):

    The prefix icon type for the current node. When `iconRenderer` is `'AntdIcon'`, it corresponds to the same parameter in `AntdIcon`. When `iconRenderer` is `'fontawesome'`, it is the CSS class name.

  - iconRenderer (options: 'AntdIcon', 'fontawesome'; optional):

    The rendering method for the prefix icon of the current node. Options include `'AntdIcon'` and `'fontawesome'`.

- isLeaf (boolean; optional):

  Whether the current node is a leaf node.