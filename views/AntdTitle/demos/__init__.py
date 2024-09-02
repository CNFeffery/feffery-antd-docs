from functools import partial
from dash.dependencies import Component

from . import (
    different_title_level,  # noqa: F401
)
from components import demos_render

# 国际化
from i18n import translator


def demos_config() -> list:
    t = partial(translator.t, locale_topic='AntdTitle')
    return [
        {
            'path': 'different_title_level',
            'title': t('不同的标题级别'),
            'description': t(
                '**AntdTitle**具有**AntdText**的所有常规渲染模式，参数同样适用，这里就不再赘述，仅展示不同`level`参数下的效果。'
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
