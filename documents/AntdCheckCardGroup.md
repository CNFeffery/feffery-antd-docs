**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的各个选择卡片*

**multiple：** *bool*型，默认为`False`

　　用于*设置是否允许多选*

**bordered：** *bool*型，默认为`True`

　　用于*设置是否为内部各个选择卡片渲染轮廓*

**value：** *int*、*float*、*string*或*list*型

　　用于*设置或监听当前已选中的选择卡片对应的值*

**defaultValue：** *int*、*float*、*string*或*list*型

　　用于*设置初始化时已选中的选择卡片对应的值*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否对当前组合选择卡片进行整体禁用*

**size：** *string*型，默认为`'default'`

　　用于*设置当前组合选择卡片的整体尺寸规格*，可选的有`'small'`、`'default'`、`'large'`

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）