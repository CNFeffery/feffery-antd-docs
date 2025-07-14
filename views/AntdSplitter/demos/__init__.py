from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    vertical,  # noqa: F401
    default_size,  # noqa: F401
    size_limit,  # noqa: F401
    collapsible,  # noqa: F401
    nested,  # noqa: F401
    lazy,  # noqa: F401
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
        {
            'path': 'size_limit',
            'title': t('限制尺寸调整范围'),
            'description': t(
                '为子项设置允许调整的尺寸范围，支持数值像素或百分比格式。'
            ),
        },
        {
            'path': 'collapsible',
            'title': t('可折叠'),
            'description': t('控制子项区域开启快捷折叠功能。'),
        },
        {
            'path': 'nested',
            'title': t('嵌套组合'),
            'description': t('通过嵌套组合分隔面板组件，实现更复杂的布局。'),
        },
        {
            'path': 'lazy',
            'title': t('延迟渲染模式'),
            'description': t(
                '设置`lazy=True`启用延迟渲染模式，即在每次拖拽调整结束后才会更新布局。'
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
