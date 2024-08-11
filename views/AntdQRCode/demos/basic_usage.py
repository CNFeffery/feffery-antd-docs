import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdQRCode(
                id='basic-qrcode-demo',
            ),
            fac.AntdInput(
                id='basic-qrcode-demo-input',
                placeholder='-',
                maxLength=60,
                value='https://fac.feffery.tech/',
            ),
        ],
        direction='vertical',
        align='center',
    )

    return demo_contents


@app.callback(
    Output('basic-qrcode-demo', 'value'),
    Input('basic-qrcode-demo-input', 'value'),
)
def basic_qrcode_demo_input_callback(input_value):
    if input_value:
        return input_value
    return '-'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdQRCode(
            id='basic-qrcode-demo',
        ),
        fac.AntdInput(
            id='basic-qrcode-demo-input',
            placeholder='-',
            maxLength=60,
            value='https://fac.feffery.tech/',
        ),
    ],
    direction='vertical',
    align='center',
)

...

@app.callback(
    Output('basic-qrcode-demo', 'value'),
    Input('basic-qrcode-demo-input', 'value'),
)
def basic_qrcode_demo_input_callback(input_value):
    if input_value:
        return input_value
    return '-'
"""
    }
]
