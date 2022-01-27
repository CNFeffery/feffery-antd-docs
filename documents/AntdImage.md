**width：** *int*或*float*型

　　用于设置*图片的固定像素宽度*

**height：** *int*或*float*型

　　用于设置*图片的固定像素高度*

**src：** *string*或*list*型

　　用于*要展示的单张或多张图片对应的src信息*，传入*string*型时为单张图片的*src属性*，传入*list*型时为*一组图片src属性所构成的列表*

**alt：** *string*型

　　用于设置*图片的描述文字*

**fallback：** *string*型

　　用于设置*图片加载失败时占位显示的图片*

**multiImageMode：** *string*型，默认为`'fold'`

　　当`src`为*list*型即要渲染多张图片时，此参数用于*设置具体的多图显示模式*，可选的有`'fold'`与`'unfold'`

**preview：** *bool*型，默认为`True`

　　用于设置*是否开启图片的交互预览模式*