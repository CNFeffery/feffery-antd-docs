**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**columns：** `list[dict]`型

　　用于*为当前表格定义要展示的字段及相关功能参数*，每个字典代表1个字段，可用的键值对参数有：

- **title：** *组件型*，必填，用于*设置当前字段的标题内容*
- **dataIndex：** *string*型，必填，用于*设置当前字段的唯一id信息*，该信息对应`data`中每条记录内的键值对
- **renderOptions：** *dict*型，用于*为当前字段设置与再渲染模式相关的配置参数*，可用的键值对参数有：
  - **renderType：** *string*型，用于*为当前字段设置所需的再渲染模式类型*，可选的有`'link'`（链接模式）、`'ellipsis'`（长内容省略模式）、`'copyable'`（可复制模式）、`'ellipsis-copyable'`（长内容省略+可复制模式）、`'tags'`（标签模式）、`'status-badge'`（状态徽标模式）、`'image'`（图片模式）、`'custom-format'`（自定义格式模式）、`'corner-mark'`（角标模式）、`'row-merge'`（跨行合并单元格模式）、`'dropdown-links'`（下拉链接菜单模式）、`'image-avatar'`（图片型头像模式）、`'mini-line'`（迷你折线图模式）、`'mini-bar'`（迷你柱状图模式）、`'mini-progress'`（迷你进度图模式）、`'mini-ring-progress'`（迷你环形进度图模式）、`'mini-area'`（迷你面积图模式）、`'button'`（按钮模式）、`'checkbox'`（勾选框模式）、`'switch'`（开关模式）、`'dropdown'`（下拉选择菜单模式）
  - **renderLinkText：** *string*型，当`renderType="link"`时，用于*统一为当前字段所渲染出的链接设置文字内容*
  - **renderButtonPopConfirmProps：** *dict*型，当`renderType="button"`时，且需要为当前字段所渲染出的按钮添加气泡确认框时，用于*设置与气泡确认相关框的配置参数*，可用的键值对参数有：
    - **title：** *string*型，用于*为气泡确认框设置标题文字*
    - **okText：** *string*型，用于*为气泡确认框的确认按钮设置文案信息*
    - **cancelText：** *string*型，用于*为气泡确认框的取消按钮设置文案信息*
  - **tooltipCustomContent：** *string*型，当`renderType`为`'mini-line'`、`'mini-area'`或`'mini-bar'`时，用于*设置针对迷你图表中的tooltip进行自定义格式化的javascript函数字符串*
  - **progressOneHundredPercentColor：** *string*型，当`renderType`为`'mini-progress'`或`'mini-ring-progress'`时，用于*设置进度图在达到1时的填充色*，默认为<font color="#52c41a">'#52c41a'</font>
  - **ringProgressFontSize：** *int*型，当`renderType="mini-ring-progress"`时，用于*设置百分比文字的字体大小*
  - **dropdownProps：** *dict*型，当`renderType="dropdown-links"`时，用于*设置与下拉链接菜单相关的配置参数*，可用的键值对参数有：
    - **title：** *string*型，用于*统一为当前字段的下拉链接菜单锚点设置文字内容*
    - **arrow：** *bool*型，用于*统一为当前字段的下拉链接菜单设置是否显示连接箭头*
    - **disabled：** *bool*型，默认为`False`，用于*统一设置是否禁用当前字段下的所有下拉链接菜单*
    - **overlayClassName：** *string*型，用于*统一为当前字段的下拉链接菜单设置下拉菜单容器的css类名*
    - **overlayStyle：** *string*型，用于*统一为当前字段的下拉链接菜单设置下拉菜单容器的css样式*
    - **placement：** *string*型，用于*统一为当前字段的下拉链接菜单设置弹出方位*，可选的有`'bottomLeft'`、`'bottomCenter'`、`'bottomRight'`、`'topLeft'`、`'topCenter'`、`'topRight'`
