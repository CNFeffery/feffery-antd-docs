from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    sizes,  # noqa: F401
    disabled,  # noqa: F401
    allow_clear,  # noqa: F401
    enable_alpha,  # noqa: F401
    different_placement,  # noqa: F401
    mode,  # noqa: F401
    show_text,  # noqa: F401
    trigger,  # noqa: F401
    presets,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '在展开的选择面板中完成颜色值的选择。',
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': '不同尺寸的颜色选择触发器。',
    },
    {
        'path': 'disabled',
        'title': '禁用状态',
        'description': '设置参数`disabled=True`开启禁用状态。',
    },
    {
        'path': 'allow_clear',
        'title': '允许清空值',
        'description': '设置参数`allowClear=True`允许用户清空已选颜色值。',
    },
    {
        'path': 'enable_alpha',
        'title': '允许选择透明度',
        'description': '设置参数`disabledAlpha=False`允许用户额外选择透明度值。',
    },
    {
        'path': 'different_placement',
        'title': '悬浮层展开方位',
        'description': '设置参数`placement`控制悬浮层展开方位。',
    },
    {
        'path': 'mode',
        'title': '颜色选择模式',
        'description': '设置参数`mode`控制颜色选择模式。',
    },
    {
        'path': 'show_text',
        'title': '显示颜色值文本',
        'description': '设置参数`showText=True`显示颜色值文本。',
    },
    {
        'path': 'trigger',
        'title': '悬浮层展开触发方式',
        'description': '设置参数`trigger`控制悬浮层展开触发方式。',
    },
    {
        'path': 'presets',
        'title': '预设颜色组',
        'description': '设置参数`presets`自定义添加预设颜色选项组。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '监听颜色值选择。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
