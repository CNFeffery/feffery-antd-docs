**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名，支持[动态css](/advanced-classname)*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**checked：** *bool*型

　　用于*设置或监听当前选择卡片的状态*

**defaultChecked：** *bool*型

　　用于*设置初始化时当前选择卡片的状态*

**bordered：** *bool*型，默认为`True`

　　用于*设置是否为当前选择卡片渲染轮廓*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前选择卡片*

**size：** *string*型，默认为`'default'`

　　用于*设置当前选择卡片的尺寸规格*，可选的有`'small'`、`'default'`、`'large'`

**value：** *int*、*float*或*string*型

　　配合`AntdCheckCardGroup`使用，用于*设置当前选择卡片对应的值*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['checked']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'checked'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）