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

**title：** *组件型*

　　用于*设置当前弹出式卡片的标题元素*

**visible：** *bool*型，默认为`True`

　　用于*设置当前弹出式卡片是否处于显示状态*

**width：** *int*或*string*型

　　用于*设置当前弹出式卡片的宽度*

**transitionType：** *string*型，默认为`'fade'`

　　用于*设置当前弹出式卡片的显隐动画类型*，可选的有`'none'`、`'fade'`、`'zoom'`、`'zoom-big'`、`'zoom-big-fast'`、`'slide-up'`、`'slide-down'`、`'slide-left'`、`'slide-right'`、`'move-up'`、`'move-down'`、`'move-left'`、`'move-right'`

**closable：** *bool*型，默认为`True`

　　用于*设置是否为当前弹出式卡片添加关闭按钮*

**closeIconType：** *string*型，默认为`'default'`

　　用于*设置当前弹出式卡片的关闭按钮类型*，可选的有`'default'`、`'outlined'`、`'two-tone'`

**draggable：** *bool*型，默认为`False`

　　用于*设置当前弹出式卡片是否可进行自由拖拽*

**zIndex：** *int*型，默认为`1000`

　　用于*设置当前弹出式卡片的z-index信息*

**bodyStyle：** *dict*型

　　用于*设置当前弹出式卡片内容区域的css样式*

**dragClassName：** *string*或*dict*型

　　用于设置*可拖拽区域的css类名*，支持[动态css](/advanced-classname)