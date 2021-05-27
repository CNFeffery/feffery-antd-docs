**linkDict：** *list*型，必填

　　用于构造层次目录，每个元素为字典，其中：

- title：*string*型，用于设置锚点目录对应显示的*标题内容*
- href：*string*型，用于设置当前锚点对应元素的*id hash*，如`id='test'`的*id hash*为`'#test'`
- children：*list*型，用于嵌套子目录锚点参数

**align：** *string*型，默认为`'right'`

　　用于设置锚点的*贴靠*方向，`'left'`贴靠左边，`'right'`贴靠右边