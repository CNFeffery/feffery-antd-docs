> 更新时间：2023-06-02

- `AntdSelect`
  - 新增*多模式搜索*相关功能，具体见[多模式搜索](/AntdSelect#多模式搜索)

- `AntdTransfer`
  - 新增*多模式搜索*相关功能，具体见[多模式搜索](/AntdTransfer#多模式搜索)

- `AntdTreeSelect`
  - 新增*多模式搜索*相关功能，具体见[多模式搜索](/AntdTreeSelect#多模式搜索)

- `AntdTable`
  - 基于`dash>=2.10.2`，新增单元格组件型输入设置，具体见[自定义单元格元素](/AntdTable-rerender#自定义单元格元素)
  - 参数`defaultExpandedRowKeys`新增对树形数据的默认展开纪录行设置支持
  - 可编辑单元格新增*文本域模式*，具体见[文本域编辑模式](/AntdTable-advanced#文本域编辑模式)
  - 针对可编辑单元格功能，为`columns`字段配置新增子参数`editOptions`
  - 新增参数`selectedRowsSyncWithData`用于在`data`变动后自动对`selectedRows`进行更新，具体见[同步刷新selectedRows](/AntdTable-advanced#同步刷新selectedRows)

- `AntdDateRangePicker`、`AntdTimeRangePicker`
  - 新增参数`open`用于监听或设置悬浮层是否展开

- `AntdInput`
  - 多选模式下优化`defaultValue`及`value`参数为`None`时的初始回填选项异常情况
