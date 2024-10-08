from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    classic_usage,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCompact')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '基于**AntdCompact**对子元素进行排列，可以实现相邻紧贴元素边框线合并效果。'
            ),
        },
        {
            'path': 'classic_usage',
            'title': t('经典用法'),
            'description': t('输入框搭配其他控件是紧凑排列经典使用场景。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
