from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdPopconfirm

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdPopconfirm(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdPopconfirm.md', encoding='utf-8').read()
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
                        fac.AntdPopconfirm(
                            fac.AntdButton(
                                '点击触发',
                                type='primary'
                            ),
                            title='气泡确认测试',
                            containerId='docs-content'
                        ),

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
fac.AntdPopconfirm(
    fac.AntdButton(
        '点击触发',
        type='primary'
    ),
    title='气泡确认测试',
    containerId='docs-content'
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPopconfirm(
                            fac.AntdButton(
                                '点击触发',
                                type='primary'
                            ),
                            id='popconfirm-demo',
                            title='气泡确认测试',
                            containerId='docs-content'
                        ),

                        html.Br(),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    [
                                        fac.AntdText('confirmCounts：', strong=True),
                                        fac.AntdText(id='popconfirm-demo-output-1')
                                    ]
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('cancelCounts：', strong=True),
                                        fac.AntdText(id='popconfirm-demo-output-2')
                                    ]
                                )
                            ],
                            direction='vertical'
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '点击触发',
        type='primary'
    ),
    id='popconfirm-demo',
    title='气泡确认测试',
    containerId='docs-content'
),

html.Br(),

fac.AntdSpace(
    [
        html.Div(
            [
                fac.AntdText('confirmCounts：', strong=True),
                fac.AntdText(id='popconfirm-demo-output-1')
            ]
        ),
        html.Div(
            [
                fac.AntdText('cancelCounts：', strong=True),
                fac.AntdText(id='popconfirm-demo-output-2')
            ]
        )
    ],
    direction='vertical'
)
...
@app.callback(
    [Output('popconfirm-demo-output-1', 'children'),
     Output('popconfirm-demo-output-2', 'children')],
    [Input('popconfirm-demo', 'confirmCounts'),
     Input('popconfirm-demo', 'cancelCounts')],
    prevent_initial_call=True
)
def popconfirm_demo_callback(confirmCounts, cancelCounts):
    return str(confirmCounts), str(cancelCounts)
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
                            {'title': '回调示例', 'href': '#回调示例'}
                        ]
                    },
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