- **fixed：** *string*型，当需要冻结固定当前字段时，用于*设置冻结固定的方位*，可选的有`'left'`、`'right'`
- **editable：** *bool*型，默认为`False`，用于*设置当前字段是否开启可编辑模式*
- **align：** *string*型，用于*设置当前字段内容的水平对齐方式*，可选的有`'left'`、`'center'`、`'right'`
- **width：** *int*或*string*型，用于*设置当前字段的宽度*
- **hidden：** *bool*型，默认为`False`，用于*设置是否需要隐藏当前字段*

**data：** *list*型，用于*为当前表格设置源数据*，每个元素为字典，其各个键名与`columns`中各个字段的`dataIndex`信息对应，并可额外设置键值对`key`作为当前行记录的唯一标识id（若未设置`key`，`AntdTable`内部会自动生成递增序号作为`key`，`data`中每条记录的字段值格式与对应字段是否开启再渲染模式，以及具体开启的再渲染模式类型有关，不同再渲染模式接受的输入值格式如下：

- **常规模式（不开启再渲染）：** *int*、*float*或*string*型

- **link（链接模式）：** *dict*型，可用的键值对参数有：

  - **content：** *string*型，用于*设置当前记录值所渲染链接的文字内容*，优先级高于`renderLinkText`
  - **href：** *string*型，用于*设置当前记录值所渲染链接的url*
  - **target：** *string*型，默认为`'_blank'`，用于*设置当前记录值所渲染链接的跳转行为*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前记录值所渲染的链接*

- **ellipsis（长内容省略模式）：** *int*、*float*或*string*型

- **copyable（可复制模式）：**  *int*、*float*或*string*型

- **ellipsis-copyable（长内容省略+可复制模式）：** *int*、*float*或*string*型

- **tags（标签模式）：** *dict*或`list[dict]`型，单个*dict*表示单个标签，多个*dict*构成的列表表示多个标签，其中每个字典可用的键值对参数有：
- **color：** *string*型，用于*为当前标签设置背景色*
  - **tag：** *string*型，用于*为当前标签设置文字内容*
  
- **status-badge（状态徽标模式）：** *dict*型，可用的键值对参数有：

  - **status：** *string*型，用于*设置当前状态徽标的状态*，可选的有`'success'`、`'processing'`、`'default'`、`'error'`、`'warning'`
  - **text：** *int*、*float*或*string*型，用于*设置当前状态徽标的后缀文字内容*

- **image（图片模式）：** *dict*型，可用的键值对参数有：

  - **src：** *string*型，用于*设置当前图片的url地址*
  - **height：** *int*、*float*或*string*型，用于*设置当前图片的高度*
  - **preview：** *bool*型，默认为`True`，用于*设置当前图片是否开启交互预览功能*

- **custom-format（自定义格式模式）：**  *int*、*float*或*string*型

- **corner-mark（角标模式）：** *dict*型，可用的键值对参数有：

  - **placement：** *string*型，用于*设置当前单元格角标的方位*，可选的有`'top-left'`、`'top-right'`、`'bottom-left'`、`'bottom-right'`
  - **color：** *string*型，默认为<font color="#1890ff">'#1890ff'</font>，用于*设置角标颜色*
  - **content：** *int*、*float*或*string*型，用于*设置当前单元格内容*
  - **offsetX：** *int*或*float*型，用于*为当前单元格角标设置水平方向上的像素偏移量*
  - **offsetY：** *int*或*float*型，用于*为当前单元格角标设置竖直方向上的像素偏移量*
  - **hide：** *bool*型，默认为`False`，用于*设置是否隐藏当前单元格角标*

- **row-merge（跨行合并单元格模式）：** *dict*型，可用的键值对参数有：

  - **content：** *int*、*float*或*string*型，用于*设置当前单元格内容*
  - **rowSpan：** *int*型，用于*设置当前单元格应向下合并的单元格数量*，`0`即代表不进行合并

