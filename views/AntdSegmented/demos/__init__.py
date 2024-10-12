from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    vertical,  # noqa: F401
    block,  # noqa: F401
    size,  # noqa: F401
    icon,  # noqa: F401
    only_icon,  # noqa: F401
    custom_render,  # noqa: F401
    disabled,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最简单的用法。',
    },
    {
        'path': 'vertical',
        'title': '垂直展示',
        'description': '设置参数`vertical=True`开启垂直展示模式。',
    },
    {
        'path': 'block',
        'title': '撑满父级元素宽度',
        'description': '设置参数`block=True`后分段控制器将撑满父元素宽度。',
    },
    {
        'path': 'size',
        'title': '不同的尺寸规格',
        'description': '通过参数`size`控制分段控制器的尺寸规格。',
    },
    {
        'path': 'icon',
        'title': '设置图标',
        'description': '为选项添加图标。',
    },
    {
        'path': 'only_icon',
        'title': '仅展示图标',
        'description': '仅为选项设置图标。',
    },
    {
        'path': 'custom_render',
        'title': '自定义渲染',
        'description': '选项的`label`参数可传入自定义组件。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`禁用当前分段控制器。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '监听当前所选项的值。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
