**options：** *list*型

　　用于设置*子项待选项*，每个元素为*dict*型，可用的键值对参数有：

- label：*string*型，用于设置*当前子项标签文字*
- value：*string*型，用于设置*当前子项对应值*

**autoSize：** *bool*或*dict*型，默认为`False`

　　用于设置*是否开启输入框自适应高度模式*，也可以传入*dict*型来自行设置至多至少要显示的输入框行数，可用的键值对参数有：

- minRows：*int*型，用于设置*最小输入框行数*
- maxRows：*int*型，用于设置*最大输入框行数*

**prefix：** *string*型，默认为`'@'`

　　用于设置*触发子项悬浮层展开的字符*

**popupContainerId：** *string*型

　　用于在*局部滚动条*模式下，以传入对应*id*的方式为子项悬浮展开层绑定合适的参考容器，从而修正一些潜在的显示问题，具体使用场景参考本页对应示例

**placement：** *string*型，默认为`'bottom'`

　　用于设置*子项弹出层的方位*，可选的有`'top'`与`'bottom'`

**disabled：** *bool*型，默认为`False`

　　用于设置*是否禁用当前组件*

**status：** *str型*

　　用于*手动设置组件的校验状态*，可选的有`'error'`和`'warning'`

**value：** *string*型

　　用于*记录当前提及输入框内全部文字内容*

**defaultValue：** *string*型

　　用于*设置初始化时提及输入框内全部文字内容*

**selectedOptions：** *list*型

　　用于*记录当前已提及的子项值*