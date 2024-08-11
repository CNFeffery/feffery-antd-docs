import dash
from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdQRCode(
                id='qrcode-callbacks',
                value='https://fac.feffery.tech/',
                status='expired',
            ),
            html.Div(id='qrcode-callbacks-demo-output'),
            dcc.Interval(id='qrcode-callbacks-demo-interval', interval=3000),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    [
        Output('qrcode-callbacks-demo-output', 'children'),
        Output('qrcode-callbacks', 'status'),
    ],
    Input('qrcode-callbacks', 'refreshClicks'),
    prevent_initial_call=True,
)
def qrcode_callback_demo(refreshClicks):
    if refreshClicks:
        return [f'refreshClicks: {refreshClicks}', 'active']


@app.callback(
    Output('qrcode-callbacks', 'status', allow_duplicate=True),
    Input('qrcode-callbacks-demo-interval', 'n_intervals'),
    State('qrcode-callbacks', 'status'),
    prevent_initial_call=True,
)
def qrcode_callback_demo_interval(n_intervals, status):
    if n_intervals and status == 'active':
        return 'expired'

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdQRCode(
            id='qrcode-callbacks',
            value='https://fac.feffery.tech/',
            status='expired',
        ),
        html.Div(id='qrcode-callbacks-demo-output'),
        dcc.Interval(id='qrcode-callbacks-demo-interval', interval=3000),
    ],
    direction='vertical',
)

...

@app.callback(
    [
        Output('qrcode-callbacks-demo-output', 'children'),
        Output('qrcode-callbacks', 'status'),
    ],
    Input('qrcode-callbacks', 'refreshClicks'),
    prevent_initial_call=True,
)
def qrcode_callback_demo(refreshClicks):
    if refreshClicks:
        return [f'refreshClicks: {refreshClicks}', 'active']


@app.callback(
    Output('qrcode-callbacks', 'status', allow_duplicate=True),
    Input('qrcode-callbacks-demo-interval', 'n_intervals'),
    State('qrcode-callbacks', 'status'),
    prevent_initial_call=True,
)
def qrcode_callback_demo_interval(n_intervals, status):
    if n_intervals and status == 'active':
        return 'expired'

    return dash.no_update
"""
    }
]
