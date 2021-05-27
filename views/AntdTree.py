import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdTree

docs_content = html.Div(
    [
        html.H2(
            'AntdTree(id, className, style, *args, **kwargs)',
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
                        {'title': '基础的树形控件', 'href': '#基础的树形控件'},
                        {'title': '可勾选的树形控件', 'href': '#可勾选的树形控件'},
                        {'title': '可点击多选的树形控件', 'href': '#可点击多选的树形控件'},
                        {'title': '为节点自定义前缀图标', 'href': '#为节点自定义前缀图标'},
                        {'title': '关闭节点连接线', 'href': '#关闭节点连接线'},
                        {'title': '大数据量时限制最大显示高度提升性能', 'href': '#大数据量时限制最大显示高度提升性能'},
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

        dcc.Markdown(open('documents/AntdTree.md', encoding='utf-8').read(),
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
                    '基础的树形控件：',
                    id='基础的树形控件',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区',
                                    'disabled': True
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                )
                ```
                '''),

                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区',
                                    'disabled': True
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '可勾选的树形控件：',
                    id='可勾选的树形控件',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区'
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    checkable=True
                )
                ```
                '''),

                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区'
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    checkable=True
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '可点击多选的树形控件：',
                    id='可点击多选的树形控件',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区'
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    multiple=True
                )
                ```
                '''),

                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区'
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    multiple=True
                ),
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '为节点自定义前缀图标：',
                    id='为节点自定义前缀图标',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTree(
                    treeData=[
                        {
                            'title': '负责人A',
                            'key': '负责人A',
                            'icon_name': 'user',
                            'children': [
                                {
                                    'title': '数仓1',
                                    'key': '数仓1',
                                    'icon_name': 'database',
                                    'children': [
                                        {
                                            'title': f'业务表1-{i}',
                                            'key': f'业务表1-{i}',
                                            'icon_name': 'table'
                                        }
                                        for i in range(5)
                                    ]
                                },
                                {
                                    'title': '数仓2',
                                    'key': '数仓2',
                                    'icon_name': 'database',
                                    'children': [
                                        {
                                            'title': f'业务表2-{i}',
                                            'key': f'业务表2-{i}',
                                            'icon_name': 'table'
                                        }
                                        for i in range(5)
                                    ]
                                }
                            ]
                        }
                    ],
                    # 设置默认全部展开
                    defaultExpandAll=True,
                    checkable=True
                )
                ```
                '''),

                fac.AntdTree(
                    treeData=[
                        {
                            'title': '负责人A',
                            'key': '负责人A',
                            'icon_name': 'user',
                            'children': [
                                {
                                    'title': '数仓1',
                                    'key': '数仓1',
                                    'icon_name': 'database',
                                    'children': [
                                        {
                                            'title': f'业务表1-{i}',
                                            'key': f'业务表1-{i}',
                                            'icon_name': 'table'
                                        }
                                        for i in range(5)
                                    ]
                                },
                                {
                                    'title': '数仓2',
                                    'key': '数仓2',
                                    'icon_name': 'database',
                                    'children': [
                                        {
                                            'title': f'业务表2-{i}',
                                            'key': f'业务表2-{i}',
                                            'icon_name': 'table'
                                        }
                                        for i in range(5)
                                    ]
                                }
                            ]
                        }
                    ],
                    # 设置默认全部展开
                    defaultExpandAll=True,
                    checkable=True
                ),
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '关闭节点连接线：',
                    id='关闭节点连接线',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区'
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    multiple=True,
                    showLine=False,
                    defaultExpandAll=True
                )
                ```
                '''),

                fac.AntdTree(
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区'
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    multiple=True,
                    showLine=False,
                    defaultExpandAll=True
                ),
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '大数据量时限制最大显示高度提升性能：',
                    id='大数据量时限制最大显示高度提升性能',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdTree(
                    treeData=[
                        {
                            'title': f'数仓{i}',
                            'key': f'数仓{i}',
                            'icon_name': 'database',
                            'children': [
                                {
                                    'title': f'业务表{i}-{j}',
                                    'key': f'业务表{i}-{j}',
                                    'icon_name': 'table'
                                }
                                for j in range(10)
                            ]
                        }
                        for i in range(100)
                    ],
                    defaultExpandAll=True,
                    height=500,
                    style={
                        'border': '2px dashed #757575'
                    }
                )
                ```
                '''),

                fac.AntdTree(
                    treeData=[
                        {
                            'title': f'数仓{i}',
                            'key': f'数仓{i}',
                            'icon_name': 'database',
                            'children': [
                                {
                                    'title': f'业务表{i}-{j}',
                                    'key': f'业务表{i}-{j}',
                                    'icon_name': 'table'
                                }
                                for j in range(10)
                            ]
                        }
                        for i in range(100)
                    ],
                    defaultExpandAll=True,
                    height=500,
                    style={
                        'border': '2px dashed #757575'
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
                html.Em('[]', id='tree-demo-output1'),
                html.Br(),
                html.Em('[]', id='tree-demo-output2'),

                fac.AntdTree(
                    id='tree-demo',
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区',
                                    'disabled': True
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    multiple=True,
                    checkable=True
                )
                ...
                @app.callback(
                    [Output('tree-demo-output1', 'children'),
                    Output('tree-demo-output2', 'children')],
                    [Input('tree-demo', 'selectedKeys'),
                     Input('tree-demo', 'checkedKeys')],
                    prevent_initial_call=True
                )
                def button_callback_demo(selectedKeys, checkedKeys):
                
                    return str(selectedKeys), str(checkedKeys)
                ```
                '''),

                html.Em('[]', id='tree-demo-output1'),
                html.Br(),
                html.Em('[]', id='tree-demo-output2'),

                fac.AntdTree(
                    id='tree-demo',
                    treeData=[
                        {
                            'title': '重庆市',
                            'key': '重庆市',
                            'children': [
                                {
                                    'title': '渝北区',
                                    'key': '渝北区'
                                },
                                {
                                    'title': '江北区',
                                    'key': '江北区',
                                    'disabled': True
                                }
                            ]
                        },
                        {
                            'title': '北京市',
                            'key': '北京市',
                            'children': [
                                {
                                    'title': '西城区',
                                    'key': '西城区'
                                },
                                {
                                    'title': '东城区',
                                    'key': '东城区'
                                }
                            ]
                        },
                        {
                            'title': '四川省',
                            'key': '四川省',
                            'children': [
                                {
                                    'title': '成都市',
                                    'key': '成都市',
                                    'children': [
                                        {
                                            'title': '天府新区',
                                            'key': '天府新区'
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    multiple=True,
                    checkable=True
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
