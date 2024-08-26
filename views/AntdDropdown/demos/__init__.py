from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    button_mode,  # noqa: F401
    custom_button_style,  # noqa: F401
    free_position_mode,  # noqa: F401
    dropdown_trigger,  # noqa: F401
    dropdown_arrow,  # noqa: F401
    dropdown_placement,  # noqa: F401
    custom_children,  # noqa: F401
    dropdown_selectable,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最基础的下拉菜单。',
    },
    {
        'path': 'button_mode',
        'title': '按钮模式',
        'description': '设置参数`buttonMode=True`后触发点显示为按钮样式。',
    },
    {
        'path': 'custom_button_style',
        'title': '自定义按钮样式',
        'description': '按钮模式时自定义按钮的样式。',
    },
    {
        'path': 'free_position_mode',
        'title': '自由位置模式',
        'description': '自由位置模式的最典型应用场景是配合`fuc.FefferyDiv`的右键事件监听功能，实现监听区域内鼠标右键触发自定义右键菜单。',
    },
    {
        'path': 'dropdown_trigger',
        'title': '点击触发方式',
        'description': "设置参数`trigger='click'`后通过点击才可触发下拉菜单。",
    },
    {
        'path': 'dropdown_arrow',
        'title': '添加箭头',
        'description': '设置参数`arrow=True`为展开的下拉菜单渲染连接箭头。',
    },
    {
        'path': 'dropdown_placement',
        'title': '不同的弹出方位',
        'description': '设置参数`placement`控制下拉菜单的展开方向。',
    },
    {
        'path': 'custom_children',
        'title': '自定义锚点元素',
        'description': '设置参数`children`自定义下拉菜单锚点元素，支持单个或多个组件。',
    },
    {
        'path': 'dropdown_selectable',
        'title': '菜单可选选择',
        'description': '设置参数`selectable=True`开启菜单选择能力，默认为单选模式，当额外设置参数`multiple=True`可以开启多选模式。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '通过`nClicks`、`clickedKey`进行下拉菜单项点击事件的监听。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
