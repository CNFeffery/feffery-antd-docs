**title：** *string*型

　　用于设置*标题内容*

**value：** *int*或*float*型

　　用于设置要展示的*统计数值*

**valueStyle：** *dict*型

　　用于设置针对统计数值的*css样式*

**showGroupSeparator：** *bool*型，默认为`True`

　　用于设置*是否针对数值添加千分位逗号标识符*

**precision：** *int*型

　　设置*要保留的小数位数*

**prefix：** *dict*型

　　用于为统计数值设置*前缀内容*，可用的键值对有：

- mode：*string*型，可选的有`'text'`（文字模式）和`'icon'`（图标模式）
- content：*string*型，**文字模式**下用于设置*前缀文字内容*；**图标模式**下用于传入适用于`AntdIcon`的所有`icon`参数值用于设置*前缀图标*

**suffix：** *dict*型

　　用于为统计数值设置*后缀内容*，可用的键值对有：

- mode：*string*型，可选的有`'text'`（文字模式）和`'icon'`（图标模式）
- content：*string*型，**文字模式**下用于设置*后缀文字内容*；**图标模式**下用于传入适用于`AntdIcon`的所有`icon`参数值用于设置*后缀图标*