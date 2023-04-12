**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**format：** *string*型

　　用于*设置当前时间范围选择框的日期解析格式*，具体见[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)

**disabled：** `list[bool]`型，默认为`[False, False]`

　　用于*分别设置是否禁用当前时间范围选择组件的开始时间和结束时间选择*，格式为`[是否禁用开始时间, 是否禁用结束时间]`

**hourStep：** *int*型，默认为`1`

　　用于*设置小时选择部分的选项间隔*

**minuteStep：** *int*型，默认为`1`

　　用于*设置分钟选择部分的选项间隔*

**secondStep：** *int*型，默认为`1`

　　用于*设置秒选择部分的选项间隔*

**use12Hours：** *bool*型，默认为`False`

　　用于*设置是否使用12小时制*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *list*型

　　用于*设置空白输入下的填充说明文字*，格式为`[开始时间空白填充文字, 结束时间空白填充文字]`

**placement：** *str*型，默认为`'bottomLeft'`

　　用于*设置下拉菜单的展开方向*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**value：** *list*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *list*型

　　用于*监听或设置初始化时的已选中值*

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户清空已选项*

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）