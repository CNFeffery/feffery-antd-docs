from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdPictureUpload

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdPictureUpload(id, className, style, *args, **kwargs)',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5'
                    }
                ),

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                html.Span(
                    '主要参数说明：',
                    id='主要参数说明',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5',
                        'fontWeight': 'bold',
                        'fontSize': '1.2rem'
                    }
                ),

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdPictureUpload.md', encoding='utf-8').read()
                ),

                html.Div(
                    html.Span(
                        '使用示例',
                        id='使用示例',
                        style={
                            'borderLeft': '4px solid grey',
                            'padding': '3px 0 3px 10px',
                            'backgroundColor': '#f5f5f5',
                            'fontWeight': 'bold',
                            'fontSize': '1.2rem'
                        }
                    ),
                    style={
                        'marginBottom': '10px'
                    }
                ),

                html.Div(
                    [
                        fac.AntdPictureUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            buttonContent='点击上传图片'
                        ),

                        fac.AntdDivider(
                            '基础使用及单文件大小限制',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdPictureUpload(
    apiUrl='/upload/',
    fileMaxSize=1
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础使用及单文件大小限制',
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
                            is_open=False,
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
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '主要参数说明', 'href': '#主要参数说明'},
                    {
                        'title': '使用示例',
                        'href': '#使用示例',
                        'children': [
                            {'title': '基础使用及单文件大小限制', 'href': '#基础使用及单文件大小限制'},
                            {'title': '图片编辑功能', 'href': '#图片编辑功能'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    }
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
