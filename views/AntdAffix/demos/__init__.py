from dash.dependencies import Component

from . import (
    offset_top,  # noqa: F401
    offset_bottom,  # noqa: F401
    local_container,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'offset_top',
        'title': '下滑锚定',
        'description': '设置参数`offsetTop`用于控制下滑触发元素相对页面顶部锚定的像素距离阈值。',
    },
    {
        'path': 'offset_bottom',
        'title': '上滑锚定',
        'description': '设置参数`offsetBottom`用于控制上滑触发元素相对页面底部锚定的像素距离阈值。',
    },
    {
        'path': 'local_container',
        'title': '局部容器内锚定',
        'description': '设置参数`target`为固钉设置锚定参考的局部容器。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
