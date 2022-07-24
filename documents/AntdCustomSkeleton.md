**skeletonContent：** *组件型*

　　用于*设置加载状态时显示的元素*

**debug：** *bool*型，默认为`False`

　　用于设置是否开启*debug模式*，开启后，每当对应`AntdCustomSkeleton`组件加载骨骼屏渲染时，`浏览器开发者工具-console`中会打印触发本次骨骼屏渲染的子节点**id**信息

**listenPropsMode：** *string*型，默认为`'default'`

　　用于设置特殊的*子节点监听过滤模式*，默认为`'default'`时，`AntdCustomSkeleton`的所有后代组件作为回调的`Output`进行回调过程时，都会触发加载动画；当设置为`'exclude'`时，会开启*排除过滤模式*，此时传入`includeProps`参数列表中的所有`'id.prop名称'`对应的后代组件处于回调时不会触发加载动画；当设置为`'include'`时，会开启*包含监听模式*，此时与`'exclude'`**恰恰相反**，只有传入到参数`includeProps`列表中的所有`'id.prop名称'`对应的后代组件的回调过程才会被`AntdCustomSkeleton`监听

**excludeProps：** *list*型

　　配合`listenPropsMode='exclude'`模式使用

**includeProps：** *list*型

　　配合`listenPropsMode='include'`模式使用