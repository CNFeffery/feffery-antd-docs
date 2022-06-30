**treeData：** *list*型，必填，无默认值

　　用于*构建树形结构*的必要参数，元素为单个或多个字典，每个字典的**键值对**有：

- title：必填，*str*型，用于设置此节点显示的文字标签
- key：必填，*str*型，相当于此节点的id，需在整棵树内保持唯一性
- disabled：可选，*bool*型，用于设置是否禁用此节点的交互性，默认为`False`即不禁用
- icon：可选，*str*型，用于在参数`showIcon=True`时设置节点的前缀图标，对应`AntdIcon`中的所有内置图标
- checkable：可选，*bool*型，用于在参数`checkable=True`时设置是否在节点前渲染勾选框，默认为`True`即渲染
- disableCheckbox：可选，*bool*型，用于在参数`checkable=True`时设置是否禁用此节点的勾选框，默认为`False`即不禁用
- selectable：可选，*bool*型，用于在参数`selectable=True`时设置此节点是否可点击选中，默认为`True`即可点击选中
- children：可选，*list*型，用于构建此节点的子节点，同`treeData`格式

　　下面是示例：

```py
treeData = [
    {
        'title': '世界',
        'key': '世界',
        'icon_name': 'user',
        'children': [
            {
                'title': '亚洲',
                'key': '亚洲',
                'children': [
                    {
                        'title': '中国', 
                        'key': '中国', 
                        'icon_name': 'table'
                    },
                    {
                        'title': '日本', 
                        'key': '日本', 
                        'icon_name': 'database', 
                        'disabled': True
                    }
                ]
            },
            {
                'title': '北美洲',
                'key': '北美洲',
                'icon_name': 'file',
                'children': [
                    {
                        'title': '美国', 
                        'key': '美国',
                        'icon_name': 'file-text'}
                ]
            }
        ]
    }
]
```

**showIcon：** *bool*型，默认为`True`

　　用于设置当前树形控件是否允许渲染节点前缀*图标*，`True`（渲染），`False`（不渲染）

**checkable：** *bool*型，默认为`False`

　　用于整体设置各节点前是否*渲染勾选框*供用户点击勾选，`True`（渲染），`False`（不渲染）

**selectable：** *bool*型，默认为`True`

　　用于整体设置各节点是否可*点击选中*，`True`（可点击），`False`（不可点击）

**defaultExpandAll：** *bool*型，默认为`False`

　　用于设置是否初始状态*展开全部*折叠的节点树

**defaultExpandedKeys：** *list*型，默认为`[]`

　　用于自定义设置初始状态哪些`key`对应节点被展开

**defaultExpandParent：** *bool*型，默认为`False`

　　当参数`defaultExpandedKeys`指定节点的上层节点未被展开时，通过设置此参数为`True`可强制其展开，保证了`defaultExpandedKeys`的展开效果

**defaultCheckedKeys：** *list*型

　　设置默认被勾选上的*节点key值列表*

**defaultSelectedKeys：** *list*型

　　设置默认被选择的*节点key值列表*

**multiple：** *bool*型，默认为`False`

　　用于设置节点被点击选中是否允许多选，`True`（允许），`False`（不允许）

**showLine：** *bool*型，默认为`True`

　　用于设置是否绘制节点之间的连接线，`True`（绘制），`False`（不绘制）

**height：** *int*型

　　用于设定树形控件的最大高度，超出部分将以滑轮滚动形式进行加载，且采用了*虚拟化*技术，适合在节点树较为庞大时使用以提升性能

**checkStrictly：** *bool*型，默认为`False`

　　用于设置先辈节点与后代节点之间的选择行为*是否彼此独立*，譬如设置为`True`时，父节点的选择行为不会使得其下所有子节点自动被选中

**selectedKeys：** *list*型

　　用于在回调中捕获*已被点击选中的节点`key`列表*

**checkedKeys：** *list*型

　　用于在回调中捕获*已被勾选选中的节点`key`列表*

**halfCheckedKeys：** *list*型

　　用于再回调中捕获*处于半勾选状态下的节点`key`列表*