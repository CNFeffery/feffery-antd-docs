**picker：** *string*型，默认为`'date'`

　　用于设置日期选择的粒度，可选项有`'date'`（精确到天），`'week'`（精确到周），`'month'`（精确到月），`'quarter'`（精确到季度），`'year'`（精确到年）

**showTime：** *bool*型，默认为`False`

　　用于设置是否显示额外的时间选择界面，`True`（显示），`False`（不显示）

**allowClear：** *bool*型，默认为`True`

　　设置是否显示输入框内容清除按钮，`True`（显示），`False`（不显示）

**format：** *string*型

　　用于设置*日期格式*（[参考资料](https://momentjscom.readthedocs.io/en/latest/moment/04-displaying/01-format/)），当`showTime=False`时默认值为`'YYYY-MM-DD'`，当`showTime=True`时默认值为`'YYYY-MM-DD hh:mm:ss'`

**placeholder：** `list[string, string]`型

　　用于设置空白输入下开始与结束输入框的*填充说明文字*

**defaultPickerValue：** *string*型

　　用于设置日期面板默认处于的*日期位置*，需要与`format`参数一致

**bordered：** *bool*型，默认为`True`

　　用于设置是否显示部件外边框，`True`（显示），`False`（不显示）

**value：** `list[string, string]`型

　　用于在回调中捕获用户选中的开始及结束*日期或日期时间字符串*

**defaultValue：** `list[string, string]`型

　　用于设置初始化时默认选中的开始及结束*日期或日期时间字符串*

**size：** *string*型，默认为`'middle'`

　　用于设置组件尺寸规格大小，可选的有`'small'`、`'middle'`与`'large'`

**disabled：** `list[bool, bool]`型，默认为`False`

　　设置是否禁用*输入框*

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`

**disabledDatesStrategy：** `list[dict]`型

　　用于自定义日期禁用策略，每个字典用于定义单条策略，满足至少一条策略的日期将会被禁用，可用的键值对参数有：

- **mode：** *str*型，用于定义当前策略类型，可选的有`'eq'`（等于）、`'ne'`（不等于）、`'le'`（小于等于）、`'lt'`（小于）、`'ge'`（大于等于）、`'gt'`（大于）、`'in'`（属于）、`'not-in'`（不属于）、`'in-enumerate-dates'`（属于日期字符串枚举数组）、`'not-in-enumerate-dates'`（不属于日期字符串枚举数组）
- **target：** *str*型，用于定义当前策略约束目标，可选的有`'day'`（按日）、`'month'`（按月份）、`'quarter'`（按月份）、`'year'`（按年）、`'dayOfYear'`（按当年第n天）、`'dayOfWeek'`（按当周第n天）
- **value：** `int、list[int]或list[str]`型，用于为当前约束策略定义对应的约束值，带有`'in'`的策略需要接受列表类型输入