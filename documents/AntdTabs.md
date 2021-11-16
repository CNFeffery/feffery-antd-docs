**children：** *list*型，必填

　　用于传入其下嵌套的**AntdTabPane**组件所组成的列表

**defaultActiveKey：** *string*型

　　用于设置默认激活打开的其下**AntdTabPane**组件对应的*key值*

**tabPosition：** *string*型，默认为`'top'`

　　用于设置标签页的*吸附位置*，可选的有`'top'`、`'left'`、`'right'`与`'bottom'`

**size：** *string*型，默认为`'default'`

　　用于设置标签页整体的尺寸规格，可选的有`'default'`、`'small'`与`'large'`

**type：** *string*型，默认为`'line'`

　　用于设置标签页的*渲染类型*，可选的有`'line'`、`'card'`与`'editable-card'`

**activeKey：** *string*型

　　记录当前被激活打开的**AntdTabPane**组件对应的*key值*

**latestDeletePane：** *string*型

　　配合`type='editable-card'`情况使用，用于记录最近一次*被点击的关闭按钮*对应的**AntdTabPane**组件*key值*