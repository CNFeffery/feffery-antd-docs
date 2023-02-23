**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*型

　　用于设置*当前组件的css类名*

**locale：** *string*型，默认为`'zh-cn'`

　　用于*为当前组件的功能文案设置语言*，可选的有`'zh-cn'`（简体中文）、`'en-us'`（英文）

**treeDataMode：** *string*型，默认为`'tree'`

　　用于*设置针对treeData参数的解析模式*，可选的有`'tree'`（树形结构）、`'flat'`（扁平结构）

**treeData：** `list[dict]`型，必填

　　用于*构建树选择的选项结构*

　　当`treeDataMode='tree'`时，`treeData`参数需要符合树形解析模式，每个字典的可用键值对参数有：

- **title：** *string*型，必填，用于*设置当前节点对应的标题内容*
- **key：** *string*型，必填，用于*唯一标识当前节点*
- **value：** *int*、*float*或*string*型，必填，用于*设置当前节点的值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前节点*
- **checkable：** *bool*型，用于*设置是否为当前节点渲染勾选框*
- **disableCheckbox：** *bool*型，用于*设置是否禁用当前节点的勾选框*
- **selectable：** *bool*型，用于*设置当前节点是否可被选中*
- **isLeaf：** *bool*型，用于*是否强制设置当前节点为叶节点*

　　下面是树形`treeData`的示例：

```python
treeData = 
```

　　当`treeDataMode='flat'`时，`treeData`参数需要符合扁平解析模式，每个字典的可用键值对参数有：

- **title：** *string*型，必填，用于*设置当前节点对应的标题内容*
- **key：** *string*型，必填，用于*唯一标识当前节点*，从而实现父节点与子节点间的关联

- **value：** *int*、*float*或*string*型，必填，用于*设置当前节点的值*
- **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前节点*
- **checkable：** *bool*型，用于*设置是否为当前节点渲染勾选框*
- **disableCheckbox：** *bool*型，用于*设置是否禁用当前节点的勾选框*
- **selectable：** *bool*型，用于*设置当前节点是否可被选中*
- **isLeaf：** *bool*型，用于*设置是否强制设置当前节点为叶节点*
- **parent：** *string*型，用于*声明当前节点的父节点key值*，从而实现父节点与子节点间的关联

　　下面是扁平`treeData`的示例：

```python
treeData = 
```

**disabled：** *bool*型，默认为`False`

　　用于*设置是否禁用当前组件*

**size：** *string*型，默认为`'middle'`

　　用于*设置当前组件的尺寸规格*，可选项有`'small'`、`'middle'`和`'large'`

**bordered：** *bool*型，默认为`True`

　　用于*设置是否渲染边框*

**placeholder：** *string*型

　　用于*设置空白输入下的填充说明文字*

**placement：** *str*型，默认为`'bottomLeft'`

　　用于*设置下拉菜单的展开方向*，可选的有`'bottomLeft'`、`'bottomRight'`、`'topLeft'`及`'topRight'`

**treeLine：** *bool*型，默认为`False`

　　用于*设置是否为树渲染连接线*

**value：** *int*、*float*、*string*或*list*型

　　用于*监听或设置当前已选中值*

**defaultValue：** *int*、*float*、*string*或*list*型

　　用于*监听或设置初始化时的已选中值*

**maxTagCount：** *int*或*str*型

　　用于*设置多选模式下选择框内展示的已选项最大数量*，亦可设置为`'responsive'`开启响应式模式进行自适应调整

**listHeight：** *int*型，默认为`256`

　　用于*设置下拉菜单的像素高度*

**multiple：** *bool*型，默认为`False`

　　用于*设置是否开启多选模式*

**treeCheckable：** *bool*型，默认为`False`

　　用于*设置是否为各节点添加勾选框*

**treeDefaultExpandAll：** *bool*型，默认为`False`

　　用于*设置初始化时是否展开所有节点*

**treeDefaultExpandedKeys：** *list*型

　　用于*设置初始化时处于处于展开状态的节点key值*

**treeExpandedKeys：** *list*型

　　用于*监听或设置当前处于展开状态的节点key值*

**treeCheckStrictly：** *bool*型，默认为`False`

　　用于*设置是否取消父子节点间的选择关联性*

**virtual：** *bool*型，默认为`True`

　　用于*设置是否启用虚拟滚动以显著提升渲染性能表现*

**status：** *string*型

　　用于*强制设置组件的状态*，可选的有`'error'`和`'warning'`

**allowClear：** *bool*型，默认为`True`

　　用于*设置是否允许用户清空已选项*

**treeNodeFilterProp：** *string*型，默认为`'value'`

　　用于*设置进行内容搜索的目标字段*，可选的有`'title'`、`'value'`

**autoClearSearchValue：** *bool*型，默认为`True`

　　用于*设置在多选模式下当有新的节点被选中时是否自动清空搜索框中的搜索内容*

**showCheckedStrategy：** *string*型，默认为`'show-all'`

　　用于*设置已选项的回填显示策略*，可选的`'show-all'`（既显示父节点也显示子节点）、有`'show-parent'`（当所有子节点都被选中时，只显示父节点）、`'show-child'`（只显示选中的子节点）

**dropdownBefore：** *组件型*

　　用于*在下拉菜单开头添加额外的自定义内容*

**dropdownAfter：** *组件型*

　　用于*在下拉菜单末尾添加额外的自定义内容*

**readOnly：** *bool*型

　　用于*设置是否以只读模式进行展示*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题