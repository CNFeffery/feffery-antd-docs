from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    hide_now,  # noqa: F401
    different_placement,  # noqa: F401
    custom_format,  # noqa: F401
    disabled,  # noqa: F401
    read_only,  # noqa: F401
    prefix,  # noqa: F401
    suffix_icon,  # noqa: F401
    status,  # noqa: F401
    time_step,  # noqa: F401
    _12_hours,  # noqa: F401
    extra_footer,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '常规的时间选择。',
    },
    {
        'path': 'hide_now',
        'title': '隐藏此刻按钮',
        'description': '设置参数`showNow=False`对选择面板中的“此刻”按钮进行隐藏。',
    },
    {
        'path': 'different_placement',
        'title': '悬浮层展开方位',
        'description': '设置参数`placement`控制悬浮层展开方位。',
    },
    {
        'path': 'custom_format',
        'title': '自定义format',
        'description': '设置参数`format`以实现不同粒度设置下适合的已选内容回填格式化。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`开启禁用状态。',
    },
    {
        'path': 'read_only',
        'title': '只读状态',
        'description': '设置参数`readOnly=True`开启只读状态。',
    },
    {
        'path': 'prefix',
        'title': '内嵌前缀内容',
        'description': '通过参数`prefix`设置选择框内嵌前缀内容。',
    },
    {
        'path': 'suffix_icon',
        'title': '内嵌后缀图标',
        'description': '通过参数`suffixIcon`设置选择框内嵌后缀图标。',
    },
    {
        'path': 'status',
        'title': '强制状态渲染',
        'description': '设置参数`status`强制状态渲染。',
    },
    {
        'path': 'time_step',
        'title': '控制各部分时间间隔',
        'description': '设置参数`hourStep`、`minuteStep`、`secondStep`分别控制不同部分的时间间隔。',
    },
    {
        'path': '_12_hours',
        'title': '使用12小时制',
        'description': '设置参数`use12Hours=True`开启12小时制。',
    },
    {
        'path': 'extra_footer',
        'title': '底部添加额外内容',
        'description': None,
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
