from functools import partial
from dash.dependencies import Component

from . import (
    different_render_mode,  # noqa: F401
    content_ellipsis,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdText')
    return [
        {
            'path': 'different_render_mode',
            'title': t('不同的渲染模式'),
            'description': t('使用不同的渲染模式展示不同样式的文字。'),
        },
        {
            'path': 'content_ellipsis',
            'title': t('内容省略功能'),
            'description': t('文字内容过长时可开启省略功能。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
