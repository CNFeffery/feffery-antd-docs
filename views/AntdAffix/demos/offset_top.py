from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        fac.AntdAffix(
            fac.AntdButton('向下滑动页面体验固钉锚定效果', type='primary'),
            offsetTop=100,
        ),
        style={'marginBottom': '1000px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    fac.AntdAffix(
        fac.AntdButton('向下滑动页面体验固钉锚定效果', type='primary'),
        offsetTop=100,
    ),
    style={'marginBottom': '1000px'},
)
"""
    }
]
