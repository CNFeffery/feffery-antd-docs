import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdDivider(
                'variant="outlined"（默认）', innerTextOrientation='left'
            ),
            fac.AntdOTP(variant='outlined'),
            fac.AntdDivider(
                'variant="borderless"', innerTextOrientation='left'
            ),
            fac.AntdOTP(variant='borderless'),
            fac.AntdDivider('variant="filled"', innerTextOrientation='left'),
            fac.AntdOTP(variant='filled'),
            fac.AntdDivider(
                'variant="underlined"', innerTextOrientation='left'
            ),
            fac.AntdOTP(variant='underlined'),
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
            'variant="outlined"（默认）', innerTextOrientation='left'
        ),
        fac.AntdOTP(variant='outlined'),
        fac.AntdDivider(
            'variant="borderless"', innerTextOrientation='left'
        ),
        fac.AntdOTP(variant='borderless'),
        fac.AntdDivider('variant="filled"', innerTextOrientation='left'),
        fac.AntdOTP(variant='filled'),
        fac.AntdDivider(
            'variant="underlined"', innerTextOrientation='left'
        ),
        fac.AntdOTP(variant='underlined'),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
