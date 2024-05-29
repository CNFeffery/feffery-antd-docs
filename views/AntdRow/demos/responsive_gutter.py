from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdRow(
        [
            fac.AntdCol(
                html.Div(
                    style={
                        'backgroundColor': '#1677ff',
                        'height': 100,
                    }
                ),
                span=6,
            )
        ]
        * 4,
        gutter={'xs': 5, 'sm': 8, 'md': 10, 'lg': 12, 'xl': 15, 'xxl': 25},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                style={
                    'backgroundColor': '#1677ff',
                    'height': 100,
                }
            ),
            span=6,
        )
    ]
    * 4,
    gutter={'xs': 5, 'sm': 8, 'md': 10, 'lg': 12, 'xl': 15, 'xxl': 25},
)
"""
    }
]
