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
                fac.AntdCenter(
                    '常规居中',
                    style={
                        'width': 300,
                        'height': 150,
                        'background': '#f0f0f0',
                    },
                ),
                fac.AntdParagraph(
                    [
                        '测试内容',
                        fac.AntdCenter(
                            '行内居中',
                            style={
                                'width': 100,
                                'height': 100,
                                'background': '#f0f0f0',
                            },
                            inline=True,
                        ),
                        '测试内容',
                    ]
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdCenter(
                    'Regular center',
                    style={
                        'width': 300,
                        'height': 150,
                        'background': '#f0f0f0',
                    },
                ),
                fac.AntdParagraph(
                    [
                        'Test content',
                        fac.AntdCenter(
                            'Inline center',
                            style={
                                'width': 100,
                                'height': 100,
                                'background': '#f0f0f0',
                            },
                            inline=True,
                        ),
                        'Test content',
                    ]
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
        fac.AntdCenter(
            '常规居中',
            style={'width': 300, 'height': 150, 'background': '#f0f0f0'},
        ),
        fac.AntdParagraph(
            [
                '测试内容',
                fac.AntdCenter(
                    '行内居中',
                    style={
                        'width': 100,
                        'height': 100,
                        'background': '#f0f0f0',
                    },
                    inline=True,
                ),
                '测试内容',
            ]
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
        fac.AntdCenter(
            'Regular center',
            style={
                'width': 300,
                'height': 150,
                'background': '#f0f0f0',
            },
        ),
        fac.AntdParagraph(
            [
                'Test content',
                fac.AntdCenter(
                    'Inline center',
                    style={
                        'width': 100,
                        'height': 100,
                        'background': '#f0f0f0',
                    },
                    inline=True,
                ),
                'Test content',
            ]
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
