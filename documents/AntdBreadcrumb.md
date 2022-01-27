**items：** *list*型

　　传入用于*构造面包屑结构*的数据，列表中元素为*dict*型，按顺序对应面包屑的不同层次节点，其中字典可用键值对参数有：

- title：*string*型，用于设置当前节点的*文字内容*
- href：*string*型，用于设置当前节对应的*链接url*
- target：*string*，用于设置当前节点链接的*跳转行为*
- icon：*string*型，同`AntdIcon`中同名参数，用于设置面包屑前缀图标
- menuItems：*list*型，当前节点需要渲染悬浮展开菜单时传入，列表中每个元素为字典，对应悬浮菜单中的一个选项，可用的键值对参数有：
  - title：*string*型，用于设置选项*文字内容*
  - href：*string*型，用于设置选项*链接url*
  - target：*string*型，用于设置选项*链接跳转行为*
  - disabled：*bool*型，默认为`False`，用于设置是否*禁用当前选项*
  - icon：*string*型，同`AntdIcon`中的同名参数，用于设置*当前选项前缀图标*

**separator：** *string*型，默认为`'/'`

　　用于自定义面包屑中各层级间的*分隔符*