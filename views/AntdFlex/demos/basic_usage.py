from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component

from i18n import get_current_locale


def render() -> Component:
    """渲染当前演示用例"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
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

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdText('Horizontal layout (default)'),
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
                fac.AntdText('Vertical layout'),
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


def code_string() -> list:
    """返回当前语种对应的演示代码"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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

    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpace(
    [
        fac.AntdText('Horizontal layout (default)'),
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
        fac.AntdText('Vertical layout'),
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
