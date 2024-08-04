import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider('status="warning"', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdInput(
                        mode=mode,
                        prefix=fac.AntdIcon(icon='antd-home'),
                        addonBefore=fac.AntdIcon(icon='antd-user'),
                        status='warning',
                        style={'width': 350},
                    )
                    for mode in ['default', 'search', 'text-area', 'password']
                ],
                direction='vertical',
            ),
            fac.AntdDivider('status="error"', innerTextOrientation='left'),
            fac.AntdSpace(
                [
                    fac.AntdInput(
                        mode=mode,
                        suffix=fac.AntdIcon(icon='antd-home'),
                        addonAfter=fac.AntdIcon(icon='antd-user'),
                        status='error',
                        style={'width': 350},
                    )
                    for mode in ['default', 'search', 'text-area', 'password']
                ],
                direction='vertical',
            ),
        ],
        direction='vertical',
        style={'width': '350px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdDivider('status="warning"', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdInput(
                    mode=mode,
                    prefix=fac.AntdIcon(icon='antd-home'),
                    addonBefore=fac.AntdIcon(icon='antd-user'),
                    status='warning',
                    style={'width': 350},
                )
                for mode in ['default', 'search', 'text-area', 'password']
            ],
            direction='vertical',
        ),
        fac.AntdDivider('status="error"', innerTextOrientation='left'),
        fac.AntdSpace(
            [
                fac.AntdInput(
                    mode=mode,
                    suffix=fac.AntdIcon(icon='antd-home'),
                    addonAfter=fac.AntdIcon(icon='antd-user'),
                    status='error',
                    style={'width': 350},
                )
                for mode in ['default', 'search', 'text-area', 'password']
            ],
            direction='vertical',
        ),
    ],
    direction='vertical',
    style={'width': '350px'},
)
"""
    }
]
