**message：** *string*或*list*型

　　用于设置警告提示的*主要文字内容*，可传入**列表**格式的其他组件（传入的组件类内容暂不支持作为回调角色，仅用作内容展示用）

**description：** *string*或*list*型

　　可选，用于设置警告提示的*辅助说明文字内容*，可传入**列表**格式的其他组件（传入的组件类内容暂不支持作为回调角色，仅用作内容展示用）

**type：** *string*型，默认为`'info'`

　　用于设置警告提示的*状态类型*，可选的有`'info'`、`'success'`、`'warning'`及`'error'`

**showIcon：** *bool*型，默认为`False`

　　用于设置是否添加*状态图标*

**closable：** *bool*型，默认为`False`

　　用于设置是否为当前警告提示渲染*关闭按钮*

**messageRenderMode：** *string*型，默认为`'default'`

　　用于设置针对`message`的*渲染模式*，可选的有`'default'`、`'loop-text'`（轮播文字模式）以及`'marquee'`（跑马灯模式），其中`'loop-text'`模式需要`message`参数传入列表类型的多条字符串

