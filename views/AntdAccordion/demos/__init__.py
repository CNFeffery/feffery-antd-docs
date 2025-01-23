from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    accordion_off,  # noqa: F401
    default_active_key,  # noqa: F401
    size,  # noqa: F401
    expand_icon_right,  # noqa: F401
    extra,  # noqa: F401
    ghost,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '默认的手风琴模式下，最多只能展开一个面板。',
    },
    {
        'path': 'accordion_off',
        'title': '关闭手风琴模式',
        'description': '设置参数`accordion=False`关闭手风琴模式。',
    },
    {
        'path': 'default_active_key',
        'title': '设置默认展开项',
        'description': '设置参数`defaultActiveKey`控制默认展开项。',
    },
    {
        'path': 'size',
        'title': '不同的尺寸规格',
        'description': '设置参数`size`控制尺寸规格。',
    },
    {
        'path': 'expand_icon_right',
        'title': '展开图标靠右',
        'description': "设置参数`expandIconPosition='right'`控制展开图标靠右。",
    },
    {
        'path': 'extra',
        'title': '子项额外内容',
        'description': '为子项设置参数`extra`添加额外内容。',
    },
    {
        'path': 'ghost',
        'title': '透明面板模式',
        'description': '设置参数`ghost=True`开启透明面板格式。',
    },
    {'path': 'basic_callbacks', 'title': '回调监听', 'description': None},
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
