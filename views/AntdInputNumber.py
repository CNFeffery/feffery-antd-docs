from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdInputNumber

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdInputNumber(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdInputNumber.md', encoding='utf-8').read()
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
                        fac.AntdInputNumber(
                            size='small',
                            placeholder='基础使用',
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
                        ),
                        html.Br(),
                        fac.AntdInputNumber(
                            size='middle',
                            placeholder='基础使用',
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
                        ),
                        html.Br(),
                        fac.AntdInputNumber(
                            size='large',
                            placeholder='基础使用',
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
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
fac.AntdInputNumber(
    size='small',
    placeholder='基础使用',
    style={
        'width': '200px',
        'marginBottom': '5px'
    }
),
html.Br(),
fac.AntdInputNumber(
    size='middle',
    placeholder='基础使用',
    style={
        'width': '200px',
        'marginBottom': '5px'
    }
),
html.Br(),
fac.AntdInputNumber(
    size='large',
    placeholder='基础使用',
    style={
        'width': '200px',
        'marginBottom': '5px'
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
                        fac.AntdInputNumber(
                            addonBefore='金额',
                            addonAfter='￥',
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
                        ),

                        fac.AntdDivider(
                            '添加前后缀额外内容',
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
fac.AntdInputNumber(
    addonBefore='金额',
    addonAfter='￥',
    style={
        'width': '200px',
        'marginBottom': '5px'
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
                    id='添加前后缀额外内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            placeholder='默认未关闭',
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
                        ),
                        html.Br(),
                        fac.AntdInputNumber(
                            placeholder='已关闭',
                            keyboard=False,
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
                        ),

                        fac.AntdDivider(
                            '关闭键盘快捷操作',
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
fac.AntdInputNumber(
    placeholder='默认未关闭',
    style={
        'width': '200px',
        'marginBottom': '5px'
    }
),
html.Br(),
fac.AntdInputNumber(
    placeholder='已关闭',
    keyboard=False,
    style={
        'width': '200px',
        'marginBottom': '5px'
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
                    id='关闭键盘快捷操作',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            min=100,
                            max=1000,
                            step=0.01,
                            precision=5,
                            style={
                                'width': '200px',
                                'marginBottom': '5px'
                            }
                        ),

                        fac.AntdDivider(
                            '上下限、步长及精度设置',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '　　设置上下限后，输入数值超出范围时，会在enter后自动校正到最近的上或下限值'
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
fac.AntdInputNumber(
    min=100,
    max=1000,
    step=0.01,
    precision=5,
    style={
        'width': '200px',
        'marginBottom': '5px'
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
                    id='上下限、步长及精度设置',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTitle('stringMode=False（默认）', level=5),
                        fac.AntdInputNumber(
                            defaultValue=10.3123123123123123123121312421413411234321432512,
                            style={
                                'width': '100%',
                                'marginBottom': '5px'
                            }
                        ),
                        fac.AntdTitle('stringMode=True', level=5),
                        fac.AntdInputNumber(
                            stringMode=True,
                            defaultValue='10.3123123123123123123121312421413411234321432512',
                            style={
                                'width': '100%',
                                'marginBottom': '5px'
                            }
                        ),

                        fac.AntdDivider(
                            '高精度模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　对数值输入精度要求很高时，需要设置'),
                                fac.AntdText('stringMode=True', code=True),
                                fac.AntdText('从而开启高精度模式，此模式下所有数值相关参数需要设置为字符串从而保证数值精度不会损失')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTitle('stringMode=False（默认）', level=5),
fac.AntdInputNumber(
    defaultValue=10.3123123123123123123121312421413411234321432512,
    style={
        'width': '100%',
        'marginBottom': '5px'
    }
),
fac.AntdTitle('stringMode=True', level=5),
fac.AntdInputNumber(
    stringMode=True,
    defaultValue='10.3123123123123123123121312421413411234321432512',
    style={
        'width': '100%',
        'marginBottom': '5px'
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
                    id='高精度模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            [
                                fac.AntdTitle('输入后请按下enter触发回调：', level=5),
                                fac.AntdInputNumber(
                                    id='input-number-demo1',
                                    placeholder='常规模式',
                                    style={
                                        'width': '500px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Br(),
                                fac.AntdInputNumber(
                                    id='input-number-demo2',
                                    placeholder='高精度模式，网络安全考虑已设置precision=25',
                                    precision=25,
                                    stringMode=True,
                                    style={
                                        'width': '500px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Br(),
                                fac.AntdSpace(id='input-number-demo-output', direction='vertical')
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
        fac.AntdTitle('输入后请按下enter触发回调：', level=5),
        fac.AntdInputNumber(
            id='input-number-demo1',
            placeholder='常规模式',
            style={
                'width': '500px',
                'marginBottom': '5px'
            }
        ),
        html.Br(),
        fac.AntdInputNumber(
            id='input-number-demo2',
            placeholder='高精度模式，网络安全考虑已设置precision=25',
            precision=25,
            stringMode=True,
            style={
                'width': '500px',
                'marginBottom': '5px'
            }
        ),
        html.Br(),
        fac.AntdSpace(id='input-number-demo-output', direction='vertical')
    ],
    text='回调中'
)
...
@app.callback(
    Output('input-number-demo-output', 'children'),
    [Input('input-number-demo1', 'nSubmit'),
     Input('input-number-demo2', 'nSubmit')],
    [State('input-number-demo1', 'value'),
     State('input-number-demo2', 'value')],
    prevent_initial_call=True
)
def input_number_callback(nSubmit1, nSubmit2, value1, value2):
    return [
        html.Div(
            [
                fac.AntdText('常规模式value：', strong=True),
                fac.AntdText(str(value1))
            ]
        ),
        html.Div(
            [
                fac.AntdText('常规模式value类型：', strong=True),
                fac.AntdText(str(type(value1)))
            ]
        ),
        fac.AntdDivider(),
        html.Div(
            [
                fac.AntdText('高精度模式value：', strong=True),
                fac.AntdText(str(value2))
            ]
        ),
        html.Div(
            [
                fac.AntdText('高精度模式value类型：', strong=True),
                fac.AntdText(str(type(value2)))
            ]
        )
    ]
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
                            {'title': '添加前后缀额外内容', 'href': '#添加前后缀额外内容'},
                            {'title': '关闭键盘快捷操作', 'href': '#关闭键盘快捷操作'},
                            {'title': '上下限、步长及精度设置', 'href': '#上下限、步长及精度设置'},
                            {'title': '高精度模式', 'href': '#高精度模式'},
                            {'title': '回调示例', 'href': '#回调示例'},
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
