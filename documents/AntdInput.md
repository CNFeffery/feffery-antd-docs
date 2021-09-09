**mode：** *string*型，默认为`'default'`

　　用于设置要渲染的*输入框类型*，可选的有`'default'`（常规输入框）、`'search'`（带搜索功能的输入框）、`'text-area'`（文本域输入框）以及`'password'`（密码输入框），不同的输入框模式下，有些大同小异的参数设计

**placeholder：** *string*型

　　用于设置输入框无输入值时的*占位提示内容*

**size：** *string*，默认为`'middle'`

　　用于设置输入框的*尺寸规格*，可选的有`'small'`、`'middle'`及`'large'`

**addonBefore：** *string*型

　　仅在**mode='default'**情况下可用，用于为常规输入框设置*前缀文字说明*

**addonAfter：** *string*型

　　仅在**mode='default'**情况下可用，用于为常规输入框设置*后缀文字说明*

**allowClear：** *string*型，默认为`False`

　　在**mode='default'**、**mode='search'**及**mode='text-area'**情况下可用，用于设置是否在输入框内渲染*内容快速清空图标*

**bordered：** *string*型，默认为`True`

　　用于设置是否为输入框渲染边框线

**defaultValue：** *string*型

　　在**mode='default'**、**mode='search'**及**mode='text-area'**情况下可用，用于为输入框设置初始化时*预填充的文字内容*

**disabled：** *string*型，默认为`False`

　　用于设置是否*禁用*当前输入框

**maxLength：** *string*型

　　用于设置输入框允许输入的*最大字符数量*，默认无限制

**showCount：** *string*型，默认为`False`

　　仅在**mode='text-area'**情况下可用，用于设置是否显示*当前已输入字符数量*提示

**value：** *string*型

　　对应当前输入框内部已输入的内容

**nSubmit：** *int*型

　　用于记录光标在输入框中时，键盘*enter键被按下的次数*

**nClicksSearch：** *int*型

　　仅在**mode='search'**情况下可用，用于记录*搜索按钮被点击次数*









