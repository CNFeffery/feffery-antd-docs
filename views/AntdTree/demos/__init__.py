from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    default_expand_all,  # noqa: F401
    not_show_line,  # noqa: F401
    show_icon,  # noqa: F401
    switcher_icon,  # noqa: F401
    custom_node_style,  # noqa: F401
    node_tooltip,  # noqa: F401
    node_context_menu,  # noqa: F401
    virtual_scroll,  # noqa: F401
    multiple,  # noqa: F401
    multiple_with_checkbox,  # noqa: F401
    node_check_status_style,  # noqa: F401
    node_check_status_suffix,  # noqa: F401
    check_strictly,  # noqa: F401
    flat_tree_data,  # noqa: F401
    draggable,  # noqa: F401
    drag_in_same_level,  # noqa: F401
    basic_callbacks,  # noqa: F401
    drag_callbacks,  # noqa: F401
    context_menu_callbacks,  # noqa: F401
    tree_search,  # noqa: F401
    node_favorited,  # noqa: F401
    node_scroll,  # noqa: F401
    async_load_node,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '树形控件的基础使用。',
    },
    {
        'path': 'default_expand_all',
        'title': '初始化展开全部节点',
        'description': '设置参数`defaultExpandAll=True`后，初始化时将展开全部节点。',
    },
    {
        'path': 'not_show_line',
        'title': '不显示连接线',
        'description': '设置参数`showLine=False`后，将隐藏树内部的连接线。',
    },
    {
        'path': 'show_icon',
        'title': '节点前缀图标',
        'description': '设置参数`showIcon=True`后，将显示各节点所定义的前缀图标。',
    },
    {
        'path': 'switcher_icon',
        'title': '自定义展开图标',
        'description': "通过参数`switcherIcon`可以传入**AntdIcon**中的`'antd-*'`类型图标组件，作为节点展开/收起控制图标。",
    },
    {
        'path': 'custom_node_style',
        'title': '自定义节点样式',
        'description': '精确控制每个节点的样式。',
    },
    {
        'path': 'node_tooltip',
        'title': '节点添加信息提示',
        'description': '各节点可自由添加随鼠标移入触发的信息提示内容。',
    },
    {
        'path': 'node_context_menu',
        'title': '节点添加右键菜单',
        'description': '各节点可自由添加随鼠标右键触发的下拉菜单。',
    },
    {
        'path': 'virtual_scroll',
        'title': '虚拟滚动',
        'description': '设置参数`height`后将开启固定像素高度下的虚拟滚动功能，适用于数据量较大的场景。',
    },
    {
        'path': 'multiple',
        'title': '多选模式',
        'description': '设置参数`multiple=True`后将开启多选模式。',
    },
    {
        'path': 'multiple_with_checkbox',
        'title': '带勾选框的多选模式',
        'description': '设置参数`checkable=True`后可为多选模式额外添加节点勾选框。',
    },
    {
        'path': 'node_check_status_style',
        'title': '节点勾选状态样式',
        'description': '控制节点在不同勾选状态下的额外样式。',
    },
    {
        'path': 'node_check_status_suffix',
        'title': '节点勾选状态后缀',
        'description': '控制节点在不同勾选状态下的额外后缀内容。',
    },
    {
        'path': 'check_strictly',
        'title': '父子节点独立勾选',
        'description': '设置参数`checkStrictly=True`后，父子节点间的勾选行为将彼此独立。',
    },
    {
        'path': 'flat_tree_data',
        'title': '扁平treeData模式',
        'description': "设置参数`treeDataMode='flat'`后，树结构应当传入扁平形式数据。",
    },
    {
        'path': 'draggable',
        'title': '树节点可拖拽',
        'description': "在参数`treeDataMode='tree'`的前提下，通过设置参数`draggable=True`可开启树节点拖拽功能。",
    },
    {
        'path': 'drag_in_same_level',
        'title': '限制仅允许同级拖拽',
        'description': '设置参数`dragInSameLevel=True`后，节点拖拽行为只允许在同一层级下进行。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '通过回调函数监听常见的交互事件。',
    },
    {
        'path': 'drag_callbacks',
        'title': '节点拖拽回调监听',
        'description': '通过回调函数监听节点拖拽事件。',
    },
    {
        'path': 'context_menu_callbacks',
        'title': '节点右键菜单点击回调监听',
        'description': '通过回调函数监听节点右键菜单点击事件。',
    },
    {
        'path': 'tree_search',
        'title': '快捷树搜索',
        'description': '基于参数`searchKeyword`快捷构建树搜索功能。',
    },
    {
        'path': 'node_favorited',
        'title': '节点收藏功能',
        'description': '快捷构建具有节点收藏功能的树形控件。',
    },
    {
        'path': 'node_scroll',
        'title': '节点滚动动作',
        'description': '基于参数`scrollTarget`针对已展开的节点进行节点滚动动作。',
    },
    {
        'path': 'async_load_node',
        'title': '异步加载节点',
        'description': '设置参数`enableAsyncLoad=True`后，对于未设置`isLeaf`为`True`且无`children`属性的节点，可通过回调监听节点展开信息，从而实现异步更新树结构。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
