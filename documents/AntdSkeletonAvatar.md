**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**active：** *bool*型，默认为`False`

　　用于*设置是否开启扫屏动画效果*

**shape：** *string*型，默认为`'circle'`

　　用于*设置头像占位图的形状*，可选的有`'circle'`、`'square'`

**size：** *int*或*string*型，默认为`'default'`

　　用于*设置头像占位图的尺寸*，*int*型输入用于设置像素尺寸，*string*型可选的有`'large'`、`'small'`、`'default'`