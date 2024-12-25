默认模式下，`treeData`参数通过`children`字段进行自由嵌套，以构造任意树形结构，其中各节点合法参数说明如下：

- title (string; required):

  当前节点标题

- key (string; required):

  当前节点唯一识别id

- children (list; optional):

  为当前节点定义子节点

- value (string or number; optional):

  当前节点唯一值

- disabled (boolean; default False):

  是否禁用当前节点

- checkable (boolean; optional):

  当`treeCheckable=True`时，控制当前节点是否显示勾选框

- disableCheckbox (boolean; optional):

  当`treeCheckable=True`时，是否禁用当前节点勾选框

- selectable (boolean; optional):

  当前节点是否可点击选择

- isLeaf (boolean; optional):

  当前节点是否为叶节点（末端节点）