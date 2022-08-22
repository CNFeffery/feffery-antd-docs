from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
import feffery_utils_components as fuc

import callbacks.AntdCheckCardGroup

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCheckCardGroup(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCheckCardGroup.md', encoding='utf-8').read()
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
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    fac.AntdStatistic(
                                        title='统计数值示例',
                                        value=1332971
                                    ),
                                    value=f'option{i}'
                                )
                                for i in range(4)
                            ]
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
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            fac.AntdStatistic(
                title='统计数值示例',
                value=1332971
            ),
            value=f'option{i}'
        )
        for i in range(4)
    ]
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
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    fac.AntdStatistic(
                                        title='统计数值示例',
                                        value=1332971
                                    ),
                                    value=f'option{i}'
                                )
                                for i in range(4)
                            ],
                            multiple=True
                        ),

                        fac.AntdDivider(
                            '多选模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            fac.AntdStatistic(
                title='统计数值示例',
                value=1332971
            ),
            value=f'option{i}'
        )
        for i in range(4)
    ],
    multiple=True
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
                    id='多选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            '单选模式',
                            innerTextOrientation='left'
                        ),
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    fac.AntdStatistic(
                                        title='统计数值示例',
                                        value=1332971
                                    ),
                                    value=f'option{i}'
                                )
                                for i in range(4)
                            ],
                            id='check-card-group-demo1'
                        ),
                        fac.AntdParagraph(
                            [
                                fac.AntdText('value: '),
                                fac.AntdText(id='check-card-group-demo1-output')
                            ]
                        ),

                        fac.AntdDivider(
                            '多选模式',
                            innerTextOrientation='left'
                        ),
                        fac.AntdCheckCardGroup(
                            [
                                fac.AntdCheckCard(
                                    fac.AntdStatistic(
                                        title='统计数值示例',
                                        value=1332971
                                    ),
                                    value=f'option{i}'
                                )
                                for i in range(4)
                            ],
                            id='check-card-group-demo2',
                            multiple=True
                        ),
                        fac.AntdParagraph(
                            [
                                fac.AntdText('value: '),
                                fac.AntdText(id='check-card-group-demo2-output')
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
fac.AntdDivider(
    '单选模式',
    innerTextOrientation='left'
),
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            fac.AntdStatistic(
                title='统计数值示例',
                value=1332971
            ),
            value=f'option{i}'
        )
        for i in range(4)
    ],
    id='check-card-group-demo1'
),
fac.AntdParagraph(
    [
        fac.AntdText('value: '),
        fac.AntdText(id='check-card-group-demo1-output')
    ]
),

fac.AntdDivider(
    '多选模式',
    innerTextOrientation='left'
),
fac.AntdCheckCardGroup(
    [
        fac.AntdCheckCard(
            fac.AntdStatistic(
                title='统计数值示例',
                value=1332971
            ),
            value=f'option{i}'
        )
        for i in range(4)
    ],
    id='check-card-group-demo2',
    multiple=True
),
fac.AntdParagraph(
    [
        fac.AntdText('value: '),
        fac.AntdText(id='check-card-group-demo2-output')
    ]
)

...

@app.callback(
    Output('check-card-group-demo1-output', 'children'),
    Input('check-card-group-demo1', 'value')
)
def check_card_group_demo1_callback(value):
    return str(value)


@app.callback(
    Output('check-card-group-demo2-output', 'children'),
    Input('check-card-group-demo2', 'value')
)
def check_card_group_demo2_callback(value):
    return str(value)
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
                            {'title': '多选模式', 'href': '#多选模式'},
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
