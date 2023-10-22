> 更新时间：2023-10-22

- 🆕新增`AntdCenter`组件，用于快捷令内部元素同时在水平、垂直方向上居中

- 💥新增懒加载特性

　　针对个别静态资源体积较大的组件，或具体分类下的多个组件，新增**懒加载**特性，即当对应组件在页面中将要渲染时才会进行相关静态资源的网络传输，具体有：`AntdTable`、上传类组件、数据录入类组件、数据展示类组件（若无需懒加载特性，可在`dash.Dash()`中设置`eager_loading=True`）

- 💥新增批量属性监听功能

　　为部分组件引入**批量属性监听**机制，即通过参数`batchPropsNames`指定的若干属性，可在回调函数中通过`batchPropsValues`进行批量监听获取

- 💥新增别名导入功能

　　现在你可以选择使用`import feffery_antd_components.alias as fac`来代替`import feffery_antd_components as fac`，从而实现对各组件`Antd`前缀的省略，例如使用`fac.Button`代替`fac.AntdButton`

- 💥为更多数据录入类组件新增只读模式

　　为`AntdCheckbox`、`AntdCheckboxGroup`、`AntdRadioGroup`、`AntdSlider`、`AntdSwitch`、`AntdTransfer`、`AntdCheckCardGroup`、`AntdCheckCard`新增参数`readOnly`用于支持只读模式 

- 💥新增第三方外部图标库支持

　　针对`AntdTree`、`AntdTable`、`AntdSegmented`、`AntdMessage`、`AntdDropdown`、`AntdBreadcrumb`、`AntdAvatar`、`AntdMenu`、`AntdTabs`组件中涉及的字符型`icon`快捷参数，新增参数`iconRenderer`用于引入第三方基于css类的图标库，如`fontawesome`

