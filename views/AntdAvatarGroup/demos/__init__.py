import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    ellipsis,  # noqa: F401
    ellipsis_trigger,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '沿水平方向错落有致的排列一组头像。',
    },
    {
        'path': 'ellipsis',
        'title': '省略显示',
        'description': '设置参数`maxCount`后，当内部头像数量超出限制时，会以省略形式展示超出部分的头像。',
    },
    {
        'path': 'ellipsis_trigger',
        'title': '点击查看省略显示',
        'description': "默认情况下，鼠标悬停于省略部分之上会触发超出部分头像的显示，在设置参数`maxPopoverTrigger='click'`后触发方式将变为点击触发。",
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
