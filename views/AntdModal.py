from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdModal

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdModal(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdModal.md', encoding='utf-8').read()
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
                        fac.AntdButton(
                            '触发对话框',
                            type='primary',
                            id='modal-demo-trigger-1'
                        ),

                        fac.AntdModal(
                            fac.AntdText('对话框内容测试'),
                            id='modal-demo-1',
                            visible=False,
                            title=html.Span(
                                [
                                    fac.AntdIcon(icon='fc-search'),
                                    '标题测试'
                                ]
                            ),
                            renderFooter=True
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
fac.AntdButton(
    '触发对话框',
    type='primary',
    id='modal-demo-trigger-1'
),

fac.AntdModal(
    fac.AntdText('对话框内容测试'),
    id='modal-demo-1',
    visible=False,
    title=html.Span(
        [
            fac.AntdIcon(icon='fc-search'),
            '标题测试'
        ]
    ),
    renderFooter=True
)
...
@app.callback(
    Output('modal-demo-1', 'visible'),
    Input('modal-demo-trigger-1', 'nClicks'),
    prevent_initial_call=True
)
def modal_demo_callback1(nClicks):
    return True
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
                        fac.AntdButton(
                            '触发对话框',
                            type='primary',
                            id='modal-demo-trigger-2'
                        ),

                        fac.AntdModal(
                            fac.AntdText('对话框内容测试'),
                            id='modal-demo-2',
                            visible=False,
                            title={
                                'content': '标题测试',
                                'prefixIcon': 'fc-search'
                            },
                            renderFooter=True
                        ),

                        html.Br(),

                        fac.AntdSpace(
                            [
                                html.Div(
                                    [
                                        fac.AntdText('okCounts：', strong=True),
                                        fac.AntdText(id='modal-demo-2-output-1')
                                    ]
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('cancelCounts：', strong=True),
                                        fac.AntdText(id='modal-demo-2-output-2')
                                    ]
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('closeCounts：', strong=True),
                                        fac.AntdText(id='modal-demo-2-output-3')
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
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdButton(
    '触发对话框',
    type='primary',
    id='modal-demo-trigger-2'
),

fac.AntdModal(
    fac.AntdText('对话框内容测试'),
    id='modal-demo-2',
    visible=False,
    title={
        'content': '标题测试',
        'prefixIcon': 'fc-search'
    },
    renderFooter=True
),

html.Br(),

fac.AntdSpace(
    [
        html.Div(
            [
                fac.AntdText('okCounts：', strong=True),
                fac.AntdText(id='modal-demo-2-output-1')
            ]
        ),
        html.Div(
            [
                fac.AntdText('cancelCounts：', strong=True),
                fac.AntdText(id='modal-demo-2-output-2')
            ]
        ),
        html.Div(
            [
                fac.AntdText('closeCounts：', strong=True),
                fac.AntdText(id='modal-demo-2-output-3')
            ]
        )
    ],
    direction='vertical'
)
...
@app.callback(
    Output('modal-demo-2', 'visible'),
    Input('modal-demo-trigger-2', 'nClicks'),
    prevent_initial_call=True
)
def modal_demo_callback2(nClicks):
    return True


@app.callback(
    [Output('modal-demo-2-output-1', 'children'),
     Output('modal-demo-2-output-2', 'children'),
     Output('modal-demo-2-output-3', 'children')],
    [Input('modal-demo-2', 'okCounts'),
     Input('modal-demo-2', 'cancelCounts'),
     Input('modal-demo-2', 'closeCounts')],
     prevent_initial_call=True
)
def modal_demo_callback3(okCounts, cancelCounts, closeCounts):
    return [str(okCounts), str(cancelCounts), str(closeCounts)]
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
