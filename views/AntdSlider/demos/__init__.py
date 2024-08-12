import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    vertical_mode,  # noqa: F401
    custom_step,  # noqa: F401
    custom_marks,  # noqa: F401
    tooltip_visible,  # noqa: F401
    tooltip_prefix_suffix,  # noqa: F401
    disabled_status,  # noqa: F401
    read_only_status,  # noqa: F401
    rail_style,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '基本滑动条。当',
                fac.AntdText('range=True', code=True),
                '时，渲染为双滑块。',
            ]
        ),
    },
    {
        'path': 'vertical_mode',
        'title': '垂直模式',
        'description': fac.AntdParagraph('垂直方向的滑动条。'),
    },
    {
        'path': 'custom_step',
        'title': '滑动步长',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('step', code=True),
                '自定义滑动步长。',
            ]
        ),
    },
    {
        'path': 'custom_marks',
        'title': '刻度标签',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('marks', code=True),
                '自定义刻度标签。',
            ]
        ),
    },
    {
        'path': 'tooltip_visible',
        'title': '滑动提示内容显示策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tooltipVisible', code=True),
                '显示或者隐藏滑动提示内容。',
            ]
        ),
    },
    {
        'path': 'tooltip_prefix_suffix',
        'title': '滑动提示内容前后缀',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('tooltipPrefix', code=True),
                '控制滑动提示内容前缀。',
                '设置参数',
                fac.AntdText('tooltipSuffix', code=True),
                '控制滑动提示内容后缀。',
            ]
        ),
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'read_only_status',
        'title': '只读状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('readOnly=True', code=True),
                '开启只读状态。',
            ]
        ),
    },
    {
        'path': 'rail_style',
        'title': '滑轨样式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('railStyle', code=True),
                '自定义滑轨样式。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('可用于监听滑动条滑动事件。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
