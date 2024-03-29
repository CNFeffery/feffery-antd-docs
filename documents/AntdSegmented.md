**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**options：** `list[dict]`型

　　用于*定义选项*，每个字典表示一个选项，可用的键值对参数有：

- **label：** *组件型*，必填，用于*设置当前选项的标签内容*
- **value：** *int*、*float*或*string*型，必填，用于*设置当前选项对应的选中值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*
- **icon：** *string*型，用于*设置当前选项的前缀图标*，同`AntdIcon`中的同名参数
- **iconRenderer：** *string*型，默认为`'AntdIcon'`，用于*为当前选项的前缀图标设置渲染方式*，可选的有`'AntdIcon'`（内置图标）、`'fontawesome'`（基于css类名渲染）

**value：** *int*、*float*或*string*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *int*、*float*或*string*型

　　用于*设置初始化时的已选中值*

**block：** *bool*型，默认为`False`

　　用于*设置当前分段控制器是否撑满父容器宽度*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选的有`'small'`、`'middle'`、`'large'`

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）