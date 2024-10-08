from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    group_separator,  # noqa: F401
    precision,  # noqa: F401
    unit,  # noqa: F401
    title_tooltip,  # noqa: F401
    countup,  # noqa: F401
    used_in_card,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': '简单的展示。',
    },
    {
        'path': 'group_separator',
        'title': '千分位分割符',
        'description': '通过设置参数`showGroupSeparator`控制千分位分割符显隐。',
    },
    {
        'path': 'precision',
        'title': '限制精度',
        'description': '通过设置参数`precision`控制显示精度。',
    },
    {
        'path': 'unit',
        'title': '单位',
        'description': '通过前缀和后缀添加单位。',
    },
    {
        'path': 'title_tooltip',
        'title': '标题额外信息提示',
        'description': '通过设置参数`titleTooltip`为标题添加额外信息提示。',
    },
    {
        'path': 'countup',
        'title': '动画效果',
        'description': '给数值添加动画进入效果，需要配合**fuc**的数字递增组件。',
    },
    {
        'path': 'used_in_card',
        'title': '在卡片中使用',
        'description': '在卡片中展示统计数值。',
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': '简单演示`AntdStatistic`在回调中的使用。',
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
