from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    right_sider,  # noqa: F401
    collapsible_sider,  # noqa: F401
    responsive_collapsible_sider,  # noqa: F401
    collapsible_sider_with_menu,  # noqa: F401
    collapsible_sider_custom_trigger,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdLayout')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '经典布局方案的重点在于用**AntdLayout**包裹嵌套其他经典布局组件，从而构建出常用的各种经典页面布局方案。'
            ),
            'iframe': True,
            'query': {'padding': 'no'},
        },
        {
            'path': 'right_sider',
            'title': t('右侧侧边栏'),
            'description': t('侧边栏方位可调整。'),
            'iframe': True,
            'query': {'padding': 'no'},
        },
        {
            'path': 'collapsible_sider',
            'title': t('可折叠侧边栏'),
            'description': t(
                '为**AntdSider**设置`collapsible=True`开启自带的侧边栏折叠功能。'
            ),
            'iframe': True,
            'query': {'padding': 'no'},
        },
        {
            'path': 'responsive_collapsible_sider',
            'title': t('响应式可折叠侧边栏'),
            'description': t(
                '侧边栏可以指定屏幕宽度断点为阈值进行自动折叠及展开。'
            ),
            'iframe': True,
            'query': {'padding': 'no'},
        },
        {
            'path': 'collapsible_sider_with_menu',
            'title': t('可折叠侧边栏+导航菜单'),
            'description': t('侧边栏折叠可联动内部的导航菜单组件。'),
            'iframe': True,
            'query': {'padding': 'no'},
        },
        {
            'path': 'collapsible_sider_custom_trigger',
            'title': t('自定义折叠触发控件'),
            'description': t(
                '设置`trigger=None`后可自定义控件配合回调函数控制侧边栏折叠状态。'
            ),
            'iframe': True,
            'query': {'padding': 'no'},
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
