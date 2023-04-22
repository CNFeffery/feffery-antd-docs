**id：** *string*或*dict*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**options：** `list[dict]`型，必填

　　用于*构建下拉选择的选项结构*，每个字典的可用键值对参数有：

- **label：** *组件型*，用于*设置当前选项的标签内容*
- **value：** *string*、*int*或*float*型，用于*设置当前选项的值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前选项*
- **colors：** `list[string]`型，用于*在色带特殊渲染模式下定义当前选项的色彩值序列*
- **group：** *string*型，用于*设置当前分组的标签内容*
- **options：** `list[dict]`型，用于*定义嵌套在当前分组下的选项配置字典数组*

**listHeight：** *int*型，默认为`256`

　　用于*设置下拉选择菜单的像素高度*

**colorsMode：** *string*型

　　当需要进行色带渲染时，用于*设置色带的渲染模式*，可选的有`'sequential'`（连续色带）、`'diverging'`（离散色带）

**colorsNameWidth：** *int*型，默认为`40`

　　用于*在色带渲染模式下设置颜色名称部分的像素宽度*

**mode：** *string*型

　　用于*设置选择模式*，可选的有`'multiple'`（多选）、`'tags'`（自由新增），默认不设置则为单选

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *string*型

　　用于*设置空白选择下的填充说明文字*

**placement：** *str*型，默认为`'bottomLeft'`

　　用于*设置下拉菜单的展开方向*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**value：** *string*、*int*、*float*或*list*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *string*、*int*、*float*或*list*型

　　用于*监听或设置初始化时的已选中值*

**maxTagCount：** *int*或*str*型

　　用于*设置多选模式下选择框内展示的已选项最大数量*，亦可设置为`'responsive'`开启响应式模式进行自适应调整

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**optionFilterProp：** *string*型，默认为`'value'`

　　用于*设置搜索内容对应各选项的匹配字段*，可选的有`value''`、`'label'`

**searchValue：** *string*型

　　用于*监听当前已输入的搜索内容*

**debounceSearchValue：** *string*型

　　用于*防抖监听当前已输入的搜索内容*

**debounceWait：** *int*型，默认为`200`

　　用于*设置针对debounceSearchValue更新的防抖延时时长*，单位：毫秒

**autoSpin：** *bool*型，默认为`False`

　　用于*设置是否在当前下拉选择的任意参数充当回调的输出角色，显示后缀加载中图标动画*

**autoClearSearchValue：** *bool*型，默认为`True`

　　当`mode='multiple'`或`mode='tags'`时，用于*设置是否在新选项被选中后自动清空输入框中的搜索内容*

**emptyContent：** *组件型*

　　用于*自定义无选项时下拉菜单中展示的提示内容*

**loadingEmptyContent：** *组件型*

　　当`autoSpin=True`且当前下拉选择的任意参数充当回调的输出角色时，用于*自定义无选项时下拉菜单中展示的提示内容*

**dropdownBefore：** *组件型*

　　用于*在下拉选择菜单开头添加额外的自定义内容*

**dropdownAfter：** *组件型*

　　用于*在下拉选择菜单末尾添加额外的自定义内容*

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户清空已选项*

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['value']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'value'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）