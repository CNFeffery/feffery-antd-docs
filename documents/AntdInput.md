**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**mode：** *string*型，默认为`'default'`

　　用于*设置当前输入框的功能模式*，可选的有`'default'`（常规输入框）、`'search'`（带搜索功能的输入框）、`'text-area'`（文本域输入框）、`'password'`（密码输入框）

**autoComplete：** *string*型，默认为`'on'`

　　用于*设置输入框对应的浏览器自带自动填充功能*，可选的有`'on'`（开启）、`'off'`（关闭）

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

**md5Value：** *string*型

　　当`passwordUseMd5=True`时，用于*监听当前已输入值对应的md5加密信息*

**debounceValue：** *string*型

　　使用`debounceValue`代替`value`配合有效的防抖延时设置，以实现有效的回调防抖效果

**passwordUseMd5：** *bool*型，默认为`False`

　　用于*设置密码输入框模式下是否开启md5加密*

**debounceWait：** *int*型，默认为`200`

　　用于*为debounceValue的监听更新设置防抖延时时长*，单位：毫秒

**addonBefore：** *组件型*

　　用于*设置输入框前置额外元素*

**addonAfter：** *组件型*

　　用于*设置输入框后置额外元素*

**prefix：** *组件型*

　　用于*设置输入框内嵌前缀元素*

**suffix：** *组件型*

　　用于*设置输入框内嵌后缀元素*

**maxLength：** *int*型

　　用于*设置输入框的最大内容输入字符数*，默认无限制

**showCount：** *bool*型，默认为`False`

　　用于*设置是否展示当前已输入字符数*

**countFormat：** *string*型

　　当`showCount=True`时，用于*自定义字符计数匹配所使用的正则表达式*

**autoSize：** *bool*或*dict*型，默认为`False`

　　用于*配置针对文本域输入框模式下的输入框自适应高度功能*，当传入*dict*型输入时，可用的键值对参数有：

- **minRows：** *int*型，用于*设置最小行数*
- **maxRows：** *int*型，用于*设置对大行数*

**nSubmit：** *int*型，默认为`0`

　　用于*监听光标在输入框内时键盘enter键被按下的次数*

**nClicksSearch：** *int*型，默认为`0`

　　用于*监听搜索输入框模式下搜索按钮被点按次数*

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户清空已选项*

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**emptyAsNone：** *bool*型，默认为`False`

　　当输入框中无有效内容时，用于*设置是否统一将value和debounceValue更新为None而不是空字符串*

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value', 'md5Value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`、`'md5Value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）