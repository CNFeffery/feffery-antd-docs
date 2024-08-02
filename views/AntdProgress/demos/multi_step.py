import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdTooltip(
                fac.AntdProgress(percent=60, success={'percent': 30}),
                title='3 done / 3 in progress / 4 to do',
            ),
            fac.AntdTooltip(
                fac.AntdProgress(
                    percent=60, success={'percent': 30}, type='circle'
                ),
                title='3 done / 3 in progress / 4 to do',
            ),
            fac.AntdTooltip(
                fac.AntdProgress(
                    percent=60, success={'percent': 30}, type='dashboard'
                ),
                title='3 done / 3 in progress / 4 to do',
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
        fac.AntdTooltip(
            fac.AntdProgress(percent=60, success={'percent': 30}),
            title='3 done / 3 in progress / 4 to do',
        ),
        fac.AntdTooltip(
            fac.AntdProgress(
                percent=60, success={'percent': 30}, type='circle'
            ),
            title='3 done / 3 in progress / 4 to do',
        ),
        fac.AntdTooltip(
            fac.AntdProgress(
                percent=60, success={'percent': 30}, type='dashboard'
            ),
            title='3 done / 3 in progress / 4 to do',
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)
"""
    }
]
