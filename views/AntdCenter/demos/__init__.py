from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    auto_style_with_config_provider,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCenter')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('常规居中与行内居中。'),
        },
        {
            'path': 'auto_style_with_config_provider',
            'title': t('样式自动联动参数配置组件'),
            'description': t(
                '设置`inheritStyleToken=True`后，背景色、字体尺寸、文字颜色默认值自动联动上层的[参数配置组件](/AntdConfigProvider)相关设定。'
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
