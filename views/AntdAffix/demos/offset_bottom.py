from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        fac.AntdAffix(
            fac.AntdButton('向上滑动页面体验固钉效果', type='dashed'),
            offsetBottom=100,
            style={'float': 'right'},
        ),
        style={'marginTop': '1000px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    fac.AntdAffix(
        fac.AntdButton('向上滑动页面体验固钉效果', type='dashed'),
        offsetBottom=100,
        style={'float': 'right'},
    ),
    style={'marginTop': '1000px'},
)
"""
    }
]
