**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**optionsMode：** *string*型，默认为`'tree'`

　　用于*设置针对options参数的解析模式*，可选的有`'tree'`（树形结构）、`'flat'`（扁平结构）

**options：** `list[dict]`型，必填

　　用于*构建级联选择的选项结构*

　　当`optionsMode='tree'`时，`options`参数需要符合树形解析模式，每个字典的可用键值对参数有：

- **value：** *string*、*int*或*float*型，必填，用于*设置当前节点对应的值*
- **label：** *string*型，必填，用于*设置当前节点的标签内容*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前节点*
- **children：** *list*型，用于*向下嵌套后代树形结构*

　　下面是树形`options`的示例：

```python
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

　　当`optionsMode='flat'`时，`options`参数需要符合扁平解析模式，每个字典的可用键值对参数有：

- **value：** *string*、*int*或*float*，必填，用于*设置当前节点对应的值*
- **label：** *string*型，必填，用于*设置当前节点的标签内容*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前节点*
- **key：** *string*型，用于*唯一标识当前节点*，从而实现父节点与子节点间的关联
- **parent：** *string*型，用于*声明当前节点的父节点key值*，从而实现父节点与子节点间的关联

　　下面是扁平`options`的示例：

```python
options = [
    {
        'value': '1',
        'label': '节点1',
        'key': '1'
    },
    *[
        {
            'value': f'1-{i}',
            'label': f'节点1-{i}',
            'key': f'1-{i}',
            'parent': '1'
        }
        for i in range(1, 4)
    ],
    {
        'value': '2',
        'label': '节点2',
        'key': '2'
    },
    {
        'value': '2-1',
        'label': '节点2-1',
        'key': '2-1',
        'parent': '2'
    },
    {
        'value': '2-2',
        'label': '节点2-2',
        'key': '2-2',
        'parent': '2'
    },
    *[
        {
            'value': f'2-2-{i}',
            'label': f'节点2-2-{i}',
            'key': f'2-2-{i}',
            'parent': '2-2'
        }
        for i in range(1, 4)
    ],
]
```

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**changeOnSelect：** *bool*型，默认为`False`

　　用于*设置是否当任意节点被选择时均对value进行更新*，当`changeOnSelect=False`时只有末端节点被选择时才会触发对`value`的更新

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *string*型

　　用于*设置空白输入下的填充说明文字*

**placement：** *str*型，默认为`'bottomLeft'`

　　用于*设置下拉菜单的展开方向*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**value：** *list*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *list*型

　　用于*监听或设置初始化时的已选中值*

**maxTagCount：** *int*或*str*型

　　用于*设置多选模式下选择框内展示的已选项最大数量*，亦可设置为`'responsive'`开启响应式模式进行自适应调整

**multiple：** *bool*型，默认为`False`

　　用于*设置是否开启多选模式*

**expandTrigger：** *str*型，默认为`'click'`

　　用于*设置触发下拉菜单展开的触发方式*，可选的有`'hover'`及`'click'`

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户清空已选项*

**showCheckedStrategy：** *string*型，默认为`'show-parent'`

　　用于*设置已选项的回填显示策略*，可选的有`'show-parent'`（当所有子节点都被选中时，只显示父节点）、`'show-child'`（只显示选中的子节点）

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）