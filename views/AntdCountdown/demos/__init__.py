import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    unit,  # noqa: F401
    title_tooltip,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('倒计时组件。'),
    },
    {
        'path': 'unit',
        'title': '单位',
        'description': fac.AntdParagraph('通过前缀和后缀添加单位。'),
    },
    {
        'path': 'title_tooltip',
        'title': '标题额外信息提示',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('通过设置参数'),
                fac.AntdText('titleTooltip', code=True),
                fac.AntdText('为标题添加额外信息提示。'),
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
