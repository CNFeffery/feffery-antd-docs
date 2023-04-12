**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户重复点击评分以清除已有评分*

**allowHalf：** *bool*型，默认为`False`

　　用于*设置是否允许半星选择*

**count：** *int*型，默认为`5`

　　用于*设置星星总数量*

**tooltips：** `list[string]`型

　　用于*为每个星级设置鼠标悬停提示文字内容*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**value：** *int*或*float*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *int*或*float*型

　　用于*监听或设置初始化时的已选中值*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）