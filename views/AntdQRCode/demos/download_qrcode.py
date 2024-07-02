import feffery_antd_components as fac
import dash
from dash.dependencies import Component, Input, Output, State

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSegmented(
                id='qrcode-download-demo-segmented',
                options=[
                    {'label': 'canvas', 'value': 'canvas'},
                    {'label': 'svg', 'value': 'svg'},
                ],
                defaultValue='canvas',
            ),
            fac.AntdQRCode(id='qrcode', value='https://fac.feffery.tech/'),
            fac.AntdButton(
                '下载',
                id='qrcode-download-button',
                type='primary',
            ),
        ],
        id='myqrcode',
        direction='vertical',
    )

    return demo_contents


@app.callback(
    [Output('qrcode', 'type'), Output('qrcode', 'icon')],
    Input('qrcode-download-demo-segmented', 'value'),
)
def qrcode_download_demo_input_callback(input_value):
    if input_value == 'canvas':
        return ['canvas', '/assets/imgs/fac-logo.svg']
    elif input_value == 'svg':
        return [
            'svg',
            'https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg',
        ]
    return dash.no_update


app.clientside_callback(
    """
    (nClicks, type) => {
        function doDownload(url, fileName) {
            const a = document.createElement('a');
            a.download = fileName;
            a.href = url;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        };
        const downloadCanvasQRCode = () => {
            const canvas = document.getElementById('myqrcode')?.querySelector('canvas');
            if (canvas) {
                const url = canvas.toDataURL();
                doDownload(url, 'QRCode.png');
            }
        };
        const downloadSvgQRCode = () => {
            const svg = document.getElementById('myqrcode')?.querySelector('svg');
            const svgData = new XMLSerializer().serializeToString(svg);
            const blob = new Blob([svgData], {
                type: 'image/svg+xml;charset=utf-8',
            });
            const url = URL.createObjectURL(blob);
            doDownload(url, 'QRCode.svg');
        };
        if (nClicks) {
            if (type === 'canvas') {
                downloadCanvasQRCode();
            } else if (type === 'svg') {
                downloadSvgQRCode();
            }
        }
    }
    """,
    Input('qrcode-download-button', 'nClicks'),
    State('qrcode', 'type'),
    prevent_initial_call=True,
)


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSegmented(
            id='qrcode-download-demo-segmented',
            options=[
                {'label': 'canvas', 'value': 'canvas'},
                {'label': 'svg', 'value': 'svg'},
            ],
            defaultValue='canvas',
        ),
        fac.AntdQRCode(id='qrcode', value='https://fac.feffery.tech/'),
        fac.AntdButton(
            '下载',
            id='qrcode-download-button',
            type='primary',
        ),
    ],
    id='myqrcode',
    direction='vertical',
)

...

@app.callback(
    [Output('qrcode', 'type'), Output('qrcode', 'icon')],
    Input('qrcode-download-demo-segmented', 'value'),
)
def qrcode_download_demo_input_callback(input_value):
    if input_value == 'canvas':
        return ['canvas', '/assets/imgs/fac-logo.svg']
    elif input_value == 'svg':
        return [
            'svg',
            'https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg',
        ]
    return dash.no_update


app.clientside_callback(
    '''
    (nClicks, type) => {
        function doDownload(url, fileName) {
            const a = document.createElement('a');
            a.download = fileName;
            a.href = url;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        };
        const downloadCanvasQRCode = () => {
            const canvas = document.getElementById('myqrcode')?.querySelector('canvas');
            if (canvas) {
                const url = canvas.toDataURL();
                doDownload(url, 'QRCode.png');
            }
        };
        const downloadSvgQRCode = () => {
            const svg = document.getElementById('myqrcode')?.querySelector('svg');
            const svgData = new XMLSerializer().serializeToString(svg);
            const blob = new Blob([svgData], {
                type: 'image/svg+xml;charset=utf-8',
            });
            const url = URL.createObjectURL(blob);
            doDownload(url, 'QRCode.svg');
        };
        if (nClicks) {
            if (type === 'canvas') {
                downloadCanvasQRCode();
            } else if (type === 'svg') {
                downloadSvgQRCode();
            }
        }
    }
    ''',
    Input('qrcode-download-button', 'nClicks'),
    State('qrcode', 'type'),
    prevent_initial_call=True,
)
"""
    }
]
