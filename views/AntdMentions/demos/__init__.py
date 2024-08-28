from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    auto_size,  # noqa: F401
    different_placement,  # noqa: F401
    disabled_status,  # noqa: F401
    render_status,  # noqa: F401
    trigger_keyword,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '输入子项菜单默认触发关键字`@`后可进行目标角色的选中和提及。',
    },
    {
        'path': 'auto_size',
        'title': '自适应高度',
        'description': '设置参数`autoSize`控制自适应高度。',
    },
    {
        'path': 'different_placement',
        'title': '子项菜单展开方向',
        'description': '设置参数`placement`控制子项菜单展开方向。',
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`开启禁用状态。',
    },
    {
        'path': 'render_status',
        'title': '强制状态渲染',
        'description': '设置参数`status`强制状态渲染。',
    },
    {
        'path': 'trigger_keyword',
        'title': '触发关键字',
        'description': '设置参数`prefix`自定义触发选择菜单展开的关键字。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '通过回调函数监听已输入内容、已提及目标项。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
