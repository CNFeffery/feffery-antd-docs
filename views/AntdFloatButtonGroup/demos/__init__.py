from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    menu_mode,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdFloatButtonGroup')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的悬浮按钮组。'),
            'iframe': True,
        },
        {
            'path': 'menu_mode',
            'title': t('菜单模式'),
            'description': t(
                '设置参数`trigger`开启不同触发方式对应的菜单模式。'
            ),
            'iframe': True,
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('监听悬浮按钮组菜单模式下的展开状态。'),
            'iframe': True,
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
