**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**autoSize：** *bool*或*dict*型，默认为`False`

　　用于*配置针对输入内容的输入框自适应高度功能*，当传入*dict*型输入时，可用的键值对参数有：

- **minRows：** *int*型，用于*设置最小行数*
- **maxRows：** *int*型，用于*设置对大行数*

**prefix：** *string*型，默认为`'@'`

　　用于*设置触发子项菜单弹出的关键字*

**value：** *list*型

　　用于*监听或设置当前已输入值*

**defaultValue：** *list*型

　　用于*监听或设置初始化时的已输入值*

**options：** `list[dict]`型，必填

　　用于*定义子项菜单中的选项*，其中每个字典可用的键值对参数有：

- **label：** *组件型*，用于*设置当前选项的标签内容*
- **value：** *string*型，用于*设置当前选项对应的值*

**selectedOptions：** *list*型

　　用于*监听当前提及组件中已被提及的选项值*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**placement：** *str*型，默认为`'bottom'`

　　用于*设置子项菜单的展开方向*，可选的有`'bottom'`、`'top'`

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题