**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的描述列表项*

**title：** *组件型*

　　用于*为当前描述列表设置标题内容*

**column：** *int*或*dict*型，默认为`3`

　　用于*设置当前描述列表每行的单位宽度*，当传入*dict*型输入时，用于设置不同响应式断点下的每行单位宽度，可用的响应式断点有`'xs'`、`'sm'`、`'md'`、`'lg'`、`'xl'`、`'xxl'`

**bordered：** *bool*型，默认为`False`

　　用于*设置是否渲染边框*

**size：** *string*型，默认为`'default'`

　　用于*设置当前组件的尺寸规格*，可选的有`'small'`、`'default'`和`'large'`

**layout：** *string*型，默认为`'horizontal'`

　　用于*设置当前描述列表的布局方式*，可选的有`'horizontal'`、`'vertical'`

**labelStyle：** *dict*型

　　用于*统一设置内部各描述列表项标题的css样式*

**contentStyle：** *dict*型

　　用于*统一设置内部各描述列表项内容区域的css样式*



