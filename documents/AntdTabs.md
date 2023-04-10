**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

<font style="color: white; background: #fab005; border-radius: 6px; padding: 3px 8px;">0.3.x将废弃</font> **children：** *组件型*

　　用于传入*嵌套的若干AntdTabPane元素*

**items：** `list[dict]`型

　　用于*定义各个标签页面板*，每个字典代表一个标签页面板，可用的键值对参数有：

- **label：** *组件型*，用于*设置当前标签页的标题内容*
- **key：** *string*型，用于*设置当前标签页的唯一识别id*
- **children：** *组件型*，用于*设置当前标签页内需要嵌套的子元素*
- **disabled：** *bool*型，用于*设置是否禁用当前标签页*
- **forceRender：** *bool*型，默认为`False`，用于*设置初始化时是否强制对当前标签页内的元素进行渲染*
- **closable：** *bool*型，在`editable-card`模式下，用于*设置当前标签页面板是否可关闭*

**activeKey：** *string*型

　　用于*设置或监听当前所激活的标签页key值*

**defaultActiveKey：** *string*型

　　用于*设置初始化时激活的标签页key值*

**disabledTabKeys：** `list[string]`型，默认为`[]`

　　用于*设置需要进行禁用的标签页key值数组*

**tabPosition：** *string*型，默认为`'top'`

　　用于*设置当前标签页的显示方位*，可选的有`'top'`、`'left'`、`'right'`、`'bottom'`

**size：** *string*型，默认为`'default'`

　　用于*设置当前标签页的尺寸规格*，可选的有`'small'`、`'default'`、`'large'`

**type：** *string*型，默认为`'line'`

　　用于*设置当前标签页的渲染类型*，可选的有`'line'`、`'card'`、`'editable-card'`

**centered：** *bool*型，默认为`False`

　　用于*设置是否为标签栏进行居中布局*

**tabBarGutter：** *int*型

　　用于*设置标签栏选项之间的像素间距*

**inkBarAnimated：** *bool*型，默认为`True`

　　用于*设置标签页切换时是否开启标签栏过渡动画*

**tabPaneAnimated：** *bool*型，默认为`False`

　　用于*设置标签页切换时是否开启内容区过渡动画*

**latestDeletePane：** *string*型

　　`type="editable-card"`时可用，用于*监听最近一次发生删除操作的标签页key值*

**tabBarLeftExtraContent：** *组件型*

　　用于*为当前标签页的标签栏设置前缀内容*

**tabBarRightExtraContent：** *组件型*

　　用于*为当前标签页的标签栏设置后缀内容*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['activeKey']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'activeKey'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）