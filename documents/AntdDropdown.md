**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**title：** *string*型

　　用于**设置下拉菜单触发元素的标题内容*

**buttonMode：** *bool*型，默认为`False`

　　用于*设置下拉菜单触发元素是否渲染为按钮的形式*

**buttonProps：** *dict*型

　　用于*在触发元素为按钮形式时配置按钮相关的参数*，可用的键值对参数有：

- **size：** *string*型，默认为`'middle'`，用于*设置触发按钮的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`
- **type：** *string*型，默认为`'default'`，用于*设置触发按钮的风格*，可选项有`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`、`'default'`
- **danger：** *bool*型，默认为`False`，用于*设置是否渲染为危险警告状态*

**freePosition：** *bool*型，默认为`False`

　　用于*设置是否强制开启自由位置模式*

**freePositionStyle：** *dict*型

　　当`freePosition=True`时，用于*调整下拉菜单的位置等样式*

**freePositionClassName：** *string*型

　　当`freePosition=True`时，用于*设置下拉菜单的css类*

**clickedKey：** *string*型

　　用于*监听下拉菜单中最近一次被点击的选项对应key值*

**nClicks：** *int*型

　　用于*监听下拉菜单中所有选项累计被点击次数*，可用于辅助监听菜单项的重复点击事件

**menuItems：** `list[dict]`型

　　用于*定义下拉菜单选项结构*，其中列表每个元素均为字典，可用的键值对参数有：

- **title：** *string*型，用于*设置当前选项的标题内容*
- **href：** *string*型，用于*设置当前选项的链接url*
- **target：** *string*型，用于*设置当前选项的链接跳转行为*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*
- **icon：** *string*型，同`AntdIcon`中的同名参数，用于*设置当前选项的前缀图标*
- **key：** *string*型，用于*设置当前选项的唯一key值*
- **isDivider：** *bool*型，默认为`False`，用于*设置当前选项是否为水平分隔符*，设置为`True`后会忽略其他键值对参数

**arrow：** *bool*型，默认为`False`

　　用于*设置是否为展开的下拉菜单渲染连接箭头*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**overlayClassName：** *string*或*dict*型

　　用于*设置下拉菜单容器的类名*，支持[动态css](/advanced-classname)

**overlayStyle：** *string*型

　　用于*设置下拉菜单容器的css样式*

**placement：** *string*型，默认为`'bottomLeft'`

　　用于*设置下拉菜单的展开方向*，可选的有`'bottomLeft'`、`'bottomCenter'`、`'bottomRight'`、`'topLeft'`、`'topCenter'`及`'topRight'`

**trigger：** *string*型，默认为`'hover'`

　　用于*设置触发下拉菜单展开的触发方式*，可选的有`'hover'`及`'click'`

**autoAdjustOverflow：** *bool*型，默认为`True`

　　用于*设置当下拉菜单被遮挡时是否自动调整位置*

**visible：** *bool*型，默认为`False`

　　用于*设置下拉菜单是否显示*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题