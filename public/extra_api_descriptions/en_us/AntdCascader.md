In the default mode, the `options` parameter allows for free nesting through the `children` field to construct any tree structure, with the following valid parameters for each node:

- label (string; required):

  The title content of the current node.

- key (string; optional):

  The unique identifier for the current node.

- value (string or number; required):

  The unique value of the current node.

- children (list; optional):

  Defines the child nodes for the current node.

- disabled (boolean; default False):

  Whether the current node is disabled.