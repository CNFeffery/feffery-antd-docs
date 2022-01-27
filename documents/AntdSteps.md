**steps：** *list*型，必填，无默认值

　　按顺序定义各个步骤相关的信息，列表每个元素为字典，其中键值对`title`必填，用于传入对应步骤的标题；键值对`subTitle`可选，用于传入对应步骤的副标题；键值对`description`可选，用于传入对应步骤的说明文字，下面是一个示例：

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

**current：** *int*型，默认为0

　　用于设定步骤条当前停留的步骤序号，默认为`0`即为第一个步骤

**direction：** *str*型，默认为`'horizontal'`

　　用于设置步骤条的*展示方向*，`horizontal`代表水平方向，`vertical`代表竖直方向

**labelPlacement：** *str*型，默认为`'horizontal'`

　　用于设置每个步骤的*标题等文字放置位置*，`'horizontal'`放置于步骤图标右侧，`'vertical'`放置于步骤图标下方

**progressDot：** *bool*型，默认为`False`

　　用于设置是否以*简洁点状步骤条*的方式渲染步骤条

**size：** *str*型，默认为`'default'`

　　用于设置*步骤条大小尺寸*，`'default'`表示默认正常尺寸，`'small'`表示迷你尺寸

**status：** *str*型，默认为`'process'`

　　用于设置当前所处的步骤*对应的显示状态*，有`'process'`、`'wait'`、`'finish'`及`'error'`四种状态，显示效果见后面的例子

**type：** *str*型，默认为`'default'`

　　用于设置步骤条*整体的渲染形式*，`'default'`表示常规形式，`'navigation'`表示带引导的导航形式

**allowClick：** *bool*型，默认为`False`

　　用于设置*是否允许直接点击步骤进行切换*