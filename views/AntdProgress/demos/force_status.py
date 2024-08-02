import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdProgress(
                        percent=80, status=status, style={'width': 425}
                    )
                    for status in ['normal', 'success', 'exception', 'active']
                ],
                direction='vertical',
                style={'width': '100%'},
            ),
            fac.AntdSpace(
                [
                    fac.AntdProgress(percent=80, status=status, type='circle')
                    for status in ['normal', 'success', 'exception']
                ],
                style={'width': '100%'},
            ),
            fac.AntdSpace(
                [
                    fac.AntdProgress(
                        percent=80, status=status, type='dashboard'
                    )
                    for status in ['normal', 'success', 'exception']
                ],
                style={'width': '100%'},
            ),
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
        fac.AntdSpace(
            [
                fac.AntdProgress(
                    percent=80, status=status, style={'width': 425}
                )
                for status in ['normal', 'success', 'exception', 'active']
            ],
            direction='vertical',
            style={'width': '100%'},
        ),
        fac.AntdSpace(
            [
                fac.AntdProgress(percent=80, status=status, type='circle')
                for status in ['normal', 'success', 'exception']
            ],
            style={'width': '100%'},
        ),
        fac.AntdSpace(
            [
                fac.AntdProgress(
                    percent=80, status=status, type='dashboard'
                )
                for status in ['normal', 'success', 'exception']
            ],
            style={'width': '100%'},
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
