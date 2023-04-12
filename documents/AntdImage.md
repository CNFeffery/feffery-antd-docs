**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**alt：** *string*型

　　用于*设置图片加载失败时的说明文字*

**width：** *int*或*string*型

　　用于*设置图片宽度*

**height：** *int*或*string*型

　　用于*设置图片高度*

**src：** *string*或*list*型

　　用于*设置图片的url地址*，当传入*list*型时，会视作多图片组合进行展示

**fallback：** *string*型

　　用于*设置图片加载失败时的占位图*，默认为自带的占位图

**multiImageMode：** *string*型，默认为`'fold'`

　　用于*设置针对多图片组合展示时的具体形式*，可选的有`'fold'`、`'unfold'`

**preview：** *bool*型，默认为`True`

　　用于*设置是否开启交互查看功能*

　　