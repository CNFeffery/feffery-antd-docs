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
    different_type,  # noqa: F401
    extra_content,  # noqa: F401
    placeholder,  # noqa: F401
    basic_callbacks,  # noqa: F401
    tab_add_delete,  # noqa: F401
    tab_context_menu,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '使用参数`items`构造各标签页。',
    },
    {
        'path': 'custom_tab_title',
        'title': '自定义标签页标题',
        'description': '标签页标题内容支持自由的组件型定义。',
    },
    {
        'path': 'disabled_tabs',
        'title': '禁用部分标签页',
        'description': '对各标签页进行禁用的不同方式。',
    },
    {
        'path': 'different_tab_position',
        'title': '不同的标签页显示方位',
        'description': '设置参数`tabPosition`控制标签页显示方位。',
    },
    {
        'path': 'sizes',
        'title': '标签页尺寸规格',
        'description': '设置参数`size`控制标签页尺寸规格。',
    },
    {
        'path': 'centered',
        'title': '标签栏居中',
        'description': '设置参数`centered=True`令标签栏居中。',
    },
    {
        'path': 'tab_bar_gutter',
        'title': '控制标签栏间距',
        'description': '设置参数`tabBarGutter`控制标签栏之间的间距。',
    },
    {
        'path': 'tab_animation',
        'title': '控制标签页动画',
        'description': '设置参数`inkBarAnimated`、`tabPaneAnimated`控制标签页切换动画效果。',
    },
    {
        'path': 'different_type',
        'title': '标签页类型',
        'description': '设置参数`type`控制标签页类型。',
    },
    {
        'path': 'extra_content',
        'title': '添加额外内容',
        'description': '设置参数`tabBarLeftExtraContent`、`tabBarRightExtraContent`添加额外内容。',
    },
    {
        'path': 'placeholder',
        'title': 'items为空时的占位内容',
        'description': '通过参数`placeholder`设置当`items`为空时，取而代之显示的内容。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '属性`activeKey`对应当前激活的标签页。',
    },
    {
        'path': 'tab_add_delete',
        'title': '标签页增删控制',
        'description': '通过回调函数控制标签页的增删。',
    },
    {
        'path': 'tab_context_menu',
        'title': '标签页右键菜单交互',
        'description': '通过回调函数响应标签页标题的右键菜单交互事件。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
