import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    transition_type,  # noqa: F401
    close_icon_type,  # noqa: F401
    draggable,  # noqa: F401
    set_default_position,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('通过回调触发弹出式卡片的显示。'),
    },
    {
        'path': 'transition_type',
        'title': '显隐动画类型',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('transitionType', code=True),
                '控制弹出式卡片显隐动画的类型。',
            ]
        ),
    },
    {
        'path': 'close_icon_type',
        'title': '关闭图标类型',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('closeIconType', code=True),
                '控制弹出式卡片关闭图标的类型。',
            ]
        ),
    },
    {
        'path': 'draggable',
        'title': '可拖拽',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('draggable=True', code=True),
                '后，可通过弹出式卡片的标题区域进行拖拽。',
            ]
        ),
    },
    {
        'path': 'set_default_position',
        'title': '设置初始化位置',
        'description': fac.AntdParagraph(
            '对弹出式卡片初始化显示的位置进行自定义。'
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
