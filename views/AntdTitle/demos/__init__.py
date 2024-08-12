import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    different_title_level,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'different_title_level',
        'title': '不同的标题级别',
        'description': fac.AntdParagraph(
            [
                fac.AntdText('AntdTitle', strong=True),
                fac.AntdText('拥有'),
                fac.AntdText('AntdText', strong=True),
                fac.AntdText(
                    '的所有常规渲染模式，参数同样适用，这里就不再赘述，仅展示不同'
                ),
                fac.AntdText('level', strong=True),
                fac.AntdText('参数下的效果'),
            ],
            style={'textIndent': '2rem'},
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
