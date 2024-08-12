import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    closable,  # noqa: F401
    description,  # noqa: F401
    icon,  # noqa: F401
    top_notice,  # noqa: F401
    loop,  # noqa: F401
    marquee,  # noqa: F401
    action,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            '最简单的用法，适用于简短的警告提示。'
        ),
    },
    {
        'path': 'type',
        'title': '四种样式',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('共有四种样式'),
                fac.AntdText('success', code=True),
                fac.AntdText('、'),
                fac.AntdText('warning', code=True),
                fac.AntdText('、'),
                fac.AntdText('error', code=True),
                fac.AntdText('、'),
                fac.AntdText('info', code=True),
                fac.AntdText('。'),
            ]
        ),
    },
    {
        'path': 'closable',
        'title': '可关闭的警告提示',
        'description': fac.AntdParagraph('显示关闭按钮，点击可关闭警告提示。'),
    },
    {
        'path': 'description',
        'title': '含有辅助性文字介绍',
        'description': fac.AntdParagraph('含有辅助性文字介绍的警告提示。'),
    },
    {
        'path': 'icon',
        'title': '图标',
        'description': fac.AntdParagraph('合适的图标让信息类型更加醒目。'),
    },
    {
        'path': 'top_notice',
        'title': '顶部公告',
        'description': fac.AntdParagraph('页面顶部通告形式。'),
        'iframe': True,
    },
    {
        'path': 'loop',
        'title': '轮播模式',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('当开启轮播模式时，参数'),
                fac.AntdText('meesage', code=True),
                fac.AntdText('需要传入数组型以便进行轮播。'),
            ]
        ),
    },
    {
        'path': 'marquee',
        'title': '走马灯模式',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('当开启走马灯模式时，参数'),
                fac.AntdText('meesage', code=True),
                fac.AntdText('需要传入数组型以便进行轮播。'),
            ]
        ),
    },
    {
        'path': 'action',
        'title': '操作',
        'description': fac.AntdParagraph('可以在右上角自定义操作项。'),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('组件型'),
                fac.AntdText('meesage', code=True),
                fac.AntdText('与'),
                fac.AntdText('description', code=True),
                fac.AntdText('。'),
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
