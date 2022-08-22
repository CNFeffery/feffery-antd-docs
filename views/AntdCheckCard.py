from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
import feffery_utils_components as fuc

import callbacks.AntdCheckCard

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCheckCard(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCheckCard.md', encoding='utf-8').read()
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
                        fac.AntdSpace(
                            [
                                fac.AntdCheckCard(
                                    fac.AntdText(
                                        '选择卡片示例' * 10
                                    )
                                ),
                                fac.AntdCheckCard(
                                    fac.AntdStatistic(
                                        title='统计数值示例',
                                        value=1332971
                                    )
                                ),
                                fac.AntdCheckCard(
                                    html.Div(
                                        [
                                            html.Div(
                                                fac.AntdAvatar(
                                                    mode='image',
                                                    size=48,
                                                    src='/assets/imgs/avatar-demo.jpg'
                                                ),
                                                style={
                                                    'flex': 'none',
                                                    'marginRight': '10px'
                                                }
                                            ),
                                            html.Div(
                                                fac.AntdText(
                                                    '选择卡片示例' * 10
                                                ),
                                                style={
                                                    'flex': 'auto'
                                                }
                                            )
                                        ],
                                        style={
                                            'display': 'flex'
                                        }
                                    )
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　'),
                                fac.AntdText('AntdCheckCard', code=True),
                                fac.AntdText('中可自由嵌套其它任意元素')
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
        fac.AntdCheckCard(
            fac.AntdText(
                '选择卡片示例' * 10
            )
        ),
        fac.AntdCheckCard(
            fac.AntdStatistic(
                title='统计数值示例',
                value=1332971
            )
        ),
        fac.AntdCheckCard(
            html.Div(
                [
                    html.Div(
                        fac.AntdAvatar(
                            mode='image',
                            size=48,
                            src='/assets/imgs/avatar-demo.jpg'
                        ),
                        style={
                            'flex': 'none',
                            'marginRight': '10px'
                        }
                    ),
                    html.Div(
                        fac.AntdText(
                            '选择卡片示例' * 10
                        ),
                        style={
                            'flex': 'auto'
                        }
                    )
                ],
                style={
                    'display': 'flex'
                }
            )
        )
    ],
    direction='vertical'
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
                        fac.AntdCheckCard(
                            fac.AntdText(
                                '选择卡片示例' * 10
                            ),
                            id='check-card-demo'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('checked: '),
                                fac.AntdText(id='check-card-demo-output')
                            ]
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
fac.AntdCheckCard(
    fac.AntdText(
        '选择卡片示例' * 10
    ),
    id='check-card-demo'
),

fac.AntdParagraph(
    [
        fac.AntdText('checked: '),
        fac.AntdText(id='check-card-demo-output')
    ]
)

...

@app.callback(
    Output('check-card-demo-output', 'children'),
    Input('check-card-demo', 'checked')
)
def check_card_demo_callback(checked):

    return str(checked)
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
