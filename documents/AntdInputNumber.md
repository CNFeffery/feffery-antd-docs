**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**addonBefore：** *组件型*

　　用于*设置输入框前置额外元素*

**addonAfter：** *组件型*

　　用于*设置输入框后置额外元素*

**autoFocus：** *bool*型，默认为`False`

　　用于*设置是否自动获取焦点*

**prefix：** *组件型*

　　用于*设置输入框内嵌前缀元素*

**controls：** *bool*型，默认为`True`

　　用于*设置是否在数字输入框右侧内部添加辅助快捷增减按钮*

**keyboard：** *bool*型，默认为`True`

　　用于*设置是否允许通过键盘上下键调整数值*

**min：** *int*、*float*或*string*型

　　用于*设置当前数字输入框的合法数值下限*，默认无限制

**max：** *int*、*float*或*string*型

　　用于*设置当前数字输入框的合法数值上限*，默认为限制

**step：** *int*、*float*或*string*型

　　用于*设置当前数字输入框的增减步长*

**precision：** *int*型

　　用于*设置当前数字输入框的数值精度即小数位数*

**stringMode：** *bool*型，默认为`False`

　　用于*设置是否开启高精度模式*，可用于准确录入高精度数值，开启后参数`min`、`max`、`step`、`value`、`defaultValue`都应为*string*型

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *string*型

　　用于*设置空白输入下的填充说明文字*

**value：** *list*型

　　用于*监听或设置当前已输入值*

**defaultValue：** *list*型

　　用于*监听或设置初始化时的已输入值*

**debounceValue：** *string*型

　　使用`debounceValue`代替`value`配合有效的防抖延时设置，以实现有效的回调防抖效果

**debounceWait：** *int*型，默认为`200`

　　用于*为debounceValue的监听更新设置防抖延时时长*，单位：毫秒

**nSubmit：** *int*型，默认为`0`

　　用于*监听光标在输入框内时键盘enter键被按下的次数*

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）