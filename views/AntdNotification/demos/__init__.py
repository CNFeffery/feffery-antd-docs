from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    placement,  # noqa: F401
    duration,  # noqa: F401
    show_progress,  # noqa: F401
    stack,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdNotification')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '通知提醒框的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的通知提醒框的新增。'
            ),
        },
        {
            'path': 'type',
            'title': t('通知类型'),
            'description': t('通过参数`type`控制通知提醒框的类型。'),
        },
        {
            'path': 'placement',
            'title': t('弹出位置'),
            'description': t('通过参数`placement`控制通知提醒框的弹出位置。'),
        },
        {
            'path': 'duration',
            'title': t('修改延时'),
            'description': t('通过参数`duration`控制通知提醒框的显示时长。'),
        },
        {
            'path': 'show_progress',
            'title': t('显示关闭进度条'),
            'description': t('设置参数`showProgress=True`显示关闭进度条。'),
        },
        {
            'path': 'stack',
            'title': t('堆叠模式'),
            'description': t('设置参数`stack=True`启用堆叠模式。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
