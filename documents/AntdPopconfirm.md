**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*气泡确认框所施加的触发元素*，通常为按钮

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**title：** *组件型*

　　用于*设置气泡确认框的标题内容*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前气泡确认框*

**placement：** *string*型，默认为`'top'`

　　用于*设置当前气泡确认框的展开方向*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`、`'leftTop'`、`'leftBottom'`、`'rightTop'`、`'rightBottom'`

**mouseEnterDelay：** *int*或*float*型，默认为`0.1`

　　用于*设置当前气泡确认框从鼠标移入到卡片显示的延时*，单位：秒

**mouseLeaveDelay：** *int*型或*float*型，默认为`0.1`

　　用于*设置当前气泡确认框从鼠标移出到卡片消失的延时*，单位：秒

**overlayStyle：** *dict*型

　　用于*设置当前气泡确认框容器的css样式*

**overlayInnerStyle：** *dict*型

　　用于*设置当前气泡确认框内容区域的css样式*

**okText：** *组件型*

　　用于*设置当前气泡确认框的确认按钮内容*

**okButtonProps：** *dict*型

　　用于*配置底部操作区域确认按钮相关参数*，可用的键值对参数有：

- **size：** *string*型，用于*设置确认按钮的尺寸规格*，可选的有`'small'`、`'middle'`、`'large'`
- **type：** *string*型，用于*设置确认按钮的风格*，可选的有`default`、`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`
- **danger：** *bool*型，用于*设置是否以危险状态渲染确认按钮*
- **disabled：** *bool*型，用于*设置是否禁用确认按钮*
- **shape：** *string*型，用于*设置确认按钮的形状*，可选的有`'circle'`、`'round'`

**cancelText：** *组件型*

　　用于*设置当前气泡确认框的取消按钮内容*

**cancelButtonProps：** *dict*型

　　用于*配置底部操作区域取消按钮相关参数*，可用的键值对参数有：

- **size：** *string*型，用于*设置取消按钮的尺寸规格*，可选的有`'small'`、`'middle'`、`'large'`
- **type：** *string*型，用于*设置取消按钮的风格*，可选的有`default`、`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`
- **danger：** *bool*型，用于*设置是否以危险状态渲染取消按钮*
- **disabled：** *bool*型，用于*设置是否禁用取消按钮*
- **shape：** *string*型，用于*设置取消按钮的形状*，可选的有`'circle'`、`'round'`

**confirmCounts：** *int*型，默认为`0`

　　用于*监听确认按钮累计点击次数*

**cancelCounts：** *int*型，默认为`0`

　　用于*监听取消按钮累计点击次数*

**trigger：** *string*或*list*型，默认为`'hover'`

　　用于*设置当前气泡卡片的显示触发行为*，可选项有`'hover'`、`'focus'`、`'click'`，也可以传入多种行为构成的列表实现多行为触发

**open：** *bool*型，默认为`False`

　　用于*设置或监听气泡卡片是否展开*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题