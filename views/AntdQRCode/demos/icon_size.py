import feffery_antd_components as fac
import dash
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                id='qrcode-icon-size-demo-segmented',
                options=[
                    {'label': '默认', 'value': '默认'},
                    {'label': '同比例', 'value': '同比例'},
                    {'label': '自定义', 'value': '自定义'},
                ],
                defaultValue='默认',
            ),
            fac.AntdQRCode(
                id='qrcode-icon-size',
                value='https://fac.feffery.tech/',
                icon='/assets/imgs/fac-logo.svg',
            ),
        ],
        id='myqrcode',
        direction='vertical',
    )

    return demo_contents


@app.callback(
    Output('qrcode-icon-size', 'iconSize'),
    Input('qrcode-icon-size-demo-segmented', 'value'),
)
def qrcode_download_demo_input_callback(input_value):
    if input_value == '同比例':
        return 60
    elif input_value == '自定义':
        return {
            'width': 60,
            'height': 80,
        }
    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='qrcode-icon-size-demo-segmented',
            options=[
                {'label': '默认', 'value': '默认'},
                {'label': '同比例', 'value': '同比例'},
                {'label': '自定义', 'value': '自定义'},
            ],
            defaultValue='默认',
        ),
        fac.AntdQRCode(
            id='qrcode-icon-size',
            value='https://fac.feffery.tech/',
            icon='/assets/imgs/fac-logo.svg',
        ),
    ],
    id='myqrcode',
    direction='vertical',
)

...

@app.callback(
    Output('qrcode-icon-size', 'iconSize'),
    Input('qrcode-icon-size-demo-segmented', 'value'),
)
def qrcode_download_demo_input_callback(input_value):
    if input_value == '同比例':
        return 60
    elif input_value == '自定义':
        return {
            'width': 60,
            'height': 80,
        }
    return dash.no_update
"""
    }
]
