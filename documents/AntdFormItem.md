**children：**

　　用于*传入对应的表单输入类组件*

**required：** *bool*型，默认为`False`

　　用于设置是否*为当前表单项的标签添加必填标识*

**labelCol：** *dict*型

　　用于*配置当前表单项的标签宽度属性*，可用键值对参数有：

- span：*int*型，同`AntdCol`中的同名参数，用于设置*标签部分在当前表单项中所占据的宽度份数*
- offset：*int*型，同`AntdCol`中的同名参数，用于设置*标签部分的平移宽度份数*

**colon：** *bool*型，默认为`True`

　　用于设置*是否在当前表单项标签后添加冒号*

**wrapperCol：** *dict*型

　　用于*配置当前表单项的输入控件部分宽度属性*，可用的键值对属性有：

- span：*int*型，同`AntdCol`中的同名参数，用于设置*输入控件部分在当前表单项中所占据的宽度份数*
- offset：*int*型，同`AntdCol`中的同名参数，用于设置*输入控件部分的平移宽度份数*

**label：** *string*型

　　用于设置*当前表单项的标签文字内容*

**labelAlign：** *string*型，默认为`'right'`

　　用于设置*当前表单项标签文字对齐方式*，可选的有`'left'`与`'right'`

**tooltip：** *string*型

　　用于设置*在当前表单项后添加的悬浮提示框文本内容*

**extra：** *string*型

　　用于设置*当前表单项的额外提示信息文本内容*

**validateStatus：** *string*型

　　用于*设置当前表单项的校验状态*，可选的有`'success'`、`'warning'`、`'error'`与`'validating'`

**help：** *string*型

　　用于设置*触发校验状态时显示出的提示文字信息*，用于配合不同的校验状态反馈给用户信息提示

**hidden：** *bool*型，默认为`False`

　　用于设置*是否隐藏当前表单项*