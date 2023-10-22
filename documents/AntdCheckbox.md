**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**label：** *组件型*

　　用于*设置当前勾选框的标签内容*

**checked：** *bool*型，默认为`False`

　　用于*设置或监听当前勾选框是否被勾选*

**indeterminate：** *bool*型，默认为`False`

　　用于*控制当前选择框的样式是否强制为半选状态*，此参数仅作用于样式，与勾选情况无关

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['checked']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'checked'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）