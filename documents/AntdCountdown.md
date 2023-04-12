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

**format：** *string*型

　　用于*设置当前倒计时组件倒计时内容的日期时间格式模板*，具体见[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)

**value：** *string*型

　　用于*设置目标截止日期的日期时间字符串*

**valueFormat：** *string*型，默认为`'YYYY-MM-DD hh:mm:ss'`

　　用于*设置针对value进行日期时间格式解析的参照格式*，具体见[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)

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