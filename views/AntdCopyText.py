from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdCopyText

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCopyText(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCopyText.md', encoding='utf-8').read()
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

                        fac.AntdCopyText(
                            text='AntdCopyText复制示例'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdCopyText(
    text='AntdCopyText复制示例'
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

                        fac.AntdCopyText(
                            text='AntdCopyText复制示例',
                            beforeIcon='点我复制',
                            afterIcon='复制成功'
                        ),

                        fac.AntdCopyText(
                            text='AntdCopyText复制示例',
                            beforeIcon=fac.AntdIcon(icon='antd-smile'),
                            afterIcon=fac.AntdIcon(icon='antd-like')
                        ),

                        fac.AntdDivider(
                            '自定义复制前后渲染内容',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdCopyText(
    text='AntdCopyText复制示例',
    beforeIcon='点我复制',
    afterIcon='复制成功'
),

fac.AntdCopyText(
    text='AntdCopyText复制示例',
    beforeIcon=fac.AntdIcon(icon='antd-smile'),
    afterIcon=fac.AntdIcon(icon='antd-like')
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
                    id='自定义复制前后渲染内容',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdSpace(
                            [
                                fac.AntdInput(
                                    id='copy-text-input',
                                    maxLength=20,
                                    style={
                                        'width': '150px'
                                    }
                                ),
                                fac.AntdCopyText(
                                    id='copy-text-output',
                                    text='无内容'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　实时同步输入框中的已输入值'
                                )
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdInput(
            id='copy-text-input',
            maxLength=20,
            style={
                'width': '150px'
            }
        ),
        fac.AntdCopyText(
            id='copy-text-output',
            text='无内容'
        )
    ]
)

...                                

@app.callback(
    Output('copy-text-output', 'text'),
    Input('copy-text-input', 'value')
)
def copy_text_callback(value):
    return value or '无内容'
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
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '自定义复制前后渲染内容', 'href': '#自定义复制前后渲染内容'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    },
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
