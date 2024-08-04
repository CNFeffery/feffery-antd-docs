import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdRate(allowClear=True, defaultValue=3),
                    fac.AntdText('allowClear：True'),
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdRate(allowClear=False, defaultValue=3),
                    fac.AntdText('allowClear：False'),
                ]
            ),
        ],
        direction='vertical',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdRate(allowClear=True, defaultValue=3),
                fac.AntdText('allowClear：True'),
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdRate(allowClear=False, defaultValue=3),
                fac.AntdText('allowClear：False'),
            ]
        ),
    ],
    direction='vertical',
)
"""
    }
]
