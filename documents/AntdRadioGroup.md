**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**direction：** *string*型，默认为`'horizontal'`

　　用于*设置单选框的选项排列方向*，可选的有`'horizontal'`、`'vertical'`

**options：** `list[dict]`型

　　用于*定义选项*，每个字典表示一个选项，可用的键值对参数有：

- **label：** *组件型*，用于*设置当前选项的标签内容*
- **value：** *string*、*int*或*float*型，用于*设置当前选项对应的选中值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**size：** *string*型，默认为`'middle'`

　　当`optionType='button'`时，用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**value：** *string*、*int*或*float*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *string*、*int*或*float*型

　　用于*监听或设置初始化时的已选中值*

**optionType：** *string*型，默认为`'default'`

　　用于*设置选项的样式类型*，可选的有`'default'`、`'button'`

**buttonStyle：** *string*型，默认为`'outline'`

　　当`optionType='button'`时，用于*设置按钮的样式风格*，可选的有`'outline'`、`'solid'`

