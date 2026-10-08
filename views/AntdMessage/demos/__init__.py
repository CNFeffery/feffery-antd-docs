from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    type,  # noqa: F401
    duration,  # noqa: F401
    top,  # noqa: F401
    max_count,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdMessage')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '全局提示的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的全局提示的新增。'
            ),
        },
        {
            'path': 'type',
            'title': t('提示类型'),
            'description': t('通过参数`type`控制全局提示的类型。'),
        },
        {
            'path': 'duration',
            'title': t('修改延时'),
            'description': t('通过参数`duration`控制全局提示的显示时长。'),
        },
        {
            'path': 'top',
            'title': t('顶端最小距离'),
            'description': t('通过参数`top`控制全局提示的顶端最小像素距离。'),
        },
        {
            'path': 'max_count',
            'title': t('提示消息数量'),
            'description': t('通过参数`maxCount`控制同屏最大消息数。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
