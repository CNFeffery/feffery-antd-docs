**message：** *string*型

　　用于设置警告提示的*主要文字内容*，当传入由字符串组成的列表时，可配合参数**renderLoopText**开启*文字轮播模式*

**description：** *string*或*list*型

　　可选，用于设置警告提示的*辅助说明文字内容*

**type：** *string*型，默认为`'info'`

　　用于设置警告提示的*状态类型*，可选的有`'info'`、`'success'`、`'warning'`及`'error'`

**showIcon：** *bool*型，默认为`False`

　　用于设置是否添加*状态图标*

**closable：** *bool*型，默认为`False`

　　用于设置是否为当前警告提示渲染*关闭按钮*

**renderLoopText：** *bool*型，默认为`False`

　　用于设置是否开启*文字轮播模式*，开启后会以*轮播*的方式展示参数**message**中所传入的字符串列表

