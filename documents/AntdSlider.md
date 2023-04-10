**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**vertical：** *bool*型，默认为`False`

　　用于*设置是否垂直展示滑动输入条*

**range：** *bool*型，默认为`False`

　　用于*设置是否启用范围选择功能*

**min：** *int*或*float*型，必填

　　用于*设置可调范围下限*

**max：** *int*或*float*型，必填

　　用于*设置可调范围上限*

**step：** *int*或*float*型，默认为`1`

　　用于*设置滑动调节步长*

**marks：** *dict*型

　　用于*设置与指定刻度值一一对应的刻度标签*

**tooltipVisible：** *bool*型

　　用于*设置滑动调节提示信息框显示策略*，`True`表示保持显示，`False`表示不显示，默认不设置则仅在用户拖拽滑动时进行展示

**tooltipPrefix：** *string*型，默认为`''`

　　用于*设置滑动调节提示信息框的额外前缀文字内容*

**tooltipSuffix：** *string*型，默认为`''`

　　用于*设置滑动调节提示信息框的额外后缀文字内容*

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**value：** *int*、*float*或*list*型

　　用于*监听或设置当前滑动选择值*

**defaultValue：** *int*、*float*或*list*型

　　用于*监听或设置初始化时的滑动选择值*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）