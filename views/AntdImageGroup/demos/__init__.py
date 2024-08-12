import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    items,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '图片组会自动识别内部元素中的所有',
                fac.AntdText('AntdImage', strong=True),
                '组件，并组合成一个图片组。',
            ]
        ),
    },
    {
        'path': 'items',
        'title': '使用items定义组内图片',
        'description': fac.AntdParagraph(
            [
                '可基于参数',
                fac.AntdText('items', code=True),
                '定义组内图片，并通过嵌套单个',
                fac.AntdText('AntdImage', strong=True),
                '作为触发相册的入口。',
            ]
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
