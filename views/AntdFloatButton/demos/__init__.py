from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    button_types,  # noqa: F401
    button_shapes,  # noqa: F401
    button_icon,  # noqa: F401
    button_description,  # noqa: F401
    button_tooltip,  # noqa: F401
    as_link,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdFloatButton')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的悬浮按钮。'),
            'iframe': True,
        },
        {
            'path': 'button_types',
            'title': t('按钮类型'),
            'description': t('不同类型的悬浮按钮。'),
            'iframe': True,
        },
        {
            'path': 'button_shapes',
            'title': t('按钮形状'),
            'description': t('不同形状的悬浮按钮。'),
            'iframe': True,
        },
        {
            'path': 'button_icon',
            'title': t('按钮图标'),
            'description': t('为悬浮按钮自定义图标元素。'),
            'iframe': True,
        },
        {
            'path': 'button_description',
            'title': t('描述信息'),
            'description': t('为悬浮按钮添加额外描述信息。'),
            'iframe': True,
        },
        {
            'path': 'button_tooltip',
            'title': t('气泡卡片'),
            'description': t('为悬浮按钮添加额外气泡卡片信息。'),
            'iframe': True,
        },
        {
            'path': 'as_link',
            'title': t('链接跳转功能'),
            'description': t('点击悬浮按钮进行链接跳转。'),
            'iframe': True,
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('监听悬浮按钮的点击事件。'),
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
