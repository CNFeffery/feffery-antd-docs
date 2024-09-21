from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    disabled,  # noqa: F401
    allow_clear,  # noqa: F401
    enable_alpha,  # noqa: F401
    different_placement,  # noqa: F401
    mode,  # noqa: F401
    show_text,  # noqa: F401
    trigger,  # noqa: F401
    presets,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdColorPicker')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('在展开的选择面板中完成颜色值的选择。'),
        },
        {
            'path': 'sizes',
            'title': t('尺寸规格'),
            'description': t('不同尺寸的颜色选择触发器。'),
        },
        {
            'path': 'disabled',
            'title': t('禁用状态'),
            'description': t('设置参数`disabled=True`开启禁用状态。'),
        },
        {
            'path': 'allow_clear',
            'title': t('允许清空值'),
            'description': t(
                '设置参数`allowClear=True`允许用户清空已选颜色值。'
            ),
        },
        {
            'path': 'enable_alpha',
            'title': t('允许选择透明度'),
            'description': t(
                '设置参数`disabledAlpha=False`允许用户额外选择透明度值。'
            ),
        },
        {
            'path': 'different_placement',
            'title': t('悬浮层展开方位'),
            'description': t('设置参数`placement`控制悬浮层展开方位。'),
        },
        {
            'path': 'mode',
            'title': t('颜色选择模式'),
            'description': t('设置参数`mode`控制颜色选择模式。'),
        },
        {
            'path': 'show_text',
            'title': t('显示颜色值文本'),
            'description': t('设置参数`showText=True`显示颜色值文本。'),
        },
        {
            'path': 'trigger',
            'title': t('悬浮层展开触发方式'),
            'description': t('设置参数`trigger`控制悬浮层展开触发方式。'),
        },
        {
            'path': 'presets',
            'title': t('预设颜色组'),
            'description': t('设置参数`presets`自定义添加预设颜色选项组。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('监听颜色值选择。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
