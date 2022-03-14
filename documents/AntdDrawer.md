**children：**

　　用于传入置于*抽屉中的前端元素*

**visible：** *bool*型，默认为`False`

　　对应当前抽屉*是否弹出*

**title：** *str*型

　　用于设置抽屉的*标题文字内容*

**placement：** *str*型，默认为`'right'`

　　用于设置抽屉从屏幕的*哪个方向弹出*，可用的有`'left'`、`'right'`、`'top'`与`'bottom'`

**closable：** *bool*型，默认为`True`

　　用于设置是否在抽屉右上角*渲染关闭按钮*

**forceRender：** *bool*型，默认为`False`

　　用于设置是否在抽屉未弹出之前就*对内部元素进行预渲染*，在某些场景下可以优化页面整体渲染速度

**destroyOnClose：** *bool*型，默认为`True`

　　用于设置是否在抽屉被关闭时，*对内部已渲染的元素进行销毁*

**containerId：** *str型*

　　抽屉默认全屏弹出，若需要在*局部区域内弹出*，可绑定`position`为`relative`的容器`id`

**height：** *int*型，默认为`256`

　　当`placement`参数为`'top'`或`'bottom'`时，用于设置*抽屉的像素高度*

**mask：** *bool*型，默认为`True`

　　用于设置是否在抽屉展开时，在抽屉之外的区域*渲染蒙版*

**maskClosable：** *bool*型，默认为`True`

　　用于设置抽屉的蒙版区域，*是否可通过点击事件来关闭抽屉自身*

**width：** *int*型，默认为`256`

　　当`placement`参数为`'left'`或`'right'`时，用于设置*抽屉的像素宽度*

**zIndex：** *int*型，默认为`1000`

　　用于快捷设置抽屉整体的`z-index`属性