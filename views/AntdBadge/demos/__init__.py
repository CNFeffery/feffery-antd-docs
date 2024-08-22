from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    color,  # noqa: F401
    just_badge,  # noqa: F401
    dynamic_number_change,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '最基础的用法是为其包裹的`children`子元素添加角标形式的徽标数，常用于配合**AntdIcon**、**AntdAvatar**等组件。',
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': "设置参数`size='small'`显示小尺寸规格的徽标数。",
    },
    {
        'path': 'color',
        'title': '颜色',
        'description': '设置参数`color`控制徽标数颜色。',
    },
    {
        'path': 'just_badge',
        'title': '独立使用徽标数',
        'description': '徽标数可不依赖其包裹的子元素，独立显示。',
    },
    {
        'path': 'dynamic_number_change',
        'title': '动态数值变化',
        'description': '通过回调函数动态修改徽标数数值时，会自动呈现动态数值变化效果。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
