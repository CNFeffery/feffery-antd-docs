import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdProgress(
                percent=80,
                gapPosition=i,
                gapDegree=j,
                type='dashboard',
                style={'width': 200},
            )
            for i, j in [
                ('top', 0),
                ('left', 60),
                ('right', 180),
                ('bottom', 295),
            ]
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=80,
            gapPosition=i,
            gapDegree=j,
            type='dashboard',
            style={'width': 200},
        )
        for i, j in [
            ('top', 0),
            ('left', 60),
            ('right', 180),
            ('bottom', 295),
        ]
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
