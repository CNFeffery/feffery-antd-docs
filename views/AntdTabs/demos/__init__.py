from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_tab_title,  # noqa: F401
    disabled_tabs,  # noqa: F401
    different_tab_position,  # noqa: F401
    sizes,  # noqa: F401
    centered,  # noqa: F401
    tab_bar_gutter,  # noqa: F401
    tab_animation,  # noqa: F401
    tab_bar_style,  # noqa: F401
    different_type,  # noqa: F401
    icon,  # noqa: F401
    extra_content,  # noqa: F401
    placeholder,  # noqa: F401
    basic_callbacks,  # noqa: F401
    tab_add_delete,  # noqa: F401
    tab_context_menu,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdTabs')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('使用参数`items`构造各标签页。'),
        },
        {
            'path': 'custom_tab_title',
            'title': t('自定义标签页标题'),
            'description': t('标签页标题内容支持自由的组件型定义。'),
        },
        {
            'path': 'disabled_tabs',
            'title': t('禁用部分标签页'),
            'description': t('对各标签页进行禁用的不同方式。'),
        },
        {
            'path': 'different_tab_position',
            'title': t('不同的标签页显示方位'),
            'description': t('设置参数`tabPosition`控制标签页显示方位。'),
        },
        {
            'path': 'sizes',
            'title': t('标签页尺寸规格'),
            'description': t('设置参数`size`控制标签页尺寸规格。'),
        },
        {
            'path': 'centered',
            'title': t('标签栏居中'),
            'description': t('设置参数`centered=True`令标签栏居中。'),
        },
        {
            'path': 'tab_bar_gutter',
            'title': t('控制标签栏间距'),
            'description': t('设置参数`tabBarGutter`控制标签栏之间的间距。'),
        },
        {
            'path': 'tab_animation',
            'title': t('控制标签页动画'),
            'description': t(
                '设置参数`inkBarAnimated`、`tabPaneAnimated`控制标签页切换动画效果。'
            ),
        },
        {
            'path': 'different_type',
            'title': t('标签页类型'),
            'description': t('设置参数`type`控制标签页类型。'),
        },
        {
            'path': 'tab_bar_style',
            'title': t('自定义标签头区域样式'),
            'description': t('设置参数`tabBarStyle`控制标签头区域整体样式。'),
        },
        {
            'path': 'icon',
            'title': t('添加图标元素'),
            'description': t('为标签页添加图标元素。'),
        },
        {
            'path': 'extra_content',
            'title': t('添加额外内容'),
            'description': t(
                '设置参数`tabBarLeftExtraContent`、`tabBarRightExtraContent`添加额外内容。'
            ),
        },
        {
            'path': 'placeholder',
            'title': t('items为空时的占位内容'),
            'description': t(
                '通过参数`placeholder`设置当`items`为空时，取而代之显示的内容。'
            ),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('属性`activeKey`对应当前激活的标签页。'),
        },
        {
            'path': 'tab_add_delete',
            'title': t('标签页增删控制'),
            'description': t('通过回调函数控制标签页的增删。'),
        },
        {
            'path': 'tab_context_menu',
            'title': t('标签页右键菜单交互'),
            'description': t('通过回调函数响应标签页标题的右键菜单交互事件。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
