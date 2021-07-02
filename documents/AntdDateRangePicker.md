**picker：** *string*型，默认为`'date'`

　　用于设置日期选择的粒度，可选项有`'date'`（精确到天），`'week'`（精确到周），`'month'`（精确到月），`'quarter'`（精确到季度），`'year'`（精确到年）

**showTime：** *bool*型，默认为`False`

　　用于设置是否显示额外的时间选择界面，`True`（显示），`False`（不显示）

**placeholderStart：** *string*型

　　空白输入下开始输入框的填充说明文字

**placeholderEnd：** *string*型

　　空白输入下结束输入框的填充说明文字

**disabledStart：** *bool*型，默认为`False`

　　设置是否禁用*开始输入框*

**disabledEnd：** *bool*型，默认为`False`

　　设置是否禁用*结束输入框*

**defaultPickerValue：** *dict*型，必填，无默认值

　　用于设置日期面板默认处于的日期位置，包含键值对`'value'`与`'format'`，均为*string*型，其中`'value'`用于设定日期值，`'format'`用于设置相对应的日期格式（[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)），例如：

```Python
defaultPickerValue = {
    'value': '2020/01/01', 
    'format': 'YYYY/MM/DD'
}
```

**bordered：** *bool*型，默认为`True`

　　用于设置是否显示部件外边框，`True`（显示），`False`（不显示）

**selectedStartDate：** *string*型

　　用于在回调中捕获用户选中的开始日期或开始日期时间字符串

**selectedEndDate：** *string*型

　　用于在回调中捕获用户选中的结束日期或结束日期时间字符串

