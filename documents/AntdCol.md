**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**span：** *int*型

　　在`fac`的网格系统中，每个`AntdRow`被等分为24份，`span`参数则用于设置对应的`AntdCol`在父级`AntdRow`中所占据的宽度份数

**offset：** *int*型，默认为`0`

　　用于*设置当前列左侧的留白份数*

**order：** *int*型，默认为`0`

　　用于*设置当前列的位序*

**pull：** *int*型，默认为`0`

　　用于*设置当前列向左移动份数*

**push：** *int*型，默认为`0`

　　用于*设置当前列向右移动份数*

**flex：** *string*或*int*型

　　对于熟悉`css`中`flex`布局的开发者，此参数等价于`css`中的`flex`参数，可对列的宽度进行更自由的自定义设置

**xs、sm、md、lg、xl、xxl：** *int*或*dict*型

　　用于*配置响应式布局*，当传入*int*型时，表示对应断点下的`span`值，当传入*dict*型时，可通过键值对的形式为对应断点设置`span`、`offset`、`order`、`pull`及`push`参数