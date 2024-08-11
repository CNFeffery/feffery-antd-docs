import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdSwitch(id='show-remove-icon', checked=True),
                    label='showRemoveIcon',
                ),
                fac.AntdFormItem(
                    fac.AntdSwitch(id='show-preview-icon', checked=True),
                    label='showPreviewIcon',
                ),
            ]
        ),
        fac.AntdPictureUpload(
            id='picture-upload-icon-hide-demo',
            apiUrl='/upload/',
            fileMaxSize=1,
            buttonContent='点击上传图片',
            defaultFileList=[
                {
                    'name': 'feffery-添加好友二维码.jpg',
                    'status': 'done',
                    'url': '/assets/imgs/index/feffery-添加好友二维码.jpg',
                }
                for i in range(1, 6)
            ],
        ),
    ]

    return demo_contents


@app.callback(
    [
        Output('picture-upload-icon-hide-demo', 'showRemoveIcon'),
        Output('picture-upload-icon-hide-demo', 'showPreviewIcon'),
    ],
    [
        Input('show-remove-icon', 'checked'),
        Input('show-preview-icon', 'checked'),
    ],
)
def picture_upload_icon_hide_demo(showRemoveIcon, showPreviewIcon):
    return showRemoveIcon, showPreviewIcon


code_string = [
    {
        'code': """
[
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdSwitch(id='show-remove-icon', checked=True),
                label='showRemoveIcon',
            ),
            fac.AntdFormItem(
                fac.AntdSwitch(id='show-preview-icon', checked=True),
                label='showPreviewIcon',
            ),
        ]
    ),
    fac.AntdPictureUpload(
        id='picture-upload-icon-hide-demo',
        apiUrl='/upload/',
        fileMaxSize=1,
        buttonContent='点击上传图片',
        defaultFileList=[
            {
                'name': 'feffery-添加好友二维码.jpg',
                'status': 'done',
                'url': '/assets/imgs/index/feffery-添加好友二维码.jpg',
            }
            for i in range(1, 6)
        ],
    ),
]

...

@app.callback(
    [
        Output('picture-upload-icon-hide-demo', 'showRemoveIcon'),
        Output('picture-upload-icon-hide-demo', 'showPreviewIcon'),
    ],
    [
        Input('show-remove-icon', 'checked'),
        Input('show-preview-icon', 'checked'),
    ],
)
def picture_upload_icon_hide_demo(showRemoveIcon, showPreviewIcon):
    return showRemoveIcon, showPreviewIcon
"""
    }
]
