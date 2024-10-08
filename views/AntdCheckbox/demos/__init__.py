from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    indeterminate,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCheckbox')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': None,
        },
        {
            'path': 'indeterminate',
            'title': t('半选中状态'),
            'description': t(
                '开启半选中状态后，仅改变勾选框显示样式，与实际勾选状态无关。'
            ),
        },
        {
            'path': 'disabled',
            'title': t('禁用状态'),
            'description': None,
        },
        {
            'path': 'read_only',
            'title': t('只读状态'),
            'description': t('只读状态适用于单纯的数据展示场景。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': None,
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
