> 更新时间：2023-04-25

- `AntdTable`
  - 新增单元格双击事件监听，涉及新增的相关属性有`nDoubleClicksCell`、`recentlyCellDoubleClickColumn`、`recentlyCellDoubleClickRecord`，具体使用参考[示例](/AntdTable-advanced#监听表格内点击事件)
- `AntdDropdown`
  - 新增参数`autoAdjustOverflow`用于控制当下拉菜单被遮挡时是否自动调整位置
- `AntdAccordion`、`AntdCollapse`
  - 参数`collapsible`新增可选项`'icon'`，用于设置仅图标区域可点击触发展开
- `AntdUpload`、`AntdDraggerUpload`、`AntdPictureUpload`
  - 参数`defaultFileList`各元素新增键值对参数`taskId`用于为`uploadId`提供默认缺省值，从而修正新的上传记录导致旧的上传记录`taskId`被覆盖的问题