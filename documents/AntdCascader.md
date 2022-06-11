**placeholder：** *string*型

　　用于设置空白输入下的填充说明文字

**options：** *list*型，必填，无默认值

　　用于*构建层级结构*的必要参数，元素为单个或多个字典，每个字典的**键值对**有：

- value：必填，*string*型，用于设置此节点对应的选中值
- label：必填，*string*型，用于设置此节点显示的文字标签
- disabled：可选，*bool*型，用于设置是否禁用此节点的交互性，默认为`False`即不禁用
- children：*list*型，用于嵌套构建此节点的子节点，同`options`格式

　　下面是示例：

```py
options = [
	{
		'value': '节点1',
		'label': '节点1',
		'children': [
			{
				'value': '节点1-1',
				'label': '节点1-1'
			},
			{
				'value': '节点1-2',
				'label': '节点1-2',
				'children': [
					{
						'value': '节点1-2-1',
						'label': '节点1-2-1'
					},
					{
						'value': '节点1-2-2',
						'label': '节点1-2-2'
					}
				]
			}
		]
	},
	{
		'value': '节点2',
		'label': '节点2',
		'children': [
			{
				'value': '节点2-1',
				'label': '节点2-1'
			},
			{
				'value': '节点2-2',
				'label': '节点2-2'
			}
		]
	}
]
```

**disabled：** *bool*型，默认为`False`

　　设置是否*禁用*组件

**allowClear：** *bool*型，默认为`True`

　　设置是否渲染已选项清除按钮

**size：** *str*型，默认为`'middle'`

　　用于设置组件尺寸大小，可选的有`'small'`、`'middle'`与`'large'`

**border：** *bool*型，默认为`True`

　　用于设置是否*渲染边框*

**placement：** *str*型，默认为`'bottomLeft'`

　　用于设置悬浮展开组件的*展开方位*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**multiple：** *bool*型，默认为`False`

　　用于设置是否开启*多选模式*

**maxTagCount：** *int*或*str*型

　　用于设置多选模式下，选择框内展示的*已选项最大数量*，亦可设置为`'responsive'`开启响应式模式进行自适应

**expandTrigger：** *str*型，默认为`'click'`

　　用于子菜单展开的交互触发方式，可选的有`'click'`与`'hover'`

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`

**changeOnSelect：** *bool*型，默认为`False`

　　对于参数`options`构造出的可供选择的树，将每条分支的末端节点称为**叶节点**，`changeOnSelect`参数即用于设置是否只有**叶节点**被选中时才会更新组件的`value`参数

**defaultValue：** *list*型

　　用于设置*默认选中选项值列表*

**value：** *list*型

　　对应*已选中值列表*