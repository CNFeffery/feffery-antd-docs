from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    status_usage,  # noqa: F401
    custom_icon,  # noqa: F401
    extra,  # noqa: F401
    complex_usage,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdResult')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '使用参数`title`、`subTitle`配置基础的结果提示信息。'
            ),
        },
        {
            'path': 'status_usage',
            'title': t('不同的状态类型'),
            'description': t('通过参数`status`显示不同的状态类型。'),
        },
        {
            'path': 'custom_icon',
            'title': t('自定义图标'),
            'description': t(
                '使用`icon`参数和**fac.AntdIcon**组件设置自定义图标。'
            ),
        },
        {
            'path': 'extra',
            'title': t('额外内容'),
            'description': t('通过参数`extra`设置额外内容。'),
        },
        {
            'path': 'complex_usage',
            'title': t('更复杂的使用'),
            'description': t(
                '使用组件型参数如`title`、`subTitle`添加更丰富的操作。'
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
