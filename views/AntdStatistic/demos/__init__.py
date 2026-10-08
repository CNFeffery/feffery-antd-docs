from functools import partial
from i18n import translator
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


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdStatistic')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('简单的展示。'),
        },
        {
            'path': 'group_separator',
            'title': t('千分位分割符'),
            'description': t(
                '通过设置参数`showGroupSeparator`控制千分位分割符显隐。'
            ),
        },
        {
            'path': 'precision',
            'title': t('限制精度'),
            'description': t('通过设置参数`precision`控制显示精度。'),
        },
        {
            'path': 'unit',
            'title': t('单位'),
            'description': t('通过前缀和后缀添加单位。'),
        },
        {
            'path': 'title_tooltip',
            'title': t('标题额外信息提示'),
            'description': t(
                '通过设置参数`titleTooltip`为标题添加额外信息提示。'
            ),
        },
        {
            'path': 'countup',
            'title': t('动画效果'),
            'description': t(
                '给数值添加动画进入效果，需要配合**fuc**的数字递增组件。'
            ),
        },
        {
            'path': 'used_in_card',
            'title': t('在卡片中使用'),
            'description': t('在卡片中展示统计数值。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('简单演示`AntdStatistic`在回调中的使用。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
