更新时间：`2022-03-12`

---

- `0.1.4`版本
  - **新特性**✨
    - `AntdTable`
      - 新增参数`miniChartAnimation`设置`迷你图`模式是否渲染出现动画效果，默认为`false`
      - 新增参数`miniChartHeight`用于自定义`迷你图`模式中图表的像素高度，默认为`30`
      - 对`pagination`参数进行优化，下属参数新增`showSizeChanger`用于设置是否渲染`页码尺寸`切换器
      - 再渲染模式新增`'mini-ring-progress'`**迷你环形进度条**模式
      - 再渲染模式新增`'status-badge'`**状态徽标**模式
      - 新增参数`summaryRowContents`用于定义表格底部总结栏内容
      - 新增参数`summaryRowFixed`设置是否以固定模式渲染总结栏
  - **已修复问题**🔧
    - `AntdTable`
    - 修复了表格中各种悬浮层元素在`containerId`参数指定的容器不存在时不显示的问题