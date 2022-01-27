**children：**

　　用于传入*需要添加徽标的目标元素*

**color：** *string*型

　　用于*自定义徽标颜色*

**count：** *int*型

　　用于设置*徽标中要显示的计数数值*，可配合`showZero`与`overflowCount`参数实现更多显示功能

**showZero：** *bool*型，默认为`False`

　　当`count=0`时，默认是不会在徽标中显示数值的，但若设置`showZero=True`，则会强制显示数值`0`

**overflowCount：** *int*型，默认为`99`

　　用于设置*徽标计数数值显示上限*，当`count`超过此上限时，会强制显示为`overflowCount+`的格式，如`99+`

**dot：** *bool*型，默认为`False`

　　用于设置*是否不展示徽标数值，而是只显示一个小红点*

**offset：** *list*型

　　用于设置*徽标向右侧与底部的偏移像素距离*，格式如`[向右侧方向偏移距离, 向底部方向偏移距离]`

**status：** *string*型

　　用于设置*徽标状态*，可选的有`'success'`、`'processing'`、`'default'`、`'error'`与`'warning'`

**text：** *string*型

　　当`status`参数已设置时，可通过此参数设置*状态徽标的文本内容*

**title：** *string*型

　　用于设置*鼠标悬停于状态徽标上时显示的文字内容*

**size：** *string*型，默认为`'default'`

　　用于设置*徽标规格大小*，可选的有`'default'`与`'small'`

**nClicks：** *int*型，默认为`0`

　　用于*记录徽标被点击次数*