**children：**

　　用于*传入内部嵌套的若干个`AntdCardGrid`或其他子元素*

**extraLink：** *dict*型

　　用于*配置卡片右上角的额外链接功能*，可用的键值对参数有：

- content：*string*型，用于设置*链接文字内容*
- href：*string*型，用于设置*链接url地址*
- target：*string*型，默认为`'_blank'`，用于设置*链接的跳转行为*
- className：*string*型，用于设置*链接的类名*
- style：*string*型，用于设置*链接的css样式*

**coverImg：** *dict*型

　　用于*配置卡片的填充封面图片功能*，图片会自适应卡片的大小，可选的键值对属性有：

- src：*string*型，用于设置*图片资源对应的src属性*
- alt：*string*型，用于设置*图片的alt属性*
- style：*string*型，用于设置*图片的css样式*

**bodyStyle：** *dict*型

　　用于设置*卡片的内容区域css样式*

**headStyle：** *dict*型

　　用于设置*卡片的标题区域css样式*

**bordered：** *bool*型，默认为`True`

　　用于设置*卡片是否渲染边框*

**hoverable：** *bool*型，默认为`False`

　　用于设置*卡片整体是否开启鼠标悬浮时凸起效果*

**size：** *string*型，默认为`'default'`

　　用于设置*卡片的尺寸*，可选的有`'default'`与`'small'`

**title：** *string*型

　　用于设置*卡片的标题内容*