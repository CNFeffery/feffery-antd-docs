**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**dataSource：** `list[dict]`型

　　用于*定义穿梭框中的各个选项*，每个字典可用的键值对参数有：

- **key：** *string*或*int*型，用于*设置当前选项的唯一标识id*
- **title：** *组件型*，用于*设置当前选项的标题内容*

**height：** *string*型

　　用于*设置当前穿梭框的高度*，接受`css`中合法的`height`输入值

**pagination：** *bool*或*dict*型，默认为`False`

　　用于*为穿梭框中的选项显示配置翻页功能*，当传入*dict*型时，可用的键值对参数有：

- **pageSize：** *int*型，用于*设置每页记录数*

**operations：** `list[string]`型，默认为`['', '']`

　　用于*分别设置左右移项操作按钮的文本内容*

**showSearch：** *bool*型，默认为`False`

　　用于*设置是否渲染搜索框*

**optionFilterMode：** *string*型，默认为`'case-insensitive'`

　　用于*设置输入框搜索的匹配模式*，可选的有`'case-insensitive'`（大小写不敏感）、`'case-sensitive'`（大小写敏感）、`'regex'`（正则表达式）

**showSelectAll：** *bool*型，默认为`True`

　　用于*设置是否渲染全选框*

**titles：** `list[组件]`型

　　用于*分别设置左右两边的穿梭框标题内容*

**targetKeys：** *list*型

　　用于*设置或监听处于穿梭框右侧区域内的选项key值*

**moveDirection：** *string*型

　　用于*监听最近一次移项操作对应的方向*，有`'left'`、`'right'`两种情况

**moveKeys：** *list*型

　　用于*监听最近一次移项操作涉及的选项key值*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['targetKeys']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'targetKeys'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）