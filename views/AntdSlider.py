from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdSlider

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdSlider(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdSlider.md', encoding='utf-8').read()
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
                        html.Div(
                            [
                                fac.AntdSlider(min=-100, max=100),
                                fac.AntdSlider(range=True, min=-100, max=100)
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

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
html.Div(
    [
        fac.AntdSlider(min=-100, max=100),
        fac.AntdSlider(range=True, min=-100, max=100)
    ],
    style={
        'width': '400px'
    }
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
                        html.Div(
                            [
                                fac.AntdSlider(defaultValue=66, min=-100, max=100),
                                fac.AntdSlider(defaultValue=[-10, 66], range=True, min=-100, max=100)
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '设置默认值',
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
                        html.Div(
                            [
                                fac.AntdSlider(defaultValue=66, min=-100, max=100),
                                fac.AntdSlider(defaultValue=[-10, 66], range=True, min=-100, max=100)
                            ],
                            style={
                                'width': '400px'
                            }
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
                    id='设置默认值',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdSlider(step=20, min=-100, max=100),
                                fac.AntdSlider(step=0.1, range=True, min=-100, max=100)
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '设置用户拖拽调节步长',
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
html.Div(
    [
        fac.AntdSlider(step=20, min=-100, max=100),
        fac.AntdSlider(step=0.1, range=True, min=-100, max=100)
    ],
    style={
        'width': '400px'
    }
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
                    id='设置用户拖拽调节步长',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdSlider(step=20, min=-100, max=100,
                                               marks={
                                                   -50: '点1',
                                                   0: '点2',
                                                   50: '点3'
                                               })
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义部分刻度显示内容',
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
html.Div(
    [
        fac.AntdSlider(step=20, min=-100, max=100,
                       marks={
                           -50: '点1',
                           0: '点2',
                           50: '点3'
                       })
    ],
    style={
        'width': '400px'
    }
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
                    id='自定义部分刻度显示内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdSlider(tooltipVisible=True, min=-100, max=100),
                                fac.AntdSlider(tooltipVisible=False, range=True, min=-100, max=100)
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '设置数值提示框显示策略',
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
html.Div(
    [
        fac.AntdSlider(tooltipVisible=True, min=-100, max=100),
        fac.AntdSlider(tooltipVisible=False, range=True, min=-100, max=100)
    ],
    style={
        'width': '400px'
    }
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
                    id='设置数值提示框显示策略',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdSlider(tooltipPrefix='指标值：', min=-100, max=100),
                                fac.AntdSlider(tooltipSuffix='°C', range=True, min=-100, max=100)
                            ],
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(
                            '设置数值提示框前后缀文字',
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
html.Div(
    [
        fac.AntdSlider(tooltipPrefix='指标值：', min=-100, max=100),
        fac.AntdSlider(tooltipSuffix='°C', range=True, min=-100, max=100)
    ],
    style={
        'width': '400px'
    }
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
                    id='设置数值提示框前后缀文字',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdSlider(id='slider-demo-1', min=-100, max=100),
                                fac.AntdSlider(id='slider-demo-2', range=True, min=-100, max=100)
                            ],
                            style={
                                'width': '400px'
                            }
                        ),
                        html.Br(),
                        fac.AntdSpin(
                            html.Em(id='slider-demo-output'),
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
html.Div(
    [
        fac.AntdSlider(id='slider-demo-1', min=-100, max=100),
        fac.AntdSlider(id='slider-demo-2', range=True, min=-100, max=100)
    ],
    style={
        'width': '400px'
    }
),
html.Br(),
html.Em(id='slider-demo-output')
...
@app.callback(
    Output('slider-demo-output', 'children'),
    [Input('slider-demo-1', 'value'),
     Input('slider-demo-2', 'value')]
)
def transfer_callback_demo(value, range_value):
    return f'单值选择当前值：{value}   范围选择当前值：{range_value}'''
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
                            {'title': '设置默认值', 'href': '#设置默认值'},
                            {'title': '设置用户拖拽调节步长', 'href': '#设置用户拖拽调节步长'},
                            {'title': '自定义部分刻度显示内容', 'href': '#自定义部分刻度显示内容'},
                            {'title': '设置数值提示框显示策略', 'href': '#设置数值提示框显示策略'},
                            {'title': '设置数值提示框前后缀文字', 'href': '#设置数值提示框前后缀文字'},
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
