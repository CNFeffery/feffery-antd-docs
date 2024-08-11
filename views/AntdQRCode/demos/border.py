import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSpace(
                [
                    fac.AntdQRCode(value='https://fac.feffery.tech/', bordered=True),
                    fac.AntdText('bordered：True'),
                ]
            ),
            fac.AntdSpace(
                [
                    fac.AntdQRCode(value='https://fac.feffery.tech/', bordered=False),
                    fac.AntdText('bordered：False'),
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
                fac.AntdQRCode(value='https://fac.feffery.tech/', bordered=True),
                fac.AntdText('bordered：True'),
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdQRCode(value='https://fac.feffery.tech/', bordered=False),
                fac.AntdText('bordered：False'),
            ]
        ),
    ],
    direction='vertical',
)
"""
    }
]
