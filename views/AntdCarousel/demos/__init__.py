import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    auto_play,  # noqa: F401
    auto_play_speed,  # noqa: F401
    dot_position,  # noqa: F401
    fade_effect,  # noqa: F401
    transition_speed,  # noqa: F401
    show_arrows,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('对一组平级的元素进行轮播切换。'),
    },
    {
        'path': 'auto_play',
        'title': '自动轮播',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('autoplay=True', code=True),
                '开启自动轮播。',
            ]
        ),
    },
    {
        'path': 'auto_play_speed',
        'title': '自动轮播速度',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('autoplaySpeed', code=True),
                '控制自动轮播间隔时长。',
            ]
        ),
    },
    {
        'path': 'dot_position',
        'title': '指示器位置',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('dotPosition', code=True),
                '控制走马灯指示器位置。',
            ]
        ),
    },
    {
        'path': 'fade_effect',
        'title': '渐显切换效果',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('effect="fade"', code=True),
                '启用渐显切换效果。',
            ]
        ),
    },
    {
        'path': 'transition_speed',
        'title': '动画过渡时长',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('speed', code=True),
                '控制切换动画过程毫秒耗时。',
            ]
        ),
    },
    {
        'path': 'show_arrows',
        'title': '显示切换箭头',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('arrows=True', code=True),
                '开启额外的切换用箭头。',
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
