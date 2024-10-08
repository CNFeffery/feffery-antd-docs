from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    exclude_mode,  # noqa: F401
    include_mode,  # noqa: F401
    custom_indicator,  # noqa: F401
    percent,  # noqa: F401
    fullscreen,  # noqa: F401
    custom_wrapper_css,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '默认情况下，加载动画会监听其内部的各个组件是否处于回调函数运算输出中状态，从而自动控制加载状态的切换。',
    },
    {
        'path': 'exclude_mode',
        'title': '排除监听模式',
        'description': "设置参数`listenPropsMode='exclude'`开启排除监听模式，该模式下加载动画将忽略监听参数`excludeProps`所定义的组件属性更新过程。",
    },
    {
        'path': 'include_mode',
        'title': '包含监听模式',
        'description': "设置参数`listenPropsMode='include'`开启包含监听模式，该模式下加载动画将只监听参数`includeProps`所定义的组件属性更新过程。",
    },
    {
        'path': 'custom_indicator',
        'title': '自定义加载动画',
        'description': '设置参数`indicator`自定义充当加载动画的元素。',
    },
    {
        'path': 'percent',
        'title': '环状进度动画',
        'description': '设置参数`percent`控制加载动画以环状进度图形式呈现。',
    },
    {
        'path': 'fullscreen',
        'title': '全屏加载动画',
        'description': '设置参数`fullscreen=True`启用全屏遮罩形式的加载动画。',
    },
    {
        'path': 'custom_wrapper_css',
        'title': '自定义包裹层css类名',
        'description': '通过参数`wrapperClassName`控制包裹层的**css**类名，来实现更丰富的样式控制，譬如此例中令高度撑满所在父容器。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