- **dropdown-links（下拉链接菜单模式）：** `list[dict]`型，其中每个字典用于定义当前下拉链接菜单中的一个链接项，可用的键值对参数有：

  - **title：** *string*型，用于*设置当前链接项的标题文字*
  - **href：** *string*型，用于*设置当前链接项的链接地址*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前链接项*
  - **icon：** *string*型，用于*为当前链接项设置前缀图标*，同`AntdIcon`中的同名参数
  - **isDivider：** *bool*型，用于*设置当前链接项是否充当分割线角色*

- **image-avatar（图片型头像模式）：** *dict*型，可用的键值对参数有：

  - **src：** *string*型，用于*设置当前图片型头像的图片url地址*
  - **size：** *int*、*string*或*dict*型，用于*设置当前头像的大小*，当传入*int*型输入时，用于设置头像的像素大小；当传入*string*型输入时，用于在预设的规格中进行选择，可选的有`'small'`、`'default'`、`'large'`；当传入*dict*型输入时，用于设置不同响应式断点下的头像像素大小，可用的响应式断点有`'xs'`、`'sm'`、`'md'`、`'lg'`、`'xl'`、`'xxl'`
  - **shape：** *string*型，默认为`'circle'`，用于*设置当前头像的形状*，可选的有`'circle'`、`'square'`

- **mini-line（迷你折线图模式）：** `list[int]`或`list[float]`型

- **mini-bar（迷你柱状图模式）：** `list[int]`或`list[float]`型

- **mini-area（迷你面积图模式）：** `list[int]`或`list[float]`型

- **mini-progress（迷你进度图模式）：** *float*或*int*型，取值应在`0`到`1`之间

- **mini-ring-progress（迷你进度图模式）：** *float*或*int*型，取值应在`0`到`1`之间

- **button（按钮模式）：** *dict*或`list[dict]`型，单个*dict*表示单个按钮，多个*dict*构成的列表表示多个按钮，其中每个字典可用的键值对参数有：

  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前按钮*
  - **type：** *string*型，用于*设置当前按钮的类型*，可选的有`'primary'`、`'ghost'`、`'dashed'`、`'link'`、`'text'`、`'default'`
  - **danger：** *bool*型，默认为`False`，用于*设置是否以危险状态渲染当前按钮*
  - **style：** *dict*型，用于*设置当前按钮的css样式*
  - **content：** *string*型，用于*设置当前按钮的文字内容*
  - **href：** *string*型，用于*设置当前按钮的链接url*
  - **target：** *string*型，默认为`'_blank'`，用于*设置当前按钮具有链接时的跳转行为*
  - **icon：** *string*型，用于*为当前按钮设置前缀图标*，同`AntdIcon`中的同名参数

- **checkbox（勾选框模式）：** *dict*型，可用的键值对参数有：

  - **checked：** *bool*型，用于*设置当前勾选框是否被勾选*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前勾选框*
  - **label：** *string*型，用于*为当前勾选框设置标签文字内容*

- **switch（开关模式）：** *dict*型，可用的键值对参数有：

  - **checked：** *bool*型，用于*设置当前开关是否处于开启状态*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前开关*
  
  - **checkedChildren：** *string*型，用于*设置当前开关开启状态下的标签文字*
  - **unCheckedChildren：** *string*型，用于*设置当前开关关闭状态下的标签文字*
  
- **dropdown（下拉选择菜单模式）：** `list[dict]`型，其中每个字典用于定义当前下拉选择菜单中的一个菜单项，可用的键值对参数有：

  - **title：** *string*型，用于*设置当前菜单项的标题文字*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前菜单项*
  - **icon：** *string*型，用于*为当前菜单项设置前缀图标*，同`AntdIcon`中的同名参数
  - **isDivider：** *bool*型，用于*设置当前菜单项是否充当分割线角色*

**bordered：** *bool*型，默认为`False`

　　用于*设置是否为全部单元格添加两侧边框线*

**maxHeight：** *int*型

