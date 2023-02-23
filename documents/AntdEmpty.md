**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**description：** *组件型*或*bool*型

　　用于*设置描述说明信息*，当设置为`False`时会隐藏描述说明信息

**image：** *string*型，默认为`'default'`

　　用于*设置空状态占位图片*，可选的有`'default'`、`'simple'`，也可以直接传入图片url地址实现自定义占位图

**imageStyle：** *dict*型

　　用于*设置占位图的css样式*