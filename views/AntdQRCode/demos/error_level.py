import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            html.Div(id='qrcode-error-level-demo-output'),
            fac.AntdSegmented(
                id='qrcode-error-level-demo-segmented',
                options=[
                    {'label': 'L', 'value': 'L'},
                    {'label': 'M', 'value': 'M'},
                    {'label': 'Q', 'value': 'Q'},
                    {'label': 'H', 'value': 'H'},
                ],
                defaultValue='L',
            ),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('qrcode-error-level-demo-output', 'children'),
    Input('qrcode-error-level-demo-segmented', 'value'),
)
def qrcode_custom_render_type_demo_input_callback(input_value):
    return fac.AntdQRCode(
        errorLevel=input_value,
        value='https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg',
    )


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        html.Div(id='qrcode-error-level-demo-output'),
        fac.AntdSegmented(
            id='qrcode-error-level-demo-segmented',
            options=[
                {'label': 'L', 'value': 'L'},
                {'label': 'M', 'value': 'M'},
                {'label': 'Q', 'value': 'Q'},
                {'label': 'H', 'value': 'H'},
            ],
            defaultValue='L',
        ),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('qrcode-error-level-demo-output', 'children'),
    Input('qrcode-error-level-demo-segmented', 'value'),
)
def qrcode_custom_render_type_demo_input_callback(input_value):
    return fac.AntdQRCode(
        errorLevel=input_value,
        value='https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg',
    )
"""
    }
]
