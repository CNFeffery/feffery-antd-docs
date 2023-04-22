**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*当前文字提示锚定展示的目标元素*

**title：** *组件型*

　　用于*设置当前文字提示的内容*

**placement：** *string*型，默认为`'top'`

　　用于*设置当前文字提示的弹出方向*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`

**color：** *string*型

　　用于*设置当前文字提示的背景色*

**mouseEnterDelay：** *int*或*float*型，默认为`0.1`

　　用于*设置当前文字提示从鼠标移入到卡片显示的延时*，单位：秒

**mouseLeaveDelay：** *int*型或*float*型，默认为`0.1`

　　用于*设置当前文字提示从鼠标移出到卡片消失的延时*，单位：秒

**overlayStyle：** *dict*型

　　用于*设置当前文字提示容器的css样式*

**overlayInnerStyle：** *dict*型

　　用于*设置当前文字提示内容区域的css样式*

**trigger：** *string‘*或*list*型，默认为`'hover'`

　　用于*设置当前文字提示的显示触发行为*，可选项有`'hover'`、`'focus'`、`'click'`，也可以传入多种行为构成的列表实现多行为触发

**zIndex：** *int*型

　　用于*为当前文字提示设置z-index属性*

**arrowPointAtCenter：** *bool*型，默认为`False`

　　用于*设置当前文字提示附带的箭头是否指向锚点元素中心*

**open：** *bool*型，默认为`False`

　　用于*监听或设置当前文字提示是否展开*

**permanent：** *bool*型，默认为`False`

　　用于*设置是否维持当前文字提示的展开状态与参数open一致*，设置为`True`后，用户的鼠标移入移出操作将不会改变文字提示的展开行为

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题