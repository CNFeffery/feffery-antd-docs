import feffery_antd_components as fac
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

demos_config = [
    {
        'path': 'primary_color',
        'title': '主题色配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('primaryColor', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部元素的主题色进行快捷设置。',
            ]
        ),
    },
    {
        'path': 'disabled',
        'title': '禁用状态配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('componentDisabled', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的禁用状态进行快捷设置。',
            ]
        ),
    },
    {
        'path': 'size',
        'title': '尺寸规格配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('componentSize', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的尺寸规格进行快捷设置。',
            ]
        ),
    },
    {
        'path': 'locale',
        'title': '国际化配置',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('locale', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的国际化语种进行快捷切换。',
            ]
        ),
    },
    {
        'path': 'algorithm',
        'title': '使用主题样式算法',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('algorithm', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素应用内置的主题样式算法。',
            ]
        ),
    },
    {
        'path': 'waves_disabled',
        'title': '禁用水波纹动效',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('wavesDisabled=True', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素的水波纹交互动效进行禁用，典型如',
                fac.AntdText('AntdButton', strong=True),
                '。',
            ]
        ),
    },
    {
        'path': 'use_old_theme',
        'title': '使用旧版主题样式',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('useOldTheme', code=True),
                '对',
                fac.AntdText('AntdConfigProvider', strong=True),
                '内部相关元素应用内置的',
                fac.AntdText('fac<0.3.0', code=True),
                '旧版本主题样式算法。',
            ]
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
