from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    unit,  # noqa: F401
    title_tooltip,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCountdown')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('倒计时组件。'),
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
            'path': 'basic_callbacks',
            'title': t('基础回调'),
            'description': t('通过`finishEvent`监听倒计时结束事件。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
