from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    auto_hide_on_single_page,  # noqa: F401
    add_more_function,  # noqa: F401
    show_less_items,  # noqa: F401
    pagination_simple_mode,  # noqa: F401
    pagination_size,  # noqa: F401
    align,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdPagination')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的分页。'),
        },
        {
            'path': 'auto_hide_on_single_page',
            'title': t('单页自动隐藏'),
            'description': t(
                '设置参数`hideOnSinglePage=True`，仅有1页时自动隐藏分页组件。'
            ),
        },
        {
            'path': 'add_more_function',
            'title': t('添加更多功能'),
            'description': t(
                '设置快速跳页、每页记录数选择器、前后缀信息等功能。'
            ),
        },
        {
            'path': 'show_less_items',
            'title': t('展示较少的跳页按钮'),
            'description': t(
                '设置参数`showLessItems=True`时会展示较少的跳页按钮。'
            ),
        },
        {
            'path': 'pagination_simple_mode',
            'title': t('极简模式'),
            'description': t('设置参数`simple=True`开启极简模式。'),
        },
        {
            'path': 'pagination_size',
            'title': t('迷你模式'),
            'description': t("设置参数`size='small'`开启迷你模式。"),
        },
        {
            'path': 'align',
            'title': t('对齐方式'),
            'description': t('设置参数`align`控制分页控件对齐方式。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('可用于监听分页相关事件。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
