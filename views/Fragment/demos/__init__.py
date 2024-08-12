import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph(
            [
                '空节点在承载包裹内部元素时，并不会像',
                fac.AntdText('html.Div', code=True),
                '等容器类组件那样在网页里渲染占用DOM节点，适合用来承载',
                fac.AntdText('dcc.Store', code=True),
                '、',
                fac.AntdText('dcc.Location', code=True),
                '、',
                fac.AntdText('AntdMessage', code=True),
                '等特殊组件，起到辅助代码逻辑组织的用处。',
            ]
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
