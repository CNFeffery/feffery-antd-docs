**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**children：** *组件型*

　　用于传入*嵌套的子元素*

**tab：** *string*型

　　用于*设置当前标签页显示的标签页标题*

**key：** *string*型

　　用于*设置当前标签页的唯一id信息*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前标签页*

**closable：** *bool*型，默认为`True`

　　当父级`AntdTabs`设置参数`type='editable-card'`时，用于*设置是否为当前标签页面板渲染关闭按钮*

**titleSideInfoPopover：** *dict*型

　　用于*在当前标签页面板标题右侧设置悬浮提示信息卡片*，可用的键值对参数有：

- **title：** *string*型，用于*设置提示信息卡片的标题*
- **content：** *string*型，用于*设置提示信息卡片的正文内容*