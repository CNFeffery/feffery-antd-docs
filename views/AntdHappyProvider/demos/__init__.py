from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    other_effects,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdHappyProvider')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '快乐工作特效组件内部的所有`AntdButton`组件，在点击时会附带额外的特效。'
            ),
        },
        {
            'path': 'other_effects',
            'title': t('其他效果'),
            'description': t(
                '快乐工作特效组件内部其他类型基础组件的交互效果。'
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
