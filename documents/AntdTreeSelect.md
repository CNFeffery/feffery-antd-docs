**placeholder：** *string*型

　　用于设置空白输入下的填充说明文字

**treeData：** *list*型，必填，无默认值

　　用于*构建层级结构*的必要参数，元素为单个或多个字典，每个字典的**键值对**有：

- title：*str*型，必填，设置节点显示的*文字标签内容*
- key：*str*型，必填，设置节点对应*唯一识别id*
- value：*str*型，必填，设置节点对应*值*
- disabled：*bool*型，设置是否*禁用当前节点*
- checkable：*bool*型，当`treeCheckable=True`时，设置当前节点*是否渲染勾选框*
- disableCheckbox：*bool*型，设置以*禁用状态*渲染当前节点勾选框
- selectable：*bool*型，设置当前节点*是否可点击选择*，优先级低于`checkable`
- children：*list*型，用于嵌套构建此节点的子节点，同`treeData`格式

　　下面是示例：

```py
treeData = [
  {
    "title": "Node1",
    "value": "0-0",
    "key": "0-0",
    "children": [
      {
        "title": "Child Node1",
        "value": "0-0-0",
        "key": "0-0-0"
      }
    ]
  },
  {
    "title": "Node2",
    "value": "0-1",
    "key": "0-1",
    "children": [
      {
        "title": "Child Node3",
        "value": "0-1-0",
        "key": "0-1-0"
      },
      {
        "title": "Child Node4",
        "value": "0-1-1",
        "key": "0-1-1"
      },
      {
        "title": "Child Node5",
        "value": "0-1-2",
        "key": "0-1-2"
      }
    ]
  }
]
```

**allowClear：** *bool*型，默认为`True`

　　设置是否渲染*内容清空按钮*

**treeLine：** *bool*型，默认为`False`

　　设置是否为树*渲染连接线*

**listHeight：** *int*型，默认为`256`

　　设置*下拉菜单像素高度*

**disabled：** *bool*型，默认为`False`

　　设置是否*禁用*组件

**size：** *str*型，默认为`'middle'`

　　用于设置组件尺寸大小，可选的有`'small'`、`'middle'`与`'large'`

**border：** *bool*型，默认为`True`

　　用于设置是否*渲染边框*

**value：** *str*或*list*型

　　对应*已选项值*，单选模式下为选中节点对应的`value`值，多选模式下为已选节点`value`值构成的列表

**defaultValue：** *str*或*list*型

　　设置初始化时*已选项值*，格式同`value`

**maxTagCount：** *int*型，默认为`5`

　　设置在输入框中显示的*最大已选项数量*

**multiple：** *bool*型，默认为`False`

　　设置是否*开启多选模式*，在勾选框模式下会屏蔽此参数自动开启多选模式

**treeCheckable：** *bool*型，默认为`False`

　　设置是否为每个节点渲染*勾选框*

**treeCheckStrictly：** *bool*型，默认为`False`

　　设置是否禁用先辈节点与后代节点之间的关联，设置为`True`之后，先辈节点与后代节点之间的勾选行为彼此独立

**treeDefaultExpandAll：** *bool*型，默认为`False`

　　设置初始化时是否*展开所有节点树*

**treeDefaultExpandedKeys：** *list*型

　　设置初始化时展开的树节点`key`值列表

**treeExpandedKeys：** *list*型

　　对应当前已被展开的树节点`key`值列表

**virtual：** *bool*型，默认为`True`

　　设置是否以*虚拟滚动*的形式渲染节点树，节点众多时可显著提升性能表现

**placement：** *str*型，默认为`'bottomLeft'`

　　用于设置*悬浮层展开方位*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`









