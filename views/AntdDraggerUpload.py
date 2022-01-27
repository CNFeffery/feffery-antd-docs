from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdDraggerUpload

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdDraggerUpload(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdDraggerUpload.md', encoding='utf-8').read()
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
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传'
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
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
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            fileListMaxLength=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传'
                        ),

                        fac.AntdDivider(
                            '限制上传列表显示任务记录最大数量',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileListMaxLength=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
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
                    id='限制上传列表显示任务记录最大数量',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            fileTypes=['csv', 'txt'],
                            text='请上传.csv或.txt文件',
                            hint='点击或拖拽文件至此处进行上传'
                        ),

                        fac.AntdDivider(
                            '限制上传文件的类型范围',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileTypes=['csv', 'txt'],
    text='请上传.csv或.txt文件',
    hint='点击或拖拽文件至此处进行上传'
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
                    id='限制上传文件的类型范围',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            multiple=True,
                            text='多文件拖拽上传示例',
                            hint='点击或拖拽多个文件至此处进行上传'
                        ),

                        fac.AntdDivider(
                            '多文件上传模式',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    multiple=True,
    text='多文件拖拽上传示例',
    hint='点击或拖拽多个文件至此处进行上传'
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
                    id='多文件上传模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            directory=True,
                            text='文件夹拖拽上传示例',
                            hint='点击或拖拽文件夹至此处进行上传'
                        ),

                        fac.AntdDivider(
                            '文件夹上传模式',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    directory=True,
    text='文件夹拖拽上传示例',
    hint='点击或拖拽文件夹至此处进行上传'
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
                    id='文件夹上传模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            failedTooltipInfo='啊哦，上传过程出了问题...',
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传'
                        ),

                        fac.AntdDivider(
                            '自定义失败任务记录悬浮提示信息',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    failedTooltipInfo='啊哦，上传过程出了问题...',
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
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
                    id='自定义失败任务记录悬浮提示信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDraggerUpload(
                            id='dragger-upload-demo',
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传'
                        ),

                        fac.AntdSpin(
                            html.Pre(id='dragger-upload-demo-output'),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　这个例子展示了在满足文件体积限制的前提下，每次上传任务执行后，对成功或失败状态进行记录的相关参数信息'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdDraggerUpload(
    id='dragger-upload-demo',
    apiUrl='/upload/',
    fileMaxSize=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
),

fac.AntdSpin(
    html.Pre(id='dragger-upload-demo-output'),
    text='回调中'
)
...
import json

@app.callback(
    Output('dragger-upload-demo-output', 'children'),
    Input('dragger-upload-demo', 'lastUploadTaskRecord'),
    prevent_initial_call=True
)
def upload_callback_demo(lastUploadTaskRecord):
    if lastUploadTaskRecord:
        return json.dumps(lastUploadTaskRecord, indent=4, ensure_ascii=False)
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
                            {'title': '限制上传列表显示任务记录最大数量', 'href': '#限制上传列表显示任务记录最大数量'},
                            {'title': '限制上传文件的类型范围', 'href': '#限制上传文件的类型范围'},
                            {'title': '多文件上传模式', 'href': '#多文件上传模式'},
                            {'title': '文件夹上传模式', 'href': '#文件夹上传模式'},
                            {'title': '自定义失败任务记录悬浮提示信息', 'href': '#自定义失败任务记录悬浮提示信息'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    }
                ],
                containerId='docs-content',
                targetOffset=200
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
