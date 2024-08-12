import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('icon', code=True),
                '来使用对应的不同类别的图标。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                '通过',
                fac.AntdText('nClicks', code=True),
                '进行图标点击事件的监听，特别地，在有效设置参数',
                fac.AntdText('debounceWait', code=True),
                '后，将针对点击事件进行防抖监听，避免过于频繁的触发。',
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
