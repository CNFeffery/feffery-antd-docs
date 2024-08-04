import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdFlex(
        [
            fac.AntdQRCode(value='https://fac.feffery.tech/', status='active'),
            fac.AntdQRCode(value='https://fac.feffery.tech/', status='expired'),
            fac.AntdQRCode(value='https://fac.feffery.tech/', status='loading'),
            fac.AntdQRCode(value='https://fac.feffery.tech/', status='scanned'),
        ],
        gap='middle',
        wrap='wrap'
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdFlex(
    [
        fac.AntdQRCode(value='https://fac.feffery.tech/', status='active'),
        fac.AntdQRCode(value='https://fac.feffery.tech/', status='expired'),
        fac.AntdQRCode(value='https://fac.feffery.tech/', status='loading'),
        fac.AntdQRCode(value='https://fac.feffery.tech/', status='scanned'),
    ],
    gap='middle',
    wrap='wrap'
)
"""
    }
]
