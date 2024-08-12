import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    circle_color,  # noqa: F401
    custom_circle_icon,  # noqa: F401
    pending,  # noqa: F401
    reverse,  # noqa: F401
    label,  # noqa: F401
    mode,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的用法。'),
    },
    {
        'path': 'circle_color',
        'title': '节点状态颜色',
        'description': fac.AntdParagraph(
            '可设置不同的节点圆圈颜色，表示各种状态。'
        ),
    },
    {
        'path': 'custom_circle_icon',
        'title': '自定义节点图标',
        'description': fac.AntdParagraph('可传入任意组件作为节点图标。'),
    },
    {
        'path': 'pending',
        'title': '末尾添加加载中节点',
        'description': fac.AntdParagraph(
            '可在时间轴末尾添加幽灵节点，表示加载中状态。'
        ),
    },
    {
        'path': 'reverse',
        'title': '翻转时间轴',
        'description': fac.AntdParagraph('可使时间轴逆序排列。'),
    },
    {
        'path': 'label',
        'title': '自定义节点标签',
        'description': fac.AntdParagraph(
            '可传入任意组件作为节点标签，显示更多信息。'
        ),
    },
    {
        'path': 'mode',
        'title': '不同的整体显示模式',
        'description': fac.AntdParagraph(
            '可设置节点标签与内容的相对位置，有内容居左、内容居右、交替显示三种模式。'
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
