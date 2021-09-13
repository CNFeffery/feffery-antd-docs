**children：** *string*型

　　用于传入对应的标题内容

**level：** *int*型

　　用于设置*标题级别*，可选1到5之间的整数，分别对应**<h1>**到**<h5>**之间的不同级别标题

**code：** *bool*型，默认为`False`

　　用于设置是否以*代码样式*渲染标题内容

**copyable：** *bool*型，默认为`False`

　　用于设置是否为标题内容添加*快捷复制*功能

**strikethrough：** *bool*型，默认为`False`

　　用于设置是否以*删除线模式*渲染标题内容

**disabled：** *bool*型，默认为`False`

　　用于设置是否以*禁用状态*渲染标题内容

**mark：** *bool*型，默认为`False`

　　用于设置是否以*高亮标黄*模式渲染标题内容

**strong：** *bool*型，默认为`False`

　　用于设置是否以*加粗*模式渲染标题内容

**italic：** *bool*型，默认为`False`

　　用于设置是否以*斜体*模式渲染标题内容

**underline：** *bool*型，默认为`False`

　　用于设置是否以*下划线*模式渲染标题内容

**keyboard：** *bool*型，默认为`False`

　　用于设置是否以*键盘按键样式*渲染标题内容

**type：** *string*型

　　用于设置标题内容的*整体状态类型*，本质上是对标题内容的颜色进行预设，可选的有`'secondary'`、`'success'`、`'warning'`及`'danger'`，默认为`None`即无状态