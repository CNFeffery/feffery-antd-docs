from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTreeSelect

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTreeSelect(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTreeSelect.md', encoding='utf-8').read()
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
                        fac.AntdTreeSelect(
                            treeData=[
                                {
                                    "title": "Node1",
                                    "value": "0-0",
                                    "key": "0-0",
                                    "children": [
                                        {
                                            "title": "Child Node1",
                                            "value": "0-0-0",
                                            "key": "0-0-0"
                                        }
                                    ]
                                },
                                {
                                    "title": "Node2",
                                    "value": "0-1",
                                    "key": "0-1",
                                    "children": [
                                        {
                                            "title": "Child Node3",
                                            "value": "0-1-0",
                                            "key": "0-1-0"
                                        },
                                        {
                                            "title": "Child Node4",
                                            "value": "0-1-1",
                                            "key": "0-1-1"
                                        },
                                        {
                                            "title": "Child Node5",
                                            "value": "0-1-2",
                                            "key": "0-1-2"
                                        }
                                    ]
                                }
                            ],
                            style={
                                'width': '250px'
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
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTreeSelect(
    treeData=[
        {
            "title": "Node1",
            "value": "0-0",
            "key": "0-0",
            "children": [
                {
                    "title": "Child Node1",
                    "value": "0-0-0",
                    "key": "0-0-0"
                }
            ]
        },
        {
            "title": "Node2",
            "value": "0-1",
            "key": "0-1",
            "children": [
                {
                    "title": "Child Node3",
                    "value": "0-1-0",
                    "key": "0-1-0"
                },
                {
                    "title": "Child Node4",
                    "value": "0-1-1",
                    "key": "0-1-1"
                },
                {
                    "title": "Child Node5",
                    "value": "0-1-2",
                    "key": "0-1-2"
                }
            ]
        }
    ],
    style={
        'width': '250px'
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
                        fac.AntdTreeSelect(
                            treeData=[
                                {
                                    "title": "Node1",
                                    "value": "0-0",
                                    "key": "0-0",
                                    "children": [
                                        {
                                            "title": "Child Node1",
                                            "value": "0-0-0",
                                            "key": "0-0-0"
                                        }
                                    ]
                                },
                                {
                                    "title": "Node2",
                                    "value": "0-1",
                                    "key": "0-1",
                                    "children": [
                                        {
                                            "title": "Child Node3",
                                            "value": "0-1-0",
                                            "key": "0-1-0"
                                        },
                                        {
                                            "title": "Child Node4",
                                            "value": "0-1-1",
                                            "key": "0-1-1"
                                        },
                                        {
                                            "title": "Child Node5",
                                            "value": "0-1-2",
                                            "key": "0-1-2"
                                        }
                                    ]
                                }
                            ],
                            multiple=True,
                            style={
                                'width': '250px'
                            }
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
fac.AntdTreeSelect(
    treeData=[
        {
            "title": "Node1",
            "value": "0-0",
            "key": "0-0",
            "children": [
                {
                    "title": "Child Node1",
                    "value": "0-0-0",
                    "key": "0-0-0"
                }
            ]
        },
        {
            "title": "Node2",
            "value": "0-1",
            "key": "0-1",
            "children": [
                {
                    "title": "Child Node3",
                    "value": "0-1-0",
                    "key": "0-1-0"
                },
                {
                    "title": "Child Node4",
                    "value": "0-1-1",
                    "key": "0-1-1"
                },
                {
                    "title": "Child Node5",
                    "value": "0-1-2",
                    "key": "0-1-2"
                }
            ]
        }
    ],
    multiple=True,
    style={
        'width': '250px'
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
                    id='多选模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTreeSelect(
                            treeData=[
                                {
                                    "title": "Node1",
                                    "value": "0-0",
                                    "key": "0-0",
                                    "children": [
                                        {
                                            "title": "Child Node1",
                                            "value": "0-0-0",
                                            "key": "0-0-0"
                                        }
                                    ]
                                },
                                {
                                    "title": "Node2",
                                    "value": "0-1",
                                    "key": "0-1",
                                    "children": [
                                        {
                                            "title": "Child Node3",
                                            "value": "0-1-0",
                                            "key": "0-1-0"
                                        },
                                        {
                                            "title": "Child Node4",
                                            "value": "0-1-1",
                                            "key": "0-1-1"
                                        },
                                        {
                                            "title": "Child Node5",
                                            "value": "0-1-2",
                                            "key": "0-1-2"
                                        }
                                    ]
                                }
                            ],
                            treeCheckable=True,
                            style={
                                'width': '250px'
                            }
                        ),

                        fac.AntdDivider(
                            '开启勾选框',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTreeSelect(
    treeData=[
        {
            "title": "Node1",
            "value": "0-0",
            "key": "0-0",
            "children": [
                {
                    "title": "Child Node1",
                    "value": "0-0-0",
                    "key": "0-0-0"
                }
            ]
        },
        {
            "title": "Node2",
            "value": "0-1",
            "key": "0-1",
            "children": [
                {
                    "title": "Child Node3",
                    "value": "0-1-0",
                    "key": "0-1-0"
                },
                {
                    "title": "Child Node4",
                    "value": "0-1-1",
                    "key": "0-1-1"
                },
                {
                    "title": "Child Node5",
                    "value": "0-1-2",
                    "key": "0-1-2"
                }
            ]
        }
    ],
    treeCheckable=True,
    style={
        'width': '250px'
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
                    id='开启勾选框',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTreeSelect(
                            treeData=[
                                {
                                    "title": "Node1",
                                    "value": "0-0",
                                    "key": "0-0",
                                    "children": [
                                        {
                                            "title": "Child Node1",
                                            "value": "0-0-0",
                                            "key": "0-0-0"
                                        }
                                    ]
                                },
                                {
                                    "title": "Node2",
                                    "value": "0-1",
                                    "key": "0-1",
                                    "children": [
                                        {
                                            "title": "Child Node3",
                                            "value": "0-1-0",
                                            "key": "0-1-0"
                                        },
                                        {
                                            "title": "Child Node4",
                                            "value": "0-1-1",
                                            "key": "0-1-1"
                                        },
                                        {
                                            "title": "Child Node5",
                                            "value": "0-1-2",
                                            "key": "0-1-2"
                                        }
                                    ]
                                }
                            ],
                            treeCheckable=True,
                            treeLine=True,
                            style={
                                'width': '250px'
                            }
                        ),

                        fac.AntdDivider(
                            '显示树连接线',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTreeSelect(
    treeData=[
        {
            "title": "Node1",
            "value": "0-0",
            "key": "0-0",
            "children": [
                {
                    "title": "Child Node1",
                    "value": "0-0-0",
                    "key": "0-0-0"
                }
            ]
        },
        {
            "title": "Node2",
            "value": "0-1",
            "key": "0-1",
            "children": [
                {
                    "title": "Child Node3",
                    "value": "0-1-0",
                    "key": "0-1-0"
                },
                {
                    "title": "Child Node4",
                    "value": "0-1-1",
                    "key": "0-1-1"
                },
                {
                    "title": "Child Node5",
                    "value": "0-1-2",
                    "key": "0-1-2"
                }
            ]
        }
    ],
    treeCheckable=True,
    treeLine=True,
    style={
        'width': '250px'
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
                    id='显示树连接线',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTreeSelect(
                            treeData=[
                                {
                                    "title": "Node1",
                                    "value": "0-0",
                                    "key": "0-0",
                                    "children": [
                                        {
                                            "title": f"Child Node{i + 1}",
                                            "value": f"0-0-{i}",
                                            "key": f"0-0-{i}"
                                        }
                                        for i in range(20)
                                    ]
                                },
                                {
                                    "title": "Node2",
                                    "value": "0-1",
                                    "key": "0-1",
                                    "children": [
                                        {
                                            "title": "Child Node3",
                                            "value": "0-1-0",
                                            "key": "0-1-0"
                                        },
                                        {
                                            "title": "Child Node4",
                                            "value": "0-1-1",
                                            "key": "0-1-1"
                                        },
                                        {
                                            "title": "Child Node5",
                                            "value": "0-1-2",
                                            "key": "0-1-2"
                                        }
                                    ]
                                }
                            ],
                            treeCheckable=True,
                            treeLine=True,
                            virtual=False,
                            treeDefaultExpandAll=True,
                            style={
                                'width': '250px'
                            }
                        ),

                        fac.AntdDivider(
                            '关闭虚拟滚动',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTreeSelect(
    treeData=[
        {
            "title": "Node1",
            "value": "0-0",
            "key": "0-0",
            "children": [
                {
                    "title": f"Child Node{i + 1}",
                    "value": f"0-0-{i}",
                    "key": f"0-0-{i}"
                }
                for i in range(20)
            ]
        },
        {
            "title": "Node2",
            "value": "0-1",
            "key": "0-1",
            "children": [
                {
                    "title": "Child Node3",
                    "value": "0-1-0",
                    "key": "0-1-0"
                },
                {
                    "title": "Child Node4",
                    "value": "0-1-1",
                    "key": "0-1-1"
                },
                {
                    "title": "Child Node5",
                    "value": "0-1-2",
                    "key": "0-1-2"
                }
            ]
        }
    ],
    treeCheckable=True,
    treeLine=True,
    virtual=False,
    treeDefaultExpandAll=True,
    style={
        'width': '250px'
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
                    id='关闭虚拟滚动',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            [
                                html.Div(
                                    [
                                        fac.AntdText('value：', strong=True),
                                        fac.AntdText(id='tree-select-demo-output')
                                    ]
                                ),
                                fac.AntdTreeSelect(
                                    id='tree-select-demo',
                                    treeData=[
                                        {
                                            "title": "Node1",
                                            "value": "0-0",
                                            "key": "0-0",
                                            "children": [
                                                {
                                                    "title": "Child Node1",
                                                    "value": "0-0-0",
                                                    "key": "0-0-0"
                                                }
                                            ]
                                        },
                                        {
                                            "title": "Node2",
                                            "value": "0-1",
                                            "key": "0-1",
                                            "children": [
                                                {
                                                    "title": "Child Node3",
                                                    "value": "0-1-0",
                                                    "key": "0-1-0"
                                                },
                                                {
                                                    "title": "Child Node4",
                                                    "value": "0-1-1",
                                                    "key": "0-1-1"
                                                },
                                                {
                                                    "title": "Child Node5",
                                                    "value": "0-1-2",
                                                    "key": "0-1-2"
                                                }
                                            ]
                                        }
                                    ],
                                    style={
                                        'width': '250px'
                                    }
                                )
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
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        html.Div(
            [
                fac.AntdText('value：', strong=True),
                fac.AntdText(id='tree-select-demo-output')
            ]
        ),
        fac.AntdTreeSelect(
            id='tree-select-demo',
            treeData=[
                {
                    "title": "Node1",
                    "value": "0-0",
                    "key": "0-0",
                    "children": [
                        {
                            "title": "Child Node1",
                            "value": "0-0-0",
                            "key": "0-0-0"
                        }
                    ]
                },
                {
                    "title": "Node2",
                    "value": "0-1",
                    "key": "0-1",
                    "children": [
                        {
                            "title": "Child Node3",
                            "value": "0-1-0",
                            "key": "0-1-0"
                        },
                        {
                            "title": "Child Node4",
                            "value": "0-1-1",
                            "key": "0-1-1"
                        },
                        {
                            "title": "Child Node5",
                            "value": "0-1-2",
                            "key": "0-1-2"
                        }
                    ]
                }
            ],
            style={
                'width': '250px'
            }
        )
    ],
    text='回调中'
)
...
@app.callback(
    Output('tree-select-demo-output', 'children'),
    Input('tree-select-demo', 'value')
)
def tree_select_demo_callback(value):

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
                            {'title': '开启勾选框', 'href': '#开启勾选框'},
                            {'title': '显示树连接线', 'href': '#显示树连接线'},
                            {'title': '关闭虚拟滚动', 'href': '#关闭虚拟滚动'},
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
