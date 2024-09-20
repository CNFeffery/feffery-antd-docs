from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    listen_style_token,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '空节点在承载包裹内部元素时，并不会像**html.Div**等容器类组件那样在网页里渲染占用DOM节点，适合用来承载**dcc.Store**、**dcc.Location**、**AntdMessage**等特殊组件，起到辅助代码逻辑组织的用处。',
    },
    {
        'path': 'listen_style_token',
        'title': '获取上层参数配置组件的样式token',
        'description': '通过回调函数监听`token`，获取来自上层中的[参数配置组件](/AntdConfigProvider)相关的样式`token`值，从而辅助控制其他任意组件的样式，推荐在浏览器端回调中使用。',
        'iframe': True,
        'query': {'padding': 'no'},
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
