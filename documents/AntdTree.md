**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名，支持[动态css](/advanced-classname)*

**treeDataMode：** *string*型，默认为`'tree'`

　　用于*设置针对treeData参数的解析模式*，可选的有`'tree'`（树形结构）、`'flat'`（扁平结构）

**treeData：** `list[dict]`型，必填

　　用于*构建树选择的选项结构*

　　当`treeDataMode='tree'`时，`treeData`参数需要符合树形解析模式，每个字典的可用键值对参数有：

- **title：** *string*型，必填，用于*设置当前节点对应的标题内容*
- **key：** *string*型，必填，用于*唯一标识当前节点*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前节点*
- **icon：** *string*型，用于*为当前节点设置前缀图标*，同`AntdIcon`中的同名参数
- **iconRenderer：** *string*型，默认为`'AntdIcon'`，用于*为当前节点前缀图标设置渲染方式*，可选的有`'AntdIcon'`（内置图标）、`'fontawesome'`（基于css类名渲染）
- **checkable：** *bool*型，用于*设置是否为当前节点渲染勾选框*
- **disableCheckbox：** *bool*型，用于*设置是否禁用当前节点的勾选框*
- **selectable：** *bool*型，用于*设置当前节点是否可被选中*
- **enableFavorites：** *bool*型，当`enableNodeFavorites=True`时，用于*设置当前节点是否可收藏*
- **style：** *dict*型，用于*设置当前节点的css样式*
- **className：** *string*型，用于*设置当前节点的css类名*
- **tooltipProps：** *dict*型，用于*为当前节点配置信息提示相关功能*，可用的键值对参数有：
  - **title：** *string*型，用于*设置当前节点对应信息提示的文字内容*
  - **placement：** *string*型，用于*设置当前节点对应信息提示的展开方位*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`
- **contextMenu：** `list[dict]`型，用于*为当前节点定义右键菜单各选项*，每个字典的可用键值对参数有：
  - **key：** *string*型，用于*设置当前右键菜单项的唯一id*
  - **label：** *string*型，用于*设置当前右键菜单项的标题内容*
  - **icon：** *string*型，用于*为当前右键菜单项设置前缀图标*，同`AntdIcon`中的同名参数
  - **iconRenderer：** *string*型，默认为`'AntdIcon'`，用于*为当前右键菜单项前缀图标设置渲染方式*，可选的有`'AntdIcon'`（内置图标）、`'fontawesome'`（基于css类名渲染）

　　下面是树形`treeData`的示例：

```python
treeData = [
    {
        'key': '节点1',
        'title': '节点1',
        'children': [
            {
                'key': f'节点1-{i}',
                'title': f'节点1-{i}'
            }
            for i in range(1, 5)
        ]
    },
    {
        'key': '节点2',
        'title': '节点2'
    }
]
```

　　当`treeDataMode='flat'`时，`treeData`参数需要符合扁平解析模式，每个字典的可用键值对参数有：

- **title：** *string*型，必填，用于*设置当前节点对应的标题内容*
- **key：** *string*型，必填，用于*唯一标识当前节点*，从而实现父节点与子节点间的关联
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前节点*
- **icon：** *string*型，用于*为当前节点设置前缀图标*，同`AntdIcon`中的同名参数
- **checkable：** *bool*型，用于*设置是否为当前节点渲染勾选框*
- **disableCheckbox：** *bool*型，用于*设置是否禁用当前节点的勾选框*
- **selectable：** *bool*型，用于*设置当前节点是否可被选中*
- **enableFavorites：** *bool*型，当`enableNodeFavorites=True`时，用于*设置当前节点是否可收藏*
- **style：** *dict*型，用于*设置当前节点的css样式*
- **className：** *string*型，用于*设置当前节点的css类名*
- **tooltipProps：** *dict*型，用于*为当前节点配置信息提示相关功能*，可用的键值对参数有：
  - **title：** *string*型，用于*设置当前节点对应信息提示的文字内容*
  - **placement：** *string*型，用于*设置当前节点对应信息提示的展开方位*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`
- **contextMenu：** `list[dict]`型，用于*为当前节点定义右键菜单各选项*，每个字典的可用键值对参数有：
  - **key：** *string*型，用于*设置当前右键菜单项的唯一id*
  - **label：** *string*型，用于*设置当前右键菜单项的标题内容*
  - **icon：** *string*型，用于*为当前右键菜单项设置前缀图标*，同`AntdIcon`中的同名参数
- **parent：** *string*型，用于*声明当前节点的父节点key值*，从而实现父节点与子节点间的关联

　　下面是扁平`treeData`的示例：

