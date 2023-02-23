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

- **label：** *组件型*，必填，用于*设置当前选项的标签内容*
- **value：** *int*、*float*或*string*型，必填，用于*设置当前选项对应的选中值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*
- **icon：** *string*型，用于*设置当前选项的前缀图标*，同`AntdIcon`中的同名参数

**value：** *int*、*float*或*string*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *int*、*float*或*string*型

　　用于*设置初始化时的已选中值*

**block：** *bool*型，默认为`False`

　　用于*设置当前分段控制器是否撑满父容器宽度*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选的有`'small'`、`'middle'`、`'large'`