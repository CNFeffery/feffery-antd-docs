更新时间：`2022-04-17`

---

- `0.1.8`版本
  
  - **新特性**✨
    
    - `AntdUpload`、`AntdDraggerUpload`
      
      - 新增参数`listUploadTaskRecord`用于记录上传文件历史列表相关信息
      
    - `AntdTable`
    
      - 新增*图片*再渲染模式`'image'`
      - 新增*自定义格式化*再渲染模式`'custom-format'`
      
      - `sortOptions.multiple`参数新增`'auto'`模式，用于开启基于用户点击顺序的多字段组合排序
      - `filterOptions`参数针对`'checkbox'`模式：
        - 新增参数`filterMultiple`设置是否允许多选，默认为`True`
        - 新增参数`filterSearch`设置是否开启搜索框，默认为`False`
      - 新增参数`conditionalStyleFuncs`进行单元格条件样式设定
      
      

