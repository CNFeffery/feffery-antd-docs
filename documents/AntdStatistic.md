**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**value：** *int*、*float*或*组件型*

　　用于*设置要展示的数值信息*，也可直接传入其他元素作为内容，典型应用场景如传入`fuc.FefferyCountUp()`实现数字递增动画

**showGroupSeparator：** *bool*型，默认为`True`

　　用于*设置针对数值型的value输入是否展示千位分割符*

**precision：** *int*型

　　用于*设置针对数值型value输入的数值精度限制*

**prefix：** *组件型*

　　用于*为数值信息添加前缀内容*

**suffix：** *组件型*

　　用于*为数值信息添加后缀内容*

**title：** *组件型*

　　用于*设置标题内容*

**titleTooltip：** *string*型

　　用于*设置标题后缀的悬停提示信息内容*

**valueStyle：** *dict*型

　　用于*设置数值信息的css样式*