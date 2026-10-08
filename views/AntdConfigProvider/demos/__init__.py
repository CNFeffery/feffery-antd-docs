from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    primary_color,  # noqa: F401
    disabled,  # noqa: F401
    size,  # noqa: F401
    locale,  # noqa: F401
    algorithm,  # noqa: F401
    waves_disabled,  # noqa: F401
    use_old_theme,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdConfigProvider')
    return [
        {
            'path': 'primary_color',
            'title': t('主题色配置'),
            'description': t(
                '通过参数`primaryColor`对**AntdConfigProvider**内部元素的主题色进行快捷设置。'
            ),
        },
        {
            'path': 'disabled',
            'title': t('禁用状态配置'),
            'description': t(
                '通过参数`componentDisabled`对**AntdConfigProvider**内部相关元素的禁用状态进行快捷设置。'
            ),
        },
        {
            'path': 'size',
            'title': t('尺寸规格配置'),
            'description': t(
                '通过参数`componentSize`对**AntdConfigProvider**内部相关元素的尺寸规格进行快捷设置。'
            ),
        },
        {
            'path': 'locale',
            'title': t('国际化配置'),
            'description': t(
                '通过参数`locale`对**AntdConfigProvider**内部相关元素的国际化语种进行快捷切换。'
            ),
        },
        {
            'path': 'algorithm',
            'title': t('使用主题样式算法'),
            'description': t(
                '通过参数`algorithm`对**AntdConfigProvider**内部相关元素应用内置的主题样式算法。'
            ),
        },
        {
            'path': 'waves_disabled',
            'title': t('禁用水波纹动效'),
            'description': t(
                '设置参数`wavesDisabled=True`对**AntdConfigProvider**内部相关元素的水波纹交互动效进行禁用，典型如**AntdButton**。'
            ),
        },
        {
            'path': 'use_old_theme',
            'title': t('使用旧版主题样式'),
            'description': t(
                '通过参数`useOldTheme`对**AntdConfigProvider**内部相关元素应用内置的`fac<0.3.0`旧版本主题样式算法。'
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
