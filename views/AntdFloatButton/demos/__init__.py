import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    button_types,  # noqa: F401
    button_shapes,  # noqa: F401
    button_icon,  # noqa: F401
    button_description,  # noqa: F401
    button_tooltip,  # noqa: F401
    as_link,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的悬浮按钮。'),
        'iframe': True,
    },
    {
        'path': 'button_types',
        'title': '按钮类型',
        'description': fac.AntdParagraph('不同类型的悬浮按钮。'),
        'iframe': True,
    },
    {
        'path': 'button_shapes',
        'title': '按钮形状',
        'description': fac.AntdParagraph('不同形状的悬浮按钮。'),
        'iframe': True,
    },
    {
        'path': 'button_icon',
        'title': '按钮图标',
        'description': fac.AntdParagraph('为悬浮按钮自定义图标元素。'),
        'iframe': True,
    },
    {
        'path': 'button_description',
        'title': '描述信息',
        'description': fac.AntdParagraph('为悬浮按钮添加额外描述信息。'),
        'iframe': True,
    },
    {
        'path': 'button_tooltip',
        'title': '气泡卡片',
        'description': fac.AntdParagraph('为悬浮按钮添加额外气泡卡片信息。'),
        'iframe': True,
    },
    {
        'path': 'as_link',
        'title': '链接跳转功能',
        'description': fac.AntdParagraph('点击悬浮按钮进行链接跳转。'),
        'iframe': True,
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('监听悬浮按钮的点击事件。'),
        'iframe': True,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
