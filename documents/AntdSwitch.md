**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名，支持[动态css](/advanced-classname)*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**checked：** *bool*型，默认为`False`

　　用于*设置或监听当前开关是否开启*

**checkedChildren：** *组件型*

　　用于*设置开启状态下的标签内容*

**unCheckedChildren：** *组件型*

　　用于*设置关闭状态下的标签内容*

**size：** *string*型，默认为`'default'`

　　用于*设置当前组件的尺寸规格*，可选项有`'default'`、`'small'`

**loading：** *bool*型，默认为`False`

　　用于*设置是否渲染加载中状态*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['checked']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'checked'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）