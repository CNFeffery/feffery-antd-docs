from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdText('水平排布（默认）'),
            fac.AntdFlex(
                [
                    html.Div(
                        style={
                            'width': '25%',
                            'height': 48,
                            'background': '#1677ff'
                            if i % 2 == 0
                            else '#1677ffbf',
                        }
                    )
                    for i in range(4)
                ]
            ),
            fac.AntdText('垂直排布'),
            fac.AntdFlex(
                [
                    html.Div(
                        style={
                            'width': '25%',
                            'height': 48,
                            'background': '#1677ff'
                            if i % 2 == 0
                            else '#1677ffbf',
                        }
                    )
                    for i in range(4)
                ],
                vertical=True,
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdText('水平排布（默认）'),
        fac.AntdFlex(
            [
                html.Div(
                    style={
                        'width': '25%',
                        'height': 48,
                        'background': '#1677ff'
                        if i % 2 == 0
                        else '#1677ffbf',
                    }
                )
                for i in range(4)
            ]
        ),
        fac.AntdText('垂直排布'),
        fac.AntdFlex(
            [
                html.Div(
                    style={
                        'width': '25%',
                        'height': 48,
                        'background': '#1677ff'
                        if i % 2 == 0
                        else '#1677ffbf',
                    }
                )
                for i in range(4)
            ],
            vertical=True,
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
