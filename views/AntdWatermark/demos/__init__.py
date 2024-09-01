from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    multiline_text,  # noqa: F401
    image_watermark,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基础的水印用法。',
    },
    {
        'path': 'multiline_text',
        'title': '多行文本水印',
        'description': '使用多行文本作为水印内容。',
    },
    {
        'path': 'image_watermark',
        'title': '图片型水印',
        'description': '使用图片作为水印内容。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
