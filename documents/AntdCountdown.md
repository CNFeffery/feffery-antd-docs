**title：** *string*型

　　用于设置*标题内容*

**value：** *string*型

　　用于设置要展示的*倒计时终点日期时间字符串*

**valueFormat：** *string*型，默认为`'YYYY-MM-DD hh:mm:ss'`

　　用于设置*倒计时终点日期格式*（[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)）

**format：** *string*型

　　用于设置*倒计时描述语句格式化字符串*，将`value`+`valueFormat`对应的时间点作为倒计时终点对倒计时进行描述，如`'还剩Y年M月D天H小时m分s秒'`

**valueStyle：** *dict*型

　　用于设置针对统计数值的*css样式*

**prefix：** *dict*型

　　用于为统计数值设置*前缀内容*，可用的键值对有：

- mode：*string*型，可选的有`'text'`（文字模式）和`'icon'`（图标模式）
- content：*string*型，**文字模式**下用于设置*前缀文字内容*；**图标模式**下用于传入适用于`AntdIcon`的所有`icon`参数值用于设置*前缀图标*

**suffix：** *dict*型

　　用于为统计数值设置*后缀内容*，可用的键值对有：

- mode：*string*型，可选的有`'text'`（文字模式）和`'icon'`（图标模式）
- content：*string*型，**文字模式**下用于设置*后缀文字内容*；**图标模式**下用于传入适用于`AntdIcon`的所有`icon`参数值用于设置*后缀图标*

