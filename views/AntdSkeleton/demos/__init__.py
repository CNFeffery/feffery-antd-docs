from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    active,  # noqa: F401
    custom_widgets,  # noqa: F401
    exclude_mode,  # noqa: F401
    include_mode,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '默认情况下，骨架屏会监听其内部的各个组件是否处于回调函数运算输出中状态，从而自动控制加载状态的切换。',
    },
    {
        'path': 'active',
        'title': '动态扫屏效果',
        'description': '设置参数`active=True`为骨架屏添加动态扫屏效果。',
    },
    {
        'path': 'custom_widgets',
        'title': '调整骨架屏不同部分',
        'description': '对骨架屏中表达不同内容的部分进行灵活调整。',
    },
    {
        'path': 'exclude_mode',
        'title': '排除监听模式',
        'description': "设置参数`listenPropsMode='exclude'`开启排除监听模式，该模式下骨架屏将忽略监听参数`excludeProps`所定义的组件属性更新过程。",
    },
    {
        'path': 'include_mode',
        'title': '包含监听模式',
        'description': "设置参数`listenPropsMode='include'`开启包含监听模式，该模式下骨架屏将只监听参数`includeProps`所定义的组件属性更新过程。",
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
