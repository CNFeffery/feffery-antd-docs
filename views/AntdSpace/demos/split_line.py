from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
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
        addSplitLine=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
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
    addSplitLine=True,
)
"""
    }
]
