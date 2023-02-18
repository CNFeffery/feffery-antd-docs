from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdUpload
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
                            'title': 'AntdUpload 上传'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于为用户提供文件上传功能。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            fileListMaxLength=1
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileListMaxLength=1
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
                    id='限制上传列表最大数量',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            fileTypes=['csv', 'txt'],
                            buttonContent='请上传.csv或.txt文件'
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    fileTypes=['csv', 'txt'],
    buttonContent='请上传csv或txt文件'
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
                    id='限制上传文件类型',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            multiple=True,
                            buttonContent='点击上传多个文件'
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    multiple=True,
    buttonContent='点击上传多个文件'
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
                    id='多文件上传模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            directory=True,
                            buttonContent='点击选择文件夹进行上传'
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    directory=True,
    buttonContent='点击选择文件夹进行上传'
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
                    id='文件夹上传模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
                            failedTooltipInfo='啊哦，上传过程出了问题...'
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    failedTooltipInfo='啊哦，上传过程出了问题...'
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
                    id='自定义失败记录提示信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
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
                            is_open=False,
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
                        fac.AntdUpload(
                            apiUrl='/upload/',
                            fileMaxSize=1,
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
fac.AntdUpload(
    apiUrl='/upload/',
    fileMaxSize=1,
    disabled=True
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
                    id='禁用状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                'multiple:',
                                fac.AntdSwitch(
                                    id='upload-demo-is-multiple',
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

                        fac.AntdUpload(
                            id='upload-demo',
                            apiUrl='/upload/',
                            fileMaxSize=1
                        ),

                        fac.AntdSpin(
                            html.Pre(id='upload-demo-output'),
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
            id='upload-demo-is-multiple',
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

fac.AntdUpload(
    id='upload-demo',
    apiUrl='/upload/',
    fileMaxSize=1
),

fac.AntdSpin(
    html.Pre(id='upload-demo-output'),
    text='回调中'
)

...

import json

...

@app.callback(
    Output('upload-demo', 'multiple'),
    Input('upload-demo-is-multiple', 'checked')
)
def upload_is_multiple(checked):
    return checked


@app.callback(
    Output('upload-demo-output', 'children'),
    [Input('upload-demo', 'lastUploadTaskRecord'),
     Input('upload-demo', 'listUploadTaskRecord')],
    prevent_initial_call=True
)
def upload_callback_demo(lastUploadTaskRecord, listUploadTaskRecord):
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
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
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
            component_name='AntdUpload'
        )
    ],
    style={
        'display': 'flex'
    }
)
