from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    mini,  # noqa: F401
    mini_circle,  # noqa: F401
    finish_style,  # noqa: F401
    force_status,  # noqa: F401
    dashboard_gap,  # noqa: F401
    step_line,  # noqa: F401
    custom_percent_content,  # noqa: F401
    gradient_color,  # noqa: F401
    multi_step,  # noqa: F401
    remaining_color,  # noqa: F401
    percent_position,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdProgress')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('基础的进度条使用。'),
        },
        {
            'path': 'mini',
            'title': t('迷你尺寸进度条'),
            'description': t('针对**line**型进度条可设置迷你尺寸规格。'),
        },
        {
            'path': 'mini_circle',
            'title': t('迷你尺寸进度圈'),
            'description': t(
                '针对**circle**型进度条，当尺寸宽度小于`20`时将自动显示为迷你进度圈形式。'
            ),
        },
        {
            'path': 'finish_style',
            'title': t('100%状态样式'),
            'description': t('设置进度条100%状态的样式。'),
        },
        {
            'path': 'force_status',
            'title': t('强制状态类型'),
            'description': t('强制设置进度条为不同状态的样式。'),
        },
        {
            'path': 'custom_percent_content',
            'title': t('自定义百分比内容'),
            'description': t('可自定义设置进度条的百分比内容。'),
        },
        {
            'path': 'gradient_color',
            'title': t('设置渐变色'),
            'description': t('支持使用渐变色设置进度条颜色。'),
        },
        {
            'path': 'multi_step',
            'title': t('多阶段进度条'),
            'description': t('可为进度条设置多个阶段。'),
        },
        {
            'path': 'remaining_color',
            'title': t('设置未完成部分颜色'),
            'description': t('可为进度条设置未完成部分的颜色。'),
        },
        {
            'path': 'dashboard_gap',
            'title': t('设置仪表盘缺口方向和角度'),
            'description': t(
                '通过参数`gapPosition`和`gapDegree`可设置圆形仪表盘的缺口方向和缺口角度大小。'
            ),
        },
        {
            'path': 'step_line',
            'title': t('分段line型进度条'),
            'description': t(
                '可设置分段型进度条，并通过[fuc.FefferyStyle](https://fuc.feffery.tech/FefferyStyle)组件来自定义分段宽度。'
            ),
        },
        {
            'path': 'percent_position',
            'title': t('控制进度数值位置'),
            'description': t(
                '针对**line**型进度条，基于参数`percentPosition`可控制进度数值的位置。'
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
