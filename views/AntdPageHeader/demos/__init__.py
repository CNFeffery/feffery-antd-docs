from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_children,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdPageHeader')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '最基础的页头包含了自带浏览器后退功能的返回按钮、主标题及副标题信息。'
            ),
        },
        {
            'path': 'custom_children',
            'title': t('传入子元素'),
            'description': t('自定义嵌套的子元素。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('可用于单纯监听返回按钮的点击事件。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
