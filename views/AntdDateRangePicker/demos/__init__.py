import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    time_default_value,  # noqa: F401
    different_placement,  # noqa: F401
    different_picker,  # noqa: F401
    custom_format,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    render_status,  # noqa: F401
    default_picker_value,  # noqa: F401
    disabled_dates,  # noqa: F401
    extra_footer,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '最基础的日期范围选择、日期时间范围选择。'
        ),
    },
    {
        'path': 'time_default_value',
        'title': '设置自动选定的时间值',
        'description': fac.AntdParagraph(
            [
                '由参数',
                fac.AntdText('showTime.defaultValue', code=True),
                '设定的默认值，将会在用户初次选中日期后，在时间选择面板中被自动选中。',
            ]
        ),
    },
    {
        'path': 'different_placement',
        'title': '悬浮层展开方位',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('placement', code=True),
                '控制悬浮层展开方位。',
            ]
        ),
    },
    {
        'path': 'different_picker',
        'title': '不同的日期范围选择粒度',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('picker', code=True),
                '选择不同的日期范围选择粒度。',
            ]
        ),
    },
    {
        'path': 'custom_format',
        'title': '自定义format',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('format', code=True),
                '以实现不同粒度设置下适合的已选内容回填格式化。',
            ]
        ),
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'read_only',
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
        'path': 'render_status',
        'title': '强制状态渲染',
        'description': fac.AntdParagraph(
            ['设置参数', fac.AntdText('status', code=True), '强制状态渲染。']
        ),
    },
    {
        'path': 'default_picker_value',
        'title': '初始化日期停留位置',
        'description': None,
    },
    {
        'path': 'disabled_dates',
        'title': '自定义日期禁用策略',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabledDatesStrategy', code=True),
                '控制需要禁止用户选中的日期。',
            ]
        ),
    },
    {
        'path': 'extra_footer',
        'title': '底部添加额外内容',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('extraFooter', code=True),
                '自定义选择面板底部额外的内容。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': None,
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
