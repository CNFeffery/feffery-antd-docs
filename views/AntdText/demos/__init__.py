import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    different_render_mode,  # noqa: F401
    content_ellipsis,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'different_render_mode',
        'title': '不同的渲染模式',
        'description': fac.AntdParagraph(
            '使用不同的渲染模式展示不同样式的文字。'
        ),
    },
    {
        'path': 'content_ellipsis',
        'title': '内容省略功能',
        'description': fac.AntdParagraph('文字内容过长时可开启省略功能。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
