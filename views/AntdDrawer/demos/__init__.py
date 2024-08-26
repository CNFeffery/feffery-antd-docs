from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    placement,  # noqa: F401
    footer,  # noqa: F401
    extra,  # noqa: F401
    local_container,  # noqa: F401
    local_container_selector,  # noqa: F401
    loading,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '通过对应的回调触发抽屉的弹出显示。',
    },
    {
        'path': 'placement',
        'title': '抽屉弹出方位',
        'description': '通过参数`placement`控制抽屉的弹出方位。',
    },
    {
        'path': 'footer',
        'title': '设置底部内容',
        'description': '通过参数`footer`为抽屉设置固定的底部内容。',
    },
    {
        'path': 'extra',
        'title': '设置额外区内容',
        'description': '通过参数`extra`为抽屉设置额外区内容。',
    },
    {
        'path': 'local_container',
        'title': '局部容器中展示抽屉',
        'description': '配合**相对-绝对**定位，在局部容器中展示抽屉。',
    },
    {
        'path': 'local_container_selector',
        'title': '更自由地指定局部容器',
        'description': '基于参数`containerSelector`更自由地指定抽屉渲染的目标局部容器。',
    },
    {
        'path': 'loading',
        'title': '加载中状态',
        'description': '设置参数`loading=True`为抽屉内容区开启加载中状态。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
