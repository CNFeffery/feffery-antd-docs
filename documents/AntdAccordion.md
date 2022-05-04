**children：**

　　用于*传入内部嵌套的若干个AntdAccordionItem*

**accordion：** *bool*型，默认为`True`

　　用于设置*是否开启手风琴模式*，即同时只会存在一个展开的手风琴项，新手风琴项的展开会伴随先前已打开手风琴项的自动关闭

**activeKey：** *string*、*int*或*list*型

　　用于*设置及记录当前处于展开状态的手风琴项key值*

**defaultActiveKey：** *string*、*int*或*list*型

　　用于*设置默认状态下处于展开状态的手风琴项key值*

**bordered：** *bool*型，默认为`True`

　　设置*是否渲染边框*

**collapsible：** *string*型

　　用于统一设置*内部所有手风琴项的点击折叠触发行为*，可选的有`'header'`（点击标题触发）、`'disabled'`（禁用折叠）

**expandIconPosition：** *string*型，默认为`'left'`

　　用于设置*每个手风琴项折叠图标的位置*，可选的有`'left'`和`'right'`

**ghost：** *bool*型，默认为`False`

　　用于设置*是否以透明无边框方式渲染每个手风琴项*