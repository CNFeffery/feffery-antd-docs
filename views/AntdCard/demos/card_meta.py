import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'AntdCardMeta基础使用', innerTextOrientation='left'
            ),
            fac.AntdCard(
                fac.AntdCardMeta(
                    avatar=fac.AntdAvatar(
                        mode='image',
                        src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                    ),
                    description='https://www.pexels.com/@mantasink/',
                    title='Mantas Sinkevičius',
                ),
                coverImg={
                    'alt': 'demo pictrue',
                    'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
                },
                hoverable=True,
                styles={'header': {'display': 'none'}},
            ),
            fac.AntdDivider(
                'AntdCardMeta可与其他组件自由组合', innerTextOrientation='left'
            ),
            fac.AntdCard(
                [
                    fac.AntdDivider('Card Meta 1'),
                    fac.AntdCardMeta(
                        avatar=fac.AntdAvatar(
                            mode='image',
                            src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                        ),
                        description='https://www.pexels.com/@mantasink/',
                        title='Mantas Sinkevičius',
                    ),
                    fac.AntdDivider('Card Meta 2'),
                    fac.AntdCardMeta(
                        avatar=fac.AntdAvatar(
                            mode='image',
                            src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                        ),
                        description='https://www.pexels.com/@mantasink/',
                        title='Mantas Sinkevičius',
                    ),
                ],
                coverImg={
                    'alt': 'demo pictrue',
                    'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
                },
                styles={
                    'body': {'flexDirection': 'column'},
                    'header': {'display': 'none'},
                },
                hoverable=True,
            ),
            fac.AntdDivider(
                '组件化使用description', innerTextOrientation='left'
            ),
            fac.AntdCard(
                fac.AntdCardMeta(
                    description=fac.AntdRow(
                        [
                            fac.AntdCol(
                                [
                                    fac.AntdText(i[0], type='secondary'),
                                    fac.AntdText(i[1]),
                                ],
                                span=6,
                                style={
                                    'display': 'flex',
                                    'flex-direction': 'column',
                                },
                            )
                            for i in [
                                ['Dimensions', '3880x5820'],
                                ['Aspect Ratio', '2:3'],
                                ['Camera', 'ILCE-6000'],
                                ['Focal', '24.0mm'],
                                ['Aperture', 'f/2.8'],
                                ['ISO', '100'],
                                ['Shutter Speed', '1/2000s'],
                                ['Taken At', 'Apr23,2023'],
                            ]
                        ],
                        gutter=[5, 10],
                    ),
                    title='Rock Formation on Sea Shore in Greece',
                ),
                coverImg={
                    'alt': 'demo pictrue',
                    'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
                },
                hoverable=True,
                styles={'header': {'display': 'none'}},
            ),
        ],
        direction='vertical',
        style={'width': 450},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('AntdCardMeta基础使用', innerTextOrientation='left'),
        fac.AntdCard(
            fac.AntdCardMeta(
                avatar=fac.AntdAvatar(
                    mode='image',
                    src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                ),
                description='https://www.pexels.com/@mantasink/',
                title='Mantas Sinkevičius',
            ),
            coverImg={
                'alt': 'demo pictrue',
                'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
            },
            hoverable=True,
            styles={'header': {'display': 'none'}},
        ),
        fac.AntdDivider(
            'AntdCardMeta可与其他组件自由组合', innerTextOrientation='left'
        ),
        fac.AntdCard(
            [
                fac.AntdDivider('Card Meta 1'),
                fac.AntdCardMeta(
                    avatar=fac.AntdAvatar(
                        mode='image',
                        src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                    ),
                    description='https://www.pexels.com/@mantasink/',
                    title='Mantas Sinkevičius',
                ),
                fac.AntdDivider('Card Meta 2'),
                fac.AntdCardMeta(
                    avatar=fac.AntdAvatar(
                        mode='image',
                        src='https://images.pexels.com/users/avatars/426868/mantas-sinkevicius-653.jpeg?auto=compress&fit=crop&h=130&w=130&dpr=1',
                    ),
                    description='https://www.pexels.com/@mantasink/',
                    title='Mantas Sinkevičius',
                ),
            ],
            coverImg={
                'alt': 'demo pictrue',
                'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
            },
            styles={
                'body': {'flexDirection': 'column'},
                'header': {'display': 'none'},
            },
            hoverable=True,
        ),
        fac.AntdDivider(
            '组件化使用description', innerTextOrientation='left'
        ),
        fac.AntdCard(
            fac.AntdCardMeta(
                description=fac.AntdRow(
                    [
                        fac.AntdCol(
                            [
                                fac.AntdText(i[0], type='secondary'),
                                fac.AntdText(i[1]),
                            ],
                            span=6,
                            style={
                                'display': 'flex',
                                'flex-direction': 'column',
                            },
                        )
                        for i in [
                            ['Dimensions', '3880x5820'],
                            ['Aspect Ratio', '2:3'],
                            ['Camera', 'ILCE-6000'],
                            ['Focal', '24.0mm'],
                            ['Aperture', 'f/2.8'],
                            ['ISO', '100'],
                            ['Shutter Speed', '1/2000s'],
                            ['Taken At', 'Apr23,2023'],
                        ]
                    ],
                    gutter=[5, 10],
                ),
                title='Rock Formation on Sea Shore in Greece',
            ),
            coverImg={
                'alt': 'demo pictrue',
                'src': 'https://images.pexels.com/photos/18664364/pexels-photo-18664364/free-photo-of-rock-formation-on-sea-shore-in-greece.jpeg',
            },
            hoverable=True,
            styles={'header': {'display': 'none'}},
        ),
    ],
    direction='vertical',
    style={'width': 450},
)
"""
    }
]
