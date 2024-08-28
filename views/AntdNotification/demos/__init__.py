from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    placement,  # noqa: F401
    duration,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '通知提醒框的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的通知提醒框的新增。',
    },
    {
        'path': 'type',
        'title': '通知类型',
        'description': '通过参数`type`控制通知提醒框的类型。',
    },
    {
        'path': 'placement',
        'title': '弹出位置',
        'description': '通过参数`placement`控制通知提醒框的弹出位置。',
    },
    {
        'path': 'duration',
        'title': '修改延时',
        'description': '通过参数`duration`控制通知提醒框的显示时长。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
