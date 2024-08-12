import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    status_usage,  # noqa: F401
    custom_icon,  # noqa: F401
    complex_usage,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '使用参数',
                fac.AntdText('title', code=True),
                '、',
                fac.AntdText('subTitle', code=True),
                '配置基础的结果提示信息。',
            ]
        ),
    },
    {
        'path': 'status_usage',
        'title': '不同的状态类型',
        'description': fac.AntdParagraph(
            [
                '使用参数',
                fac.AntdText('status', code=True),
                '设置结果的状态类型，可用的内置状态有',
                fac.AntdText('"info"', code=True),
                '、',
                fac.AntdText('"success"', code=True),
                '、',
                fac.AntdText('"error"', code=True),
                '、',
                fac.AntdText('"warning"', code=True),
                '、',
                fac.AntdText('"404"', code=True),
                '、',
                fac.AntdText('"403"', code=True),
                '、',
                fac.AntdText('"500"', code=True),
                '、',
                fac.AntdText('"loading"', code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'custom_icon',
        'title': '自定义图标',
        'description': fac.AntdParagraph(
            [
                '使用',
                fac.AntdText('icon', code=True),
                '参数和',
                fac.AntdText('fac.AntdIcon()', code=True),
                '组件设置自定义图标。',
            ]
        ),
    },
    {
        'path': 'complex_usage',
        'title': '更复杂的使用',
        'description': fac.AntdParagraph(
            [
                '使用组件型参数如',
                fac.AntdText('title', code=True),
                '、',
                fac.AntdText('subTitle', code=True),
                '添加更丰富的操作。',
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
