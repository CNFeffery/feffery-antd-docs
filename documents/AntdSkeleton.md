**active：** *bool*型，默认为`False`

　　用于设置*是否渲染动态骨骼屏效果*

**avatar：** *bool*或*dict*型，默认为`False`

　　用于设置*骨骼屏中的头像占位效果*，可设置为`True`开启基础头像，亦可传入字典进行精细化设置，可用的键值对参数有：

- active：*bool*型，默认为`False`，仅在**单独**使用头像占位时生效，用于设置是否对头像*渲染动态效果*
- shape：*string*型，默认为`'circle'`，用于设置头像占位的形状，可选的有`'circle'`及`'square'`
- size：*int*或*string*型，默认为`'default'`，用于设置头像占位图的大小规格，传入*int*型数值时表示头像的像素大小，传入`'large'`、`'small'`或`'default'`可使用预设的固定规格尺寸

**paragraph：** *bool*或*dict*型，默认为`True`

　　用于设置*骨骼屏中的段落占位效果*，可设置为`True`开启基础段落，亦可传入字典进行精细化设置，可用的键值对参数有：

- rows：*int*型，用于设置*段落占位的行数*
- width：*int*、*string*或*list*型，当传入*int*型时，用于设置段落占位**最后一行**的像素宽度；当传入*string*型时，用于设置段落占位**最后一行**的`css`宽度值，如`'50%'`；当传入*list*型时，列表中每个元素可接受*int*或*string*型，用于分别设置对应行的宽度

**title：** *bool*或*dict*型，默认为`True`

　　用于设置*骨骼屏中的标题占位效果*，可设置为`True`开启基础标题，亦可传入字典进行精细化设置，可用的键值对参数有：

- width：*int*或*string*型，当传入*int*型时，用于设置标题占位的像素宽度；当传入*string*型时，用于设置`css`宽度值，如`'2rem'`

**round：** *bool*型，默认为`False`

　　用于设置*段落与标题占位是否以圆角矩形形式进行渲染*

**debug：** *bool*型，默认为`False`

　　用于设置是否开启*debug模式*，开启后，每当对应`AntdSkeleton`组件加载骨骼屏渲染时，`浏览器开发者工具-console`中会打印触发本次骨骼屏渲染的子节点**id**信息

**listenPropsMode：** *string*型，默认为`'default'`

　　用于设置特殊的*子节点监听过滤模式*，默认为`'default'`时，`AntdSkeleton`的所有后代组件作为回调的`Output`进行回调过程时，都会触发加载动画；当设置为`'exclude'`时，会开启*排除过滤模式*，此时传入`includeProps`参数列表中的所有`'id.prop名称'`对应的后代组件处于回调时不会触发加载动画；当设置为`'include'`时，会开启*包含监听模式*，此时与`'exclude'`**恰恰相反**，只有传入到参数`includeProps`列表中的所有`'id.prop名称'`对应的后代组件的回调过程才会被`AntdSkeleton`监听

**excludeProps：** *list*型

　　配合`listenPropsMode='exclude'`模式使用

**includeProps：** *list*型

　　配合`listenPropsMode='include'`模式使用