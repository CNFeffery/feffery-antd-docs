from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    transition_type,  # noqa: F401
    close_icon_type,  # noqa: F401
    draggable,  # noqa: F401
    set_default_position,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdPopupCard')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('通过回调触发弹出式卡片的显示。'),
        },
        {
            'path': 'transition_type',
            'title': t('显隐动画类型'),
            'description': t(
                '通过参数`transitionType`控制弹出式卡片显隐动画的类型。'
            ),
        },
        {
            'path': 'close_icon_type',
            'title': t('关闭图标类型'),
            'description': t(
                '通过参数`closeIconType`控制弹出式卡片关闭图标的类型。'
            ),
        },
        {
            'path': 'draggable',
            'title': t('可拖拽'),
            'description': t(
                '设置参数`draggable=True`后，可通过弹出式卡片的标题区域进行拖拽。'
            ),
        },
        {
            'path': 'set_default_position',
            'title': t('设置初始化位置'),
            'description': t('对弹出式卡片初始化显示的位置进行自定义。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
