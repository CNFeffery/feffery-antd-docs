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

**autoplay：** *bool*型，默认为`False`

　　用于*设置是否开启自动轮播*

**dotPosition：** *string*型，默认为`'bottom'`

　　用于*设置指示器的显示位置*，可选的有`'top'`、`'bottom'`、`'left'`和`'right'`

**easing：** *string*型，默认为`'linear'`

　　用于*设置轮播切换动画函数*，同`css`中的`animation-timing-function`属性

**effect：** *string*型，默认为`'scrollx'`

　　用于*设置轮播切换动化效果*，可选的有`'scrollx'`、`'fade'`

**autoplaySpeed：** *int*型，默认为`3000`

　　用于*设置轮播之间的时间间隔*，单位：毫秒

**speed：** *int*型，默认为`500`

　　用于*设置轮播过渡动画的耗时*，单位：毫秒

**pauseOnHover：** *bool*型，默认为`False`

　　用于*设置鼠标悬停是否会暂停轮播过程*