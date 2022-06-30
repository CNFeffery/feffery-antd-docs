**message：** *string*、*list*或*组件*型

　　用于设置警告提示的*主要文字内容*，亦可传入单个组件或多个组件构成的列表实现自由内容嵌套

**description：** *string*或*组件*型

　　可选，用于设置警告提示的*辅助说明文字内容*，亦可传入单个组件或多个组件构成的列表实现自由内容嵌套

**type：** *string*型，默认为`'info'`

　　用于设置警告提示的*状态类型*，可选的有`'info'`、`'success'`、`'warning'`及`'error'`

**showIcon：** *bool*型，默认为`False`

　　用于设置是否添加*状态图标*

**closable：** *bool*型，默认为`False`

　　用于设置是否为当前警告提示渲染*关闭按钮*

**messageRenderMode：** *string*型，默认为`'default'`

　　用于设置针对`message`的*渲染模式*，可选的有`'default'`、`'loop-text'`（轮播文字模式）以及`'marquee'`（跑马灯模式），其中`'loop-text'`模式需要`message`参数传入列表类型的多条字符串

