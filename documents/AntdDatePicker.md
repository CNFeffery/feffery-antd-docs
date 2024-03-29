**id：** *string*或*dict*型

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

　　用于*设置当前日期选择框的日期解析格式*，具体见[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)

**picker：** *string*型，默认为`'date'`

　　用于*设置日期选择的粒度*，可选的有`'date'`、`'week'`、`'month'`、`'quarter'`、`'year'`

**firstDayOfWeek：** *int*型

　　用于*自定义每周的第一天*，如`1`表示周一

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**showTime：** *bool*或*dict*型，默认为`False`

　　用于*设置是否开启额外的时间选择功能*，当传入*dict*型输入时，会在开启时间选择功能的同时，自动设定默认选中的时间值，该默认时间值将会在用户点击选择完日期之后自动选中，其中可用的键值对参数有：

- **defaultValue：** *string*型，用于*设置时间字符串*
- **format：** *string*型，默认为`'HH:mm:ss'`，用于*设置与showTime.defaultValue对应的时间解析格式*，具体见[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *string*型

　　用于*设置空白输入下的填充说明文字*

**placement：** *str*型，默认为`'bottomLeft'`

　　用于*设置下拉菜单的展开方向*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**value：** *string*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *string*型

　　用于*监听或设置初始化时的已选中值*

**defaultPickerValue：** *string*型

　　用于*设置初始化时日期选择面板停留的日期位置*

**disabledDatesStrategy：** `list[dict]`型

　　用于*自定义日期禁用策略*，每个字典代表单条策略，满足至少一条策略的日期将会被禁用，可用的键值对参数有：

- **mode：** *str*型，用于*定义当前策略类型*，可选的有`'eq'`（等于）、`'ne'`（不等于）、`'le'`（小于等于）、`'lt'`（小于）、`'ge'`（大于等于）、`'gt'`（大于）、`'in'`（属于）、`'not in'`（不属于）、`'in-enumerate-dates'`（属于日期字符串枚举数组）、`'not-in-enumerate-dates'`（不属于日期字符串枚举数组）
- **target：** *str*型，用于*定义当前策略约束目标*，可选的有`'day'`（按日）、`'month'`（按月份）、`'quarter'`（按季度）、`'year'`（按年）、`'dayOfYear'`（按当年第n天）、`'dayOfWeek'`（按本周第n天）、`'specific-date'`（具体日期）
- **value：** *int*、*string*、`list[int]`或`list[str]`型，用于*为当前约束策略定义对应的约束值*，带有`'in'`的策略需要接受列表类型输入

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户清空已选项*

**autoFocus：** *bool*型，默认为`False`

　　用于*设置是否自动获取焦点*

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**showToday：** *bool*型，默认为`True`

　　用于*设置是否渲染“今天”快捷按钮*

**extraFooter：** *组件型*

　　用于*设置选择面板底部额外元素*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）