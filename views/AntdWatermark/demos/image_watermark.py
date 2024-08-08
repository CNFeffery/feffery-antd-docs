import feffery_antd_components as fac
from dash.dependencies import Component
from dash import html


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdWatermark(
            html.Div(
                style={
                    'height': '500px',
                    'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                    'marginBottom': '25px',
                }
            ),
            image='assets/imgs/fac-logo.svg',
            width=48,
            height=48,
            rotate=0,
        )
    ]

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdWatermark(
    html.Div(
        style={
            'height': '500px',
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'marginBottom': '25px'
        }
    ),
    image='assets/imgs/fac-logo.svg',
    width=48,
    height=48,
    rotate=0
)
"""
    }
]