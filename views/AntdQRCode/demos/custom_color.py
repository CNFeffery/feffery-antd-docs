import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdQRCode(value='https://fac.feffery.tech/', color='#52c41a'),
            fac.AntdQRCode(
                value='https://fac.feffery.tech/',
                color='#1677ff',
                bgColor='#f5f5f5',
            ),
        ]
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdQRCode(value='https://fac.feffery.tech/', color='#52c41a'),
        fac.AntdQRCode(
            value='https://fac.feffery.tech/',
            color='#1677ff',
            bgColor='#f5f5f5',
        ),
    ]
)
"""
    }
]
