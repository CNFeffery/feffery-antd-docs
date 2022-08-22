from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTree

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTree(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTree.md', encoding='utf-8').read()
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
                        ),

                        fac.AntdDivider(
                            '基础的树形控件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
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
                    id='基础的树形控件',
                    className='div-highlight'
                ),

                html.Div(
                    [
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
                        ),

                        fac.AntdDivider(
                            '可勾选的树形控件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
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
                    id='可勾选的树形控件',
                    className='div-highlight'
                ),

                html.Div(
                    [
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

                        fac.AntdDivider(
                            '可点击多选的树形控件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
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
                    id='可点击多选的树形控件',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': '负责人A',
                                    'key': '负责人A',
                                    'icon': 'antd-user',
                                    'children': [
                                        {
                                            'title': '数仓1',
                                            'key': '数仓1',
                                            'icon': 'antd-database',
                                            'children': [
                                                {
                                                    'title': f'业务表1-{i}',
                                                    'key': f'业务表1-{i}',
                                                    'icon': 'antd-table'
                                                }
                                                for i in range(5)
                                            ]
                                        },
                                        {
                                            'title': '数仓2',
                                            'key': '数仓2',
                                            'icon': 'antd-database',
                                            'children': [
                                                {
                                                    'title': f'业务表2-{i}',
                                                    'key': f'业务表2-{i}',
                                                    'icon': 'antd-table'
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

                        fac.AntdDivider(
                            '为节点自定义前缀图标',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTree(
    treeData=[
        {
            'title': '负责人A',
            'key': '负责人A',
            'icon': 'antd-user',
            'children': [
                {
                    'title': '数仓1',
                    'key': '数仓1',
                    'icon': 'antd-database',
                    'children': [
                        {
                            'title': f'业务表1-{i}',
                            'key': f'业务表1-{i}',
                            'icon': 'antd-table'
                        }
                        for i in range(5)
                    ]
                },
                {
                    'title': '数仓2',
                    'key': '数仓2',
                    'icon': 'antd-database',
                    'children': [
                        {
                            'title': f'业务表2-{i}',
                            'key': f'业务表2-{i}',
                            'icon': 'antd-table'
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
                    id='为节点自定义前缀图标',
                    className='div-highlight'
                ),

                html.Div(
                    [
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

                        fac.AntdDivider(
                            '关闭节点连接线',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
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
                    id='关闭节点连接线',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTree(
                            treeData=[
                                {
                                    'title': f'数仓{i}',
                                    'key': f'数仓{i}',
                                    'icon': 'antd-database',
                                    'children': [
                                        {
                                            'title': f'业务表{i}-{j}',
                                            'key': f'业务表{i}-{j}',
                                            'icon': 'antd-table'
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

                        fac.AntdDivider(
                            '大数据量时限制最大显示高度提升性能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTree(
    treeData=[
        {
            'title': f'数仓{i}',
            'key': f'数仓{i}',
            'icon': 'antd-database',
            'children': [
                {
                    'title': f'业务表{i}-{j}',
                    'key': f'业务表{i}-{j}',
                    'icon': 'antd-table'
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
                    id='大数据量时限制最大显示高度提升性能',
                    className='div-highlight'
                ),

                html.Div(
                    [
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
                            checkable=True,
                            selectable=False,
                            checkStrictly=True,
                            defaultExpandAll=True
                        ),

                        fac.AntdDivider(
                            '设置先辈节点与后代节点勾选行为彼此独立',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　设置'),
                                fac.AntdText('checkStrictly=True', code=True),
                                fac.AntdText('时，可令先辈节点与后代节点之间的选择行为彼此独立')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
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
    checkable=True,
    selectable=False,
    checkStrictly=True,
    defaultExpandAll=True
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
                    id='设置先辈节点与后代节点勾选行为彼此独立',
                    className='div-highlight'
                ),

                html.Div(
                    [
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
                        ),

                        fac.AntdSpin(
                            html.Div(id='tree-demo-output'),
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
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
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
),

fac.AntdSpin(
    html.Div(id='tree-demo-output'),
    text='回调中'
)
...
@app.callback(
    Output('tree-demo-output', 'children'),
    [Input('tree-demo', 'selectedKeys'),
     Input('tree-demo', 'checkedKeys'),
     Input('tree-demo', 'halfCheckedKeys')],
    prevent_initial_call=True
)
def tree_callback_demo(selectedKeys, checkedKeys, halfCheckedKeys):
    return [
        fac.AntdTitle('selectedKeys：', level=5),
        html.Pre(str(selectedKeys)),

        fac.AntdTitle('checkedKeys：', level=5),
        html.Pre(str(checkedKeys)),

        fac.AntdTitle('halfCheckedKeys：', level=5),
        html.Pre(str(halfCheckedKeys))
    ]'''
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
                            {'title': '基础的树形控件', 'href': '#基础的树形控件'},
                            {'title': '可勾选的树形控件', 'href': '#可勾选的树形控件'},
                            {'title': '可点击多选的树形控件', 'href': '#可点击多选的树形控件'},
                            {'title': '为节点自定义前缀图标', 'href': '#为节点自定义前缀图标'},
                            {'title': '关闭节点连接线', 'href': '#关闭节点连接线'},
                            {'title': '大数据量时限制最大显示高度提升性能', 'href': '#大数据量时限制最大显示高度提升性能'},
                            {'title': '设置先辈节点与后代节点勾选行为彼此独立', 'href': '#设置先辈节点与后代节点勾选行为彼此独立'},
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
