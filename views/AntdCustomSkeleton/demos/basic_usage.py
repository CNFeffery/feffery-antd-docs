import time
from dash import html
from faker import Faker
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app

faker = Faker(locale='zh_CN')


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                '触发2秒自定义骨架屏动画',
                id='skeleton-custom-demo-input',
                type='primary',
            ),
            fac.AntdCustomSkeleton(
                id='custom-skeleton-demo',
                skeletonContent=html.Div(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    fac.AntdSkeletonButton(
                                        block=True, active=True
                                    ),
                                    span=6,
                                    style={'padding': '4px'},
                                )
                            ]
                            * 16
                        ),
                        fac.AntdSpace(
                            [
                                html.Div(
                                    fac.AntdSkeletonButton(
                                        active=True, size='small', block=True
                                    ),
                                    style={'width': '80px'},
                                ),
                                html.Div(
                                    fac.AntdSkeletonButton(
                                        active=True, size='small', block=True
                                    ),
                                    style={'width': '60px'},
                                ),
                            ],
                            style={
                                'float': 'right',
                                'paddingRight': '4px',
                                'paddingTop': '15px',
                            },
                        ),
                    ]
                ),
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('custom-skeleton-demo', 'children'),
    Input('skeleton-custom-demo-input', 'nClicks'),
)
def skeleton_custom_callback_demo(nClicks):
    time.sleep(2)

    return fac.AntdTable(
        columns=[
            {'title': '国家名示例', 'dataIndex': '国家名示例', 'width': '25%'},
            {'title': '省份名示例', 'dataIndex': '省份名示例', 'width': '25%'},
            {'title': '城市名示例', 'dataIndex': '城市名示例', 'width': '25%'},
            {'title': '日期示例', 'dataIndex': '日期示例', 'width': '25%'},
        ],
        bordered=True,
        data=[
            {
                'key': i,
                '国家名示例': faker.country(),
                '省份名示例': faker.province(),
                '城市名示例': faker.city_name(),
                '日期示例': faker.date(pattern='%Y-%m-%d', end_datetime=None),
            }
            for i in range(3)
        ],
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdButton(
            '触发2秒自定义骨架屏动画',
            id='skeleton-custom-demo-input',
            type='primary',
        ),
        fac.AntdCustomSkeleton(
            id='custom-skeleton-demo',
            skeletonContent=html.Div(
                [
                    fac.AntdRow(
                        [
                            fac.AntdCol(
                                fac.AntdSkeletonButton(
                                    block=True, active=True
                                ),
                                span=6,
                                style={'padding': '4px'},
                            )
                        ]
                        * 16
                    ),
                    fac.AntdSpace(
                        [
                            html.Div(
                                fac.AntdSkeletonButton(
                                    active=True, size='small', block=True
                                ),
                                style={'width': '80px'},
                            ),
                            html.Div(
                                fac.AntdSkeletonButton(
                                    active=True, size='small', block=True
                                ),
                                style={'width': '60px'},
                            ),
                        ],
                        style={
                            'float': 'right',
                            'paddingRight': '4px',
                            'paddingTop': '15px',
                        },
                    ),
                ]
            ),
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('custom-skeleton-demo', 'children'),
    Input('skeleton-custom-demo-input', 'nClicks'),
)
def skeleton_custom_callback_demo(nClicks):
    time.sleep(2)

    return fac.AntdTable(
        columns=[
            {'title': '国家名示例', 'dataIndex': '国家名示例', 'width': '25%'},
            {'title': '省份名示例', 'dataIndex': '省份名示例', 'width': '25%'},
            {'title': '城市名示例', 'dataIndex': '城市名示例', 'width': '25%'},
            {'title': '日期示例', 'dataIndex': '日期示例', 'width': '25%'},
        ],
        bordered=True,
        data=[
            {
                'key': i,
                '国家名示例': faker.country(),
                '省份名示例': faker.province(),
                '城市名示例': faker.city_name(),
                '日期示例': faker.date(pattern='%Y-%m-%d', end_datetime=None),
            }
            for i in range(3)
        ],
    )
"""
    }
]
