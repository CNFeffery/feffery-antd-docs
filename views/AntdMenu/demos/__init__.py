from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    mode,  # noqa: F401,  # noqa: F401
    component_as_item,  # noqa: F401
    dark_mode,  # noqa: F401
    default_expand_nodes,  # noqa: F401
    default_select_node,  # noqa: F401
    prefix_icon,  # noqa: F401
    as_link,  # noqa: F401
    builtin_collapse,  # noqa: F401
    collapse_with_sider,  # noqa: F401
    indent,  # noqa: F401
    expand_icon,  # noqa: F401
    trigger_sub_menu_action,  # noqa: F401
    basic_callbacks,  # noqa: F401
    advanced_callbacks,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdMenu')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('基础的导航菜单。'),
        },
        {
            'path': 'mode',
            'title': t('显示模式'),
            'description': t(
                '导航菜单具有三种显示模式，其中`horizontal`模式会在宽度受限时自动呈现省略状态。'
            ),
        },
        {
            'path': 'component_as_item',
            'title': t('组件型菜单项'),
            'description': t(
                '配合参数`menuItemKeyToTitle`可以将指定的菜单项标题用组件元素代替。'
            ),
        },
        {
            'path': 'dark_mode',
            'title': t('暗黑主题'),
            'description': t('内置的暗黑主题风格。'),
        },
        {
            'path': 'default_expand_nodes',
            'title': t('设置默认展开项'),
            'description': t(
                '为导航菜单设置初始化时就处于展开状态的子菜单节点。'
            ),
        },
        {
            'path': 'default_select_node',
            'title': t('设置默认选中项'),
            'description': t(
                '为导航菜单设置初始化时就处于选中状态的菜单项节点。'
            ),
        },
        {
            'path': 'prefix_icon',
            'title': t('前缀图标'),
            'description': t('为各菜单项快捷设置前缀图标。'),
        },
        {
            'path': 'as_link',
            'title': t('菜单项链接跳转'),
            'description': t('菜单项节点可设置对应的跳转链接地址。'),
        },
        {
            'path': 'builtin_collapse',
            'title': t('内置折叠状态控制'),
            'description': t('使用导航菜单内置的折叠状态控制功能。'),
        },
        {
            'path': 'collapse_with_sider',
            'title': t('配合侧边栏自定义控制折叠'),
            'description': t(
                '配合侧边栏组件**AntdSider**可实现针对导航菜单更灵活的折叠控制。'
            ),
        },
        {
            'path': 'indent',
            'title': t('调整子菜单缩进宽度'),
            'description': t('子菜单逐级缩进的像素宽度可调整。'),
        },
        {
            'path': 'expand_icon',
            'title': t('自定义子菜单展开图标'),
            'description': t(
                '设置参数`expandIcon`自定义树节点的展开/折叠图标。'
            ),
        },
        {
            'path': 'trigger_sub_menu_action',
            'title': t('控制子菜单展开触发行为'),
            'description': t(
                "设置参数`triggerSubMenuAction='click'`控制子菜单展开触发行为为“点击”。"
            ),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('通过回调监听当前选中的菜单项。'),
        },
        {
            'path': 'advanced_callbacks',
            'title': t('进阶回调监听'),
            'description': t(
                '通过回调监听参数`currentItem`、`currentKeyPath`、`currentItemPath`获取更多选中项相关信息。'
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
