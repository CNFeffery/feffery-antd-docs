import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    menu_mode,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的悬浮按钮组。'),
        'iframe': True,
    },
    {
        'path': 'menu_mode',
        'title': '菜单模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('trigger', code=True),
                '开启不同触发方式对应的菜单模式。',
            ]
        ),
        'iframe': True,
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '监听悬浮按钮组菜单模式下的展开状态。',
        'iframe': True,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
