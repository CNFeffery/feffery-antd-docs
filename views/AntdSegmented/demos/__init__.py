import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    block,  # noqa: F401
    size,  # noqa: F401
    icon,  # noqa: F401
    custom_render,  # noqa: F401
    disabled,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最简单的用法。'),
    },
    {
        'path': 'block',
        'title': '撑满父级元素宽度',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('block', code=True),
                fac.AntdText('属性使其适应父元素宽度。'),
            ]
        ),
    },
    {
        'path': 'size',
        'title': '不同的尺寸规格',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('size', code=True),
                fac.AntdText('支持三种尺寸（小、默认、大）。'),
            ]
        ),
    },
    {
        'path': 'icon',
        'title': '设置图标',
        'description': fac.AntdParagraph('为选项添加前缀图标。'),
    },
    {
        'path': 'custom_render',
        'title': '自定义渲染',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('给'),
                fac.AntdText('options', code=True),
                fac.AntdText('中的'),
                fac.AntdText('label', code=True),
                fac.AntdText('传入组件型内容即可完成自定义渲染。'),
            ]
        ),
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('AntdSegmented', code=True),
                fac.AntdText('不可用。'),
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph('监听当前所选项的值。'),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
