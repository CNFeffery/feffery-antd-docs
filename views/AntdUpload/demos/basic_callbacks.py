import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdSpace(
            [
                'multiple:',
                fac.AntdSwitch(
                    id='upload-demo-is-multiple',
                    checked=False,
                    checkedChildren='True',
                    unCheckedChildren='False',
                ),
            ],
            style={'marginBottom': '5px', 'width': '100%'},
        ),
        fac.AntdUpload(id='upload-demo', apiUrl='/upload/', fileMaxSize=1),
        fac.AntdSpin(html.Pre(id='upload-demo-output'), text='回调中'),
    ]

    return demo_contents


@app.callback(
    Output('upload-demo', 'multiple'),
    Input('upload-demo-is-multiple', 'checked'),
)
def upload_is_multiple(checked):
    return checked


@app.callback(
    Output('upload-demo-output', 'children'),
    [
        Input('upload-demo', 'lastUploadTaskRecord'),
        Input('upload-demo', 'listUploadTaskRecord'),
    ],
    prevent_initial_call=True,
)
def upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(
            {
                'lastUploadTaskRecord': lastUploadTaskRecord,
                'listUploadTaskRecord': listUploadTaskRecord,
            },
            indent=4,
            ensure_ascii=False,
        )


code_string = [
    {
        'code': """
[
    fac.AntdSpace(
        [
            'multiple:',
            fac.AntdSwitch(
                id='upload-demo-is-multiple',
                checked=False,
                checkedChildren='True',
                unCheckedChildren='False',
            ),
        ],
        style={'marginBottom': '5px', 'width': '100%'},
    ),
    fac.AntdUpload(id='upload-demo', apiUrl='/upload/', fileMaxSize=1),
    fac.AntdSpin(html.Pre(id='upload-demo-output'), text='回调中'),
]

...

@app.callback(
    Output('upload-demo', 'multiple'),
    Input('upload-demo-is-multiple', 'checked'),
)
def upload_is_multiple(checked):
    return checked


@app.callback(
    Output('upload-demo-output', 'children'),
    [
        Input('upload-demo', 'lastUploadTaskRecord'),
        Input('upload-demo', 'listUploadTaskRecord'),
    ],
    prevent_initial_call=True,
)
def upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(
            {
                'lastUploadTaskRecord': lastUploadTaskRecord,
                'listUploadTaskRecord': listUploadTaskRecord,
            },
            indent=4,
            ensure_ascii=False,
        )
"""
    }
]
