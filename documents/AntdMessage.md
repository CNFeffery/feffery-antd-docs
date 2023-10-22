**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**content：** *string*型

　　用于*设置消息提示内的文字内容*

**type：** *string*型，默认为`'default'`

　　用于*设置消息提示的类型*，可选的有`'default'`、`'success'`、`'error'`、`'info'`、`'warning'`

**duration：** *int*或*float*型，默认为`3`

　　用于*设置消息提示从开始显示到自动消失的延时时长*，单位：秒

**top：** *int*型，默认为`8`

　　用于*设置消息提示默认距离顶端的像素距离*

**maxCount：** *int*型

　　用于*设置全局允许同时显示的提示框数量*，默认无限制

**icon：** *string*型

　　用于*自定义消息提示前缀图标*，同`AntdIcon`中的同名参数

**iconRenderer：** *string*型，默认为`'AntdIcon'`

　　用于*为自定义消息提示前缀图标设置渲染方式*，可选的有`'AntdIcon'`（内置图标）、`'fontawesome'`（基于css类名渲染）