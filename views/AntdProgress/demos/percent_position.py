import json
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdDivider(
                        'percentPosition='
                        + json.dumps(
                            {
                                'align': align,
                                'type': _type,
                            }
                        )
                    ),
                    fac.AntdProgress(
                        percent=0,
                        size=['100%', 18],
                        percentPosition={
                            'align': align,
                            'type': _type,
                        },
                    ),
                    fac.AntdProgress(
                        percent=66.6,
                        size=['100%', 18],
                        percentPosition={
                            'align': align,
                            'type': _type,
                        },
                    ),
                    fac.AntdProgress(
                        percent=100,
                        size=['100%', 18],
                        percentPosition={
                            'align': align,
                            'type': _type,
                        },
                    ),
                ],
                direction='vertical',
                style={'width': '100%'},
            )
            for align in ['start', 'center', 'end']
            for _type in ['inner', 'outer']
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
                fac.AntdDivider(
                    'percentPosition='
                    + json.dumps(
                        {
                            'align': align,
                            'type': _type,
                        }
                    )
                ),
                fac.AntdProgress(
                    percent=0,
                    size=['100%', 18],
                    percentPosition={
                        'align': align,
                        'type': _type,
                    },
                ),
                fac.AntdProgress(
                    percent=66.6,
                    size=['100%', 18],
                    percentPosition={
                        'align': align,
                        'type': _type,
                    },
                ),
                fac.AntdProgress(
                    percent=100,
                    size=['100%', 18],
                    percentPosition={
                        'align': align,
                        'type': _type,
                    },
                ),
            ],
            direction='vertical',
            style={'width': '100%'},
        )
        for align in ['start', 'center', 'end']
        for _type in ['inner', 'outer']
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
