from dash import dcc
import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    color,  # noqa: F401
    custom_preset_color,  # noqa: F401
    border,  # noqa: F401
    icon,  # noqa: F401
    close_icon,  # noqa: F401
    close_counts,  # noqa: F401
    add_delete_tag,  # noqa: F401
    draggable_tag,  # noqa: F401
    as_link,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '基本的标签用法，向标签的',
                fac.AntdText('content', strong=True),
                '属性传入标签内容。',
            ]
        ),
    },
    {
        'path': 'border',
        'title': '无边框标签',
        'description': fac.AntdParagraph('可设置是否渲染边框。'),
    },
    {
        'path': 'color',
        'title': '标签颜色',
        'description': fac.AntdParagraph(
            [
                '可以自定义标签颜色，可使用内置的11种色彩主题，色彩主题会配置好',
                fac.AntdText('color', code=True),
                '、',
                fac.AntdText('background-color', code=True),
                '、',
                fac.AntdText('border-color', code=True),
                '三种CSS属性。而直接传入CSS颜色值则会令文字颜色为白色，背景颜色为传入的CSS颜色。',
            ]
        ),
    },
    {
        'path': 'custom_preset_color',
        'title': '扩展预设颜色',
        'description': fac.AntdParagraph(
            '可以自行设计算法，实现近似内置色彩主题的效果。'
        ),
    },
    {
        'path': 'icon',
        'title': '标签内前缀图标',
        'description': fac.AntdParagraph(
            [
                '可设置标签内的前置图标，如需将图标设置在其他位置，仍需以组件形式传入',
                fac.AntdText('content', strong=True),
                '属性。',
            ]
        ),
    },
    {
        'path': 'close_icon',
        'title': '关闭标签按钮',
        'description': fac.AntdParagraph(
            [
                '可设置是否渲染标签内部右侧的关闭按钮。',
            ]
        ),
    },
    {
        'path': 'close_counts',
        'title': '关闭标签按钮监听回调',
        'description': fac.AntdParagraph(
            [
                '通过监听关闭标签按钮的点击数量来触发回调。',
            ]
        ),
    },
    {
        'path': 'as_link',
        'title': '充当链接使用',
        'description': fac.AntdParagraph(
            [
                '可设置',
                fac.AntdText('href', strong=True),
                '和',
                fac.AntdText('target', strong=True),
                '属性，将标签作为链接使用。',
            ]
        ),
    },
    {
        'path': 'add_delete_tag',
        'title': '动态增删标签示例',
        'description': fac.AntdParagraph(
            [
                '通过设置新增按钮和监听',
                fac.AntdText('closeCounts', strong=True),
                '回调，实现动态增删标签。配合',
                dcc.Link(
                    'fuc.FefferyAutoAnimate',
                    href='https://fuc.feffery.tech/FefferyAutoAnimate',
                    target='_blank',
                ),
                '可实现增删动画效果。',
            ]
        ),
    },
    {
        'path': 'draggable_tag',
        'title': '可拖拽标签组示例',
        'description': fac.AntdParagraph(
            [
                '配合',
                fac.AntdText('fuc.FefferySortable', strong=True),
                '组件，实现可拖拽的标签组效果。',
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