　　用于*设置当前表格区域的最大像素高度*，当单页内容总高度超出时会自动渲染竖向滚动条，默认无限制

**maxWidth：** *int*型

　　用于*设置当前表格区域的最大像素宽度*，当表格横向宽度超时时会自动渲染横向滚动条，默认无限制

**size：** *string*型，默认为`'default'`

　　用于*设置当前表格的尺寸规格*，可选的有`'small'`、`'default'`和`'large'`，此设定会被可编辑单元格等特殊单元格渲染模式所覆盖

---

**rowSelectionType：** *string型*

　　用于*设置针对当前表格的行选择模式*，可选的有`'checkbox'`（多选）、`'radio'`（单选），默认不设置则不会开启行选择功能

**selectedRowKeys：** *list*型

　　用于*监听当前已被选择的行key值列表*

**rowSelectionWidth：** *int*或*string*型，默认为`32`

　　用于*设置行选择框所在列的宽度*

**selectedRows：** `list[dict]`型

　　用于*监听当前已被选择的行记录值列表*

**sticky：** *bool*型，默认为`False`

　　用于*设置是否开启粘性表头功能*

**titlePopoverInfo：** *dict*型

　　用于*为各个字段配置字段名旁附带的气泡卡片提示信息*，键为相应字段的`dataIndex`，值为字典，可用的键值对参数有：

- **title：** *组件型*，用于*设置气泡卡片的标题内容*

- **content：** *组件型*，用于*设置气泡卡片的内容*

