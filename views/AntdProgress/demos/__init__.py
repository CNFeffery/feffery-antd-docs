from dash import dcc
import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    mini,  # noqa: F401
    finish_style,  # noqa: F401
    force_status,  # noqa: F401
    dashboard_gap,  # noqa: F401
    step_line,  # noqa: F401
    custom_percent_content,  # noqa: F401
    gradient_color,  # noqa: F401
    multi_step,  # noqa: F401
    remaining_color,  # noqa: F401
    basic_callback,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('基础的进度条使用。'),
    },
    {
        'path': 'finish_style',
        'title': '100%状态样式',
        'description': fac.AntdParagraph('设置进度条100%状态的样式。'),
    },
    {
        'path': 'force_status',
        'title': '强制状态类型',
        'description': fac.AntdParagraph('强制设置进度条为不同状态的样式。'),
    },
    {
        'path': 'mini',
        'title': '迷你尺寸进度条',
        'description': fac.AntdParagraph(
            [
                '针对',
                fac.AntdText('line', strong=True),
                '型进度条可设置迷你尺寸规格。',
            ]
        ),
    },
    {
        'path': 'custom_percent_content',
        'title': '自定义百分比内容',
        'description': fac.AntdParagraph('可自定义设置进度条的百分比内容。'),
    },
    {
        'path': 'gradient_color',
        'title': '设置渐变色',
        'description': fac.AntdParagraph('支持使用渐变色设置进度条颜色。'),
    },
    {
        'path': 'multi_step',
        'title': '多阶段进度条',
        'description': fac.AntdParagraph('可为进度条设置多个阶段。'),
    },
    {
        'path': 'remaining_color',
        'title': '设置未完成部分颜色',
        'description': fac.AntdParagraph('可为进度条设置未完成部分的颜色。'),
    },
    {
        'path': 'dashboard_gap',
        'title': '设置仪表盘缺口方向和角度',
        'description': fac.AntdParagraph(
            [
                '通过',
                fac.AntdText('gapPosition', strong=True),
                '和',
                fac.AntdText('gapDegree', strong=True),
                '参数可设置圆形仪表盘的缺口方向和缺口角度大小。',
            ]
        ),
    },
    {
        'path': 'step_line',
        'title': '分段line型进度条',
        'description': fac.AntdParagraph(
            [
                '可设置分段型进度条，并通过',
                dcc.Link(
                    'fuc.FefferyStyle',
                    href='https://fuc.feffery.tech/FefferyStyle',
                    target='_blank',
                ),
                '组件来自定义分段宽度。',
            ]
        ),
    },
    # {
    #     'path': 'basic_callback',
    #     'title': '回调实时更新进度条',
    #     'description': fac.AntdParagraph(
    #         '使用浏览器端回调，在耗时任务中实时更新进度条。'
    #     ),
    # },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
