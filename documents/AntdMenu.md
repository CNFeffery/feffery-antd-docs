**id：** *string*型

　　用于设置*当前组件的唯一id信息*

**key：** *string*型

　　对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果

**style：** *dict*型

　　用于设置*当前组件的css样式*

**className：** *string*或*dict*型

　　用于设置*当前组件的css类名*，支持[动态css](/advanced-classname)

**menuItems：** `list[dict]`型

　　用于*定义导航菜单结构*，列表中每个字典用于定义导航菜单中的对应元素，可用的键值对参数有：

- **component：** *string*型，用于*定义当前元素的角色*，可选的有`'Item'`（菜单项，用户可点击选中，应作为整个菜单结构的末端节点）、`'SubMenu'`（子菜单，用于嵌套下一层元素，用户可点击进行展开/关闭）、`'ItemGroup'`（菜单项分组，用于分组直接展示内部嵌套的元素，类似`AntdSelect`中对选项分组后的效果）、`'Divider'`（水平分割线）

- **props：** *dict*型，用于*设置当前元素的其他参数*，其中：
  - **key：** *str*型，用于*设置当前元素的唯一id*
  - **title：** *str*型，用于*设置当前元素的标题内容*
  - **disabled：** *bool*型，默认为`False`，用于*设置是否禁用当前元素*
  - **icon：** *str*型，用于*为当前元素添加前缀图标*，同`AntdIcon`中的`icon`参数
  - **danger：** *bool*型，默认为`False`，用于*设置是否以危险状态显示当前元素*，此参数仅`Item`可用
  - **href：** *str*型，用于*为当前节点设置跳转链接url*，此参数仅`Item`可用
  - **target：** *str*型，用于*为当前节点设置跳转行为*，此参数仅`Item`可用
  - **dashed：** *bool*型，默认为`False`，用于*设置当前水平分割线元素是否为虚线*，此参数仅`Divider`可用
  
- **children：** `list[dict]`型，用于*传入内部嵌套的其它元素*，此参数仅`SubMenu`和`ItemGroup`可用

　　用户可以在上述参数结构体系下自由配置任意的导航菜单结构，下面是一个示例：

```python
menuItems = [
    {
        'component': 'Item',
        'props': {
            'key': '/home-page',
            'title': '主页',
            'icon': 'home'
        }
    },
    {
        'component': 'SubMenu',
        'props': {
            'key': '/sub-menu1',
            'title': '子菜单1'
        },
        'children': [
            {
                'component': 'ItemGroup',
                'props': {
                    'key': '/sub-menu1/item-group1',
                    'title': '菜单项分组1-1'
                },
                'children': [
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/sub-menu1/item-group1/item1',
                            'title': '菜单项1-1-1'
                        }
                    },
                    {
                        'component': 'Item',
                        'props': {
                            'key': '/sub-menu1/item-group1/item2',
                            'title': '菜单项1-1-2',
                            'disabled': True
                        }
                    },
                    {
                        'component': 'SubMenu',
                        'props': {
                            'key': '/sub-menu1/item-group1/sub-menu1',
                            'title': '子菜单1-1-3'
                        },
                        'children': [
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/sub-menu1/item-group1/sub-menu1/item1',
                                    'title': '菜单项1-1-3-1'
                                }
                            },
                            {
                                'component': 'Item',
                                'props': {
                                    'key': '/sub-menu1/item-group1/sub-menu1/item2',
                                    'title': '菜单项1-1-3-2'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
```

**mode：** *str*型，默认为`'vertical'` 

　　用于*设置导航菜单显示模式*，可选的有`'vertical'`（垂直模式）、`'inline'`（内嵌模式）、`'horizontal'`（水平模式）

**theme：** *str*型，默认为`'light'`

　　用于*设置整体色彩风格模式*，可选的有`'light'`（浅色模式）、`'dark'`（暗色模式）

**currentKey：** *str*型

　　用于*监听或设置被选中的`Item`元素的`key`*值

**defaultSelectedKey：** *str*型

　　用于*设置初始化时被选中的`Item`元素的`key`*值

**openKeys：** *list*型

　　用于*监听或设置当前菜单中处于展开状态的`SubMenu`元素的`key`值列表*

**defaultOpenKeys：** *list*型

　　用于*设置初始化时当前菜单中处于展开状态的`SubMenu`元素的`key`值列表*

**renderCollapsedButton：** *bool*型，默认为`False`

　　用于*设置是否渲染菜单自带的折叠/展开触发按钮*

**popupContainer：** *string*型，默认为`'body'`

　　用于*为当前组件涉及的悬浮层元素设置参考容器类型*，可选的有`'body'`（以页面根节点为参考）和`'parent'`（以当前元素的父容器为参考），当组件位于局部滚动容器内时，通过设置`popupContainer='parent'`可以解决悬浮层滚动不跟随的问题

**inlineCollapsed：** *bool*型，默认为`False`

　　用于*设置当前菜单是否处于折叠状态*，进`mode='inline'`时有效

**persistence：** *bool*型

　　用于*设置是否为当前组件开启属性持久化*

**persisted_props：** *list*型，默认为`['currentKey', 'openKeys']`

　　用于*设置针对当前组件的哪些属性进行持久化*，可选的有`'currentKey'`、`'openKeys'`

**persistence_type：** *string*型，默认为`'local'`

　　用于*设置针对当前组件进行属性持久化的存储类型*，可选的有`'local'`（浏览器本地缓存）、`'session'`（当前标签页会话缓存）、`'memory'`（内存临时缓存）