import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    indeterminate,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': None,
    },
    {
        'path': 'indeterminate',
        'title': '半选中状态',
        'description': fac.AntdParagraph(
            '开启半选中状态后，仅改变勾选框显示样式，与实际勾选状态无关。'
        ),
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
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
