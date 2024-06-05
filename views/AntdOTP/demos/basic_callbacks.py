import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdOTP(id='otp-demo'),
            fac.AntdText(id='otp-demo-output'),
        ],
        direction='vertical',
        style={
            'width': '100%',
        },
    )

    return demo_contents


@app.callback(
    Output('otp-demo-output', 'children'),
    Input('otp-demo', 'value'),
    prevent_initial_call=True,
)
def show_otp_value(value):
    return f'value: {value}'


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdOTP(id='otp-demo'),
        fac.AntdText(id='otp-demo-output'),
    ],
    direction='vertical',
    style={
        'width': '100%',
    },
)

...

@app.callback(
    Output('otp-demo-output', 'children'),
    Input('otp-demo', 'value'),
    prevent_initial_call=True,
)
def show_otp_value(value):
    return f'value: {value}'
"""
    }
]
