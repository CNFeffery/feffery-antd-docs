默认模式下，`menuItems`参数通过`children`字段进行自由嵌套，以构造任意树形菜单结构，其中各节点合法参数说明如下：

- component (可选项有：'Item', 'SubMenu', 'ItemGroup', 'Divider; required):

  当前菜单节点类型，可选项有`'Item'`（菜单项）、`'SubMenu'`（子菜单）、`'ItemGroup'`（菜单项分组）、`'Divider'`（分隔线）

- props (dict; optional):

  配置当前节点相关属性值

  - key (string; required):

    当前节点唯一识别id

  - title (string; optional):

    当前节点标题

  - disabled (boolean; default False):

    是否禁用当前节点

  - danger (boolean; default False):

    当前节点是否显示为危险状态

  - href (string; optional):

    当前节点跳转链接地址

  - icon (string; optional):

    当前节点前缀图标类型，`iconRenderer`为`'AntdIcon'`时同`AntdIcon`同名参数，`iconRenderer`为`'fontawesome'`时为css类名

  - iconRenderer (可选项有：'AntdIcon', 'fontawesome'; optional):

    当前节点前缀图标渲染方式，可选项有`'AntdIcon'`、`'fontawesome'`

  - dashed (boolean; default False):

    若当前节点为分割线，设置是否显示为虚线

  - name (string; optional):

    当前节点唯一辅助标识