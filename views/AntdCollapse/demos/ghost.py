from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        fac.AntdCollapse(
            fac.AntdParagraph('内容示例' * 20), ghost=True, title='折叠面板示例'
        ),
        style={'background': '#e7f5ff', 'width': 300},
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    fac.AntdCollapse(
        fac.AntdParagraph('内容示例' * 20), ghost=True, title='折叠面板示例'
    ),
    style={'background': '#e7f5ff', 'width': 300},
)
"""
    }
]
