import feffery_antd_components as fac
import dash
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdCompact(
                [
                    fac.AntdButton(
                        'Smaller',
                        id='qrcode-size-smaller-button',
                        icon=fac.AntdIcon(icon='antd-minus'),
                    ),
                    fac.AntdButton(
                        'Larger',
                        id='qrcode-size-larger-button',
                        icon=fac.AntdIcon(icon='antd-plus'),
                    ),
                ]
            ),
            fac.AntdQRCode(
                id='qrcode-size-demo',
                errorLevel='H',
                size=160,
                iconSize=40,
                value='https://fac.feffery.tech/',
                icon='/assets/imgs/fac-logo.svg',
            ),
        ],
        direction='vertical',
    )

    return demo_contents


@app.callback(
    [
        Output('qrcode-size-demo', 'size'),
        Output('qrcode-size-demo', 'iconSize'),
    ],
    [
        Input('qrcode-size-smaller-button', 'nClicks'),
        Input('qrcode-size-larger-button', 'nClicks'),
    ],
    State('qrcode-size-demo', 'size'),
    prevent_initial_call=True,
)
def qrcode_size_demo_input_callback(smaller_clicks, larger_clicks, size):
    triggered_id = dash.ctx.triggered_id
    if triggered_id == 'qrcode-size-smaller-button':
        new_size = size - 10
        if new_size <= 48:
            return [48, 12]
        return [new_size, new_size / 4]
    if triggered_id == 'qrcode-size-larger-button':
        new_size = size + 10
        if new_size >= 300:
            return [300, 75]
        return [new_size, new_size / 4]

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdCompact(
            [
                fac.AntdButton(
                    'Smaller',
                    id='qrcode-size-smaller-button',
                    icon=fac.AntdIcon(icon='antd-minus'),
                ),
                fac.AntdButton(
                    'Larger',
                    id='qrcode-size-larger-button',
                    icon=fac.AntdIcon(icon='antd-plus'),
                ),
            ]
        ),
        fac.AntdQRCode(
            id='qrcode-size-demo',
            errorLevel='H',
            size=160,
            iconSize=40,
            value='https://fac.feffery.tech/',
            icon='/assets/imgs/fac-logo.svg',
        ),
    ],
    direction='vertical',
)

...

@app.callback(
    [
        Output('qrcode-size-demo', 'size'),
        Output('qrcode-size-demo', 'iconSize'),
    ],
    [
        Input('qrcode-size-smaller-button', 'nClicks'),
        Input('qrcode-size-larger-button', 'nClicks'),
    ],
    State('qrcode-size-demo', 'size'),
    prevent_initial_call=True,
)
def qrcode_size_demo_input_callback(smaller_clicks, larger_clicks, size):
    triggered_id = dash.ctx.triggered_id
    if triggered_id == 'qrcode-size-smaller-button':
        new_size = size - 10
        if new_size <= 48:
            return [48, 12]
        return [new_size, new_size / 4]
    if triggered_id == 'qrcode-size-larger-button':
        new_size = size + 10
        if new_size >= 300:
            return [300, 75]
        return [new_size, new_size / 4]

    return dash.no_update
"""
    }
]
