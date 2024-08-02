import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdProgress(
                percent=80, status=status, size='small', style={'width': 425}
            )
            for status in ['normal', 'success', 'exception', 'active']
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
            status=status,
            size='small',
            style={
                'width': 425
            }
        )
        for status in [
            'normal', 'success', 'exception', 'active'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)
"""
    }
]
