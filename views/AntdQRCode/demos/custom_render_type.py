import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                id='qrcode-custom-render-type-demo-segmented',
                options=[
                    {'label': 'canvas', 'value': 'canvas'},
                    {'label': 'svg', 'value': 'svg'},
                ],
                defaultValue='canvas',
            ),
            html.Div(id='qrcode-custom-render-type-demo-output'),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('qrcode-custom-render-type-demo-output', 'children'),
    Input('qrcode-custom-render-type-demo-segmented', 'value'),
)
def qrcode_custom_render_type_demo_input_callback(input_value):
    return fac.AntdQRCode(type=input_value, value='https://fac.feffery.tech/')


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='qrcode-custom-render-type-demo-segmented',
            options=[
                {'label': 'canvas', 'value': 'canvas'},
                {'label': 'svg', 'value': 'svg'},
            ],
            defaultValue='canvas',
        ),
        html.Div(id='qrcode-custom-render-type-demo-output'),
    ],
    direction='vertical',
)

...

@app.callback(
    Output('qrcode-custom-render-type-demo-output', 'children'),
    Input('qrcode-custom-render-type-demo-segmented', 'value'),
)
def qrcode_custom_render_type_demo_input_callback(input_value):
    return fac.AntdQRCode(type=input_value, value='https://fac.feffery.tech/')
"""
    }
]
