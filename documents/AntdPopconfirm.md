**children：**

　　用于传入*触发对话确认气泡卡片*的前端元素

**title：** *组件型*

　　用于设置气泡确认卡片的*标题内容*

**disabled：** *bool*型，默认为`False`

　　用于设置是否*禁用气泡确认卡片*

**placement：** *str*型，默认为`top`

　　设置气泡确认卡片的*弹出方位*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`、`'leftTop'`、`'leftBottom'`、`'rightTop'`、`'rightBottom'`

**mouseEnterDelay：** *int*或*float*型，默认为`0.1`

　　用于设置鼠标移入目标元素后，*延时多少秒*才显示气泡卡片

**mouseLeaveDelay：** *int*或*float*型，默认为`0.1`

　　用于设置鼠标移出目标元素后，*延时多少秒*才隐藏气泡卡片

**overlayStyle：** *dict*型

　　用于设置气泡确认卡片的*css样式*

**overlayInnerStyle：** *dict*型

　　用于设置气泡卡片内容区的*css样式*

**trigger：** *str*或*list*型，默认为`'hover'`

　　用于设置触发气泡确认卡片弹出的*交互行为*，可选的有`'hover'`、`'focus'`与`'click'`，或是前三者中的若干种所组成的列表

**okText：** *str*型

　　设置*确认按钮文字*

**okButtonProps：** *dict*型

　　设置*确认按钮的常用参数属性*，同`AntdButton`参数体系

**cancelText：** *str*型

　　设置*取消按钮文字*

**cancelButtonProps：** *dict*型

　　设置*取消按钮的常用参数属性*，同`AntdButton`参数体系

**confirmCounts：** *int*型

　　对应*确认按钮累计被点击次数*

**cancelCounts：** *int*型

　　对应*取消按钮累计被点击次数*