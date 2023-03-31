**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*当前气泡卡片锚定展示的目标元素*

**title：** *组件型*

　　用于*设置当前气泡卡片的标题元素*

**content：** *组件型*

　　用于*设置当前气泡卡片的内容元素*

**placement：** *string*型，默认为`'top'`

　　用于*设置当前气泡卡片的弹出方向*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`、`'leftTop'`、`'leftBottom'`、`'rightTop'`、`'rightBottom'`

**color：** *string*型

　　用于*设置当前气泡卡片的背景色*

**mouseEnterDelay：** *int*或*float*型，默认为`0.1`

　　用于*设置当前气泡卡片从鼠标移入到卡片显示的延时*，单位：秒

**mouseLeaveDelay：** *int*型或*float*型，默认为`0.1`

　　用于*设置当前气泡卡片从鼠标移出到卡片消失的延时*，单位：秒

**overlayStyle：** *dict*型

　　用于*设置当前气泡卡片容器的css样式*

**overlayInnerStyle：** *dict*型

　　用于*设置当前气泡卡片内容区域的css样式*

**trigger：** *string*或*list*型，默认为`'hover'`

　　用于*设置当前气泡卡片的显示触发行为*，可选项有`'hover'`、`'focus'`、`'click'`，也可以传入多种行为构成的列表实现多行为触发

**zIndex：** *int*型

　　用于*为当前气泡卡片设置z-index属性*

**arrowPointAtCenter：** *bool*型，默认为`False`

　　用于*设置当前气泡卡片附带的箭头是否指向锚点元素中心*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题