```python
treeData = [
    {
        'title': '四川省',
        'key': '四川省'
    },
    {
        'title': '成都市',
        'key': '成都市',
        'parent': '四川省'
    },
    {
        'title': '广安市',
        'key': '广安市',
        'parent': '四川省'
    },
    {
        'title': '重庆市',
        'key': '重庆市'
    },
    {
        'title': '渝中区',
        'key': '渝中区',
        'parent': '重庆市'
    },
    {
        'title': '渝北区',
        'key': '渝北区',
        'parent': '重庆市'
    },
    {
        'title': '解放碑街道',
        'key': '解放碑街道',
        'parent': '渝中区'
    }
]
```

**showIcon：** *bool*型，默认为`False`

　　用于*设置是否渲染树节点前缀的图标*

**selectable：** *bool*型，默认为`True`

　　用于*设置树节点是否可选中*

**multiple：** *bool*型，默认为`False`

　　用于*设置树节点是否可进行多选点选*

**checkable：** *bool*型，默认为`False`

　　用于*设置是否为树节点前添加勾选框*

**defaultExpandAll：** *bool*型，默认为`False`

　　用于*设置初始化时是否展开全部节点*

**expandedKeys：** `list[string]`型

　　用于*设置或监听处于展开状态的节点key值数组*

**defaultExpandedKeys：** `list[string]`型

　　用于*设置初始化时处于展开状态的节点key值数组*

**defaultExpandParent：** *bool*型，默认为`False`

　　用于*设置初始化时展开的节点的父节点是否自动一并展开*

**selectedKeys：** `list[string]`型

　　用于*设置或监听处于选中状态的节点key值数组*

**defaultSelectedKeys：** `list[string]`型

　　用于*设置初始化时处于选中状态的节点key值数组*

**checkedKeys：** `list[string]`型

　　用于*设置或监听处于勾选状态的节点key值数组*

**defaultCheckedKeys：** `list[string]`型

　　用于*设置初始化时处于勾选状态的节点key值数组*

**halfCheckedKeys：** `list[string]`型

　　用于*监听处于半勾选状态下的节点key值数组*

**checkStrictly：** *bool*型，默认为`False`

　　用于*设置节点与其后代节点之间的勾选行为是否彼此独立不关联*

**showLine：** *bool*或*dict*型，默认为`{'showLeafIcon': False}`

　　用于*设置是否显示连接线*，当传入*dict*型输入时，可用的键值对参数有：

- **showLeafIcon：** *bool*型，用于*设置是否为叶节点渲染前缀图标*

**height：** *int*或*float*型

　　用于*设置虚拟滚动模式下的窗口像素高度*，不设置则不会开启虚拟滚动功能

**draggable：** *bool*型，默认为`False`

　　当`treeDataMode="tree"`时，用于*设置是否开启节点可拖拽功能*，每次有效拖拽行为完成后会将新的树结构更新到`treeData`中

**dragInSameLevel：** *bool*型，默认为`False`

　　当`draggable=True`时，用于*设置是否仅允许同级节点拖拽*

**draggedNodeKey：** *string*型

　　用于*监听每次有效节点拖拽行为对应的节点key值*

**clickedContextMenu：** *dict*型

　　用于*监听每次有效的节点右键菜单点击事件*，具有的键值对属性有：

- **nodeKey：** *string*型，用于*监听右键菜单点击事件对应的树节点key值*
- **menuKey：** *string*型，用于*监听右键菜单点击事件对应的选项key值*
- **timestamp：** *int*型，用于*监听右键菜单点击事件发生时间戳*

**enableNodeFavorites：** *bool*型，默认为`False`

　　用于*设置是否启用树节点收藏功能*

**favoritedKeys：** *list*型

　　用于*设置或监听当前处于收藏状态的节点key值数组*

**scrollTarget：** *dict*型

　　用于*配置树节点滚动动作相关参数*，可用的键值对参数有：

- **key：** *string*型，必填，用于*设置滚动目标节点的key值*
- **align：** *string*型，用于*设置滚动动作后的节点对齐位置*，可选的有`'top'`、`'bottom'`、`'auto'`
- **offset：** *int*型，用于*设置滚动动作像素偏移量*

**searchKeyword：** *string*型

　　用于*实现快捷树搜索功能*，匹配目标为树节点`title`字段

**highlightStyle：** *dict*型

　　配合`searchKeyword`使用，用于*自定义搜索匹配高亮内容的css样式*

**nodeCheckedStyle：** *dict*型

　　用于*设置已勾选节点的css样式*

**nodeUncheckedStyle：** *dict*型

　　用于*设置未勾选节点的css样式*

**nodeCheckedSuffix：** *组件型*

　　用于*设置已勾选节点的后缀内容*

**nodeUncheckedSuffix：** *组件型*

　　用于*设置未勾选节点的后缀内容*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['selectedKeys', 'checkedKeys', 'expandedKeys', 'halfCheckedKeys']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'selectedKeys'`、`'checkedKeys'`、`'expandedKeys'`、`'halfCheckedKeys'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）

