**message：** *string*型

　　用于设置通知提示框的*主要文字内容*

**description：** *string*型

　　可选，用于设置通知提示框的*辅助说明文字内容*

**type：** *string*型，默认为`'default'`

　　用于设置通知提示框的*状态类型*，可选的有`'default'`、`'success'`、`'error'`、`'info'`、`'warning'`

**placement：** *string*型，默认为`'topRight'`

　　用于设置通知提示框在整个屏幕中的弹出位置，可选的有`'topLeft'`、`'topRight'`、`'bottomLeft'`及`'bottomRight'`

**top：** *int*型

　　当通知提示框在顶部位置弹出时，用于设置通知提示框距离顶端的*像素距离*

**bottom：** *int*型

　　当通知提示框在底部位置弹出时，用于设置通知提示框距离底端的*像素距离*

**duration：** *int*型，默认为`4.5`

　　用于设置通知提示框从显示到自动消失经历的时长（单位：秒），当传入`None`时，则通知提示框不会自动消失，只能由用户点击关闭按钮手动关闭

