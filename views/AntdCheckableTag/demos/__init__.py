from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callbacks,  # noqa: F401
    checked_unchecked_content,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基本的使用示例。',
    },
    {
        'path': 'checked_unchecked_content',
        'title': '不同状态下的组件内容',
        'description': '可设置选中状态下和未选中状态下的组件内容。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '监听标签的选择状态。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
