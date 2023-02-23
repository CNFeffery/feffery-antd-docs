**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*需要嵌套的若干头像*

**maxCount：** *int*型

　　用于*设置最大显示的头像数量*，超出部分将进行省略展示，默认无限制

**maxPopoverPlacement：** *string*型，默认为`'top'`

　　用于*设置省略展示部分气泡卡片的弹出方位*，可选的有`'top'`、`'bottom'`

**maxPopoverTrigger：** *string*型，默认为`'hover'`

　　用于*设置省略展示部分气泡卡片弹出的触发动作*，可选的有`'hover'`、`'focus'`、`'click'`

**maxStyle：** *dict*型

　　用于*设置省略展示部分的css样式*

**size：** *int*、*string*或*dict*型，默认为`'default'`

　　用于*统一设置各个嵌套头像的大小*，当传入*int*型输入时，用于设置头像的像素大小；当传入*string*型输入时，用于在预设的规格中进行选择，可选的有`'small'`、`'default'`、`'large'`；当传入*dict*型输入时，用于设置不同响应式断点下的头像像素大小，可用的响应式断点有`'xs'`、`'sm'`、`'md'`、`'lg'`、`'xl'`、`'xxl'`