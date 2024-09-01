from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '空节点在承载包裹内部元素时，并不会像**html.Div**等容器类组件那样在网页里渲染占用DOM节点，适合用来承载**dcc.Store**、**dcc.Location**、**AntdMessage**等特殊组件，起到辅助代码逻辑组织的用处。',
    }
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
