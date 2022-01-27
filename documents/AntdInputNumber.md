**placeholder：** *string*型

　　用于设置输入框无输入值时的*占位提示内容*

**size：** *string*，默认为`'middle'`

　　用于设置输入框的*尺寸规格*，可选的有`'small'`、`'middle'`及`'large'`

**addonBefore：** *string*型

　　用于为数字输入框设置*前缀文字说明*

**addonAfter：** *string*型

　　用于为数字输入框设置*后缀文字说明*

**bordered：** *string*型，默认为`True`

　　用于设置是否为输入框*渲染边框线*

**disabled：** *string*型，默认为`False`

　　用于设置是否*禁用*当前输入框

**controls：** *bool*型，默认为`True`

　　设置是否为数字输入框右侧边渲染*加减数值按钮*

**keyboard：** *bool*型，默认为`True`

　　设置是否启用*键盘快捷方式*，即当光标在`AntdInputNumber`内时，可通过按下键盘上下键来调节输入的数值

**stringMode：** *bool*型，默认为`False`

　　设置是否开启*字符值模式*，此模式是为了数字输入框传递高精度数值时不会因为编程语言自身的限制导致精度丢失，**请注意！**，字符值模式开启后，相关的参数都需变为*string*型

**min：** *int*、*float*或*string*型

　　用于设置允许输入的*数值下限*

**max：** *int*、*float*或*string*型

　　用于设置允许输入的*数值上限*

**step：** *int*、*float*或*string*型，默认为`1`

　　用于设置数值改变的*步长*

**precision：** *int*型

　　用于设置数值*精度*

**readOnly：** *bool*型，默认为`False`

　　设置是否*以只读模式渲染组件*

**value：** *string*型

　　对应当前输入框内部已输入的内容

**defaultValue：** *int*、*float*或*string*型

　　设置初始化时*输入框内部默认填入的内容*

**nSubmit：** *int*、*float*或*string*型

　　用于记录光标在输入框中时，键盘*enter键被按下的次数*
