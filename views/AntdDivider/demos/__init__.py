import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    inner_text,  # noqa: F401
    vertical,  # noqa: F401
    variant,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('常规水平实线、虚线分割。'),
    },
    {
        'path': 'inner_text',
        'title': '内嵌文字',
        'description': fac.AntdParagraph('内嵌文字内容，并控制对齐方式。'),
    },
    {
        'path': 'vertical',
        'title': '竖直分割线',
        'description': fac.AntdParagraph('用竖直分割线水平排布若干元素。'),
    },
    {
        'path': 'variant',
        'title': '形态变体',
        'description': '设置参数`variant`使用不同的形态变体。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
