import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdSlider

docs_content = html.Div(
    [
        html.H2(
            'AntdSlider(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

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
            ]
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

        dcc.Markdown(open('documents/AntdSlider.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
            id='使用示例',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        html.Hr(),

        html.Div(
            [
                html.Strong(
                    '基础使用：',
                    id='基础使用',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdSlider(min=-100, max=100),
                        fac.AntdSlider(range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdSlider(min=-100, max=100),
                        fac.AntdSlider(range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置默认值：',
                    id='设置默认值',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdSlider(defaultValue=66, min=-100, max=100),
                        fac.AntdSlider(defaultValue=[-10, 66], range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdSlider(defaultValue=66, min=-100, max=100),
                        fac.AntdSlider(defaultValue=[-10, 66], range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置用户拖拽调节步长：',
                    id='设置用户拖拽调节步长',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdSlider(step=20, min=-100, max=100),
                        fac.AntdSlider(step=0.1, range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdSlider(step=20, min=-100, max=100),
                        fac.AntdSlider(step=0.1, range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '自定义部分刻度显示内容：',
                    id='自定义部分刻度显示内容',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                )
                ```
                '''),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置数值提示框显示策略：',
                    id='设置数值提示框显示策略',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdSlider(tooltipVisible=True, min=-100, max=100),
                        fac.AntdSlider(tooltipVisible=False, range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdSlider(tooltipVisible=True, min=-100, max=100),
                        fac.AntdSlider(tooltipVisible=False, range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置数值提示框前后缀文字：',
                    id='设置数值提示框前后缀文字',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                html.Div(
                    [
                        fac.AntdSlider(tooltipVisible=True, min=-100, max=100),
                        fac.AntdSlider(tooltipVisible=False, range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                )
                ```
                '''),

                html.Div(
                    [
                        fac.AntdSlider(tooltipPrefix='指标值：', min=-100, max=100),
                        fac.AntdSlider(tooltipSuffix='°C', range=True, min=-100, max=100)
                    ],
                    style={
                        'width': '400px'
                    }
                ),

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '回调示例：',
                    id='回调示例',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                     Input('slider-demo-2', 'value')],
                    prevent_initial_call=True
                )
                def transfer_callback_demo(value, range_value):
                    return f'单值选择当前值：{value}   范围选择当前值：{range_value}'

                ```
                '''),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
