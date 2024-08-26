from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    simple,  # noqa: F401
    custom_image,  # noqa: F401
    image_style,  # noqa: F401
    hide_description,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '默认的空状态。',
    },
    {
        'path': 'simple',
        'title': '简洁占位图',
        'description': "设置参数`image='simple'`启用内置的简洁风格占位图。",
    },
    {
        'path': 'custom_image',
        'title': '自定义占位图',
        'description': '向参数`image`传入合法的图片地址，进行占位图的自定义。',
    },
    {
        'path': 'image_style',
        'title': '占位图样式',
        'description': '设置参数`imageStyle`控制占位图样式。',
    },
    {
        'path': 'hide_description',
        'title': '隐藏描述内容',
        'description': '设置参数`description=False`隐藏描述内容。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
