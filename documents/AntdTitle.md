**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**level：** *int*型，默认为`1`

　　用于*设置标题级别*，可选1到5之间的整数，分别对应`<h1>`到`<h5>`之间的不同级别标题

**code：** *bool*型，默认为`False`

　　用于*设置是否以代码样式渲染标题内容*

**copyable：** *bool*型，默认为`False`

　　用于*设置是否为标题内容添加快捷复制功能*

**strikethrough：** *bool*型，默认为`False`

　　用于*设置是否以删除线模式渲染标题内容*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否以禁用状态渲染标题内容*

**mark：** *bool*型，默认为`False`

　　用于*设置是否以高亮标黄模式渲染标题内容*

**strong：** *bool*型，默认为`False`

　　用于*设置是否以加粗模式渲染标题内容*

**italic：** *bool*型，默认为`False`

　　用于*设置是否以斜体模式渲染标题内容*

**underline：** *bool*型，默认为`False`

　　用于*设置是否以下划线模式渲染标题内容*

**keyboard：** *bool*型，默认为`False`

　　用于*设置是否以键盘按键样式渲染标题内容*

**type：** *string*型

　　用于*设置标题内容的整体状态类型*，本质上是对标题内容的颜色进行预设，可选的有`'secondary'`、`'success'`、`'warning'`及`'danger'`，默认为`None`即无状态