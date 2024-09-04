from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    inner_text,  # noqa: F401
    vertical,  # noqa: F401
    variant,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdDivider')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('常规水平实线、虚线分割。'),
        },
        {
            'path': 'inner_text',
            'title': t('内嵌文字'),
            'description': t('内嵌文字内容，并控制对齐方式。'),
        },
        {
            'path': 'vertical',
            'title': t('竖直分割线'),
            'description': t('用竖直分割线水平排布若干元素。'),
        },
        {
            'path': 'variant',
            'title': t('形态变体'),
            'description': t('设置参数`variant`使用不同的形态变体。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
