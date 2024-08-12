import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    mode,  # noqa: F401,  # noqa: F401
    component_as_item,  # noqa: F401
    dark_mode,  # noqa: F401
    default_expand_nodes,  # noqa: F401
    default_select_node,  # noqa: F401
    prefix_icon,  # noqa: F401
    as_link,  # noqa: F401
    builtin_collapse,  # noqa: F401
    collapse_with_sider,  # noqa: F401
    indent,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基础的导航菜单。'),
    },
    {
        'path': 'mode',
        'title': '显示模式',
        'description': fac.AntdParagraph(
            [
                '导航菜单具有三种显示模式，',
                '其中',
                fac.AntdText('horizontal', code=True),
                '模式会在宽度受限时自动呈现省略状态。',
            ]
        ),
    },
    {
        'path': 'component_as_item',
        'title': '组件型菜单项',
        'description': fac.AntdParagraph(
            [
                '配合参数',
                fac.AntdText('menuItemKeyToTitle', code=True),
                '可以将指定的菜单项标题用组件元素代替。',
            ]
        ),
    },
    {
        'path': 'dark_mode',
        'title': '暗黑主题',
        'description': fac.AntdParagraph('内置的暗黑主题风格。'),
    },
    {
        'path': 'default_expand_nodes',
        'title': '设置默认展开项',
        'description': fac.AntdParagraph(
            '为导航菜单设置初始化时就处于展开状态的子菜单节点。'
        ),
    },
    {
        'path': 'default_select_node',
        'title': '设置默认选中项',
        'description': fac.AntdParagraph(
            '为导航菜单设置初始化时就处于选中状态的菜单项节点。'
        ),
    },
    {
        'path': 'prefix_icon',
        'title': '前缀图标',
        'description': fac.AntdParagraph('为各菜单项快捷设置前缀图标。'),
    },
    {
        'path': 'as_link',
        'title': '菜单项链接跳转',
        'description': fac.AntdParagraph(
            '菜单项节点可设置对应的跳转链接地址。'
        ),
    },
    {
        'path': 'builtin_collapse',
        'title': '内置折叠状态控制',
        'description': fac.AntdParagraph(
            '使用导航菜单内置的折叠状态控制功能。'
        ),
    },
    {
        'path': 'collapse_with_sider',
        'title': '配合侧边栏自定义控制折叠',
        'description': fac.AntdParagraph(
            [
                '配合侧边栏组件',
                fac.AntdText('AntdSider', strong=True),
                '可实现针对导航菜单更灵活的折叠控制。',
            ]
        ),
    },
    {
        'path': 'indent',
        'title': '调整子菜单缩进宽度',
        'description': fac.AntdParagraph('子菜单逐级缩进的像素宽度可调整。'),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('通过回调监听当前选中的菜单项。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
