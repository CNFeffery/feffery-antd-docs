import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdSelect

docs_content = html.Div(
    [
        html.H2(
            'AntdSelect(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        html.Span(
            '主要参数说明：',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdSelect.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
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
                html.Strong('基础的下拉选择：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国', 'disabled': True},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国', 'disabled': True},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('分组下拉选择：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {
                            'group': '亚洲',
                            'options': [
                                {'label': '中国', 'value': '中国'}
                            ]
                        },
                        {
                            'group': '北美洲',
                            'options': [
                                {'label': '美国', 'value': '美国'},
                                {'label': '加拿大', 'value': '加拿大'}
                            ]
                        },
                        {
                            'group': '欧洲',
                            'options': [
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国', 'disabled': True}
                            ]
                        }
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {
                            'group': '亚洲',
                            'options': [
                                {'label': '中国', 'value': '中国'}
                            ]
                        },
                        {
                            'group': '北美洲',
                            'options': [
                                {'label': '美国', 'value': '美国'},
                                {'label': '加拿大', 'value': '加拿大'}
                            ]
                        },
                        {
                            'group': '欧洲',
                            'options': [
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国', 'disabled': True}
                            ]
                        }
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('多选与自由新增模式：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择国家（多选）：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国'},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    mode='multiple',
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                ),

                # 自由新增模式下，输入框内即使输入不存在的选项
                # 按下enter之后也会被添加到已选择
                fac.AntdSelect(
                    placeholder='请选择国家（自由新增）：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国'},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    mode='tags',
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择国家（多选）：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国'},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    mode='multiple',
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                ),

                # 自由新增模式下，输入框内即使输入不存在的选项
                # 按下enter之后也会被添加到已选择
                fac.AntdSelect(
                    placeholder='请选择国家（自由新增）：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国'},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    mode='tags',
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('设置默认选中值：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '项目1', 'value': 1},
                        {'label': '项目2', 'value': 2},
                        {'label': '项目3', 'value': 3}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择国家：',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国'},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    defaultValue=['中国', '美国'],
                    mode='multiple',
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('修改下拉选择最大高度：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择项目：',
                    options=[
                        {'label': f'项目{i}', 'value': f'项目{i}'}
                        for i in range(200)
                    ],
                    mode='multiple',
                    listHeight=500,
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择项目：',
                    options=[
                        {'label': f'项目{i}', 'value': f'项目{i}'}
                        for i in range(200)
                    ],
                    mode='multiple',
                    listHeight=500,
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('设置输入框已选择选项最大显示数量：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                fac.AntdSelect(
                    placeholder='请选择项目：',
                    options=[
                        {'label': f'项目{i}', 'value': f'项目{i}'}
                        for i in range(200)
                    ],
                    mode='multiple',
                    listHeight=500,
                    maxTagCount=3, # 设置最大显示3个
                    style={
                        # 使用css样式固定宽度
                        'width': '350px'
                    }
                )
                ```
                '''),

                fac.AntdSelect(
                    placeholder='请选择项目：',
                    options=[
                        {'label': f'项目{i}', 'value': f'项目{i}'}
                        for i in range(200)
                    ],
                    mode='multiple',
                    listHeight=500,
                    maxTagCount=3,  # 设置最大显示3个
                    style={
                        # 使用css样式固定宽度
                        'width': '350px'
                    }
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong('回调示例：', style={'paddingTop': '5px'}),

                dcc.Markdown('''
                ```Python
                html.Pre('[]', id='select-demo-output'),
                fac.AntdSelect(
                    id='select-demo',
                    placeholder='请选择国家：',
                    mode='multiple',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国', 'disabled': True},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )
                ...
                @app.callback(
                    Output('select-demo-output', 'children'),
                    Input('select-demo', 'value'),
                    prevent_initial_call=True
                )
                def button_callback_demo(value):
                
                    return str(value)
                ```
                '''),

                html.Pre('[]', id='select-demo-output'),
                fac.AntdSelect(
                    id='select-demo',
                    placeholder='请选择国家：',
                    mode='multiple',
                    options=[
                        {'label': '中国', 'value': '中国'},
                        {'label': '美国', 'value': '美国'},
                        {'label': '俄罗斯', 'value': '俄罗斯'},
                        {'label': '德国', 'value': '德国', 'disabled': True},
                        {'label': '加拿大', 'value': '加拿大'}
                    ],
                    style={
                        # 使用css样式固定宽度
                        'width': '200px'
                    }
                )

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
