from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdDivider('水平方向（默认）', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                html.Div(
                    style={
                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                        'height': '50px',
                        'width': '50px',
                    }
                )
            ]
            * 3
        ),
        fac.AntdDivider('竖直方向', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                html.Div(
                    style={
                        'backgroundColor': 'rgba(64, 173, 255, 1)',
                        'height': '50px',
                        'width': '50px',
                    }
                )
            ]
            * 3,
            direction='vertical',
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdDivider('水平方向（默认）', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            )
        ]
        * 3
    ),
    fac.AntdDivider('竖直方向', innerTextOrientation='left'),
    fac.AntdSpace(
        [
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '50px',
                    'width': '50px',
                }
            )
        ]
        * 3,
        direction='vertical',
    ),
]
"""
    }
]
