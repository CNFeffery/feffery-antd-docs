**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**contentClassName：** *string*型

　　用于*设置当前展开收起组件内容区的css类名*

**contentStyle：** *dict*型

　　用于*设置当前展开收起组件内容区的css样式*

**hideLabel：** *组件型*

　　用于*设置当前展开收起组件收起状态下的展开按钮文案信息*

**showLabel：** *组件型*

　　用于*设置当前展开收起组件展开状态下的收起按钮文案信息*

**labelPosition：** *string*型，默认为`left`

　　用于*设置展开收起按钮的位置*，可选的有`'left'`、`'right'`

**open：** *bool*型，默认为`False`

　　用于*设置或监听当前展开收起组件是否处于展开状态*

**maxHeight：** *int*型，默认为`50`

　　用于*设置当前展开收起组件在收起状态下的内容区域最大像素高度*

**transitionDuration：** *int*或*float*型，默认为`0.1`

　　用于*设置当前展开收起组件状态切换动画的耗时*，单位：秒