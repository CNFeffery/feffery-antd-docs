**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名，支持[动态css](/advanced-classname)*

**steps：**`list[dict]`型，必填

　　用于*定义各步骤结构*，每个字典的可用键值对参数有：

- **title：** *组件型*，用于*设置当前步骤的标题内容*
- **subTitle：** *组件型*，用于*设置当前步骤的副标题内容*
- **description：** *组件型*，用于*设置当前步骤的描述文案内容*
- **icon：** *组件型*，用于*设置当前步骤的图标内容*

　　下面是一个示例：

```python
steps = [
    {
        'title': '步骤1',
        'subTitle': '1',
        'description': '这是步骤1'
    },
    {
        'title': '步骤2',
        'subTitle': '2',
        'description': '这是步骤2'
    },
    {
        'title': '步骤3',
        'subTitle': '3',
        'description': '这是步骤3'
    }
]
```

**current：** *int*型，默认为`0`

　　用于*设置步骤条当前所在步骤序号*，默认为`0`即为第一个步骤

**direction：** *str*型，默认为`'horizontal'`

　　用于*设置步骤条的展示方向*，可选的有`'horizontal'`（水平方向）、`'vertical'`（竖直方向）

**labelPlacement：** *str*型，默认为`'horizontal'`

　　用于*设置每个步骤的标题等内容的方位*，可选的有`'horizontal'`（置于图标右侧）、`'vertical'`（置于图标下方）

**progressDot：** *bool*型，默认为`False`

　　用于*设置是否以简洁点状步骤条的方式渲染步骤条*

**size：** *str*型，默认为`'default'`

　　用于*设置步骤条的规格大小*，可选的有`'default'`（默认尺寸）、`'small'`（迷你尺寸）

**status：** *str*型，默认为`'process'`

　　用于*设置当前步骤对应的显示状态*，可选的有`'process'`、`'wait'`、`'finish'`和`'error'`

**type：** *str*型，默认为`'default'`

　　用于*设置步骤条整体的风格类型*，可选的有`'default'`（默认风格）、`'navigation'`（导航风格）

**allowClick：** *bool*型，默认为`False`

　　用于*设置是否允许直接点击步骤进行切换*

**responsive：** *bool*型，默认为`True`

　　用于*设置是否在页面宽度低于532px时自动强制垂直渲染步骤条*