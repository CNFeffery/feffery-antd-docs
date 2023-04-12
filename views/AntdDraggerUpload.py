from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdDraggerUpload
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
                            'title': 'AntdDraggerUpload 拖拽上传'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于为用户提供拖拽式的文件上传功能。')
                    ]
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
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
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            fileListMaxLength=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传'
                        ),

                        fac.AntdDivider(
                            '限制上传列表最大数量',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileListMaxLength=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
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
                    id='限制上传列表最大数量',
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
                            '限制上传文件类型',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileTypes=['csv', 'txt'],
    text='请上传.csv或.txt文件',
    hint='点击或拖拽文件至此处进行上传'
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
                    id='限制上传文件类型',
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    multiple=True,
    text='多文件拖拽上传示例',
    hint='点击或拖拽多个文件至此处进行上传'
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    directory=True,
    text='文件夹拖拽上传示例',
    hint='点击或拖拽文件夹至此处进行上传'
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
                            '自定义失败记录提示信息',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    failedTooltipInfo='啊哦，上传过程出了问题...',
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传'
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
                    id='自定义失败记录提示信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传',
                            defaultFileList=[
                                {
                                    'name': f'demo{i}.txt',
                                    'status': 'done'
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传',
    defaultFileList=[
        {
            'name': f'demo{i}.txt',
            'status': 'done'
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
                        fac.AntdDraggerUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传',
                            disabled=True
                        ),

                        fac.AntdDivider(
                            '禁用状态',
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
fac.AntdDraggerUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    text='拖拽上传示例',
    hint='点击或拖拽文件至此处进行上传',
    disabled=True
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
                    id='禁用状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                'multiple:',
                                fac.AntdSwitch(
                                    id='dragger-upload-demo-is-multiple',
                                    checked=False,
                                    checkedChildren='True',
                                    unCheckedChildren='False'
                                )
                            ],
                            style={
                                'marginBottom': '5px',
                                'width': '100%'
                            }
                        ),

                        fac.AntdDraggerUpload(
                            id='dragger-upload-demo',
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            text='拖拽上传示例',
                            hint='点击或拖拽文件至此处进行上传',
                            showPercent=True
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

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        'multiple:',
        fac.AntdSwitch(
            id='dragger-upload-demo-is-multiple',
            checked=False,
            checkedChildren='True',
            unCheckedChildren='False'
        )
    ],
    style={
        'marginBottom': '5px',
        'width': '100%'
    }
),

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

...

@app.callback(
    Output('dragger-upload-demo', 'multiple'),
    Input('dragger-upload-demo-is-multiple', 'checked')
)
def dragger_upload_is_multiple(checked):
    return checked


@app.callback(
    Output('dragger-upload-demo-output', 'children'),
    [Input('dragger-upload-demo', 'lastUploadTaskRecord'),
     Input('dragger-upload-demo', 'listUploadTaskRecord')],
    prevent_initial_call=True
)
def dragger_upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
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
                    {'title': '限制上传列表最大数量', 'href': '#限制上传列表最大数量'},
                    {'title': '限制上传列表最大数量', 'href': '#限制上传列表最大数量'},
                    {'title': '限制上传文件类型', 'href': '#限制上传文件类型'},
                    {'title': '多文件上传模式', 'href': '#多文件上传模式'},
                    {'title': '文件夹上传模式', 'href': '#文件夹上传模式'},
                    {'title': '自定义失败记录提示信息', 'href': '#自定义失败记录提示信息'},
                    {'title': '为删除操作添加二次确认', 'href': '#为删除操作添加二次确认'},
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
            component_name='AntdDraggerUpload'
        )
    ],
    style={
        'display': 'flex'
    }
)
