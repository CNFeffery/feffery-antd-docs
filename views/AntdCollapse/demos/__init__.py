from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    is_open,  # noqa: F401
    non_bordered,  # noqa: F401
    size,  # noqa: F401
    ghost,  # noqa: F401
    collapsible,  # noqa: F401
    force_render,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '常规居中与行内居中。',
    },
    {
        'path': 'is_open',
        'title': '展开状态',
        'description': '设置参数`isOpen`控制展开状态。',
    },
    {
        'path': 'non_bordered',
        'title': '无边框模式',
        'description': '设置参数`bordered=False`开启无边框模式。',
    },
    {
        'path': 'size',
        'title': '不同的尺寸规格',
        'description': '设置参数`size`控制尺寸规格。',
    },
    {
        'path': 'ghost',
        'title': '透明面板模式',
        'description': '设置参数`ghost=True`开启透明面板模式。',
    },
    {
        'path': 'collapsible',
        'title': '不同的折叠触发策略',
        'description': '设置参数`collapsible`使用不同的折叠触发策略。',
    },
    {
        'path': 'force_render',
        'title': '使用forceRender参数',
        'description': '在设置参数`forceRender=True`后，即使折叠面板初始化时处于折叠状态，也会强制提前将内部元素渲染到页面中，从而便于一些初始化回调的正常赋值。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '通过回调监听面板的折叠状态。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
