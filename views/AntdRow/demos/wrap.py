import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

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

    return demo_contents


code_string = [
    {
        'code': """

"""
    }
]
