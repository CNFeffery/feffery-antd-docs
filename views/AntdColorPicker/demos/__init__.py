import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    disabled,  # noqa: F401
    allow_clear,  # noqa: F401
    enable_alpha,  # noqa: F401
    different_placement,  # noqa: F401
    show_text,  # noqa: F401
    trigger,  # noqa: F401
    presets,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '在展开的选择面板中完成颜色值的选择。'
        ),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph('不同尺寸的颜色选择触发器。'),
    },
    {
        'path': 'disabled',
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
        'path': 'allow_clear',
        'title': '允许清空值',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('allowClear=True', code=True),
                '允许用户清空已选颜色值。',
            ]
        ),
    },
    {
        'path': 'enable_alpha',
        'title': '允许选择透明度',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabledAlpha=False', code=True),
                '允许用户额外选择透明度值。',
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
        'path': 'show_text',
        'title': '显示颜色值文本',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('showText=True', code=True),
                '显示颜色值文本。',
            ]
        ),
    },
    {
        'path': 'trigger',
        'title': '悬浮层展开触发方式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('trigger', code=True),
                '控制悬浮层展开触发方式。',
            ]
        ),
    },
    {
        'path': 'presets',
        'title': '预设颜色组',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('presets', code=True),
                '自定义添加预设颜色选项组。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('监听颜色值选择。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
