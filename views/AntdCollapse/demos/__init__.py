import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    is_open,  # noqa: F401
    non_bordered,  # noqa: F401
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
        'description': fac.AntdParagraph('常规居中与行内居中。'),
    },
    {
        'path': 'is_open',
        'title': '展开状态',
        'description': fac.AntdParagraph(
            ['设置参数', fac.AntdText('isOpen', code=True), '控制展开状态。']
        ),
    },
    {
        'path': 'non_bordered',
        'title': '无边框模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('bordered=False', code=True),
                '开启无边框模式。',
            ]
        ),
    },
    {
        'path': 'ghost',
        'title': '透明面板模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('ghost=True', code=True),
                '开启透明面板模式。',
            ]
        ),
    },
    {
        'path': 'collapsible',
        'title': '不同的折叠触发策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('collapsible', code=True),
                '使用不同的折叠触发策略。',
            ]
        ),
    },
    {
        'path': 'force_render',
        'title': '使用forceRender参数',
        'description': fac.AntdParagraph(
            [
                '在设置参数',
                fac.AntdText('forceRender=True', code=True),
                '后，即使折叠面板初始化时处于折叠状态，也会强制提前将内部元素渲染到页面中，从而便于一些初始化回调的正常赋值。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('通过回调监听面板的折叠状态。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
