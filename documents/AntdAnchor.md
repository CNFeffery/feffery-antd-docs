**linkDict：** *list*型，必填

　　用于构造层次目录，每个元素为字典，其中：

- title：*string*型，用于设置锚点目录对应显示的*标题内容*
- href：*string*型，用于设置当前锚点对应元素的*id hash*，如`id='test'`的*id hash*为`'#test'`
- children：*list*型，用于嵌套子目录锚点参数

**align：** *string*型，默认为`'right'`

　　用于设置锚点的*贴靠*方向，`'left'`贴靠左边，`'right'`贴靠右边

**containerId：** *string*型

　　当锚点组件位于局部滚动页面内时（典型如本在线文档中的所有组件说明页），用于绑定`position`为`relative`的祖先容器作为位置计算的参考，从而修正显示异常情况

**targetOffset：** *int*型

　　用于设置点击锚点定位到目标元素时，y轴上的*像素偏移距离*，譬如本网站中所有锚点都设置了`targetOffset=200`

**affix：** *bool*型，默认为`True`

　　用于设置*是否开启固定模式*

**bounds：** *int*型，默认为`5`

　　用于设置*组件四周边界的像素宽度*

**offsetTop：** *int*型

　　用于设置*固定后的锚点距离顶端的像素距离*