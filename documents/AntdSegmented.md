**options：** *list*型

　　用于定义组内每个选项相关参数，每个选项由字典定义，可用的键有：

- label：*str*型，用于设置当前选择框显示的*文本内容*
- value：*str*或*int*型，用于设置当前选择框对应值
- disabled：*bool*型，用于设置是否禁用当前选项

**block：** *bool*型，默认为`False`

　　用于*设置当前组件是否撑满父容器的宽度*

**disabled：** *bool*型，默认为`False`

　　用于设置是否*禁用组件*

**size：** *str*型，默认为`'middle'`

　　用于设置*组件尺寸大小*，可选的有`'large'`、`'middle'`与`'small'`

**defaultValue：** *str*或*int*型

　　设置*默认选中*的选项对应`value`

**value：** *str*型

　　对应*当前已选中*的选项对应`value`