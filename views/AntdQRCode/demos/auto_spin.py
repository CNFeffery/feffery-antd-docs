import feffery_antd_components as fac
import dash
import time
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdQRCode(
                id='auto-spin-qrcode-demo',
                value='https://fac.feffery.tech/',
                autoSpin=True,
            ),
            fac.AntdButton(
                '重新生成', id='auto-spin-qrcode-demo-button', type='primary'
            ),
        ],
        direction='vertical',
        align='center',
    )

    return demo_contents


@app.callback(
    Output('auto-spin-qrcode-demo', 'value'),
    Input('auto-spin-qrcode-demo-button', 'nClicks'),
    State('auto-spin-qrcode-demo', 'value'),
    prevent_initial_call=True,
)
def auto_spin_qrcode_demo_input_callback(nClicks, value):
    if nClicks:
        time.sleep(1)
        if value == 'https://fac.feffery.tech/':
            return 'https://ant.design/'
        elif value == 'https://ant.design/':
            return 'https://fac.feffery.tech/'

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdQRCode(
            id='auto-spin-qrcode-demo',
            value='https://fac.feffery.tech/',
            autoSpin=True
        ),
        fac.AntdButton(
            '重新生成',
            id='auto-spin-qrcode-demo-button',
            type='primary'
        ),
    ],
    direction='vertical',
    align='center',
)

...

@app.callback(
    Output('auto-spin-qrcode-demo', 'value'),
    Input('auto-spin-qrcode-demo-button', 'nClicks'),
    State('auto-spin-qrcode-demo', 'value'),
    prevent_initial_call=True,
)
def auto_spin_qrcode_demo_input_callback(nClicks, value):
    if nClicks:
        time.sleep(1)
        if value == 'https://fac.feffery.tech/':
            return 'https://ant.design/'
        elif value == 'https://ant.design/':
            return 'https://fac.feffery.tech/'
    
    return dash.no_update
"""
    }
]
