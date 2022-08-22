from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdMentions

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdMentions(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdMentions.md', encoding='utf-8').read()
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

                        fac.AntdMentions(
                            options=[
                                {
                                    'label': '费弗里',
                                    'value': '费弗里'
                                },
                                {
                                    'label': '小A',
                                    'value': '小A'
                                },
                                {
                                    'label': 'liz',
                                    'value': 'liz'
                                }
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　输入'),
                                fac.AntdText('prefix', code=True),
                                fac.AntdText('参数指定的子项层触发字符（默认为'),
                                fac.AntdText('"@"', code=True),
                                fac.AntdText('），即可选择需要在此处提及的对象进行插入')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdMentions(
    options=[
        {
            'label': '费弗里',
            'value': '费弗里'
        },
        {
            'label': '小A',
            'value': '小A'
        },
        {
            'label': 'liz',
            'value': 'liz'
        }
    ],
    style={
        'width': '400px'
    }
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

                        fac.AntdDivider('autoSize=True', innerTextOrientation='left'),
                        fac.AntdMentions(
                            options=[
                                {
                                    'label': f'用户{i}',
                                    'value': f'用户{i}'
                                }
                                for i in list('ABCDEFGH')
                            ],
                            defaultValue='请 @用户A 协助 @用户B 与 @用户C 完成 @用户D 离职后遗留的工作内容，' * 5,
                            autoSize=True,
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider('autoSize={"minRows": 3, "maxRows": 5}', innerTextOrientation='left'),
                        fac.AntdMentions(
                            options=[
                                {
                                    'label': f'用户{i}',
                                    'value': f'用户{i}'
                                }
                                for i in list('ABCDEFGH')
                            ],
                            defaultValue='请 @用户A 协助 @用户B 与 @用户C 完成 @用户D 离职后遗留的工作内容，' * 5,
                            autoSize={"minRows": 3, "maxRows": 5},
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '配置输入框自适应高度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('autoSize=True', innerTextOrientation='left'),
fac.AntdMentions(
    options=[
        {
            'label': f'用户{i}',
            'value': f'用户{i}'
        }
        for i in list('ABCDEFGH')
    ],
    defaultValue='请 @用户A 协助 @用户B 与 @用户C 完成 @用户D 离职后遗留的工作内容，' * 5,
    autoSize=True,
    style={
        'width': '400px'
    }
),

fac.AntdDivider('autoSize={"minRows": 3, "maxRows": 5}', innerTextOrientation='left'),
fac.AntdMentions(
    options=[
        {
            'label': f'用户{i}',
            'value': f'用户{i}'
        }
        for i in list('ABCDEFGH')
    ],
    defaultValue='请 @用户A 协助 @用户B 与 @用户C 完成 @用户D 离职后遗留的工作内容，' * 5,
    autoSize={"minRows": 3, "maxRows": 5},
    style={
        'width': '400px'
    }
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
                    id='配置输入框自适应高度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('placement="top"', innerTextOrientation='left'),
                        fac.AntdMentions(
                            placement='top',
                            options=[
                                {
                                    'label': '费弗里',
                                    'value': '费弗里'
                                },
                                {
                                    'label': '小A',
                                    'value': '小A'
                                },
                                {
                                    'label': 'liz',
                                    'value': 'liz'
                                }
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '不同的子项悬浮层弹出方位',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('placement="top"', innerTextOrientation='left'),
fac.AntdMentions(
    placement='top',
    options=[
        {
            'label': '费弗里',
            'value': '费弗里'
        },
        {
            'label': '小A',
            'value': '小A'
        },
        {
            'label': 'liz',
            'value': 'liz'
        }
    ],
    style={
        'width': '400px'
    }
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
                    id='不同的子项悬浮层弹出方位',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdMentions(
                            id='mentions-demo',
                            placement='top',
                            autoSize=True,
                            options=[
                                {
                                    'label': '费弗里',
                                    'value': '费弗里'
                                },
                                {
                                    'label': '小A',
                                    'value': '小A'
                                },
                                {
                                    'label': 'liz',
                                    'value': 'liz'
                                }
                            ],
                            style={
                                'width': '400px'
                            }
                        ),
                        fac.AntdButton('提交', id='mentions-submit', type='primary'),
                        fac.AntdSpace(
                            [
                                html.Div(
                                    [
                                        fac.AntdText('value: ', strong=True),
                                        fac.AntdText(id='mentions-demo-output-value')
                                    ]
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('selectedOptions: ', strong=True),
                                        fac.AntdText(id='mentions-demo-output-selectedOptions')
                                    ]
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　本回调示例出于对服务器网络安全的考虑使用了'),
                                fac.AntdText('浏览器端回调', strong=True)
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdMentions(
    id='mentions-demo',
    placement='top',
    autoSize=True,
    options=[
        {
            'label': '费弗里',
            'value': '费弗里'
        },
        {
            'label': '小A',
            'value': '小A'
        },
        {
            'label': 'liz',
            'value': 'liz'
        }
    ],
    style={
        'width': '400px'
    }
),
fac.AntdButton('提交', id='mentions-submit', type='primary'),
fac.AntdSpace(
    [
        html.Div(
            [
                fac.AntdText('value: ', strong=True),
                fac.AntdText(id='mentions-demo-output-value')
            ]
        ),
        html.Div(
            [
                fac.AntdText('selectedOptions: ', strong=True),
                fac.AntdText(id='mentions-demo-output-selectedOptions')
            ]
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)
...
app.clientside_callback(
    """
    function(nClicks, value, selectedOptions) {
    
        if ( !value ) {
            value = ''
        }
        
        if ( !selectedOptions ) {
            selectedOptions = []
        }
    
        return [
            value.toString(),
            selectedOptions.toString()
        ];
    }
    """,
    [Output('mentions-demo-output-value', 'children'),
     Output('mentions-demo-output-selectedOptions', 'children')],
    Input('mentions-submit', 'nClicks'),
    [State('mentions-demo', 'value'),
     State('mentions-demo', 'selectedOptions')],
    prevent_initial_call=True
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
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '配置输入框自适应高度', 'href': '#配置输入框自适应高度'},
                            {'title': '不同的子项悬浮层弹出方位', 'href': '#不同的子项悬浮层弹出方位'},
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
