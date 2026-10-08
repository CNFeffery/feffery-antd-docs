from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    ellipsis,  # noqa: F401
    ellipsis_trigger,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdAvatarGroup')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('沿水平方向错落有致的排列一组头像。'),
        },
        {
            'path': 'ellipsis',
            'title': t('省略显示'),
            'description': t(
                '配置参数`max`后，当内部头像数量超出限制时，会以省略形式展示超出部分的头像。'
            ),
        },
        {
            'path': 'ellipsis_trigger',
            'title': t('点击查看省略显示'),
            'description': t(
                '默认情况下，鼠标悬停于省略部分之上会触发超出部分头像的显示，在配置参数`max`后触发方式将变为点击触发。'
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
