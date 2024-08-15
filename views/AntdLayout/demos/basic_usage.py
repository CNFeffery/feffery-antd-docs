import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdLayout(
        [
            fac.AntdHeader(
                fac.AntdTitle(
                    '页首示例', level=2, style={'color': 'white', 'margin': '0'}
                ),
                style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                },
            ),
            fac.AntdLayout(
                [
                    fac.AntdSider(
                        fac.AntdCenter(
                            fac.AntdTitle(
                                '侧边栏示例', level=2, style={'margin': '0'}
                            ),
                            style={
                                'height': '100%',
                            },
                        ),
                        style={
                            'backgroundColor': 'rgb(240, 242, 245)',
                            'display': 'flex',
                            'justifyContent': 'center',
                        },
                    ),
                    fac.AntdLayout(
                        [
                            fac.AntdContent(
                                fac.AntdCenter(
                                    fac.AntdTitle(
                                        '内容区示例',
                                        level=2,
                                        style={'margin': '0'},
                                    ),
                                    style={
                                        'height': '100%',
                                    },
                                ),
                                style={'backgroundColor': 'white'},
                            ),
                            fac.AntdFooter(
                                fac.AntdCenter(
                                    fac.AntdTitle(
                                        '页尾示例',
                                        level=2,
                                        style={'margin': '0'},
                                    ),
                                    style={
                                        'height': '100%',
                                    },
                                ),
                                style={
                                    'backgroundColor': 'rgb(193, 193, 193)',
                                    'height': '40px',
                                },
                            ),
                        ]
                    ),
                ],
                style={'height': '100%'},
            ),
        ],
        style={'height': '100vh'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdLayout(
    [
        fac.AntdHeader(
            fac.AntdTitle(
                '页首示例', level=2, style={'color': 'white', 'margin': '0'}
            ),
            style={
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center',
            },
        ),
        fac.AntdLayout(
            [
                fac.AntdSider(
                    fac.AntdCenter(
                        fac.AntdTitle(
                            '侧边栏示例', level=2, style={'margin': '0'}
                        ),
                        style={
                            'height': '100%',
                        },
                    ),
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)',
                        'display': 'flex',
                        'justifyContent': 'center',
                    },
                ),
                fac.AntdLayout(
                    [
                        fac.AntdContent(
                            fac.AntdCenter(
                                fac.AntdTitle(
                                    '内容区示例',
                                    level=2,
                                    style={'margin': '0'},
                                ),
                                style={
                                    'height': '100%',
                                },
                            ),
                            style={'backgroundColor': 'white'},
                        ),
                        fac.AntdFooter(
                            fac.AntdCenter(
                                fac.AntdTitle(
                                    '页尾示例',
                                    level=2,
                                    style={'margin': '0'},
                                ),
                                style={
                                    'height': '100%',
                                },
                            ),
                            style={
                                'backgroundColor': 'rgb(193, 193, 193)',
                                'height': '40px',
                            },
                        ),
                    ]
                ),
            ],
            style={'height': '100%'},
        ),
    ],
    style={'height': '100vh'},
)
"""
    }
]
