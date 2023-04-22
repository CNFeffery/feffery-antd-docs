**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**color：** *string*型

　　用于*设置徽标颜色*

**count：** *int*型

　　用于*设置徽标中要显示的计数数值*，可配合`showZero`与`overflowCount`参数实现更多显示功能

**dot：** *bool*型，默认为`False`

　　用于设置*是否不展示徽标数值，而是只显示一个小红点*

**showZero：** *bool*型，默认为`False`

　　当`count=0`时，默认不在徽标中显示数值，在设置`showZero=True`后会强制显示数值`0`

**overflowCount：** *int*型，默认为`99`

　　用于*设置徽标计数数值显示上限*，当`count`超过此上限时，会强制显示为`overflowCount+`的格式，如`99+`

**offset：** *list*型

　　用于*设置徽标向右侧与底部的偏移像素距离*，格式为`[向右侧方向偏移距离, 向底部方向偏移距离]`

**status：** *string*型

　　用于*设置徽标状态*，可选的有`'success'`、`'processing'`、`'default'`、`'error'`与`'warning'`

**text：** *string*型

　　当`status`参数已设置时，可通过此参数*设置状态徽标的文本内容*

**title：** *string*型

　　用于*设置鼠标悬停于状态徽标上时显示的文字内容*

**size：** *string*型，默认为`'default'`

　　用于*设置当前组件的尺寸规格*，可选的有`'default'`与`'small'`

**nClicks：** *int*型，默认为`0`

　　用于*监听徽标的点击事件*