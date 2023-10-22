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

**total：** *int*型

　　用于*设置总记录数量*，从而进行应有页数的推断

**defaultCurrent：** *int*型，默认为`1`

　　用于*设置初始化时的停留页码*

**defaultPageSize：** *int*型，默认为`10`

　　用于*设置初始化时的每页记录数量*

**current：** *int*型

　　用于*设置或监听当前所停留的页码*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**hideOnSinglePage：** *bool*型，默认为`False`

　　用于*设置是否在只有一页时自动隐藏分页组件*

**pageSize：** *int*型

　　用于*设置或监听当前每页记录数*

**pageSizeOptions：** `list[int]`型

　　用于*设置每页记录数选择器中的可选项*

**showSizeChanger：** *bool*型，默认为`False`

　　用于*设置是否渲染每页记录数选择器*

**showQuickJumper：** *bool*型，默认为`False`

　　用于*设置是否开启快速跳页功能*

**showLessItems：** *bool*型，默认为`False`

　　用于*设置是否展示较少的跳页按钮*

**showTotalPrefix：** *str*型，默认为`'共 '`

　　用于*设置总记录行数前缀文字*

**showTotalSuffix：** *str*型，默认为`' 条记录'`

　　用于*设置总记录行数后缀文字*

**showTotal：** *bool*型，默认为`True`

　　用于*设置是否展示总记录行数文案信息*

**simple：** *bool*型，默认为`False`

　　用于*设置是否开启极简模式*

**size：** *str*型，默认为`'default'`

　　用于*设置当前组件的尺寸规格*，可选的有`'default'`、`'small'`

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['current', 'pageSize']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'current'`、`'pageSize'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）