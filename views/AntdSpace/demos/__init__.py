from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    align,  # noqa: F401
    size,  # noqa: F401
    split_line,  # noqa: F401
    custom_split_line,  # noqa: F401
    wrap,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdSpace')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '**AntdSpace**可以视作页面元素排列的快捷方式，用于解决基础的多个组件水平方向或竖直方向上单一的等间距排列需求，更复杂的网格排列布局需求请前往**AntdRow/AntdCol**进行进一步学习。'
            ),
        },
        {
            'path': 'align',
            'title': t('对齐方式'),
            'description': t('不同的子元素对齐方式。'),
        },
        {
            'path': 'size',
            'title': t('间距大小'),
            'description': t('控制子元素间的间距大小。'),
        },
        {
            'path': 'split_line',
            'title': t('添加分割线'),
            'description': t('水平排列下可在子元素之间添加分割线。'),
        },
        {
            'path': 'custom_split_line',
            'title': t('自定义分割线'),
            'description': t('分割线可设置为任意的内容。'),
        },
        {
            'path': 'wrap',
            'title': t('自动换行'),
            'description': t('控制子元素超宽后是否自动换行。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
