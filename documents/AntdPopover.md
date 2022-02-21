**children：**

　　用于传入与气泡卡片相配合的*前端元素*

**title：** *str*或*dict*型

　　设置气泡卡片中的*标题内容*，可以传入纯文字，也可以传入具有下列键的字典：

- content：*str*型，设置文字内容
- prefixIcon：*str*型，设置标题前缀图标，可使用`AntdIcon`内置的所有图标

**content：** *list*型

　　用于传入*列表格式的气泡卡片内容元素*

**placement：** *str*型，默认为`'top'`

　　设置气泡卡片的*弹出方位*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`、`'leftTop'`、`'leftBottom'`、`'rightTop'`、`'rightBottom'`

**color：** *str*型

　　用于设置气泡卡片的*背景颜色*

**mouseEnterDelay：** *int*或*float*型，默认为`0.1`

　　用于设置鼠标移入目标元素后，*延时多少秒*才显示气泡卡片

**mouseLeaveDelay：** *int*或*float*型，默认为`0.1`

　　用于设置鼠标移出目标元素后，*延时多少秒*才隐藏气泡卡片

**overlayStyle：** *dict*型

　　用于设置气泡卡片的*css样式*

**overlayInnerStyle：** *dict*型

　　用于设置气泡卡片内容区的*css样式*

**trigger：** *str*或*list*型，默认为`'hover'`

　　用于设置触发提示卡片弹出的*交互行为*，可选的有`'hover'`、`'focus'`与`'click'`，或是前三者中的若干种所组成的列表
