**size：** *string*，默认为`'middle'`

　　用于设置*组件整体尺寸规格*，可选的有`'small'`、`'middle'`及`'large'`

**bordered：** *string*型，默认为`True`

　　用于设置*是否显示组件整体外边框线*

**disabled：** *string*型，默认为`False`

　　用于设置*是否禁用整个组件*

**controls：** *bool*型，默认为`True`

　　设置是否为每个数字输入框右侧边渲染*加减数值按钮*

**keyboard：** *bool*型，默认为`True`

　　设置*是否为每个数字输入框启用键盘快捷方式*，即当光标在输入框内时，可通过按下键盘上下键来调节输入的数值

**placeholder：** *string*型

　　用于*为所有数字输入框设置统一的输入框占位提示信息*

**min：** *int*、*float*或*string*型

　　用于设置*每个数字输入框允许输入的数值下限*

**max：** *int*、*float*或*string*型

　　用于设置*每个数字输入框允许输入的数值上限*

**step：** *int*、*float*或*string*型，默认为`1`

　　用于设置*数字输入框数值改变的步长*

**precision：** *int*型

　　用于设置数值*精度*

**readOnly：** *bool*型，默认为`False`

　　设置是否*以只读模式渲染组件*

**breakpoints：** `list[int]`或`list[float]`型

　　用于设置及监听*分段断点值*

**colors：** `list[string]`型

　　用于设置*对应每个分段的css颜色值*，长度为`breakpoints`长度-1

**inputNumberStyle：** *dict*型

　　用于统一设置*每个数字输入框的css样式*

**colorBlockStyle：** *dict*型

　　用于统一设置*每个填充色块的css样式*

**colorBlockPosition：** *string*型，默认为`'right'`

　　用于设置*填充色块相对输入框的方位*，可选的有`'left'`、`'right'`