- **placement：** *string*型，默认为`'bottom'`，用于*设置气泡卡片的展开方位*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`、`'topLeft'`、`'topRight'`、`'bottomLeft'`、`'bottomRight'`、`'leftTop'`、`'leftBottom'`、`'rightTop'`、`'rightBottom'`

- **overlayStyle：** *dict*型，用于*设置气泡卡片的css样式*

**columnsFormatConstraint：** *dict*型

　　用于*为各个开启可编辑单元格功能的字段配置输入内容格式校验相关功能*，键为相应字段的`dataIndex`，值为字典，可用的键值对参数有：

- **rule：** *string*型，用于*设置针对当前字段合法输入格式的正则表达式*
- **content：** *string*型，用于*设置用户输入内容格式校验失败后的消息提示文字*

**sortOptions：** *dict*型

　　用于*配置字段排序相关功能*，可用的键值对参数有：

- **sortDataIndexes：** `list[dict]`型，用于*设置需要开启排序功能字段的dataIndex值*
- **multiple：** *bool*或*string*型，默认为`False`，用于*设置是否开启组合排序功能*，当设置为`True`时`sortDataIndexes`的字段顺序将被视作组合排序的优先级；当设置为`'auto'`时，组合排序的优先级将由用户点击排序的字段先后决定

**sorter：** *dict*型

　　用于*监听最近一次排序操作后各个字段对应的排序状态*

**filterOptions：** *dict*型

　　用于*配置字段筛选相关功能*，键为相应字段的`dataIndex`，值为字典，可用的键值对参数有：

- **filterMode：** *string*型，默认为`'checkbox'`，用于*设置当前字段筛选功能类型*，可选的有`'checkbox'`、`'keyword'`
- **filterCustomItems：** *list*型，当`filterMode`为`'checkbox'`时，用于*手动设置筛选项值列表*
- **filterMultiple：** *bool*型，默认为`True`，当`filterMode`为`'checkbox'`时，用于*设置是否允许多选*
- **filterSearch：** *bool*型，默认为`False`，当`filterMode`为`'checkbox'`时，用于*设置开启搜索框*

**filter：** *dict*型

　　用于*监听最近一次筛选操作后各个字段对应的筛选值条件*

**pagination：** *dict*或*bool*型

　　用于*配置表格分页相关功能*，设置为`False`时会关闭分页功能，传入*dict*型输入时，可用的键值对参数有：

- **position：** *string*型，默认为`'bottomRight'`，用于*设置分页控件相对于表格区域的方位*，可选的有`'topLeft'`、`'topCenter'`、`'topRight'`、`'bottomLeft'`、`'bottomCenter'`、`'bottomRight'`
- **pageSize：** *int*型，用于*设置每页行记录数量*
- **current：** *int*型，用于*设置或监听当前分页所在的页码*
- **showSizeChanger：** *bool*型，用于*设置是否开启每页行记录数量切换功能*
- **pageSizeOptions：** `list[int]`型，用于*设置可供切换的每页行记录数量选项*
- **showTitle：** *bool*型，用于*设置是否显示分页控件附带的额外说明文字信息*
- **showQuickJumper：** *bool*型，用于*设置是否开启快捷页码切换功能*
- **showTotalPrefix：** *string*型，用于*设置额外说明文字信息中位于总记录数之前的内容*
- **showTotalSuffix：** *string*型，用于*设置额外说明文字信息中位于总记录数之后的内容*
- **hideOnSinglePage：** *bool*型，用于*设置分页控件是否在表格中总记录数不足一页时自动隐藏分页控件*
- **simple：** *bool*型，用于*设置是否开启简洁模式*
- **disabled：** *bool*型，用于*设置是否禁用分页控件*
- **size：** *string*型，用于*设置分页控件的尺寸规格*，可选的有`'default'`、`'small'`
- **total：** *int*型，当`mode="server-side"`时，用于*手动设置表格总记录数量*

**recentlyChangedRow：** *dict*型

　　用于*监听最近一次可编辑单元格操作后发生变动的行记录字典*

**summaryRowContents：** `list[dict]`型

　　用于*配置总结栏相关功能*，每个字典元素按顺序共同构成当前表格的总结栏，可用的键值对参数有：

- **content：** *组件型*，用于*设置当前对应总结栏的内容*

- **colSpan：** *int*型，默认为`1`，用于*设置当前总结栏横跨的字段数量*

- **align：** *string*型，默认为`'left'`，用于*设置当前总结栏内容的对齐方式*，可选的有`'left'`、`'center'`、`'right'`

**summaryRowFixed：** *bool*型，默认为`False`

　　用于*设置当前总结栏是否固定在底端显示*

**conditionalStyleFuncs：** *dict*型

　　用于*为各个字段配置用于处理自定义样式的javascript函数字符串*，键为相应字段的`dataIndex`，值为字字符串，注意，此功能与单元格可编辑功能不能同时使用

**expandedRowKeyToContent：** `list[dict]`型

　　用于*为对应行配置可展开内容*，每个字典元素用于定义对应行的可展开内容，可用的键值对参数有：

- **key：** *string*型，用于*设置当前可展开内容对应的行记录key值*
- **content：** *组件型*，用于*设置当前可展开行内容*

**expandedRowWidth：** *int*或*string*型

　　用于*设置当前表格中行展开控件列的宽度*

**expandRowByClick：** *bool*型，默认为`False`

　　用于*设置当前表格的可展开内容是否可通过点击对应行任意位置进行触发*

**enableCellClickListenColumns：** `list[string]`型

　　用于*设置当前表格中开启单元格点击事件监听的字段dataIndex信息*，此功能开启后会影响到多种再渲染模式的正常使用，请谨慎使用

**recentlyCellClickColumn：** *string*型

　　当`enableCellClickListenColumns`进行有效设置后，用于*监听最近一次单元格点击事件对应字段的dataIndex信息*

**recentlyCellClickRecord：** *dict*型

　　当`enableCellClickListenColumns`进行有效设置后，用于*监听最近一次单元格点击事件对应的行记录字典*

**nClicksCell：** *int*型，默认为`0`

　　当`enableCellClickListenColumns`进行有效设置后，用于*监听当前表格中相关单元格的累计点击次数*

**enableHoverListen：** *bool*型，默认为`False`

　　用于*设置是否开启行鼠标悬停事件监听*，注意，此功能开启后会影响到多种再渲染模式的正常使用，请谨慎使用

**recentlyMouseEnterColumnDataIndex：** *string*型

　　当`enableHoverListen=True`时，用于*监听最近一次鼠标移入列事件对应字段的dataIndex信息*

**recentlyMouseEnterRowKey：** *int*或*string*型

　　当`enableHoverListen=True`时，用于*监听最近一次鼠标移入行事件对应的行记录key值*

**recentlyMouseEnterRow：** *dict*型

　　当`enableHoverListen=True`时，用于*监听最近一次鼠标移入事件对应的行记录字典*

**emptyContent：** *组件型*

　　用于*自定义当前表格数据记录为空时的提示信息*

**containerId：** *string*型

　　用于*为当前表格中的各种悬浮层元素设置参考容器id*，从而解决局部容器内已展开的悬浮层元素不跟随滑动等问题

**cellUpdateOptimize：** *bool*型，默认为`False`

　　用于*设置是否针对当前表格开启单元格内容渲染优化加速*，开启后，当`data`更新时，由行`key`和列`dataIndex`唯一定位的单元格对应源数据无变化时不会进行重绘，从而降低页面刷新开销，但可能会导致一些内容刷新异常问题

**mode：** *string*型，默认为`'client-side'`

　　用于*设置表格数据渲染模式*，可选的有`'client-side'`（浏览器端渲染）、`'server-side'`（服务端渲染）

---

**miniChartHeight：** *int*型，默认为`30`

　　用于*为当前表格中的所有迷你图模式相关单元格设置像素高度*

**miniChartAnimation：** *bool*型，默认为`False`

　　用于*为当前表格中的所有迷你图模式相关单元格设置是否开启迷你图初始化动画效果*

**recentlyButtonClickedRow：** *dict*型

　　用于*监听最近一次按钮模式相关点击事件对应的行记录字典*

**nClicksButton：** *int*型，默认为`0`

　　用于*监听当前表格中各按钮模式字段按钮的累计点击次数*

**clickedContent：** *string*型

　　用于*监听最近一次按钮模式相关点击事件对应的按钮内容*

**recentlyButtonClickedDataIndex：** *string*型

　　用于*监听最近一次按钮模式相关点击事件对应的字段dataIndex信息*

**customFormatFuncs：** *dict*型

　　用于*为当前表格中各自定义格式模式字段设置相应的javascript函数字符串*，键为相应字段的`dataIndex`，值为字字符串

**recentlyCheckedRow：** *dict*型

　　用于*监听最近一次勾选框模式相关勾选事件对应的行记录字典*

**recentlyCheckedLabel：** *string*型

　　用于*监听最近一次勾选框模式相关勾选事件对应的勾选框标签内容*

**recentlyCheckedDataIndex：** *string*型

　　用于*监听最近一次勾选框模式相关勾选事件对应的字段dataIndex信息*

**recentlyCheckedStatus：** *bool*型

　　用于*监听最近一次勾选框模式相关勾选事件对应的勾选框状态*

**recentlySwitchRow：** *dict*型

　　用于*监听最近一次开关模式相关事件对应的行记录字典*

**recentlySwitchDataIndex：** *string*型

　　用于*监听最近一次开关模式相关事件对应的字段dataIndex信息*

**recentlySwitchStatus：** *bool*型

　　用于*监听最近一次开关模式相关事件对应的开关状态*

**nClicksDropdownItem：** *int*型，默认为`0`

　　用于*监听当前表格中各下拉选择菜单模式相关选项的累计点击次数*

**recentlyClickedDropdownItemTitle：** *string*型

　　用于*监听最近一次下拉选择菜单模式选项点击事件对应的选项标题内容*

**recentlyDropdownItemClickedDataIndex：** *string*型

　　用于*监听最近一次下拉选择菜单模式选项点击事件对应的字段dataIndex信息*

**recentlyDropdownItemClickedRow：** *dict*型

　　用于*监听最近一次下拉选择菜单模式选项点击事件对应的行记录字典*