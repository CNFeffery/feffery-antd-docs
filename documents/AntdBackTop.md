**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**duration：** *int*或*float*型，默认为`0.45`

　　用于*设置回到顶部滚动过程耗时*，单位：秒

**visibilityHeight：** *int*型，默认为`400`

　　用于*设置当页面向下滚动到出现回到顶部按钮的像素距离阈值*

**containerId：** *string*型

　　用于*设置要绑定的局部容器id*

**containerSelector：** *string*型

　　优先级低于`containerId`，用于*传入js代码字符串进行目标局部容器的设置*