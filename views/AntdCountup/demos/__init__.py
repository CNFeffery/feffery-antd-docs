from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    unit,  # noqa: F401
    title_tooltip,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '正计时组件从指定时间开始进行持续递增。',
    },
    {
        'path': 'unit',
        'title': '单位',
        'description': '通过前缀和后缀添加单位。',
    },
    {
        'path': 'title_tooltip',
        'title': '标题额外信息提示',
        'description': '通过设置参数`titleTooltip`为标题添加额外信息提示。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
