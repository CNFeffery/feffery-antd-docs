from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    as_link,  # noqa: F401
    breadcrumb_icon,  # noqa: F401
    breadcrumb_hover_menu,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdBreadcrumb')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的面包屑。'),
        },
        {
            'path': 'as_link',
            'title': t('添加链接跳转功能'),
            'description': t('设置参数`href`添加链接跳转功能。'),
        },
        {
            'path': 'breadcrumb_icon',
            'title': t('添加前缀图标'),
            'description': t(
                '通过参数`icon`，可基于图标代号直接使用**AntdIcon**中的各种图标作为节点的前缀图标。'
            ),
        },
        {
            'path': 'breadcrumb_hover_menu',
            'title': t('节点添加悬浮菜单'),
            'description': t('在面包屑的节点添加悬浮菜单。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('通过`clickedItem`进行面包屑节点点击事件的监听。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
