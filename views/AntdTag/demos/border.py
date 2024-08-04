import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdTag(
                        content=f'标签{i}',
                        bordered=False,
                    )
                    for i in range(1, 6)
                ],
                wrap=True,
            ),
            fac.AntdSpace(
                [
                    fac.AntdTag(
                        content=i,
                        color=i,
                        bordered=False,
                    )
                    for i in [
                        'magenta',
                        'red',
                        'volcano',
                        'orange',
                        'gold',
                        'lime',
                        'green',
                        'cyan',
                        'blue',
                        'geekblue',
                        'purple',
                    ]
                ],
                wrap=True,
            ),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdTag(
                    content=f'标签{i}',
                    bordered=False,
                )
                for i in range(1, 6)
            ],
            wrap=True,
        ),
        fac.AntdSpace(
            [
                fac.AntdTag(
                    content=i,
                    color=i,
                    bordered=False,
                )
                for i in [
                    'magenta',
                    'red',
                    'volcano',
                    'orange',
                    'gold',
                    'lime',
                    'green',
                    'cyan',
                    'blue',
                    'geekblue',
                    'purple',
                ]
            ],
            wrap=True,
        ),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)
"""
    }
]
