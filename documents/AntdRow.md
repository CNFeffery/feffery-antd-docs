**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**align：** *string*型，默认为`'top'`

　　用于*设置垂直方向上对齐方式*，可选的有`'top'`、`'middle'`和`'bottom'`

**gutter：** *int*、*list*或*dict*型，默认为`0`

　　用于设置行、列之间的像素间隔距离，当传入*int*值时，用于设置所包含的列之间的水平间隔；也可传入格式为`[水平间距, 垂直间距]`的列表来同时设置两个方向上列组件之间的像素间隔距离；也可以传入以响应式断点如`xs`为键的字典，来为每个不同断点水平单独设置列之间的水平间隔

**justify：** *string*型，默认为`'start'`

　　用于*设置其内部所有列组件整体的水平布局方式*，可选的有`'start'`、`'end'`、`'center'`、`'space-around'`、`'space-between'`

**wrap：** *bool*型，默认为`True`

　　用于*设置当内部列元素单位宽度溢出时是否自动换行*