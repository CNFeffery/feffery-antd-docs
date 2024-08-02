import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('type="line"（默认）', innerTextOrientation='left'),
            fac.AntdProgress(percent=80, style={'width': 200}),
            fac.AntdDivider('type="circle"', innerTextOrientation='left'),
            fac.AntdProgress(percent=80, type='circle'),
            fac.AntdDivider('type="dashboard"', innerTextOrientation='left'),
            fac.AntdProgress(percent=80, type='dashboard'),
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
        fac.AntdDivider(
            'type="line"（默认）', innerTextOrientation='left'
        ),
        fac.AntdProgress(percent=80, style={'width': 200}),
        fac.AntdDivider('type="circle"', innerTextOrientation='left'),
        fac.AntdProgress(percent=80, type='circle'),
        fac.AntdDivider(
            'type="dashboard"', innerTextOrientation='left'
        ),
        fac.AntdProgress(percent=80, type='dashboard'),
    ],
    direction='vertical',
)
"""
    }
]
