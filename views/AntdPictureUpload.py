from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdPictureUpload
from .side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '组件介绍'
                        },
                        {
                            'title': '数据录入'
                        },
                        {
                            'title': 'AntdPictureUpload 图片上传'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于为用户提供图片上传功能。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdPictureUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            buttonContent='点击上传图片'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPictureUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    buttonContent='点击上传图片'
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPictureUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            buttonContent='点击上传图片',
                            editable=True,
                            editConfig={
                                'grid': True,
                                'rotate': True,
                                'modalTitle': '图片编辑窗口标题示例',
                                'modalWidth': 600
                            }
                        ),

                        fac.AntdDivider(
                            '图片编辑功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPictureUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    buttonContent='点击上传图片',
    editable=True,
    editConfig={
        'grid': True,
        'rotate': True,
        'modalTitle': '图片编辑窗口标题示例',
        'modalWidth': 600
    }
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='图片编辑功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPictureUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            buttonContent='点击上传图片',
                            defaultFileList=[
                                {
                                    'name': 'feffery-添加好友二维码.jpg',
                                    'status': 'done',
                                    'url': '/assets/imgs/feffery-添加好友二维码.jpg'
                                }
                                for i in range(1, 6)
                            ],
                            confirmBeforeDelete=True
                        ),

                        fac.AntdDivider(
                            '为删除操作添加二次确认',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPictureUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    buttonContent='点击上传图片',
    defaultFileList=[
        {
            'name': 'feffery-添加好友二维码.jpg',
            'status': 'done',
            'url': '/assets/imgs/feffery-添加好友二维码.jpg'
        }
        for i in range(1, 6)
    ],
    confirmBeforeDelete=True
)
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='为删除操作添加二次确认',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='show-remove-icon',
                                        checked=True
                                    ),
                                    label='showRemoveIcon'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdSwitch(
                                        id='show-preview-icon',
                                        checked=True
                                    ),
                                    label='showPreviewIcon'
                                )
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
                                    'url': '/assets/imgs/feffery-添加好友二维码.jpg'
                                }
                                for i in range(1, 6)
                            ]
                        ),

                        fac.AntdDivider(
                            '控制预览及删除图标的显隐',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='show-remove-icon',
                checked=True
            ),
            label='showRemoveIcon'
        ),
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='show-preview-icon',
                checked=True
            ),
            label='showPreviewIcon'
        )
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
            'url': '/assets/imgs/feffery-添加好友二维码.jpg'
        }
        for i in range(1, 6)
    ]
)

...

@app.callback(
    [Output('picture-upload-icon-hide-demo', 'showRemoveIcon'),
     Output('picture-upload-icon-hide-demo', 'showPreviewIcon')],
    [Input('show-remove-icon', 'checked'),
     Input('show-preview-icon', 'checked')]
)
def picture_upload_icon_hide_demo(showRemoveIcon, showPreviewIcon):

    return showRemoveIcon, showPreviewIcon
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='控制预览及删除图标的显隐',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPictureUpload(
                            id='picture-upload-demo',
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            buttonContent='点击上传图片'
                        ),

                        fac.AntdSpin(
                            html.Pre(id='picture-upload-demo-output'),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPictureUpload(
    id='picture-upload-demo',
    apiUrl='/upload/',
    fileMaxSize=1,
    buttonContent='点击上传图片'
),

fac.AntdSpin(
    html.Pre(id='picture-upload-demo-output'),
    text='回调中'
)

...

import json

...

@app.callback(
    Output('picture-upload-demo-output', 'children'),
    [Input('picture-upload-demo', 'lastUploadTaskRecord'),
     Input('picture-upload-demo', 'listUploadTaskRecord')],
    prevent_initial_call=True
)
def picture_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(
            {
                'lastUploadTaskRecord': lastUploadTaskRecord,
                'listUploadTaskRecord': listUploadTaskRecord
            },
            indent=4,
            ensure_ascii=False
        )
'''
                            ),
                            title='点击查看代码',
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='回调示例',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '图片编辑功能', 'href': '#图片编辑功能'},
                    {'title': '为删除操作添加二次确认', 'href': '#为删除操作添加二次确认'},
                    {'title': '控制预览及删除图标的显隐', 'href': '#控制预览及删除图标的显隐'},
                    {'title': '禁用状态', 'href': '#禁用状态'},
                    {'title': '回调示例', 'href': '#回调示例'},
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='AntdPictureUpload'
        )
    ],
    style={
        'display': 'flex'
    }
)
