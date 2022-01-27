from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdRate

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdRate(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdRate.md', encoding='utf-8').read()
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
                        fac.AntdTitle('整星选择：', level=5),
                        fac.AntdRate(count=10),
                        fac.AntdTitle('半星选择：', level=5),
                        fac.AntdRate(count=10, allowHalf=True),

                        fac.AntdDivider(
                            '基础使用',
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
fac.AntdTitle('整星选择：', level=5),
fac.AntdRate(count=10),
fac.AntdTitle('半星选择：', level=5),
fac.AntdRate(count=10, allowHalf=True)
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
                        fac.AntdRate(
                            count=10,
                            tooltips=[f'等级{i + 1}' for i in range(10)]
                        ),

                        fac.AntdDivider(
                            '为各个等级设置说明提示',
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
fac.AntdRate(
    count=10,
    tooltips=[f'等级{i + 1}' for i in range(10)]
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
                    id='为各个等级设置说明提示',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdRate(
                            count=10,
                            defaultValue=7.5,
                            allowHalf=True,
                            disabled=True
                        ),

                        fac.AntdDivider(
                            '只读模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　设置参数'),
                                fac.AntdText('defaultValue', code=True),
                                fac.AntdText('及'),
                                fac.AntdText('disabled=True', code=True),
                                fac.AntdText('之后，即等价于'),
                                fac.AntdText('只读模式', strong=True),
                                fac.AntdText('，适合单纯的星级展示')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdRate(
    count=10,
    defaultValue=7.5,
    allowHalf=True,
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
                    id='只读模式',
                    className='div-highlight'
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
                        fac.AntdSpin(
                            [
                                fac.AntdRate(id='rate-demo', count=10, allowHalf=True),
                                html.Br(),
                                fac.AntdText('value: ', strong=True),
                                fac.AntdText(id='rate-demo-output')
                            ],
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
fac.AntdSpin(
    [
        fac.AntdRate(id='rate-demo', count=10, allowHalf=True),
        html.Br(),
        fac.AntdText('value: ', strong=True),
        fac.AntdText(id='rate-demo-output')
    ],
    text='回调中'
)
...
@app.callback(
    Output('rate-demo-output', 'children'),
    Input('rate-demo', 'value'),
    prevent_initial_call=True
)
def rate_demo_callback(value):
    return value
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
                            {'title': '为各个等级设置说明提示', 'href': '#为各个等级设置说明提示'},
                            {'title': '只读模式', 'href': '#只读模式'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
            ),
            style={
                'flex': 'none',
                'padding': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
