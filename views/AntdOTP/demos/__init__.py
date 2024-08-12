import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    length,  # noqa: F401
    sizes,  # noqa: F401
    variant,  # noqa: F401
    disabled,  # noqa: F401
    status,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '英文输入法下默认接收6位数字或字母输入。'
        ),
    },
    {
        'path': 'length',
        'title': '输入框数量',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('length', code=True),
                '控制单体输入框的数量。',
            ]
        ),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('size', code=True),
                '控制尺寸规格。',
            ]
        ),
    },
    {
        'path': 'variant',
        'title': '形态变体',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('variant', code=True),
                '控制形态变体风格。',
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
                '控制是否禁用当前组件。',
            ]
        ),
    },
    {
        'path': 'status',
        'title': '强制渲染校验状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('status', code=True),
                '控制强制校验状态渲染。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('AntdOTP', strong=True),
                '的属性',
                fac.AntdText('value', code=True),
                '将在全部输入框均输入完毕的情况下触发更新。',
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
