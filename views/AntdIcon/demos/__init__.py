from functools import partial
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    basic_callbacks,  # noqa: F401
    use_iconfont,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdIcon')
    return [
        {
            'path': 'basic_usage',
            'title': t('基础使用'),
            'description': t('通过参数`icon`来使用对应的不同类别的图标。'),
        },
        {
            'path': 'basic_callbacks',
            'title': t('回调监听'),
            'description': t(
                '通过`nClicks`进行图标点击事件的监听，特别地，在有效设置参数`debounceWait`后，将针对点击事件进行防抖监听，避免过于频繁的触发。'
            ),
        },
        {
            'path': 'use_iconfont',
            'title': t('配合iconfont图标资源'),
            'description': t(
                "设置参数`mode='iconfont'`后可使用参数`scriptUrl`引用单个或多个基于[iconfont](https://www.iconfont.cn/)项目导出的图标资源。"
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
