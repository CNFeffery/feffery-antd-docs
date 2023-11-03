**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**mode：** *string*型，默认为`'icon'`

　　用于*设置当前头像的模式*，可选的有`'text'`、`'icon'`、`'image'`

**gap：** *int*型，默认为`4`

　　当`mode="text"`时，用于*设置头像内的文字到左右两侧的像素间隔大小*

**text：** *string*型

　　当`mode="text"`时，用于*设置头像内的文字内容*

**icon：** *string*型

　　当`mode="icon"`时，用于*设置头像内显示的图标*，同`AntdIcon`中的同名参数

**iconRenderer：** *string*型，默认为`'AntdIcon'`

　　用于*为当前节点的前缀图标设置渲染方式*，可选的有`'AntdIcon'`（内置图标）、`'fontawesome'`（基于css类名渲染）

**alt：** *string*型

　　当`mode="image"`时，用于*设置头像图片加载失败时的占位文字信息*

**src：** *string*型

　　当`mode="image"`时，用于*设置头像图片的url地址*

**srcSet：** *string*型

　　当`mode="image"`时，用于*设置头像图片的base64格式地址*，是`src`的备选

**draggable：** *bool*型，默认为`False`

　　当`mode="image"`时，用于*设置头像图片是否允许拖动*

**crossOrigin：** *string*型

　　当`mode="image"`时，用于*设置头像CORS属性*，可选的有`'anonymous'`、`'use-credentials'`、`''`，`'anonymous'`表示跨域请求不发送凭证信息、`'use-credentials'`表示跨域请求发送凭证信息、`''`表示不返回跨域资源，并在控制台中报告错误，而不加载跨域资源

**size：** *int*、*string*或*dict*型，默认为`'default'`

　　用于*设置头像的大小*，当传入*int*型输入时，用于设置头像的像素大小；当传入*string*型输入时，用于在预设的规格中进行选择，可选的有`'small'`、`'default'`、`'large'`；当传入*dict*型输入时，用于设置不同响应式断点下的头像像素大小，可用的响应式断点有`'xs'`、`'sm'`、`'md'`、`'lg'`、`'xl'`、`'xxl'`

**shape：** *string*型，默认为`'circle'`

　　用于*设置头像的形状*，可选的有`'circle'`、`'square'`