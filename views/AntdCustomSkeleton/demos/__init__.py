from functools import partial
from i18n import translator
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdCustomSkeleton')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t(
                '传入参数`skeletonContent`的任何组件内容都将作为骨架屏加载动画进行渲染。'
            ),
        }
    ]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
