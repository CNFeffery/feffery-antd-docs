**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**loadingChildren：** *组件型*

　　用于*设置loading状态时按钮嵌套的子元素*

**type：** *string*型，默认为`'default'`

　　用于*设置按钮风格*，可选项有`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`、`'default'`

**href：** *string*型

　　当传入*url*时，可令`AntdButton`充当网页跳转功能

**target：** *string*型

　　当`href`参数有合法*url*传入时，用于设置跳转动作类型，[参考资料](https://www.w3school.com.cn/tags/att_a_target.asp)

**block：** *bool*型，默认为`False`

　　用于*设置按钮宽度是否撑满父级元素*

**danger：** *bool*型，默认为`False`

　　用于*设置是否渲染为危险警告状态*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**shape：** *string*型或*None*，默认为`None`

　　用于*设置按钮形状*，可选项有`'circle'`（圆形）、`'round'`（圆角矩形）

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**nClicks：** *int*型，默认为`0`

　　用于*在回调中记录按钮被点按次数*

**debounceWait：** *int*型，默认为`0`

　　用于*为nClicks的监听更新设置防抖延时时长*，单位：毫秒

**icon：** *组件型*

　　用于*为当前按钮设置内嵌前缀子元素*

**loading：** *bool*型，默认为`False`

　　用于*设置是否以加载中状态渲染按钮*

**autoSpin：** *bool*型，默认为`False`

　　用于*设置当前按钮在被点击后是否自动进入loading状态*