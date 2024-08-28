from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    custom_description,  # noqa: F401
    custom_icon,  # noqa: F401
    hide_arrow,  # noqa: F401
    placement,  # noqa: F401
    custom_style,  # noqa: F401
    control_open,  # noqa: F401
    basic_callbacks,  # noqa: F401
    question_with_absolute_position,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '为子元素添加气泡确认框。',
    },
    {
        'path': 'custom_description',
        'title': '自定义描述信息',
        'description': '设置参数`description`控制描述信息内容。',
    },
    {
        'path': 'custom_icon',
        'title': '自定义图标',
        'description': '设置参数`icon`控制图标内容。',
    },
    {
        'path': 'hide_arrow',
        'title': '隐藏附带箭头',
        'description': '控制参数`arrow`隐藏气泡确认框附带的箭头。',
    },
    {
        'path': 'placement',
        'title': '悬浮层展开方向',
        'description': '控制参数`placement`设置不同的悬浮层展开方向。',
    },
    {
        'path': 'custom_style',
        'title': '自定义样式',
        'description': '控制不用部分的样式。',
    },
    {
        'path': 'control_open',
        'title': '展开状态受控',
        'description': '气泡确认框的展开状态可通过回调进行控制。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '通过回调函数监听确认、取消按钮的点击事件。',
    },
    {
        'path': 'question_with_absolute_position',
        'title': '常见问题：配合绝对定位',
        'description': '当直接将**AntdPopconfirm**施加于具有绝对定位样式的元素之上时，可能会遇到悬浮层位置显示异常的问题，推荐的稳定做法是为对应的**AntdPopconfirm**添加一层**Span**父元素，并将原先的绝对定位相关样式转而施加于此父元素之上。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
