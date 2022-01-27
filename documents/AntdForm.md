**children：**

 　　用于传入*当前表单下所包含的各个`AntdFormItem`*

**layout：** *string*型，默认为`'horizontal'`

　　用于*设置表单布局模式*，可选的有`'horizontal'`、`'vertical'`与`'inline'`

**labelCol：** *dict*型

　　用于*整体设置当前表单中各个表单项标签部分的列宽相关属性*，具体参数同`AntdFormItem`中的同名参数，这里不再赘述，但优先级低于`AntdFormItem`中单独设置的`labelCol`参数

**wrapperCol：** *dict*型

　　用于*整体设置当前表单中各个表单项输入控件部分的列宽相关属性*，具体参数同`AntdFormItem`中的同名参数，这里不再赘述，但优先级低于`AntdFormItem`中单独设置的`wrapperCol`参数

**colon：** *bool*型，默认为`True`

　　用于*整体设置其下所有表单项标签是否添加后缀冒号*

**labelAlign：** *string*型，默认为`'right'`

　　用于*整体设置其下所有表单项标签的文本对齐方式*，可选的有`'left'`与`'right'`