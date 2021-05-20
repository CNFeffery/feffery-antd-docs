**type：** *string*型，默认为`'default'`

　　用于设置按钮整体风格，可选项有`'primary'`、`'dashed'`、`'link'`、`'text'`、`'default'`

**href：** *string*型

　　当传入*url*时，可使得`AntdButton`充当类似`a`标签的网页跳转作用

**target：** *string*型

　　当`href`参数有合法*url*传入时，用于设置跳转动作类型，[参考资料](https://www.w3school.com.cn/tags/att_a_target.asp)

**block：** *bool*型，默认为`False`

　　用于设置按钮宽度是否撑满父级元素，`True`（撑满），`False`（不撑满）

**danger：** *bool*型，默认为`False`

　　用于设置是否显示为*危险警告*状态，`True`（显示），`False`（不显示）

**disabled：** *bool*型，默认为`False`

　　用于设置是否显示为*不可点击*状态，`True`（显示），`False`（不显示）

**shape：** *string*型或*None*，默认为`None`

　　用于设置按钮形状，可选项有`'circle'`（原型）、`'round'`（圆角矩形）

**nClicks：** *int*型

　　用于在回调中记录按钮被点按次数，初始化为0