- `AntdMenu`

  - 💥新增参数`menuItemKeyToTitle`用于实现自定义**组件型**菜单项标题 [示例](/AntdMenu#组件型菜单项标题)
  - 新增参数`inlineIndent`用于设置子菜单缩进像素宽度 [示例](/AntdMenu#调整子菜单缩进宽度)

- `AntdTree`

  - 💥新增快捷树搜索功能 [示例](/AntdTree#快捷树搜索)
  - 💥新增参数`dragInSameLevel`用于在节点可拖拽时，限制仅允许同级拖拽 [示例](/AntdTree#限制仅允许同级拖拽)
  - 新增参数`nodeCheckedStyle`、`nodeUncheckedStyle`分别控制节点勾选/未勾选**状态样式** [示例](/AntdTree#节点勾选状态样式)
  - 新增参数`nodeCheckedSuffix`、`nodeUncheckedSuffix`分别控制节点勾选/未勾选**状态后缀内容** [示例](/AntdTree#节点勾选状态后缀)
  - 新增**节点收藏**功能 [示例](/AntdTree#节点收藏功能)
  - 新增参数`scrollTarget`用于实现滚动到指定节点相关功能 [示例](/AntdTree#节点滚动动作)

- `AntdTabs`

  - 💥标签页标题新增自定义**右键菜单**功能 [示例](/AntdTabs#标签页右键菜单示例)
  - 新增参数`destroyInactiveTabPane`用于设置标签页不激活时是否自动销毁内部元素
  - 新增监听属性`tabCount`用于获取当前标签页个数 [示例](/AntdTabs#标签页自由增删示例)

- `AntdTable`

  - 💥表头字段支持任意层级表头合并 [示例](/AntdTable-basic#为字段分组)
  - 字段筛选新增**树形筛选菜单**功能 [示例](/AntdTable-advanced#勾选型筛选)
  - 字段筛选新增参数`defaultFilteredValues`用于为指定字段设置初始化已选中值 [示例](/AntdTable-advanced#设置初始化选中值)
  - `columns`针对各字段定义新增子参数`filterResetToDefaultFilteredValue`用于设置当用户点击重置筛选菜单时，是否恢复`defaultFilteredValues`参数所定义的默认选中值
  - 支持同时使用单元格自定义样式、单元格点击事件监听功能
  - `button`再渲染模式点击事件监听新增`clickedCustom`属性 [示例](/AntdTable-rerender#button按钮模式及回调示例)
  - `pagination`新增子参数`showLessItems`用于设置是否展示较少的跳页按钮 [示例](/AntdTable-advanced#展示较少的跳页按钮)
  - 新增参数`recentlyChangedColumn`用于监听单元格编辑事件对应的所属字段信息 [示例](/AntdTable-basic#通过回调监听编辑记录)
  - 可编辑模式新增`placeholder`参数 [示例](/AntdTable-basic#可编辑单元格)

- `AntdTimePicker`

  - 新增参数`showNow` [示例](/AntdTimePicker#隐藏此刻按钮)
  - 新增**组件型**参数`extraFooter`用于为选择面板设置额外自定义页脚内容 [示例](/AntdTimePicker#底部添加额外内容)

- `AntdDatePicker`

  - 新增参数`showToday` [示例](/AntdDatePicker#隐藏今天按钮)
  - 新增**组件型**参数`extraFooter`用于为选择面板设置额外自定义页脚内容 [示例](/AntdDatePicker#底部添加额外内容)

- `AntdTimeRangePicker`

  - 新增**组件型**参数`extraFooter`用于为选择面板设置额外自定义页脚内容 [示例](/AntdTimeRangePicker#底部添加额外内容)

- `AntdDateRangePicker`

  - 新增**组件型**参数`extraFooter`用于为选择面板设置额外自定义页脚内容 [示例](/AntdDateRangePicker#底部添加额外内容)

- `AntdUpload`

  - 针对上传按钮新增`block`参数用于撑满父级宽度 [示例](/AntdUpload#按钮撑满父级宽度)

- `AntdForm`

  - 参数`labelCol`、`wrapperCol`新增`flex`子参数，以提升表单宽度划分灵活性 [示例](/AntdForm#基于flex布局分配宽度)
  - 新增参数`labelWrap`用于设置表单项标签内容超长自动换行 [示例](/AntdForm#表单项标签超长换行)

- `AntdFormItem`

  - 参数`labelCol`、`wrapperCol`新增`flex`子参数，以提升表单宽度划分灵活性 [示例](/AntdForm#基于flex布局分配宽度)

- `AntdPagination`

  - 新增参数`showLessItems`用于设置是否展示较少的跳页按钮 [示例](/AntdPagination#展示较少的跳页按钮)

- `AntdDrawer`

  - 新增参数组件型参数`footer`用于为抽屉设置页脚内容 [示例](/AntdDrawer#设置页脚内容)
  - 新增参数`containerSelector`用于更灵活的指定所绑定的局部容器 [示例](/AntdDrawer#更自由地指定局部容器)
  - 新增样式定义相关参数`drawerStyle`、`bodyStyle`、`headerStyle`、`footerStyle`、`maskStyle`、`contentWrapperStyle`

- `AntdCheckCardGroup`

  - 新增参数`allowNoValue`用于设置是否限制至少选中一项 [示例](/AntdCheckCardGroup#限制必须有选中值)

- `AntdText`、`AntdParagraph`

  - 新增内容省略相关功能 [示例](/AntdParagraph#内容省略功能)

- `AntdProgress`

  - 新增参数`success`用于配置分段进度条相关功能 [示例](/AntdProgress#多阶段进度条)

- `AntdCascader`

  - 单选模式下新增`show-child`策略支持 [示例](/AntdCascader#已选项回填策略)

- `AntdPopover`、`AntdPopconfirm`

  - 新增可控参数`open` [示例1](/AntdPopover#展开状态可控) [示例2](/AntdPopconfirm#展开状态可控)

- `AntdDescriptions`

  - 新增`items`参数定义子项新方式 [示例](/AntdDescriptions#基于items参数定义子项)

- `AntdPopupCard`

  - 新增参数`dragClassName`用于设置可拖拽区域css类
  
- `AntdWatermark`

  - 新增多行文字水印支持 [示例](/AntdWatermark#多行文字水印)
  - 新增图片型水印支持 [示例](/AntdWatermark#图片型水印)

- `AntdModal`

  - 参数`okButtonProps`、`cancelButtonProps`新增子参数`style`、`className`
  - 新增参数`destroyOnClose`用于在模态框关闭后强制销毁内部元素

- `AntdBackTop`

  - 新增参数`containerSelector`用于更灵活的指定所绑定的局部容器

- `AntdBreadcrumb`

  - 新增节点点击事件监听属性`clickedItem` [示例](/AntdBreadcrumb#回调示例)

- `AntdInput`

  - 新增参数`countFormat`用于基于正则表达式自定义已输入内容计数规则 [示例](/AntdInput#自定义文字计数规则)

- `AntdSider`

  - 参数`width`新增字符型输入支持

- 🐞修复了`AntdSpin`、`AntdSkeleton`、`AntdCustomSkeleton`无法监听已设置`allow_duplicate=True`回调角色的问题

- 🐞修复了当`AntdTable`中存在自定义组件型字段时，在回调中使用返回行记录信息的相关事件监听属性时出现异常错误的问题
