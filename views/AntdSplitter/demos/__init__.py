from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    vertical,  # noqa: F401
    default_size,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdSplitter')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '默认情况下，每个子项会自动均等分所在分隔面板容器。'
            ),
        },
        {
            'path': 'vertical',
            'title': t('垂直布局'),
            'description': t("设置参数`layout='vertical'`启用垂直布局。"),
        },
        {
            'path': 'default_size',
            'title': t('默认尺寸'),
            'description': t('为子项设置默认尺寸。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
