**children：**

　　用于传入置于*对话框中的前端元素*

**visible：** *bool*型，默认为`False`

　　对应当前对话框*是否弹出*

**title：** *str*或*dict*型

　　设置对话框中的*标题内容*，可以传入纯文字，也可以传入具有下列键的字典：

- content：*str*型，设置文字内容
- prefixIcon：*str*型，设置标题前缀图标，可使用`AntdIcon`内置的所有图标

**okText：** *str*型

　　设置*确认按钮文字*

**okButtonProps：** *dict*型

　　设置*确认按钮的常用参数属性*，同`AntdButton`参数体系

**cancelText：** *str*型

　　设置*取消按钮文字*

**cancelButtonProps：** *dict*型

　　设置*取消按钮的常用参数属性*，同`AntdButton`参数体系

**renderFooter：** *bool*型，默认为`True`

　　设置是否*渲染对话框底部按钮区域*

**width：** *int*型

　　设置*对话框像素宽度*

**centered：** *bool*型，默认为`False`

　　设置*是否垂直居中显示对话框*

**keyboard：** *bool*型，默认为`True`

　　设置是否允许键盘`esc`键*触发对话框的关闭操作*

**closable：** *bool*型，默认为`True`

　　设置是否*在对话框右上角渲染关闭按钮*

**mask：** *bool*型，默认为`True`

　　设置是否*显示背景蒙版*

**maskClosable：** *bool*型，默认为`True`

　　设置*点击背景蒙版是否可触发对话框关闭*

**okCounts：** *int*型

　　对应对话框的*确认按钮累计被点击的次数*

**cancelCounts：** *int*型

　　对应对话框的*取消按钮累计被点击的次数*

**closeCounts：** *int*型

　　对应对话框的*累计被关闭次数*