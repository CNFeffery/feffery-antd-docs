**title：** *string*型

　　设置下拉菜单*触发点文字标题内容*

**buttonMode：** *bool*型，默认为`False`

　　设置下拉菜单触发点*是否渲染为按钮的形式*

**clickedKey：** *string*型

　　用于记录下拉菜单中*最近一次被点击的选项对应key值*

**nClicks：** *int*型

　　用于记录下拉菜单中各项*累计被点击次数*，可用于辅助监听菜单项的重复点击事件

**menuItems：** *list*型

　　传入*用于构建下拉菜单结构*的数据，其中列表每个元素均为字典，字典可用的键值对有：

- title：*string*型，用于设置当前选项*文字内容*
- href：*string*型，用于设置当前选项*链接url*
- target：*string*型，用于设置当前选项*链接跳转行为*
- disabled：*bool*型，默认为`False`，用于设置是否*禁用当前选项*
- icon：*string*型，同`AntdIcon`中的同名参数，用于设置当前选项*前缀图标*
- key：*string*型，用于设置当前下拉菜单下每个选项的*唯一key值*
- isDivider：*bool*型，默认为`False`，用于设置是否应当将当前选项*视作单纯的分隔符*，设置为`True`后会忽略其他键值对参数

**arrow：** *bool*型，默认为`False`

　　设置悬浮下拉框是否显示*连接箭头*

**disabled：** *bool*型，默认为`False`

　　设置是否*禁用当前组件*

**overlayClassName：** *string*型

　　用于设置悬浮菜单层*容器的类名*

**overlayStyle：** *string*型

　　用于设置悬浮菜单层*容器的css样式*

**placement：** *string*型，默认为`'bottomLeft'`

　　用于设置悬浮菜单层的*展开方向*，可选的有`'bottomLeft'`、`'bottomCenter'`、`'bottomRight'`、`'topLeft'`、`'topCenter'`及`'topRight'`

**trigger：** *string*型，默认为`'hover'`

　　用于设置触发下拉菜单展示的*触发事件*，可选的有`'hover'`及`'click'`

**visible：** *bool*型，默认为`False`

　　用于设置下拉菜单*是否显示*