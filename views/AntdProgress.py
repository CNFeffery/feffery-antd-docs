from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdProgress(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdProgress.md', encoding='utf-8').read()
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
                        fac.AntdDivider('type="line"（默认）', innerTextOrientation='left'),
                        fac.AntdProgress(percent=80, style={'width': '200px'}),
                        fac.AntdDivider('type="circle"', innerTextOrientation='left'),
                        fac.AntdProgress(percent=80, type='circle'),
                        fac.AntdDivider('type="dashboard"', innerTextOrientation='left'),
                        fac.AntdProgress(percent=80, type='dashboard'),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　基础的3种进度条类型')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('type="line"（默认）', innerTextOrientation='left'),
fac.AntdProgress(percent=80, style={'width': '200px'}),
fac.AntdDivider('type="circle"', innerTextOrientation='left'),
fac.AntdProgress(percent=80, type='circle'),
fac.AntdDivider('type="dashboard"', innerTextOrientation='left'),
fac.AntdProgress(percent=80, type='dashboard')
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
                        fac.AntdProgress(percent=100, style={'width': '200px'}),
                        html.Br(),
                        fac.AntdProgress(percent=100, type='circle'),
                        html.Br(),
                        fac.AntdProgress(percent=100, type='dashboard'),

                        fac.AntdDivider(
                            'percent达到100时的状态',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　基础的3种进度条类型')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdProgress(percent=100, style={'width': '200px'}),
html.Br(),
fac.AntdProgress(percent=100, type='circle'),
html.Br(),
fac.AntdProgress(percent=100, type='dashboard')
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
                    id='percent达到100时的状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdProgress(
                            percent=100,
                            format={
                                'prefix': '结果：',
                                'suffix': '分'
                            },
                            style={
                                'width': '200px'
                            }
                        ),
                        html.Br(),
                        fac.AntdProgress(
                            percent=60,
                            format={
                                'content': '及格'
                            },
                            type='circle'
                        ),
                        html.Br(),
                        fac.AntdProgress(
                            percent=30,
                            format={
                                'content': '不及格'
                            },
                            type='dashboard'
                        ),

                        fac.AntdDivider(
                            '自定义百分比数值内容',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdProgress(
    percent=100,
    format={
        'prefix': '结果：',
        'suffix': '分'
    },
    style={
        'width': '200px'
    }
),
html.Br(),
fac.AntdProgress(
    percent=60,
    format={
        'content': '及格'
    },
    type='circle'
),
html.Br(),
fac.AntdProgress(
    percent=30,
    format={
        'content': '不及格'
    },
    type='dashboard'
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
                    id='自定义百分比数值内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    [
                                        fac.AntdDivider('status="success"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='success',
                                            style={
                                                'width': '200px'
                                            }
                                        ),
                                        fac.AntdDivider('status="exception"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='exception',
                                            style={
                                                'width': '200px'
                                            }
                                        ),
                                        fac.AntdDivider('status="normal"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='normal',
                                            style={
                                                'width': '200px'
                                            }
                                        ),
                                        fac.AntdDivider('status="active"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='active',
                                            style={
                                                'width': '200px'
                                            }
                                        )
                                    ],
                                    tab='线型进度条',
                                    key='线型进度条'
                                ),
                                fac.AntdTabPane(
                                    [
                                        fac.AntdDivider('status="success"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='success',
                                            type='circle'
                                        ),
                                        fac.AntdDivider('status="exception"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='exception',
                                            type='circle'
                                        ),
                                        fac.AntdDivider('status="normal"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='normal',
                                            type='circle'
                                        )
                                    ],
                                    tab='环形进度条',
                                    key='环形进度条'
                                ),
                                fac.AntdTabPane(
                                    [
                                        fac.AntdDivider('status="success"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='success',
                                            type='dashboard'
                                        ),
                                        fac.AntdDivider('status="exception"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='exception',
                                            type='dashboard'
                                        ),
                                        fac.AntdDivider('status="normal"', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            status='normal',
                                            type='dashboard'
                                        )
                                    ],
                                    tab='仪表盘进度条',
                                    key='仪表盘进度条'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的自定义状态',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTabs(
    [
        fac.AntdTabPane(
            [
                fac.AntdDivider('status="success"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='success',
                    style={
                        'width': '200px'
                    }
                ),
                fac.AntdDivider('status="exception"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='exception',
                    style={
                        'width': '200px'
                    }
                ),
                fac.AntdDivider('status="normal"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='normal',
                    style={
                        'width': '200px'
                    }
                ),
                fac.AntdDivider('status="active"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='active',
                    style={
                        'width': '200px'
                    }
                )
            ],
            tab='线型进度条',
            key='线型进度条'
        ),
        fac.AntdTabPane(
            [
                fac.AntdDivider('status="success"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='success',
                    type='circle'
                ),
                fac.AntdDivider('status="exception"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='exception',
                    type='circle'
                ),
                fac.AntdDivider('status="normal"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='normal',
                    type='circle'
                )
            ],
            tab='环形进度条',
            key='环形进度条'
        ),
        fac.AntdTabPane(
            [
                fac.AntdDivider('status="success"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='success',
                    type='dashboard'
                ),
                fac.AntdDivider('status="exception"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='exception',
                    type='dashboard'
                ),
                fac.AntdDivider('status="normal"', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    status='normal',
                    type='dashboard'
                )
            ],
            tab='仪表盘进度条',
            key='仪表盘进度条'
        )
    ]
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
                    id='不同的自定义状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdProgress(
                            percent=100,
                            showInfo=False,
                            style={
                                'width': '200px'
                            }
                        ),
                        html.Br(),
                        fac.AntdProgress(
                            percent=60,
                            showInfo=False,
                            type='circle'
                        ),
                        html.Br(),
                        fac.AntdProgress(
                            percent=30,
                            showInfo=False,
                            type='dashboard'
                        ),

                        fac.AntdDivider(
                            '关闭额外说明内容',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdProgress(
    percent=100,
    showInfo=False,
    style={
        'width': '200px'
    }
),
html.Br(),
fac.AntdProgress(
    percent=60,
    showInfo=False,
    type='circle'
),
html.Br(),
fac.AntdProgress(
    percent=30,
    showInfo=False,
    type='dashboard'
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
                    id='关闭额外说明内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    [
                                        fac.AntdDivider('单一色彩', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            strokeColor='#2e62cd',
                                            style={
                                                'width': '200px'
                                            }
                                        ),
                                        fac.AntdDivider('渐变色彩', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            strokeColor={
                                                'from': '#00F5A0',
                                                'to': '#00D9F5'
                                            },
                                            style={
                                                'width': '200px'
                                            }
                                        )
                                    ],
                                    tab='线型进度条',
                                    key='线型进度条'
                                ),
                                fac.AntdTabPane(
                                    [
                                        fac.AntdDivider('单一色彩', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            strokeColor='#2e62cd',
                                            type='circle'
                                        ),
                                        fac.AntdDivider('渐变色彩', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            strokeColor={
                                                'from': '#00F5A0',
                                                'to': '#00D9F5'
                                            },
                                            type='circle'
                                        )
                                    ],
                                    tab='环形进度条',
                                    key='环形进度条'
                                ),
                                fac.AntdTabPane(
                                    [
                                        fac.AntdDivider('单一色彩', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            strokeColor='#2e62cd',
                                            type='dashboard'
                                        ),
                                        fac.AntdDivider('渐变色彩', innerTextOrientation='left'),
                                        fac.AntdProgress(
                                            percent=80,
                                            strokeColor={
                                                'from': '#00F5A0',
                                                'to': '#00D9F5'
                                            },
                                            type='dashboard'
                                        )
                                    ],
                                    tab='仪表盘进度条',
                                    key='仪表盘进度条'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '自定义进度条颜色',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTabs(
    [
        fac.AntdTabPane(
            [
                fac.AntdDivider('单一色彩', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    strokeColor='#2e62cd',
                    style={
                        'width': '200px'
                    }
                ),
                fac.AntdDivider('渐变色彩', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    strokeColor={
                        'from': '#00F5A0',
                        'to': '#00D9F5'
                    },
                    style={
                        'width': '200px'
                    }
                )
            ],
            tab='线型进度条',
            key='线型进度条'
        ),
        fac.AntdTabPane(
            [
                fac.AntdDivider('单一色彩', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    strokeColor='#2e62cd',
                    type='circle'
                ),
                fac.AntdDivider('渐变色彩', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    strokeColor={
                        'from': '#00F5A0',
                        'to': '#00D9F5'
                    },
                    type='circle'
                )
            ],
            tab='环形进度条',
            key='环形进度条'
        ),
        fac.AntdTabPane(
            [
                fac.AntdDivider('单一色彩', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    strokeColor='#2e62cd',
                    type='dashboard'
                ),
                fac.AntdDivider('渐变色彩', innerTextOrientation='left'),
                fac.AntdProgress(
                    percent=80,
                    strokeColor={
                        'from': '#00F5A0',
                        'to': '#00D9F5'
                    },
                    type='dashboard'
                )
            ],
            tab='仪表盘进度条',
            key='仪表盘进度条'
        )
    ]
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
                    id='自定义进度条颜色',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdProgress(
                            percent=80,
                            steps=10
                        ),
                        html.Br(),
                        fac.AntdProgress(
                            percent=80,
                            steps=10,
                            size='small'
                        ),

                        fac.AntdDivider(
                            '分段线型进度条',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdProgress(
    percent=80,
    steps=10
),
html.Br(),
fac.AntdProgress(
    percent=80,
    steps=10,
    size='small'
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
                    id='分段线型进度条',
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
                            {'title': 'percent达到100时的状态', 'href': '#percent达到100时的状态'},
                            {'title': '自定义百分比数值内容', 'href': '#自定义百分比数值内容'},
                            {'title': '不同的自定义状态', 'href': '#不同的自定义状态'},
                            {'title': '关闭额外说明内容', 'href': '#关闭额外说明内容'},
                            {'title': '自定义进度条颜色', 'href': '#自定义进度条颜色'},
                            {'title': '分段线型进度条', 'href': '#分段线型进度条'},
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
