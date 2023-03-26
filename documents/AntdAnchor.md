**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**linkDict：** `list[dict]`型，必填

　　用于*定义当前锚点的层次结构*，每个*dict*型表示1个节点，可通过`children`参数向下进行嵌套，可用的键值对参数有：

- **title：** *string*型，用于*设置当前节点的标题文字*
- **href：** *string*型，用于*设置当前节点对应的网址*
- **target：** *string*型，用于*设置当前节点的链接跳转行为*
- **children：** `list[dict]`型，用于*继续向下嵌套节点*

**align：** *string*型，默认为`'right'`

　　用于*设置锚点组件的布局方位*，可选的有`'left'`、`'right'`

**containerId：** *string*型

　　用于*为锚点设置参考局部容器的id*

**targetOffset：** *int*或*float*型

　　用于*设置锚点点击切换到目标元素后的位移偏移量*

**affix：** *bool*型，默认为`True`

　　用于*设置是否开启锚定模式*

**bounds：** *int*型，默认为`5`

　　用于*设置锚点区域的像素外边距*

**offsetTop：** *int*或*float*型

　　用于*设置锚点触发锚定效果对应的顶端像素距离阈值*

**clickedLink：** *dict*型

　　用于*监听锚点中的点击事件*

