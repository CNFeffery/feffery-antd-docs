from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    horizontal,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdAnchor')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的锚点。'),
            'iframe': True,
        },
        {
            'path': 'horizontal',
            'title': t('水平锚点'),
            'description': t(
                "设置参数`direction='horizontal'`启用水平方向锚点，注意此模式下锚点不支持嵌套。"
            ),
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
