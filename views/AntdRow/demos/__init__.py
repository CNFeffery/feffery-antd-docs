from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    responsive,  # noqa: F401
    wrap,  # noqa: F401
    align,  # noqa: F401
    flex,  # noqa: F401
    responsive_gutter,  # noqa: F401
    with_resizable,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '常规居中与行内居中。',
    },
    {
        'path': 'responsive',
        'title': '响应式布局',
        'description': '设置不同屏幕宽度断点下的列宽分配值。',
    },
    {
        'path': 'wrap',
        'title': '自动换行',
        'description': '控制子元素宽度溢出时自动换行。',
    },
    {
        'path': 'align',
        'title': '对齐方式',
        'description': '通过参数`justify`与`align`控制不同方向上的对齐方式。',
    },
    {
        'path': 'flex',
        'title': '基于flex灵活控制列宽',
        'description': '基于参数`flex`实现更灵活的列宽分配。',
    },
    {
        'path': 'responsive_gutter',
        'title': '响应式gutter',
        'description': '设置不同屏幕宽度断点下的`gutter`值。',
    },
    {
        'path': 'with_resizable',
        'title': '尺寸可调整',
        'description': '配合[fuc.FefferyResizable](https://fuc.feffery.tech/FefferyResizable)实现两侧宽度可调整。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
