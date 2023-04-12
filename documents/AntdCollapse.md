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

**title：** *组件型*

　　用于*设置当前折叠面板的标题内容*

**isOpen：** *bool*型，默认为`True`

　　用于*设置或监听当前折叠面板是否展开*

**bordered：** *bool*型，默认为`True`

　　用于*设置是否为当前组件渲染边框*

**showArrow：** *bool*型，默认为`True`

　　用于*设置是否显示箭头*

**ghost：** *bool*型，默认为`False`

　　用于*设置是否开启透明面板模式*

**collapsible：** *string*型

　　用于*设置折叠/展开触发策略*，可选的有`'header'`（仅标题内容部分触发）、`'disabled'`（禁用）

**forceRender：** *bool*型，默认为`False`

　　用于*设置当折叠面板初始化未展开时是否强制渲染内部子元素*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['isOpen']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'isOpen'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）