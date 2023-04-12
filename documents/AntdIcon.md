**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**icon：** *string*型

　　用于*设置要渲染图标的名称*

**nClicks：** *int*型，默认为`0`

　　用于*在回调中记录图标被点按次数*

**debounceWait：** *int*型，默认为`200`

　　用于*为nClicks的监听更新设置防抖延时时长*，单位：毫秒
