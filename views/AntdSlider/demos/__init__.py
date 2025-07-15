from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    vertical_mode,  # noqa: F401
    custom_step,  # noqa: F401
    custom_marks,  # noqa: F401
    tooltip_visible,  # noqa: F401
    tooltip_prefix_suffix,  # noqa: F401
    disabled_status,  # noqa: F401
    read_only_status,  # noqa: F401
    rail_style,  # noqa: F401
    editable,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基本滑动条。当`range=True`时，渲染为双滑块。',
    },
    {
        'path': 'vertical_mode',
        'title': '垂直模式',
        'description': '垂直方向的滑动条。',
    },
    {
        'path': 'custom_step',
        'title': '滑动步长',
        'description': '设置参数`step`自定义滑动步长。',
    },
    {
        'path': 'custom_marks',
        'title': '刻度标签',
        'description': '设置参数`marks`自定义刻度标签。',
    },
    {
        'path': 'tooltip_visible',
        'title': '滑动提示内容显示策略',
        'description': '设置参数`tooltipVisible`显示或者隐藏滑动提示内容。',
    },
    {
        'path': 'tooltip_prefix_suffix',
        'title': '滑动提示内容前后缀',
        'description': '设置参数`tooltipPrefix`控制滑动提示内容前缀。设置参数`tooltipSuffix`控制滑动提示内容后缀。',
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`开启禁用状态。',
    },
    {
        'path': 'read_only_status',
        'title': '只读状态',
        'description': '设置参数`readOnly=True`开启只读状态。',
    },
    {
        'path': 'rail_style',
        'title': '滑轨样式',
        'description': '设置参数`styles`自定义滑轨样式。',
    },
    {
        'path': 'editable',
        'title': '范围多节点可编辑',
        'description': '针对参数`range`传入字典型参数，进行范围内多节点可编辑功能的配置使用，该模式下，可通过选中节点后快速拽出或按键盘`delete`键进行删除。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '监听滑动条滑动事件。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
