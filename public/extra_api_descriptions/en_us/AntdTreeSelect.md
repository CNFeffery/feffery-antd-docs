In the default mode, the `treeData` parameter is freely nested through the `children` field to construct any tree structure, where the legal parameters for each node are described as follows:

- title (string; required):

  The title of the current node.

- key (string; required):

  The unique identifier ID of the current node.

- children (list; optional):

  Defines the child nodes for the current node.

- value (string or number; optional):

  The unique value of the current node.

- disabled (boolean; default False):

  Whether the current node is disabled.

- checkable (boolean; optional):

  Controls whether the checkbox is displayed for the current node when `treeCheckable=True`.

- disableCheckbox (boolean; optional):

  Whether the checkbox of the current node is disabled when `treeCheckable=True`.

- selectable (boolean; optional):

  Whether the current node is clickable for selection.

- isLeaf (boolean; optional):

  Whether the current node is a leaf node (terminal node).