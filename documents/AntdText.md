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

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**code：** *bool*型，默认为`False`

　　用于*设置是否以代码样式渲染文字内容*

**copyable：** *bool*型，默认为`False`

　　用于*设置是否为文字内容添加快捷复制功能*

**strikethrough：** *bool*型，默认为`False`

　　用于*设置是否以删除线模式渲染文字内容*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否以禁用状态渲染文字内容*

**mark：** *bool*型，默认为`False`

　　用于*设置是否以高亮标黄模式渲染文字内容*

**strong：** *bool*型，默认为`False`

　　用于*设置是否以加粗模式渲染文字内容*

**italic：** *bool*型，默认为`False`

　　用于*设置是否以斜体模式渲染文字内容*

**underline：** *bool*型，默认为`False`

　　用于*设置是否以下划线模式渲染文字内容*

**keyboard：** *bool*型，默认为`False`

　　用于*设置是否以键盘按键样式渲染文字内容*

**type：** *string*型

　　用于*设置文字内容的整体状态类型*，本质上是对文字内容的颜色进行预设，可选的有`'secondary'`、`'success'`、`'warning'`及`'danger'`，默认为`None`即无状态

**ellipsis：** *bool*或*dict*型，默认为`False`

　　用于*设置是否开启内容省略功能*，当传入字典型时，可用的键值对参数有：

- **suffix：** *string*型，用于*设置省略内容额外后缀*