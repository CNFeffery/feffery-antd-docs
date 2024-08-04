import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdPictureUpload(
            id='picture-upload-demo',
            apiUrl='/upload/',
            fileMaxSize=1,
            buttonContent='点击上传图片',
        ),
        fac.AntdSpin(html.Pre(id='picture-upload-demo-output'), text='回调中'),
    ]

    return demo_contents


@app.callback(
    Output('picture-upload-demo-output', 'children'),
    [
        Input('picture-upload-demo', 'lastUploadTaskRecord'),
        Input('picture-upload-demo', 'listUploadTaskRecord'),
    ],
    prevent_initial_call=True,
)
def picture_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
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
    fac.AntdPictureUpload(
        id='picture-upload-demo',
        apiUrl='/upload/',
        fileMaxSize=1,
        buttonContent='点击上传图片',
    ),
    fac.AntdSpin(html.Pre(id='picture-upload-demo-output'), text='回调中'),
]

...

@app.callback(
    Output('picture-upload-demo-output', 'children'),
    [
        Input('picture-upload-demo', 'lastUploadTaskRecord'),
        Input('picture-upload-demo', 'listUploadTaskRecord'),
    ],
    prevent_initial_call=True,
)
def picture_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
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
