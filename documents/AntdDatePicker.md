**picker：** *string*型，默认为`'date'`

　　用于设置日期选择的粒度，可选项有`'date'`（精确到天），`'week'`（精确到周），`'month'`（精确到月），`'quarter'`（精确到季度），`'year'`（精确到年）

**showTime：** *bool*型，默认为`False`

　　用于设置是否显示额外的时间选择界面，`True`（显示），`False`（不显示）

**allowClear：** *bool*型，默认为`True`

　　设置是否显示输入框内容清除按钮，`True`（显示），`False`（不显示）

**format：** *string*型

　　用于设置*日期格式*（[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)），当`showTime=False`时默认值为`'YYYY-MM-DD'`，当`showTime=True`时默认值为`'YYYY-MM-DD hh:mm:ss'`

**defaultPickerValue：** *string*型

　　用于设置日期面板默认处于的*日期位置*，需要与`format`参数一致

**placeholder：** *string*型

　　用于设置空白输入下的*填充说明文字*

**bordered：** *bool*型，默认为`True`

　　用于设置是否显示部件外边框，`True`（显示），`False`（不显示）

**value：** *string*型

　　用于在回调中捕获用户选中的*日期或日期时间字符串*

**defaultValue：** *string*型

　　用于设置初始化时默认选中的*日期或日期时间字符串*

**size：** *string*型，默认为`'middle'`

　　用于设置组件尺寸规格大小，可选的有`'small'`、`'middle'`与`'large'`

**disabled：** `list[bool, bool]`型，默认为`False`

　　设置是否*禁用当前组件*

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`