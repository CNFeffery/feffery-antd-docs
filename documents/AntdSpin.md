**size：** *string*型，默认为`'middle'`

　　设置加载中部件的*显示尺寸*，可选的有`'small'`、`middle`和`'large'`

**delay：** *int*型

　　设置*延迟加载时长*，单位毫秒，若子节点在设置的`delay`时长之内即加载完毕，则不会渲染加载动画过程，此参数用于避免短暂回调过程导致的加载动画*闪烁*情况，从而提高用户体验

**text：** *string*型

　　用于在加载动画中添加*说明文字*内容

**debug：** *bool*型，默认为`False`

　　用于设置是否开启*debug模式*，开启后，每当对应`AntdSpin`组件加载动画渲染时，`浏览器开发者工具-console`中会打印触发本次加载动画的子节点**id**信息

**listenPropsMode：** *string*型，默认为`'default'`

　　用于设置特殊的*子节点监听过滤模式*，默认为`'default'`时，`AntdSpin`的所有后代组件作为回调的`Output`进行回调过程时，都会触发加载动画；当设置为`'exclude'`时，会开启*排除过滤模式*，此时传入`includeProps`参数列表中的所有`'id.prop名称'`对应的后代组件处于回调时不会触发加载动画；当设置为`'include'`时，会开启*包含监听模式*，此时与`'exclude'`**恰恰相反**，只有传入到参数`includeProps`列表中的所有`'id.prop名称'`对应的后代组件的回调过程才会被`AntdSpin`监听

**excludeProps：** *list*型

　　配合`listenPropsMode='exclude'`模式使用

**includeProps：** *list*型

　　配合`listenPropsMode='include'`模式使用