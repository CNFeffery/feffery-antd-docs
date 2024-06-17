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
                    id='dragger-upload-demo-is-multiple',
                    checked=False,
                    checkedChildren='True',
                    unCheckedChildren='False',
                ),
            ],
            style={'marginBottom': '5px', 'width': '100%'},
        ),
        fac.AntdDraggerUpload(
            id='dragger-upload-demo',
            apiUrl='/upload/',
            fileMaxSize=1,
            text='拖拽上传示例',
            hint='点击或拖拽文件至此处进行上传',
        ),
        fac.AntdSpin(html.Pre(id='dragger-upload-demo-output'), text='回调中'),
    ]

    return demo_contents


@app.callback(
    Output('dragger-upload-demo', 'multiple'),
    Input('dragger-upload-demo-is-multiple', 'checked'),
)
def dragger_upload_is_multiple(checked):
    return checked


@app.callback(
    Output('dragger-upload-demo-output', 'children'),
    [
        Input('dragger-upload-demo', 'lastUploadTaskRecord'),
        Input('dragger-upload-demo', 'listUploadTaskRecord'),
    ],
    prevent_initial_call=True,
)
def dragger_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
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
                id='dragger-upload-demo-is-multiple',
                checked=False,
                checkedChildren='True',
                unCheckedChildren='False',
            ),
        ],
        style={'marginBottom': '5px', 'width': '100%'},
    ),
    fac.AntdDraggerUpload(
        id='dragger-upload-demo',
        apiUrl='/upload/',
        fileMaxSize=1,
        text='拖拽上传示例',
        hint='点击或拖拽文件至此处进行上传',
    ),
    fac.AntdSpin(html.Pre(id='dragger-upload-demo-output'), text='回调中'),
]

...

@app.callback(
    Output('dragger-upload-demo', 'multiple'),
    Input('dragger-upload-demo-is-multiple', 'checked'),
)
def dragger_upload_is_multiple(checked):
    return checked


@app.callback(
    Output('dragger-upload-demo-output', 'children'),
    [
        Input('dragger-upload-demo', 'lastUploadTaskRecord'),
        Input('dragger-upload-demo', 'listUploadTaskRecord'),
    ],
    prevent_initial_call=True,
)
def dragger_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
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
