import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdPopover(
        fac.AntdButton('Hover me', type='primary'),
        content=fac.AntdQRCode(
            value='https://fac.feffery.tech/', bordered=False
        ),
        overlayInnerStyle={'padding': 0},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdPopover(
    fac.AntdButton('Hover me', type='primary'),
    content=fac.AntdQRCode(
        value='https://fac.feffery.tech/', bordered=False
    ),
    overlayInnerStyle={'padding': 0},
)
"""
    }
]
