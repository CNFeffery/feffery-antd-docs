**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**items：** `list[dict]`型

　　用于*定义面包屑结构*，每个*dict*型元素，按顺序对应面包屑的不同层次节点，其中可用的键值对参数有：

- **title：** *string*型，用于*设置当前节点的文字内容*
- **href：** *string*型，用于*设置当前节对应的链接url*
- **target：** *string*，用于*设置当前节点链接的跳转行为*
- **icon：** *string*型，同`AntdIcon`中同名参数，用于*设置面包屑前缀图标*
- **menuItems：** `list[dict]`型，用于*为当前节点渲染悬浮展开菜单*，列表中每个*dict*型元素对应悬浮菜单中的一个选项，可用的键值对参数有：
  - **title：** *string*型，用于设置*当前选项的文字内容*
  - **href：** *string*型，用于设置*当前选项的链接url*
  - **target：** *string*型，用于设置*当前选项的链接跳转行为*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*
  - **icon：** *string*型，同`AntdIcon`中的同名参数，用于*设置当前选项的前缀图标*

**separator：** *组件型*，默认为`'/'`

　　用于*自定义面包屑中各层级间的分隔符*