from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    use_items,  # noqa: F401
    vertical_layout,  # noqa: F401
    column,  # noqa: F401
    item_span,  # noqa: F401
    extra,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '基础的无边框、无边框描述列表。',
    },
    {
        'path': 'use_items',
        'title': '使用items定义子项',
        'description': '推荐使用参数`items`代替`children`进行子项的定义。',
    },
    {
        'path': 'vertical_layout',
        'title': '垂直布局模式',
        'description': "设置参数`layout='vertical'`开启垂直布局模式。",
    },
    {
        'path': 'column',
        'title': '控制每行宽度份数',
        'description': '通过参数`column`控制每行宽度份数。',
    },
    {
        'path': 'item_span',
        'title': '控制子项所占单位宽度',
        'description': '通过参数`span`控制子项所占单位宽度。',
    },
    {
        'path': 'extra',
        'title': '额外内容',
        'description': '通过参数`extra`添加额外内容。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
