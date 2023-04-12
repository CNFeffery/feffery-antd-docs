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

**align：** *string*型

　　用于*设置内部嵌套元素的对齐方式*，可选的有`'start'`、`'end'`、`'center'`、`'baseline'`

**direction：** *string*型，默认为`'horizontal'`

　　用于*设置内部元素的排列方向*，可选的有`'vertical'`（竖直排列）及`'horizontal'`（水平排列）

**size：** *string*或*int*型，默认为`'small'`

　　用于*设置内部元素之间的间隔大小*，可选的有`'small'`、`'middle'`、`'large'`，或传入*int*型代表像素单位间隔

**addSplitLine：** *bool*型，默认为`False`

　　用于*设置是否为内部的各个元素之间添加分隔线*

**wrap：** *bool*型，默认为`False`

　　仅在**水平排列模式**下可用，用于*设置当内部水平排列的元素宽度溢出时是否自动换行*

