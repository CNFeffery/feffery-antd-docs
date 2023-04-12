**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**wrapperClassName：** *string*或*dict*型

　　用于设置*当前加载动画组件容器的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前加载动画的尺寸规格*，可选的有`'small'`、`'middle'`和`'large'`

**delay：** *int*型，默认为`0`

　　用于*设置加载动画展示延时*，单位：毫秒

**text：** *string*型

　　用于*设置加载动画附带说明文字的内容*

**debug：** *bool*型，默认为`False`

　　用于*设置是否开启调试模式*，开启后当骨骼屏内部嵌套的元素作为回调函数`Output`角色且回调函数执行中时，会在浏览器控制台打印相关组件的`id`及`prop`信息

**listenPropsMode：** *string*型，默认为`'default'`

　　用于*设置骨骼屏针对内部嵌套元素回调行为的监听方式*，可用的有`'default'`（默认全监听模式）、`'exclude'`（排除模式）、`'include'`（包含模式）

**excludeProps：** *list*型

　　当`listenPropsMode='exclude'`时，用于*设置需要排除监听的内部嵌套组件对应属性*，列表中每个元素用于定义要排除的目标，格式为`组件id.属性名称`，如`'demo-input.value'`

**includeProps：** *list*型

　　当`listenPropsMode='include'`时，用于*设置需要包含监听的内部嵌套组件对应属性*，列表中每个元素用于定义要包含的目标，格式为`组件id.属性名称`，如`'demo-input.value'`

**indicator：** *组件型*

　　用于*自定义加载动画元素*，推荐搭配`fuc`中的`FefferyExtraSpinner`使用