**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**message：** *组件型*

　　用于*为当前警告提示设置主要信息内容*

**description：** *组件型*

　　用于*为当前警告提示设置次要信息内容*

**type：** *string*型，默认为`'info'`

　　用于*为当前警告提示设置状态类型*，可选的有`'success'`、`'info'`、`'warning'`、`'error'`

**showIcon：** *bool*型，默认为`False`

　　用于*设置是否为当前警告提示添加状态图标*

**closable：** *bool*型，默认为`False`

　　用于*设置当前警告提示是否可关闭*

**messageRenderMode：** *string*型，默认为`'default'`

　　用于*设置当前警告提示的渲染模式*，可选的有`'default'`、`'loop-text'`（轮播模式）、`'marquee'`（走马灯模式），其中`'loop-text'`模式下需要参数`message`输入数组格式

**action：** *组件型*

　　用于*为当前警告提示设置右上角额外内容*

**banner：** *组件型*，默认为`False`

　　用于*设置是否开启顶部公告模式*