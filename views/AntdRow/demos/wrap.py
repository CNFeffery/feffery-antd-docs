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
                fac.AntdDivider(
                    'span之和溢出24单位时', innerTextOrientation='left'
                ),
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            fac.AntdCenter(
                                f'col{i}',
                                style={
                                    'backgroundColor': '#1677ff'
                                    if i % 2 == 0
                                    else '#1677ffbf',
                                    'color': 'white',
                                    'height': 100,
                                },
                            ),
                            span=6,
                        )
                        for i in range(1, 10)
                    ],
                    gutter=[10, 10],
                ),
                fac.AntdDivider(
                    '像素宽度之和溢出父容器100%时', innerTextOrientation='left'
                ),
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            fac.AntdCenter(
                                'width: 200',
                                style={
                                    'backgroundColor': '#1677ff'
                                    if i % 2 == 0
                                    else '#1677ffbf',
                                    'color': 'white',
                                    'height': 100,
                                    'width': 200,
                                },
                            ),
                            flex='none',
                        )
                        for i in range(1, 10)
                    ],
                    gutter=[10, 10],
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )

    elif current_locale == 'en-us':
        # construct demo contents
        demo_contents = fac.AntdSpace(
            [
                fac.AntdDivider(
                    'Sum of span larger than 24', innerTextOrientation='left'
                ),
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            fac.AntdCenter(
                                f'col{i}',
                                style={
                                    'backgroundColor': '#1677ff'
                                    if i % 2 == 0
                                    else '#1677ffbf',
                                    'color': 'white',
                                    'height': 100,
                                },
                            ),
                            span=6,
                        )
                        for i in range(1, 10)
                    ],
                    gutter=[10, 10],
                ),
                fac.AntdDivider(
                    'When the sum of the pixel width exceeds 100% of the parent container',
                    innerTextOrientation='left',
                ),
                fac.AntdRow(
                    [
                        fac.AntdCol(
                            fac.AntdCenter(
                                'width: 200',
                                style={
                                    'backgroundColor': '#1677ff'
                                    if i % 2 == 0
                                    else '#1677ffbf',
                                    'color': 'white',
                                    'height': 100,
                                    'width': 200,
                                },
                            ),
                            flex='none',
                        )
                        for i in range(1, 10)
                    ],
                    gutter=[10, 10],
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
        fac.AntdDivider(
            'span之和溢出24单位时', innerTextOrientation='left'
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdCenter(
                        f'col{i}',
                        style={
                            'backgroundColor': '#1677ff'
                            if i % 2 == 0
                            else '#1677ffbf',
                            'color': 'white',
                            'height': 100,
                        },
                    ),
                    span=6,
                )
                for i in range(1, 10)
            ],
            gutter=[10, 10],
        ),
        fac.AntdDivider(
            '像素宽度之和溢出父容器100%时', innerTextOrientation='left'
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdCenter(
                        'width: 200',
                        style={
                            'backgroundColor': '#1677ff'
                            if i % 2 == 0
                            else '#1677ffbf',
                            'color': 'white',
                            'height': 100,
                            'width': 200,
                        },
                    ),
                    flex='none',
                )
                for i in range(1, 10)
            ],
            gutter=[10, 10],
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
        fac.AntdDivider(
            'Sum of span larger than 24', innerTextOrientation='left'
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdCenter(
                        f'col{i}',
                        style={
                            'backgroundColor': '#1677ff'
                            if i % 2 == 0
                            else '#1677ffbf',
                            'color': 'white',
                            'height': 100,
                        },
                    ),
                    span=6,
                )
                for i in range(1, 10)
            ],
            gutter=[10, 10],
        ),
        fac.AntdDivider(
            'When the sum of the pixel width exceeds 100% of the parent container',
            innerTextOrientation='left',
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdCenter(
                        'width: 200',
                        style={
                            'backgroundColor': '#1677ff'
                            if i % 2 == 0
                            else '#1677ffbf',
                            'color': 'white',
                            'height': 100,
                            'width': 200,
                        },
                    ),
                    flex='none',
                )
                for i in range(1, 10)
            ],
            gutter=[10, 10],
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
            }
        ]
