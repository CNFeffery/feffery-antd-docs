from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_addon,  # noqa: F401
    tooltips,  # noqa: F401
    _format,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '点击复制文本内容到剪贴板。',
    },
    {
        'path': 'custom_addon',
        'title': '自定义复制前后渲染内容',
        'description': '可自定义设置复制前后的渲染内容，可传入任意Dash组件。',
    },
    {
        'path': 'tooltips',
        'title': '控制提示信息',
        'description': '通过参数`tooltips`控制复制操作前后的额外提示信息行为。',
    },
    {
        'path': '_format',
        'title': '控制复制内容格式',
        'description': '通过参数`format`控制复制内容对应的`Mime Type`，你可以将不同的复制内容粘贴到**excel**中查看效果。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '配合回调复制其他组件传入的文本内容。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
