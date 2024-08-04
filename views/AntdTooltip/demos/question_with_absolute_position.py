from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = html.Div(
        [
            html.Span(
                fac.AntdTooltip(
                    fac.AntdButton('示例1', type='primary'), title='示例内容'
                ),
                style={'position': 'absolute', 'left': 15, 'bottom': 15},
            ),
            html.Span(
                fac.AntdTooltip(
                    fac.AntdButton('示例2', type='primary'), title='示例内容'
                ),
                style={'position': 'absolute', 'right': 15, 'top': 15},
            ),
            html.Span(
                fac.AntdTooltip(
                    fac.AntdButton('示例3', type='primary'), title='示例内容'
                ),
                style={'position': 'absolute', 'right': 15, 'bottom': 15},
            ),
        ],
        style={'position': 'relative', 'height': 300, 'background': '#dee2e6'},
    )

    return demo_contents


code_string = [
    {
        'code': """
html.Div(
    [
        html.Span(
            fac.AntdTooltip(
                fac.AntdButton('示例1', type='primary'), title='示例内容'
            ),
            style={'position': 'absolute', 'left': 15, 'bottom': 15},
        ),
        html.Span(
            fac.AntdTooltip(
                fac.AntdButton('示例2', type='primary'), title='示例内容'
            ),
            style={'position': 'absolute', 'right': 15, 'top': 15},
        ),
        html.Span(
            fac.AntdTooltip(
                fac.AntdButton('示例3', type='primary'), title='示例内容'
            ),
            style={'position': 'absolute', 'right': 15, 'bottom': 15},
        ),
    ],
    style={'position': 'relative', 'height': 300, 'background': '#dee2e6'},
)
"""
    }
]
