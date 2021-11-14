**options：** *list*型

　　用于定义组内每个选项相关参数，每个选项由字典定义，可用的键有：

- label：*str*型，用于设置当前选择框显示的*文本内容*
- value：*str*型，用于设置当前选择框对应值
- disabled：*bool*型，用于设置是否禁用当前选项

**direction：** *str*型，默认为`'horizontal'`

　　用于设置组件的*排列方向*，可选的有`'horizontal'`与`'vertical'`

**optionType：** *str*型，默认为`'default'`

　　用于设置选项*渲染方式*，可选的有`'default'`与`'button'`

**buttonStyle：** *str*型，默认为`'outline'`

　　当`optionType='button'`开启按钮模式时，用于设置按钮的显示样式，可选的有`'outline'`与`'solid'`

**disabled：** *bool*型，默认为`False`

　　用于设置是否*禁用组件*

**size：** *str*型，默认为`'middle'`

　　当`optionType='button'`开启按钮模式时，用于设置*组件按钮尺寸大小*，可选的有`'large'`、`'middle'`与`'small'`

**defaultValue：** *str*型

　　设置*默认选中*的选项对应`value`

**value：** *str*型

　　对应*当前已选中*的选项对应`value`