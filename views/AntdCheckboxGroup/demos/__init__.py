import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    basic_callbacks,  # noqa: F401
    select_all_with_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': None,
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': None,
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': fac.AntdParagraph('只读状态适用于单纯的数据展示场景。'),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
    {
        'path': 'select_all_with_callbacks',
        'title': '基于回调实现全选',
        'description': fac.AntdParagraph(
            '本例基于浏览器端回调，以实现更流畅的交互响应速度。'
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
