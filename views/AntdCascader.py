from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
import feffery_utils_components as fuc

import callbacks.AntdCascader

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCascader(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCascader.md', encoding='utf-8').read()
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
                        fac.AntdCascader(
                            placeholder='请在下列层级结构中进行选择',
                            options=[
                                {
                                    'value': '节点1',
                                    'label': '节点1',
                                    'children': [
                                        {
                                            'value': '节点1-1',
                                            'label': '节点1-1'
                                        },
                                        {
                                            'value': '节点1-2',
                                            'label': '节点1-2',
                                            'children': [
                                                {
                                                    'value': '节点1-2-1',
                                                    'label': '节点1-2-1'
                                                },
                                                {
                                                    'value': '节点1-2-2',
                                                    'label': '节点1-2-2'
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    'value': '节点2',
                                    'label': '节点2',
                                    'children': [
                                        {
                                            'value': '节点2-1',
                                            'label': '节点2-1'
                                        },
                                        {
                                            'value': '节点2-2',
                                            'label': '节点2-2'
                                        }
                                    ]
                                }
                            ],
                            style={
                                'width': '300px'
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　默认参数下，'),
                                fac.AntdText('AntdCascader', strong=True),
                                fac.AntdText('以单选的模式，供用户进行末端叶节点的选择')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdCascader(
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    style={
        'width': '300px'
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
                        fac.AntdSpace(
                            [
                                fac.AntdCascader(
                                    placeholder='placement="bottomRight"',
                                    options=[
                                        {
                                            'value': '节点1',
                                            'label': '节点1',
                                            'children': [
                                                {
                                                    'value': '节点1-1',
                                                    'label': '节点1-1'
                                                },
                                                {
                                                    'value': '节点1-2',
                                                    'label': '节点1-2',
                                                    'children': [
                                                        {
                                                            'value': '节点1-2-1',
                                                            'label': '节点1-2-1'
                                                        },
                                                        {
                                                            'value': '节点1-2-2',
                                                            'label': '节点1-2-2'
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ],
                                    placement='bottomRight',
                                    style={
                                        'width': '300px'
                                    }
                                ),
                                fac.AntdCascader(
                                    placeholder='placement="topLeft"',
                                    options=[
                                        {
                                            'value': '节点1',
                                            'label': '节点1',
                                            'children': [
                                                {
                                                    'value': '节点1-1',
                                                    'label': '节点1-1'
                                                },
                                                {
                                                    'value': '节点1-2',
                                                    'label': '节点1-2',
                                                    'children': [
                                                        {
                                                            'value': '节点1-2-1',
                                                            'label': '节点1-2-1'
                                                        },
                                                        {
                                                            'value': '节点1-2-2',
                                                            'label': '节点1-2-2'
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ],
                                    placement='topLeft',
                                    style={
                                        'width': '300px'
                                    }
                                ),
                                fac.AntdCascader(
                                    placeholder='placement="topRight"',
                                    options=[
                                        {
                                            'value': '节点1',
                                            'label': '节点1',
                                            'children': [
                                                {
                                                    'value': '节点1-1',
                                                    'label': '节点1-1'
                                                },
                                                {
                                                    'value': '节点1-2',
                                                    'label': '节点1-2',
                                                    'children': [
                                                        {
                                                            'value': '节点1-2-1',
                                                            'label': '节点1-2-1'
                                                        },
                                                        {
                                                            'value': '节点1-2-2',
                                                            'label': '节点1-2-2'
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ],
                                    placement='topRight',
                                    style={
                                        'width': '300px'
                                    }
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的悬浮层展开方位',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdCascader(
            placeholder='placement="bottomRight"',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                }
            ],
            placement='bottomRight',
            style={
                'width': '300px'
            }
        ),
        fac.AntdCascader(
            placeholder='placement="topLeft"',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                }
            ],
            placement='topLeft',
            style={
                'width': '300px'
            }
        ),
        fac.AntdCascader(
            placeholder='placement="topRight"',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                }
            ],
            placement='topRight',
            style={
                'width': '300px'
            }
        )
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
                    id='不同的悬浮层展开方位',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCascader(
                            placeholder='请在下列层级结构中进行选择',
                            options=[
                                {
                                    'value': '节点1',
                                    'label': '节点1',
                                    'children': [
                                        {
                                            'value': '节点1-1',
                                            'label': '节点1-1'
                                        },
                                        {
                                            'value': '节点1-2',
                                            'label': '节点1-2',
                                            'children': [
                                                {
                                                    'value': '节点1-2-1',
                                                    'label': '节点1-2-1'
                                                },
                                                {
                                                    'value': '节点1-2-2',
                                                    'label': '节点1-2-2'
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ],
                            expandTrigger='hover',
                            style={
                                'width': '300px'
                            }
                        ),

                        fac.AntdDivider(
                            '鼠标悬浮触发展开子菜单',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdCascader(
    placeholder='请在下列层级结构中进行选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        }
    ],
    expandTrigger='hover',
    style={
        'width': '300px'
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
                    id='鼠标悬浮触发展开子菜单',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCascader(
                            placeholder='多选模式：',
                            options=[
                                {
                                    'value': '节点1',
                                    'label': '节点1',
                                    'children': [
                                        {
                                            'value': '节点1-1',
                                            'label': '节点1-1'
                                        },
                                        {
                                            'value': '节点1-2',
                                            'label': '节点1-2',
                                            'children': [
                                                {
                                                    'value': '节点1-2-1',
                                                    'label': '节点1-2-1'
                                                },
                                                {
                                                    'value': '节点1-2-2',
                                                    'label': '节点1-2-2'
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    'value': '节点2',
                                    'label': '节点2',
                                    'children': [
                                        {
                                            'value': '节点2-1',
                                            'label': '节点2-1'
                                        },
                                        {
                                            'value': '节点2-2',
                                            'label': '节点2-2'
                                        }
                                    ]
                                }
                            ],
                            multiple=True,
                            style={
                                'width': '300px'
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
fac.AntdCascader(
    placeholder='多选模式：',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    multiple=True,
    style={
        'width': '300px'
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
                        fac.AntdSpin(
                            fac.AntdSpace(
                                [
                                    html.Div(
                                        [
                                            fac.AntdText('单选value：', strong=True),
                                            fac.AntdText(id='cascader-demo-output')
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            fac.AntdText('多选value：', strong=True),
                                            fac.AntdText(id='cascader-multiple-demo-output')
                                        ]
                                    ),
                                    fac.AntdCascader(
                                        id='cascader-demo',
                                        placeholder='单选回调示例：',
                                        options=[
                                            {
                                                'value': '节点1',
                                                'label': '节点1',
                                                'children': [
                                                    {
                                                        'value': '节点1-1',
                                                        'label': '节点1-1'
                                                    },
                                                    {
                                                        'value': '节点1-2',
                                                        'label': '节点1-2',
                                                        'children': [
                                                            {
                                                                'value': '节点1-2-1',
                                                                'label': '节点1-2-1'
                                                            },
                                                            {
                                                                'value': '节点1-2-2',
                                                                'label': '节点1-2-2'
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'value': '节点2',
                                                'label': '节点2',
                                                'children': [
                                                    {
                                                        'value': '节点2-1',
                                                        'label': '节点2-1'
                                                    },
                                                    {
                                                        'value': '节点2-2',
                                                        'label': '节点2-2'
                                                    }
                                                ]
                                            }
                                        ],
                                        style={
                                            'width': '300px'
                                        }
                                    ),
                                    fac.AntdCascader(
                                        id='cascader-multiple-demo',
                                        placeholder='多选回调示例：',
                                        options=[
                                            {
                                                'value': '节点1',
                                                'label': '节点1',
                                                'children': [
                                                    {
                                                        'value': '节点1-1',
                                                        'label': '节点1-1'
                                                    },
                                                    {
                                                        'value': '节点1-2',
                                                        'label': '节点1-2',
                                                        'children': [
                                                            {
                                                                'value': '节点1-2-1',
                                                                'label': '节点1-2-1'
                                                            },
                                                            {
                                                                'value': '节点1-2-2',
                                                                'label': '节点1-2-2'
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'value': '节点2',
                                                'label': '节点2',
                                                'children': [
                                                    {
                                                        'value': '节点2-1',
                                                        'label': '节点2-1'
                                                    },
                                                    {
                                                        'value': '节点2-2',
                                                        'label': '节点2-2'
                                                    }
                                                ]
                                            }
                                        ],
                                        multiple=True,
                                        style={
                                            'width': '300px'
                                        }
                                    )
                                ],
                                direction='vertical'
                            ),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdCascader', strong=True),
                                fac.AntdText('已选择的值会在value中以层级选择路径对应值列表的形式进行记录，当满足后代节点被全选时则会仅记录对应的祖先节点值')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    fac.AntdSpace(
        [
            html.Div(
                [
                    fac.AntdText('单选value：', strong=True),
                    fac.AntdText(id='cascader-demo-output')
                ]
            ),
            html.Div(
                [
                    fac.AntdText('多选value：', strong=True),
                    fac.AntdText(id='cascader-multiple-demo-output')
                ]
            ),
            fac.AntdCascader(
                id='cascader-demo',
                placeholder='单选回调示例：',
                options=[
                    {
                        'value': '节点1',
                        'label': '节点1',
                        'children': [
                            {
                                'value': '节点1-1',
                                'label': '节点1-1'
                            },
                            {
                                'value': '节点1-2',
                                'label': '节点1-2',
                                'children': [
                                    {
                                        'value': '节点1-2-1',
                                        'label': '节点1-2-1'
                                    },
                                    {
                                        'value': '节点1-2-2',
                                        'label': '节点1-2-2'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'value': '节点2',
                        'label': '节点2',
                        'children': [
                            {
                                'value': '节点2-1',
                                'label': '节点2-1'
                            },
                            {
                                'value': '节点2-2',
                                'label': '节点2-2'
                            }
                        ]
                    }
                ],
                style={
                    'width': '300px'
                }
            ),
            fac.AntdCascader(
                id='cascader-multiple-demo',
                placeholder='多选回调示例：',
                options=[
                    {
                        'value': '节点1',
                        'label': '节点1',
                        'children': [
                            {
                                'value': '节点1-1',
                                'label': '节点1-1'
                            },
                            {
                                'value': '节点1-2',
                                'label': '节点1-2',
                                'children': [
                                    {
                                        'value': '节点1-2-1',
                                        'label': '节点1-2-1'
                                    },
                                    {
                                        'value': '节点1-2-2',
                                        'label': '节点1-2-2'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'value': '节点2',
                        'label': '节点2',
                        'children': [
                            {
                                'value': '节点2-1',
                                'label': '节点2-1'
                            },
                            {
                                'value': '节点2-2',
                                'label': '节点2-2'
                            }
                        ]
                    }
                ],
                multiple=True,
                style={
                    'width': '300px'
                }
            )
        ],
        direction='vertical'
    ),
    text='回调中'
)
...
@app.callback(
    Output('cascader-demo-output', 'children'),
    Input('cascader-demo', 'value')
)
def cascader_demo_callback(value):

    return str(value)


@app.callback(
    Output('cascader-multiple-demo-output', 'children'),
    Input('cascader-multiple-demo', 'value')
)
def cascader_multiple_demo_callback(value):

    return str(value)'''
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
                            {'title': '不同的悬浮层展开方位', 'href': '#不同的悬浮层展开方位'},
                            {'title': '鼠标悬浮触发展开子菜单', 'href': '#鼠标悬浮触发展开子菜单'},
                            {'title': '多选模式', 'href': '#多选模式'},
                            {'title': '回调示例', 'href': '#回调示例'}
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
