from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    direction,  # noqa: F401
    button_mode,  # noqa: F401
    block,  # noqa: F401
    disabled_status,  # noqa: F401
    read_only_status,  # noqa: F401
    sizes,  # noqa: F401
    fast_options,  # noqa: F401
    component_label,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最简单的单选框。',
    },
    {
        'path': 'direction',
        'title': '选项排列方向',
        'description': '设置参数`direction`控制单选框的选项排列方向。',
    },
    {
        'path': 'button_mode',
        'title': '按钮模式',
        'description': "设置参数`optionType='button'`时选项的渲染为按钮形式。",
    },
    {
        'path': 'block',
        'title': '撑满父容器',
        'description': '设置参数`block=True`后单选框整体宽度将撑满父容器。',
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
        'path': 'sizes',
        'title': '不同的尺寸规格',
        'description': "当`optionType='button'`时，设置参数`size`控制各选项按钮尺寸规格。",
    },
    {
        'path': 'fast_options',
        'title': '快捷定义options',
        'description': '当`options`每个元素的`label`和`value`值相同时，可通过传入一个包含字符串或数字的列表快速定义`options`。',
    },
    {
        'path': 'component_label',
        'title': '组件型label',
        'description': '`options`中各选项的`label`支持传入组件。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
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
