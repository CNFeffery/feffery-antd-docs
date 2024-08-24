from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '传入参数`skeletonContent`的任何组件内容都将作为骨架屏加载动画进行渲染。',
    }
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
