**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**children：** *组件型*

　　用于传入*嵌套的子元素*

**active：** *bool*型，默认为`False`

　　用于*设置当前骨骼屏是否开启扫屏动画效果*

**avatar：** *bool*或*dict*型，默认为`False`

　　用于*设置是否在骨骼屏中添加头像占位图*，当传入*dict*型时可对头像占位图进行配置，可用的键值对参数有：

- **active：** *bool*型，默认为`False`，用于*设置头像占位图是否开启扫屏动画效果*
- **shape：** *string*型，可选的有`'circle'`、`'square'`
- **size：** *int*或*string*型，默认为`'default'`，用于*设置头像占位图的尺寸*，*int*型输入用于设置像素尺寸，*string*型可选的有`'large'`、`'small'`、`'default'`

**paragraph：** *bool*或*dict*型，默认为`True`

　　用于*设置是否在骨骼屏中添加段落占位图*，当传入*dict*型时可对段落占位图进行配置，可用的键值对参数有：

- **rows：** *int*型，用于*设置段落占位图实际行数*
- **width：** *int*、*string*或*list*型，当传入*int*或*string*型时，用于设置段落占位图最后一行的宽度，当传入*list*型时，用于逐行设置宽度

**title：** *bool*或*dict*型，默认为`True`

　　用于*设置是否在骨骼屏中添加标题占位图*，当传入*dict*型时可对标题占位图进行配置，可用的键值对参数有：

- **width：** *int*或*string*型，用于*设置标题占位图宽度*

**round：** *bool*型，默认为`False`

　　用于*设置段落和标题占位图是否启用圆角效果*

**debug：** *bool*型，默认为`False`

　　用于*设置是否开启调试模式*，开启后当骨骼屏内部嵌套的元素作为回调函数`Output`角色且回调函数执行中时，会在浏览器控制台打印相关组件的`id`及`prop`信息

**listenPropsMode：** *string*型，默认为`'default'`

　　用于*设置骨骼屏针对内部嵌套元素回调行为的监听方式*，可用的有`'default'`（默认全监听模式）、`'exclude'`（排除模式）、`'include'`（包含模式）

**excludeProps：** *list*型

　　当`listenPropsMode='exclude'`时，用于*设置需要排除监听的内部嵌套组件对应属性*，列表中每个元素用于定义要排除的目标，格式为`组件id.属性名称`，如`'demo-input.value'`

**includeProps：** *list*型

　　当`listenPropsMode='include'`时，用于*设置需要包含监听的内部嵌套组件对应属性*，列表中每个元素用于定义要包含的目标，格式为`组件id.属性名称`，如`'demo-input.value'`