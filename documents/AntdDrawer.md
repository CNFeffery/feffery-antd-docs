**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**visible：** *bool*型，默认为`False`

　　用于*设置或监听当前抽屉的展开状态*

**title：** *组件型*

　　用于*设置当前抽屉的标题内容*

**placement：** *string*型，默认为`'right'`

　　用于*设置当前抽屉的展开方位*，可选的有`'left'`、`'right'`、`'top'`、`'bottom'`

**closable：** *bool*型，默认为`True`

　　用于*设置是否为当前抽屉渲染关闭按钮*

**forceRender：** *bool*型，默认为`False`

　　用于*设置在抽屉初始化关闭时是否预先渲染内部元素*

**destroyOnClose：** *bool*型，默认为`False`

　　用于*设置在抽屉被关闭后是否销毁内部元素*

**width：** *int*、*float*或*string*型，默认为`256`

　　当`placement`为`'left'`或`'right'`时，用于*设置当前抽屉的宽度*

**height：** *int*、*float*或*string*型，默认为`256`

　　当`placement`为`'top'`或`'bottom'`时，用于*设置当前抽屉的高度*

**mask：** *bool*型，默认为`True`

　　当抽屉展开时，用于*设置是否在抽屉以外区域渲染蒙版层*

**maskClosable：** *bool*型，默认为`True`

　　用于*设置是否可以通过点击蒙版层的方式关闭已展开的抽屉*

**zIndex：** *int*型，默认为`1000`

　　用于*设置当前抽屉的z-index属性*

**extra：** *组件型*

　　用于*为当前抽屉设置额外操作区元素*

**containerId：** *string*型

　　当需要抽屉在局部容器内展示时，用于*设置目标局部容器的id*，注意，该目标局部容器`position`需为`relative`



