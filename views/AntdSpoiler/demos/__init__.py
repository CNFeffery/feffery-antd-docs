from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    label_position,  # noqa: F401
    transition_duration,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最简单的展开收起。',
    },
    {
        'path': 'label_position',
        'title': '展开收起按钮位置',
        'description': '通过设置参数`labelPosition`控制展开收起按钮的位置。',
    },
    {
        'path': 'transition_duration',
        'title': '动画时长',
        'description': '通过设置参数`transitionDuration`控制动画时长。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
