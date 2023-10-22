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

**required：** *bool*型，默认为`False`

　　用于*设置是否为当前表单项标签添加必填标识*

**labelCol：** *dict*型

　　用于*配置当前表单项的标签宽度属性*，可用的键值对参数有：

- **span：** *int*型，同`AntdCol`中的同名参数，用于*设置标签部分在当前表单项中所占据的宽度份数*
- **offset：** *int*型，同`AntdCol`中的同名参数，用于*设置标签部分向右平移的宽度份数*
- **flex：** *int*或*string*型，用于*基于css中的flex属性配置标签部分宽度*

**colon：** *bool*型，默认为`True`

　　用于*设置是否在当前表单项标签后添加冒号*

**wrapperCol：** *dict*型

　　用于*配置当前表单项的表单控件部分宽度属性*，可用的键值对参数有：

- **span：** *int*型，同`AntdCol`中的同名参数，用于*设置表单控件部分在当前表单项中所占据的宽度份数*
- **offset：** *int*型，同`AntdCol`中的同名参数，用于*设置表单控件部分向右平移的宽度份数*
- **flex：** *int*或*string*型，用于*基于css中的flex属性配置表单控件部分宽度*

**label：** *组件型*

　　用于*设置当前表单项的标签内容*

**labelAlign：** *string*型，默认为`'right'`

　　用于*设置当前表单项标签内容对齐方式*，可选的有`'left'`、`'right'`

**tooltip：** *组件型*

　　用于*设置在当前表单项标签内容后添加的悬浮提示框内容*

**extra：** *组件型*

　　用于*设置当前表单项的额外提示信息*

**validateStatus：** *string*型

　　用于*设置当前表单项的校验状态*，可选的有`'success'`、`'warning'`、`'error'`、`'validating'`

**help：** *组件型*

　　用于*设置触发校验状态时显示出的提示信息*，用于配合不同的校验状态反馈给用户信息提示

**hidden：** *bool*型，默认为`False`

　　用于设置*是否隐藏当前表单项*