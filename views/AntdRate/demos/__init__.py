from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    half_star,  # noqa: F401
    star_tooltips,  # noqa: F401
    read_only_status,  # noqa: F401
    clear,  # noqa: F401
    basic_callbacks,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdRate')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('最基础的评分组件。'),
        },
        {
            'path': 'half_star',
            'title': t('半星选择'),
            'description': t('设置参数`allowHalf=True`开启半星选择功能。'),
        },
        {
            'path': 'star_tooltips',
            'title': t('文案展现'),
            'description': t('设置参数`tooltips`为评分组件加上文案展示。'),
        },
        {
            'path': 'read_only_status',
            'title': t('只读状态'),
            'description': t(
                '设置参数`defaultValue`及`disabled=True`之后，即等价于只读模式，适合单纯的星级展示。'
            ),
        },
        {
            'path': 'clear',
            'title': t('清除'),
            'description': t('设置参数`allowClear`允许或者禁用清除。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t('可用于监听评分组件的选择事件。'),
        },
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
