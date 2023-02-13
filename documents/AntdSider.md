**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**collapsed：** *bool*型，默认为`False`

　　用于*设置当前侧边栏区域是否折叠*

**defaultCollapsed：** *bool*型，默认为`False`

　　用于*设置当前侧边栏初始化时是否处于折叠状态*

**collapsedWidth：** *int*型，默认为`80`

　　用于*设置折叠状态下侧边栏像素宽度*，当设置为`0`时会额外渲染特殊的折叠状态切换按钮，以避免折叠后无法触发展开操作

**collapsible：** *bool*型，默认为`False`

　　用于*设置当前侧边栏是否可折叠*

**reverseArrow：** *bool*型，默认为`False`

　　用于*设置是否水平翻转折叠触发区域箭头方向*，通常在`AntdSider`位于页面右侧时需要进行设置

**theme：** *string*型，默认为`'dark'`

　　用于*设置主题风格*，可选的有`'dark'`、`'light'`

**width：** *int*或*string*型，默认为`200`

　　用于*设置当前侧边栏的宽度*

**trigger：**

　　当需要隐藏自带的侧边栏折叠触发元素，而通过回调自定义折叠触发元素时，请设置`trigger=None`

**breakpoint：** *string*型

　　当需要侧边栏实现响应式自动化折叠/展开功能时，用于*设置临界断点*，可选的有`'xs'`、`'sm'`、`'md'`、`'lg'`、`'xl'`、`'xxl'`