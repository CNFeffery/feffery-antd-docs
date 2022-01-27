**mode：** *string*型，默认为`'icon'`

　　用于设置*头像渲染模式*，可选的有`'text'`（文本模式）、`'icon'`（图标模式）与`'image'`（图片模式）

**text：** *string*型

　　仅`mode="text"`时可用，用于设置*头像填充文字内容*

**gap：** *int*型，默认为`4`

　　仅`mode="text"`时可用，用于设置*头像填充文字左右两侧留白像素距离*

**icon：** *string*型

　　仅`mode="icon"`时可用，用于设置*头像填充图标*，同`AntdIcon`中的同名参数

**src：** *string*型

　　仅`mode="image"`时可用，用于*设置头像图片url地址*

**srcSet：** *string*型

　　仅`mode="image"`时可用，用于*设置头像图片base64字符串*

**alt：** *string*型

　　仅`mode="image"`时可用，用于*设置头像图片加载失败时的备选填充文字*

**size：** *int*、*string*或*dict*型，默认为`'default'`

　　用于设置*头像尺寸大小*，传入*int*型时代表像素边长；传入*string*型，用于在预设的几种尺寸规格中进行选择，可选的有`'default'`、`'small'`及`'large'`；传入*dict*型时，用于以各个断点为键设置**响应式**尺寸，分别设置*int*型像素边长值，可用断点有`xs`、`sm`、`md`、`lg`、`xl`及`xxl`

**shape：** *string*型，默认为`'circle'`

　　用于设置*头像的形状*，可选的有`'circle'`与`'square'`