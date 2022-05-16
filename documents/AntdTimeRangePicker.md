**format：** *string*型，默认为`'HH:mm:ss'`

　　用于设置*时间格式*（[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)）

**hourStep：** *int*型，默认为`1`

　　用于设置*小时选项粒度*

**minuteStep：** *int*型，默认为`1`

　　用于设置*分钟选项粒度*

**secondStep：** *int*型，默认为`1`

　　用于设置*秒选项粒度*

**use12Hours：** *bool*型，默认为`False`

　　用于设置*是否采用12小时制*，当设置为`True`时，`format`参数强制变更为`'h:mm:ss a'`

**placeholder：** `list[string, string]`型

　　用于设置空白输入下开始与结束输入框的*填充说明文字*

**bordered：** *bool*型，默认为`True`

　　用于设置是否显示部件外边框，`True`（显示），`False`（不显示）

**value：** `list[string, string]`型

　　用于在回调中捕获用户选中的开始及结束*时间字符串*

**defaultValue：** `list[string, string]`型

　　用于设置初始化时默认选中的开始及结束*时间字符串*

**size：** *string*型，默认为`'middle'`

　　用于设置组件尺寸规格大小，可选的有`'small'`、`'middle'`与`'large'`

**disabled：** `list[bool, bool]`型，默认为`False`

　　设置是否禁用*输入框*

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`