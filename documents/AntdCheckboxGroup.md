**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**options：** `list[dict]`型

　　用于*定义选项*，每个字典表示一个选项，可用的键值对参数有：

- **label：** *组件型*，用于*设置当前选项的标签内容*
- **value：** *string*、*int*或*float*型，用于*设置当前选项对应的选中值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*

**value：** *list*型

　　用于*监听或设置当前已选中值*

