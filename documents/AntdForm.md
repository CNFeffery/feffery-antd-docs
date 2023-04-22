**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**layout：** *string*型，默认为`'horizontal'`

　　用于*设置表单布局模式*，可选的有`'horizontal'`、`'vertical'`与`'inline'`

**labelCol：** *dict*型

　　用于*整体设置当前表单中各个表单项标签部分的列宽相关属性*，具体参数同`AntdFormItem`中的同名参数，优先级低于`AntdFormItem`中单独设置的`labelCol`参数

**wrapperCol：** *dict*型

　　用于*整体设置当前表单中各个表单项控件部分的列宽相关属性*，具体参数同`AntdFormItem`中的同名参数，优先级低于`AntdFormItem`中单独设置的`wrapperCol`参数

**colon：** *bool*型，默认为`True`

　　用于*整体设置其下所有表单项标签是否添加后缀冒号*，仅在`layout='horizontal'`时可用

**labelAlign：** *string*型，默认为`'right'`

　　用于*整体设置其下所有表单项标签内容对齐方式*，可选的有`'left'`与`'right'`