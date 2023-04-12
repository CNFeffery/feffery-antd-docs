**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名，支持[动态css](/advanced-classname)*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**title：** *组件型*

　　用于*为当前卡片设置标题部分内容*

**extraLink：** *dict*型

　　用于*配置卡片右上角额外链接相关功能*，可用的键值对参数有：

- **content：** *string*型，用于*设置链接文字内容*
- **href：** *string*型，用于*设置链接地址*
- **target：** *string*型，默认为`'_blank'`，用于*设置链接跳转行为*
- **className：** *string*型，用于*设置链接的css类名*
- **style：** *dict*型，用于*设置链接的css样式*

**coverImg：** *dict*型

　　用于*配置卡片封面填充相关功能*，可用的键值对参数有：

- **src：** *string*型，用于*设置封面图片的地址*
- **alt：** *string*型，用于*设置封面图片加载失败时的占位文字*
- **className：** *string*型，用于*设置封面图片的css类名*
- **style：** *dict*型，用于*设置封面图片的css样式*

**bodyStyle：** *dict*型

　　用于*设置卡片内容区域的css样式*

**headStyle：** *dict*型

　　用于*设置卡片标题区域的css样式*

**bordered：** *bool*型，默认为`True`

　　用于*设置是否为当前卡片渲染边框*

**hoverable：** *bool*型，默认为`False

　　用于*设置是否为当前卡片开启鼠标悬停阴影效果*

**size：** *string*型，默认为`'default'`

　　用于*设置当前卡片的尺寸规格*，可选的有`'default'`、`'small'`