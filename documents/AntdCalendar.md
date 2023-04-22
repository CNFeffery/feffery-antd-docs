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

**size：** *string*型，默认为`'default'`

　　用于*设置当前组件的尺寸规格*，可选项有`'default'`和`'large'`

**value：** *string*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *string*型

　　用于*监听或设置初始化时的已选中值*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）