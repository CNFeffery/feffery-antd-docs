import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    direction,  # noqa: F401
    button_mode,  # noqa: F401
    disabled_status,  # noqa: F401
    read_only_status,  # noqa: F401
    sizes,  # noqa: F401
    fast_options,  # noqa: F401
    component_label,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的单选框。'),
    },
    {
        'path': 'direction',
        'title': '选项排列方向',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('direction', code=True),
                '控制单选框的选项排列方向，可选的有',
                fac.AntdText("'horizontal'", code=True),
                '、',
                fac.AntdText("'vertical'", code=True),
                '，默认的为',
                fac.AntdText("'horizontal'", code=True),
            ]
        ),
    },
    {
        'path': 'button_mode',
        'title': '按钮模式',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText("optionType='button'", code=True),
                '时选项的渲染为按钮形式。',
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
        'path': 'sizes',
        'title': '不同的尺寸规格',
        'description': fac.AntdParagraph(
            [
                fac.AntdText("optionType='button'", code=True),
                '时，设置参数',
                fac.AntdText('size', code=True),
                '控制各选项按钮尺寸规格。',
            ]
        ),
    },
    {
        'path': 'fast_options',
        'title': '快捷定义options',
        'description': fac.AntdParagraph(
            [
                '当',
                fac.AntdText('options', code=True),
                '每个元素的',
                fac.AntdText('label', code=True),
                '和',
                fac.AntdText('value', code=True),
                '值相同时，可通过传入一个包含字符串或数字的列表快速定义',
                fac.AntdText('options', code=True),
                '。',
            ]
        ),
    },
    {
        'path': 'component_label',
        'title': '组件型label',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('options', code=True),
                '中元素的',
                fac.AntdText('label', code=True),
                '支持传入组件。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('可用于监听单选框选择事件。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
