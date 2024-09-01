from dash.dependencies import Component

from . import (
    arrow_placement,  # noqa: F401
    basic_usage,  # noqa: F401
    mask,  # noqa: F401,
    buttons,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最简单的用法。',
    },
    {
        'path': 'mask',
        'title': '设置遮罩层',
        'description': "可对遮罩层的样式进行修改，或设置为非模态引导（即无遮罩，同时为了强调引导本身，建议与`type='primary'`配合使用）。",
    },
    {
        'path': 'arrow_placement',
        'title': '设置引导弹框位置和箭头',
        'description': '可设置引导弹框相对于元素的位置，以及箭头的方向及是否指向中心。',
    },
    {
        'path': 'buttons',
        'title': '设置上一步和下一步按钮',
        'description': '可传入任意组件设置为上一步和下一步按钮的内容。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
