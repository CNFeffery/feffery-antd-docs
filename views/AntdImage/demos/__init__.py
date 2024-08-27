from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    preview_false,  # noqa: F401
    multi,  # noqa: F401
    fallback,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '默认情况下，可点击图片进入预览模式。',
    },
    {
        'path': 'preview_false',
        'title': '静态展示',
        'description': '设置参数`preview=False`关闭图片预览功能。',
    },
    {
        'path': 'multi',
        'title': '展示一组图片',
        'description': '参数`src`可接受一组图片资源地址实现展示一组图片，并配合参数`multiImageMode`控制显示模式。',
    },
    {
        'path': 'fallback',
        'title': '加载失败占位图',
        'description': '通过参数`fallback`控制图片加载失败时显示的占位图。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
