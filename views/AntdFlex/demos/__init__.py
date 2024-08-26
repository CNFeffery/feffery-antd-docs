from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    align,  # noqa: F401
    gap,  # noqa: F401
    wrap,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基础的水平排布与垂直排布。',
    },
    {
        'path': 'align',
        'title': '对齐方式',
        'description': '通过参数`justify`与`align`控制不同方向上的对齐方式。',
    },
    {
        'path': 'gap',
        'title': '间距',
        'description': '灵活控制子元素之间的间距。',
    },
    {
        'path': 'wrap',
        'title': '自动换行',
        'description': '控制子元素超宽后是否自动换行。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
