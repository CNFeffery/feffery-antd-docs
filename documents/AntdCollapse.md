**id：** *string*型

　　用于设置*当前组件的唯一id信息*

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