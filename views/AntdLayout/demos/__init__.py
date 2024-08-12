import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    right_sider,  # noqa: F401
    collapsible_sider,  # noqa: F401
    responsive_collapsible_sider,  # noqa: F401
    collapsible_sider_with_menu,  # noqa: F401
    collapsible_sider_custom_trigger,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '经典布局方案的重点在于用',
                fac.AntdText('AntdLayout', strong=True),
                '包裹嵌套其他经典布局组件，从而构建出常用的各种经典页面布局方案。',
            ]
        ),
    },
    {
        'path': 'right_sider',
        'title': '右侧侧边栏',
        'description': fac.AntdParagraph('侧边栏方位可调整。'),
    },
    {
        'path': 'collapsible_sider',
        'title': '可折叠侧边栏',
        'description': fac.AntdParagraph(
            [
                '为',
                fac.AntdText('AntdSider', strong=True),
                '设置',
                fac.AntdText('collapsible=True', code=True),
                '开启自带的侧边栏折叠功能。',
            ]
        ),
        'iframe': True,
        'no_padding': True,
    },
    {
        'path': 'responsive_collapsible_sider',
        'title': '响应式可折叠侧边栏',
        'description': fac.AntdParagraph(
            '侧边栏可以指定屏幕宽度断点为阈值进行自动折叠及展开。'
        ),
        'iframe': True,
        'no_padding': True,
    },
    {
        'path': 'collapsible_sider_with_menu',
        'title': '可折叠侧边栏+导航菜单',
        'description': fac.AntdParagraph(
            '侧边栏折叠可联动内部的导航菜单组件。'
        ),
        'iframe': True,
        'no_padding': True,
    },
    {
        'path': 'collapsible_sider_custom_trigger',
        'title': '自定义折叠触发控件',
        'description': fac.AntdParagraph(
            [
                '设置',
                fac.AntdText('trigger=None', code=True),
                '后可自定义控件配合回调函数控制侧边栏折叠状态。',
            ]
        ),
        'iframe': True,
        'no_padding': True,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
