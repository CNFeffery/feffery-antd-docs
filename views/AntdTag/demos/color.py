import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('使用内置色彩主题', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdTag(
                        content=i,
                        color=i,
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
            fac.AntdDivider('使用任意css颜色值', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdTag(
                        content=i,
                        color=i,
                    )
                    for i in [
                        '#8039d6',
                        '#d63987',
                        'hsl(188.51deg 85.45% 32.35%)',
                        'rgb(60, 150, 231)',
                        'rgb(198 143 22 / 100%)',
                        'rgba(231, 76, 60, 1)',
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
        fac.AntdDivider('使用内置色彩主题', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdTag(
                    content=i,
                    color=i,
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
        fac.AntdDivider('使用任意css颜色值', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdTag(
                    content=i,
                    color=i,
                )
                for i in [
                    '#8039d6',
                    '#d63987',
                    'hsl(188.51deg 85.45% 32.35%)',
                    'rgb(60, 150, 231)',
                    'rgb(198 143 22 / 100%)',
                    'rgba(231, 76, 60, 1)',
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
