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

**offsetBottom：** *int*型

　　用于*设置固钉在用户滚动页面后距离窗口底部的像素阈值*，到达这个阈值后会触发固钉的锚定页面功能

**offsetTop：** *int*型

　　用于*设置固钉在用户滚动页面后距离窗口顶部的像素阈值*，到达这个阈值后会触发固钉的锚定页面功能

**target：** *string*型

　　用于*设置固钉监听滚动事件从而进行锚定操作的目标容器元素id*，不设置则锚定页面根节点