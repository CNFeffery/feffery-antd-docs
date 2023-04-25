**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**items：** `list[dict]`型

　　用于*定义当前手风琴列表*，每个字典可用的键值对参数有：

- **children：** *组件型*，用于*设置当前手风琴项的内部元素*
- **className：** *string*或*dict*型，用于*设置当前手风琴项的css类名*，支持[动态css](/advanced-classname)
- **style：** *dict*型，用于*设置当前手风琴项的css样式*
- **key：** *int*或*string*型，必填，用于*设置当前手风琴项的唯一识别id*
- **collapsible：** *string*型，用于*设置当前手风琴项的折叠触发方式*，可选的有`'header'`、`'disabled'`
- **title：** *组件型*，用于*设置当前手风琴项的标题内容*
- **extra：** *组件型*，用于*为当前手风琴项设置额外区域内容*
- **showArrow：** *bool*型，默认为`True`，用于*设置当前手风琴项是否展示箭头图标*
- **forceRender：** *bool*型，默认为`False`，用于*设置初始化是否强制渲染内部元素*

**accordion：** *bool*型，默认为`True`

　　用于*设置是否开启手风琴模式*

**activeKey：** *int*、*string*或*list*型

　　用于*设置或监听手风琴已展开项key值*

**defaultActiveKey：** *int*、*string*或*list*型

　　用于*设置初始化时手风琴已展开项key值*

**bordered：** *bool*型，默认为`True`

　　用于*设置是否为当前手风琴渲染边框*

**collapsible：** *string*型

　　用于*为所有手风琴项设置折叠触发方式*，可选的有`'header'`、`'disabled'`、`'icon'`

**expandIconPosition：** *string*型，默认为`'left'`

　　用于*设置折叠图标显示方位*，可选的有`'left'`、`'right'`

**ghost：** *bool*型，默认为`False`

　　用于*设置是否开启透明面板模式*