from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            html.Div(style={'height': '100px'}),
            fac.AntdAffix(
                fac.AntdButton('请在当前局部容器内下滑', danger=True),
                offsetTop=50,
                target='affix-container-demo',
            ),
            html.Div(style={'height': '1000px'}),
        ],
        id='affix-container-demo',
        style={
            'border': '1px solid #f0f0f0',
            'maxHeight': '300px',
            'padding': '10px',
            'overflowY': 'auto',
            'background': '#f8f9fa',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    [
        html.Div(style={'height': '100px'}),
        fac.AntdAffix(
            fac.AntdButton('请在当前局部容器内下滑', danger=True),
            offsetTop=50,
            target='affix-container-demo',
        ),
        html.Div(style={'height': '1000px'}),
    ],
    id='affix-container-demo',
    style={
        'border': '1px solid #f0f0f0',
        'maxHeight': '300px',
        'padding': '10px',
        'overflowY': 'auto',
        'background': '#f8f9fa',
    },
)
"""
    }
]
