**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**innerTextOrientation：** *string*型，默认为`'center'`

　　用于*设置内嵌内容的对齐方式*（通过`children`参数传入内嵌内容），可选项有`'left'`（左对齐）、`'center'`（居中）、`'right'`（右对齐）

**isDashed：** *bool*型，默认为`False`

　　用于*设置是否以虚线方式渲染分割线*

**direction：** *string*型，默认为`'horizontal'`

　　用于*设置分割线方向*，可选项有`'horizontal'`（水平）、`'vertical'`（竖直）

**fontSize：** *string*型

　　用于*设置分割线内嵌内容的字体大小*，接受`css`中合法的`font-size`输入值，如`'16px'`

**lineColor：** *string*型，默认为`'lightgrey'`

　　用于*设置分割线颜色*，接受`css`中合法的颜色值

**fontStyle：** *string*型，默认为`'initial'`

　　用于*设置分割线内嵌内容的字体风格*，接受`css`中合法的`font-style`输入值，如`'oblique'`代表斜体

**fontWeight：** *string*型，默认为`'initial'`

　　用于*设置分割线内嵌内容的字重*，接受`css`中合法的`font-weight`输入值，如`'bold'`代表加粗

**fontFamily：** *string*型，默认为`'initial'`

　　用于*设置分割线内嵌内容的字体族*，接受`css`中合法的`font-family`输入值，如`'KaiTi'`代表楷体

**fontColor：** *string*型，默认为`'#000000'`

　　用于*设置内嵌内容的字体颜色*，接受`css`中合法的`color`输入值，如`'black'`