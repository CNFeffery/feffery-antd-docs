**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**message：** *string*型

　　用于*设置当前通知提醒框的主要信息内容*

**description：** *string*型

　　用于*设置当前通知提醒框的次要信息内容*

**type：** *string*型，默认为`'default'`

　　用于*设置当前通知提醒框的状态类型*，可选的有`'default'`、`'success'`、`'error'`、`'info'`、`'warning'`

**placement：** *string*型，默认为`'topRight'`

　　用于*设置当前通知提醒框的弹出位置*，可选的有`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`

**top：** *int*型，默认为`24`

　　当通知提醒框从页面顶部弹出时，用于*设置到顶部的像素距离*

**bottom：** *int*型，默认为`24`

　　当通知提醒框从页面底部弹出时，用于*设置其到底部的像素距离*

**duration：** *int*或*float*型，默认为`4.5`

　　用于*设置当前通知提醒框从显示到消失的延时时长*，单位：秒

**closable：** *bool*型，默认为`True`

　　用于*设置是否为当前通知提醒框添加关闭按钮*