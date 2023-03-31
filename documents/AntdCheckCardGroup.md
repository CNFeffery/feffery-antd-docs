**id：** *string*型

　　用于设置*当前组件的唯一id信息*

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

