**menuItems：** *list*型，必填，无默认值

　　用于自由设计导航菜单结构，列表中元素为字典（通过`children`键值对向下嵌套以构成复杂的层级导航菜单结构），每个字典都代表导航菜单中的一个元素，其中：

- 键值对`component`：`str`型，表示当前元素的*角色*，`'Item'`表示*菜单项*元素，也是唯一供用户点击*选中*的元素，应作为整个菜单结构的末端元素；`'SubMenu'`表示*子菜单*元素，用于嵌套存放下一层元素，供用户点击*展开/关闭*；`'ItemGroup'`表示*菜单项分组*，用于以静态的方式（即无点击交互操作，直接展示）对其内部其他元素进行分组，类似`AntdSelect`中对选项分组后的效果

- 键值对`props`：`dict`型，用于传入当前元素对应的*额外属性*，其中：

  - 键值对`key`：`str`型，用于传入当前元素*唯一id*
  - 键值对`title`：`str`型，用于传入当前元素在导航菜单中*显示的文字标题*
  - 键值对`disabled`：`bool`型，用于设置是否*禁用当前元素*（禁用效果会覆盖其内部嵌套的所有元素），默认为`False`
  - 键值对`icon`：`str`型，用于为对应元素添加*前缀图标*，目前版本支持的图标有`'home'`、`'upload'`、`'bar-chart'`、`'pie-chart'`、`'dot-chart'`、`'line-chart'`、`'apartment'`、`'app-store'`、`'app-store-add'`、`'bell'`、`'calculator'`、`'calendar'`、`'database'`、`'history'`，具体效果见后面的例子
  - 键值对`danger`：`bool`型，用于设置是否以*危险状态*显示当前元素（**注意**，此参数仅`Item`可用）

- 键值对`children`：`list`型，**注意**，此参数仅`SubMenu`和`ItemGroup`可用，用于传入内部嵌套的其它元素

　　用户可以在上述参数结构体系下自由组合出需要的复杂导航菜单结构，下面是一个示例：

```Python
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

　　用于设置导航菜单*整体显示模式*，`'vertical'`表示垂直显示模式，`'inline'`表示垂直内嵌显示模式，`'horizontal'`表示水平显示模式

**theme：** *str*型，默认为`'light'`

　　用于设置整体色彩风格模式，`'light'`表示浅色模式，`'dark'`表示暗色模式

**defaultOpenKeys：** *list*型

　　针对导航菜单中的`SubMenu`元素，设置页面初始化状态下哪些`key`值对应的`SubMenu`会*默认展开*

**defaultSelectedKey：** *str*型

　　针对导航菜单中的`Item`元素，设置页面初始化状态下哪一个`key`值对应的`Item`会默认被选中

**renderCollapsedButton：** *bool*型，默认为`False`

　　用于设置是否渲染动态折叠导航菜单的交互按钮

**currentKey：** *str*型

　　用于在回调中捕获当前被选中的`Item`元素对应的`key`值