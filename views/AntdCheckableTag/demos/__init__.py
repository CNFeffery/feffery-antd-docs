from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callbacks,  # noqa: F401
    checked_unchecked_content,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCheckableTag')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('基本的使用示例。'),
        },
        {
            'path': 'checked_unchecked_content',
            'title': t('不同状态下的组件内容'),
            'description': t('可设置选中状态下和未选中状态下的组件内容。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('监听标签的选择状态。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
