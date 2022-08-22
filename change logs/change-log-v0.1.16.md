更新时间：`2022-08-22` 

---

- `0.1.16`版本
  
  - **新特性**✨
    
    - `AntdModal`
      - 参数`title`升级为组件型参数，同时移除先前`title`参数设定
    - `AntdCollapse`
      - 新增参数`forceRender`用于确保初始化未展开时强制预渲染内部子元素
    - `AntdAccordionItem`
      - 新增参数`forceRender`用于确保初始化未展开时强制预渲染内部子元素
    - `AntdTable`
      - 为字段筛选`keyword`模式新增国际化文案适配
      - 新增参数`expandedRowKeyToContent`用于同时定义行展开`key`及对应展开内容信息，同时移除先前行展开所使用到的参数`expandedRowContentsKeys`、`expandedRowContents`
    - `AntdSelect`
      - 新增参数`optionFilterProp`用于自定义搜索依据的字段
    - `AntdTreeSelect`
      - 新增参数`treeNodeFilterProp`用于自定义搜索依据的字段
    
  - **已修复问题**🔧
    
    - 针对所有上传类组件，修复历史任务信息中`completeTimestamp`在每次有新上传任务完成后都会被刷新的问题
      
    - 修复`AntdTable`当`data`为`None`时会报错的问题
      
    - 修复`AntdSlider`单值选择模式下，`defaultValue`设置为0时失效的问题
      
      
      
      
      
      
      
      
      
    

