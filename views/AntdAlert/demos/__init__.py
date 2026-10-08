from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    closable,  # noqa: F401
    description,  # noqa: F401
    icon,  # noqa: F401
    custom_icon,  # noqa: F401
    top_notice,  # noqa: F401
    loop,  # noqa: F401
    marquee,  # noqa: F401
    action,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdAlert')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最简单的用法，适用于简短的警告提示。'),
        },
        {
            'path': 'type',
            'title': t('四种样式'),
            'description': t(
                '共有四种样式`success`、`warning`、`error`、`info`。'
            ),
        },
        {
            'path': 'closable',
            'title': t('可关闭的警告提示'),
            'description': t('显示关闭按钮，点击可关闭警告提示。'),
        },
        {
            'path': 'description',
            'title': t('含有辅助性文字介绍'),
            'description': t('含有辅助性文字介绍的警告提示。'),
        },
        {
            'path': 'icon',
            'title': t('图标'),
            'description': t('合适的图标让信息类型更加醒目。'),
        },
        {
            'path': 'custom_icon',
            'title': t('自定义图标'),
            'description': t('通过`icon`参数自定义图标元素。'),
        },
        {
            'path': 'top_notice',
            'query': {'padding': 'no'},
            'title': t('顶部公告'),
            'description': t('页面顶部通告形式。'),
            'iframe': True,
        },
        {
            'path': 'loop',
            'title': t('轮播模式'),
            'description': t(
                '当开启轮播模式时，参数`message`需要传入数组型以便进行轮播。'
            ),
        },
        {
            'path': 'marquee',
            'title': t('走马灯模式'),
            'description': t(
                '当开启走马灯模式时，参数`message`需要传入数组型以便进行轮播。'
            ),
        },
        {
            'path': 'action',
            'title': t('操作'),
            'description': t('可以在右上角自定义操作项。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
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
