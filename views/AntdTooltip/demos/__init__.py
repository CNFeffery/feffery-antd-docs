from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    hide_arrow,  # noqa: F401
    placement,  # noqa: F401
    color,  # noqa: F401
    custom_style,  # noqa: F401
    control_open,  # noqa: F401
    question_with_absolute_position,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdTooltip')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('为子元素添加信息提示。'),
        },
        {
            'path': 'hide_arrow',
            'title': t('隐藏附带箭头'),
            'description': t('控制参数`arrow`隐藏信息提示附带的箭头。'),
        },
        {
            'path': 'placement',
            'title': t('悬浮层展开方向'),
            'description': t('控制参数`placement`设置不同的悬浮层展开方向。'),
        },
        {
            'path': 'color',
            'title': t('自定义背景色'),
            'description': t('控制参数`color`设置不同的背景色。'),
        },
        {
            'path': 'custom_style',
            'title': t('自定义样式'),
            'description': t('控制不用部分的样式。'),
        },
        {
            'path': 'control_open',
            'title': t('展开状态受控'),
            'description': t('信息提示的展开状态可通过回调进行控制。'),
        },
        {
            'path': 'question_with_absolute_position',
            'title': t('常见问题：配合绝对定位'),
            'description': t(
                '当直接将**AntdTooltip**施加于具有绝对定位样式的元素之上时，可能会遇到悬浮层位置显示异常的问题，推荐的稳定做法是为对应的**AntdTooltip**添加一层**Span**父元素，并将原先的绝对定位相关样式转而施加于此父元素之上。'
            ),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
