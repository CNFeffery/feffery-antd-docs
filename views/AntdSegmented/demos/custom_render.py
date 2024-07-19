import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdSegmented(
                options=[
                    {
                        'label': html.Div(
                            [
                                fac.AntdAvatar(
                                    mode='image',
                                    src='https://api.dicebear.com/7.x/miniavs/svg?seed=8',
                                ),
                                html.Div('User 1'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'user1',
                    },
                    {
                        'label': html.Div(
                            [
                                fac.AntdAvatar(
                                    mode='text',
                                    text='K',
                                    style={
                                        'backgroundColor': '#f56a00',
                                    },
                                ),
                                html.Div('User 2'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'user2',
                    },
                    {
                        'label': html.Div(
                            [
                                fac.AntdAvatar(
                                    mode='icon',
                                    icon='antd-user',
                                    style={
                                        'backgroundColor': '#87d068',
                                    },
                                ),
                                html.Div('User 3'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'user3',
                    },
                ]
            ),
            fac.AntdSegmented(
                options=[
                    {
                        'label': html.Div(
                            [
                                html.Div('Spring'),
                                html.Div('Jan-Mar'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'spring',
                    },
                    {
                        'label': html.Div(
                            [
                                html.Div('Summer'),
                                html.Div('Apr-Jun'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'summer',
                    },
                    {
                        'label': html.Div(
                            [
                                html.Div('Autumn'),
                                html.Div('Jul-Sept'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'autumn',
                    },
                    {
                        'label': html.Div(
                            [
                                html.Div('Winter'),
                                html.Div('Oct-Dec'),
                            ],
                            style={'padding': 4},
                        ),
                        'value': 'winter',
                    },
                ]
            ),
        ],
        gap='small',
        align='flex-start',
        vertical=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdSegmented(
            options=[
                {
                    'label': html.Div(
                        [
                            fac.AntdAvatar(
                                mode='image',
                                src='https://api.dicebear.com/7.x/miniavs/svg?seed=8',
                            ),
                            html.Div('User 1'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'user1',
                },
                {
                    'label': html.Div(
                        [
                            fac.AntdAvatar(
                                mode='text',
                                text='K',
                                style={
                                    'backgroundColor': '#f56a00',
                                },
                            ),
                            html.Div('User 2'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'user2',
                },
                {
                    'label': html.Div(
                        [
                            fac.AntdAvatar(
                                mode='icon',
                                icon='antd-user',
                                style={
                                    'backgroundColor': '#87d068',
                                },
                            ),
                            html.Div('User 3'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'user3',
                },
            ]
        ),
        fac.AntdSegmented(
            options=[
                {
                    'label': html.Div(
                        [
                            html.Div('Spring'),
                            html.Div('Jan-Mar'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'spring',
                },
                {
                    'label': html.Div(
                        [
                            html.Div('Summer'),
                            html.Div('Apr-Jun'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'summer',
                },
                {
                    'label': html.Div(
                        [
                            html.Div('Autumn'),
                            html.Div('Jul-Sept'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'autumn',
                },
                {
                    'label': html.Div(
                        [
                            html.Div('Winter'),
                            html.Div('Oct-Dec'),
                        ],
                        style={'padding': 4},
                    ),
                    'value': 'winter',
                },
            ]
        ),
    ],
    gap='small',
    align='flex-start',
    vertical=True,
)
"""
    }
]
