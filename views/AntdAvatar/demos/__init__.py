from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    background,  # noqa: F401
    use_with_AntdIcon,  # noqa: F401
    use_with_AntdBadge,  # noqa: F401
    sizes,  # noqa: F401
    responsive_sizes,  # noqa: F401
    square_shape,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基础的图标、文字及图片类型头像。',
    },
    {
        'path': 'background',
        'title': '背景色',
        'description': '通过设置参数`style`控制头像的背景色。',
    },
    {
        'path': 'use_with_AntdIcon',
        'title': '配合AntdIcon',
        'description': '图标型头像直接使用**AntdIcon**中内置的大量图标。',
    },
    {
        'path': 'use_with_AntdBadge',
        'title': '添加额外徽标',
        'description': '配合**AntdBadge**为头像添加额外徽标。',
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': '头像可灵活地设置尺寸规格。',
    },
    {
        'path': 'responsive_sizes',
        'title': '响应式尺寸规格',
        'description': '通过参数`size`可控制头像在不同屏幕宽度断点下的尺寸规格。',
    },
    {
        'path': 'square_shape',
        'title': '方形头像',
        'description': "设置参数`shape='square'`渲染方形头像。",
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
