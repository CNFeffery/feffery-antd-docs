默认模式下，`treeData`参数通过`children`字段进行自由嵌套，以构造任意树形结构，其中各节点合法参数说明如下：

- title (string; required):

  当前节点标题

- key (string; required):

  当前节点唯一识别id

- children (list; optional):

  为当前节点定义子节点

- disabled (boolean; default False):

  是否禁用当前节点

- icon (string; optional):

  当前节点前缀图标类型，`iconRenderer`为`'AntdIcon'`时同`AntdIcon`同名参数，`iconRenderer`为`'fontawesome'`时为css类名

- iconRenderer (可选项有：'AntdIcon', 'fontawesome'; optional):

  当前节点前缀图标渲染方式，可选项有`'AntdIcon'`、`'fontawesome'`

- checkable (boolean; optional):

  当树组件整体的`checkable=True`时，单独控制当前节点是否渲染勾选框

- disableCheckbox (boolean; optional):

  当树组件整体的`checkable=True`时，控制是否禁用当前节点的勾选框

- selectable (boolean; optional):

  当前节点是否可点击选择

- enableFavorites (boolean; optional):

  当树组件整体的`enableNodeFavorites=True`时，控制是否可对当前节点进行收藏

- style (dict; optional):

  当前节点css样式

- className (string; optional):

  当前节点css类名

- tooltipProps (dict; optional):

  配置当前节点文字提示相关参数

  - title (string; optional):

    当前节点文字提示内容

  - placement (可选项有：'top', 'left', 'right', 'bottom', 'topLeft', 'topRight', 'bottomLeft', 'bottomRight'; default 'top'):

    当前节点文字提示展开方向，可选项有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`

- contextMenu (dict; optional):

  配置当前节点右键菜单相关参数

  - key (string; optional):

    当前右键菜单项唯一识别id

  - label (string; optional):

    当前右键菜单项标题内容

  - icon (string; optional):

    当前节点前缀图标类型，`iconRenderer`为`'AntdIcon'`时同`AntdIcon`同名参数，`iconRenderer`为`'fontawesome'`时为css类名

  - iconRenderer (可选项有：'AntdIcon', 'fontawesome'; optional):

    当前节点前缀图标渲染方式，可选项有`'AntdIcon'`、`'fontawesome'`

- isLeaf (boolean; optional):

  当前节点是否为叶节点