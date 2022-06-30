更新时间：`2022-06-30` 

---

- `0.1.14`版本
  
  - **新特性**✨
    
    - 💥基于`dash`2.5.0及以上版本新特性，先行对下列组件参数添加组件型输入支持
    
      - `AntdAlert`
    
        `message`、`description`参数
    
      - `AntdPageHeader`
    
        `title`、`subTitle参数`
    
      - `AntdPopover`
    
        `content`参数
    
      - `AntdResult`
    
        `icon`、`title`、`subTitle`参数
    
      - `AntdSpin`
    
        `indicator`参数
    
    - `AntdStatistics`
    
      - `value`参数新增对`string`类型输入的接受
    
    - `AntdDropdown`
    
      - 新增属性`nClicks`用于辅助监听下拉菜单项重复点击事件
    
    - `AntdTable`
    
      - 针对`'mini-line'`、`'mini-area'`、`'mini-bar'`再渲染模式，新增参数`tooltipCustomContent`用于自定义`js`箭头函数字符串实现自定义`tooltip`内容及样式
    
    - `AntdInput`
    
      - 针对`'text-area'`文本域模式，新增参数`autoSize`
    
  - **已修复问题**🔧
    
    - 修复`AntdCard`中传入`AntdCardGrid`时异常排列问题
      
    - 修复`AntdTree`参数`defaultExpandAll`无效的问题
      
      
      
      
      
      
      
      
      
    

