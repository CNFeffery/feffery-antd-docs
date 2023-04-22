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

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**visible：** *bool*型，默认为`False`

　　用于*设置或监听当前对话框是否可见*

**title：** *组件型*

　　用于*设置当前对话框的标题内容*

**renderFooter：** *bool*型，默认为`False`

　　用于*设置是否渲染底部按钮操作区域*

**okText：** *组件型*

　　用于*设置当前对话框确认按钮内容*

**okButtonProps：** *dict*型

　　用于*配置底部操作区域确认按钮相关参数*，可用的键值对参数有：

- **size：** *string*型，用于*设置确认按钮的尺寸规格*，可选的有`'small'`、`'middle'`、`'large'`
- **type：** *string*型，用于*设置确认按钮的风格*，可选的有`default`、`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`
- **danger：** *bool*型，用于*设置是否以危险状态渲染确认按钮*
- **disabled：** *bool*型，用于*设置是否禁用确认按钮*
- **shape：** *string*型，用于*设置确认按钮的形状*，可选的有`'circle'`、`'round'`

**cancelText：** *组件型*

　　用于*设置当前对话框取消按钮内容*

**cancelButtonProps：** *dict*型

　　用于*配置底部操作区域取消按钮相关参数*，可用的键值对参数有：

- **size：** *string*型，用于*设置取消按钮的尺寸规格*，可选的有`'small'`、`'middle'`、`'large'`
- **type：** *string*型，用于*设置取消按钮的风格*，可选的有`default`、`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`
- **danger：** *bool*型，用于*设置是否以危险状态渲染取消按钮*
- **disabled：** *bool*型，用于*设置是否禁用取消按钮*
- **shape：** *string*型，用于*设置取消按钮的形状*，可选的有`'circle'`、`'round'`

**width：** *int*或*string*型，默认为`520`

　　用于*设置当前对话框的宽度*

**centered：** *bool*型，默认为`False`

　　用于*设置当前对话框是否垂直居中展示*

**keyboard：** *bool*型，默认为`True`

　　用于*设置当前对话框是否允许通过键盘esc键进行关闭*

**closable：** *bool*型，默认为`True`

　　用于*设置是否为当前对话框渲染关闭按钮*

**mask：** *bool*型，默认为`True`

　　用于*设置是否渲染背景蒙版*

**maskClosable：** *bool*型，默认为`True`

　　用于*设置是否允许点击蒙版进行对话框的关闭*

**okClickClose：** *bool*型，默认为`True`

　　用于*设置点击确认按钮后是否自动关闭对话框*

**zIndex：** *int*型，默认为`1000`

　　用于*设置当前对话框的z-index属性*

**maskStyle：** *dict*型

　　用于*设置蒙版的css样式*

**bodyStyle：** *dict*型

　　用于*设置对话框主体区域的css样式*

**okCounts：** *int*型，默认为`0`

　　用于*监听当前对话框中确认按钮的累计被点击次数*

**cancelCounts：** *int*型，默认为`0`

　　用于*监听当前对话框中取消按钮的累计被点击次数*

**closeCounts：** *int*型，默认为`0`

　　用于*监听当前对话框累计关闭次数*

**confirmAutoSpin：** *bool*型，默认为`False`

　　用于*设置当前对话框中的确认按钮是否在点击后自动进入加载中状态*

**loadingOkText：** *组件型*

　　用于*设置当前对话框中的确认按钮处于加载中状态时显示的内容*

**confirmLoading：** *bool*型，默认为`False`

　　用于*手动设置当前对话框中的确认按钮是否处于加载中状态*

**transitionType：** *string*型，默认为`'zoom'`

　　用于*设置当前对话框的显隐动画类型*，可选的有`'none'`、`'fade'`、`'zoom'`、`'zoom-big'`、`'zoom-big-fast'`、`'slide-up'`、`'slide-down'`、`'slide-left'`、`'slide-right'`、`'move-up'`、`'move-down'`、`'move-left'`、`'move-right'`



