**duration：** *float*型，默认为0.45

　　用于设置点击组件后回到顶部*所需时间*，单位秒

**visibilityHeight：** *int*型，默认为400

　　用于设置开始出现**回到顶部**组件对应的滚动条*像素高度阈值*

**containerId：** *string*型

　　当回到顶部组件位于局部滚动页面内时（典型如本在线文档中的所有组件说明页），用于绑定`position`为`relative`的祖先容器作为位置计算的参考，从确保回到顶部组件可以正确监听对应容器的滚动事件