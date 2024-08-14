import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    calendar_size,  # noqa: F401
    custom_cells,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的日历。'),
    },
    {
        'path': 'calendar_size',
        'title': '不同的尺寸规格',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('size', code=True),
                '调整日历的尺寸规格。',
            ]
        ),
    },
    {
        'path': 'custom_cells',
        'title': '自定义单元格内容',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('customCells', code=True),
                '为指定模式下的指定日期单元格添加自定义内容。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('用于监听日历的点击事件。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
