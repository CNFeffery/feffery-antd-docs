from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTabs

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTabs(children, id, className, style, **kwargs)',
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
                    '主要参数说明',
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
                    markdownStr=open('documents/AntdTabs.md', encoding='utf-8').read()
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
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    html.Div(
                                        '标签页1测试',
                                        style={
                                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    html.Div(
                                        fac.AntdButton('标签页2测试', type='primary'),
                                        style={
                                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    html.Div(
                                        fac.AntdButton('标签页3测试', type='dashed'),
                                        style={
                                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ]
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
fac.AntdTabs(
    [
        fac.AntdTabPane(
            html.Div(
                '标签页1测试',
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            html.Div(
                fac.AntdButton('标签页2测试', type='primary'),
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            html.Div(
                fac.AntdButton('标签页3测试', type='dashed'),
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            tab='标签页3',
            key='标签页3'
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    html.Div(
                                        '标签页1测试',
                                        style={
                                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    html.Div(
                                        fac.AntdButton('标签页2测试', type='primary'),
                                        style={
                                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    html.Div(
                                        fac.AntdButton('标签页3测试', type='dashed'),
                                        style={
                                            'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                                            'height': '200px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ],
                            defaultActiveKey='标签页2'
                        ),

                        fac.AntdDivider(
                            '手动设置默认激活的标签页',
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
fac.AntdTabs(
    [
        fac.AntdTabPane(
            html.Div(
                '标签页1测试',
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            html.Div(
                fac.AntdButton('标签页2测试', type='primary'),
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            html.Div(
                fac.AntdButton('标签页3测试', type='dashed'),
                style={
                    'backgroundColor': 'rgba(241, 241, 241, 0.4)',
                    'height': '200px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            tab='标签页3',
            key='标签页3'
        )
    ],
    defaultActiveKey='标签页2'
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
                    id='手动设置默认激活的标签页',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('top', innerTextOrientation='left'),
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ]
                        ),

                        fac.AntdDivider('left', innerTextOrientation='left'),
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ],
                            tabPosition='left'
                        ),

                        fac.AntdDivider('right', innerTextOrientation='left'),
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ],
                            tabPosition='right'
                        ),

                        fac.AntdDivider('bottom', innerTextOrientation='left'),
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ],
                            tabPosition='bottom'
                        ),

                        fac.AntdDivider(
                            '不同的标签页吸附位置',
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
fac.AntdDivider('top', innerTextOrientation='left'),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            tab='标签页3',
            key='标签页3'
        )
    ]
),

fac.AntdDivider('left', innerTextOrientation='left'),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            tab='标签页3',
            key='标签页3'
        )
    ],
    tabPosition='left'
),

fac.AntdDivider('right', innerTextOrientation='left'),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            tab='标签页3',
            key='标签页3'
        )
    ],
    tabPosition='right'
),

fac.AntdDivider('bottom', innerTextOrientation='left'),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            tab='标签页3',
            key='标签页3'
        )
    ],
    tabPosition='bottom'
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
                    id='不同的标签页吸附位置',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('type="card"', innerTextOrientation='left'),
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ],
                            type='card'
                        ),

                        fac.AntdDivider('type="editable-card"', innerTextOrientation='left'),
                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab='标签页1',
                                    key='标签页1'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页2',
                                    key='标签页2'
                                ),
                                fac.AntdTabPane(
                                    tab='标签页3',
                                    key='标签页3'
                                )
                            ],
                            type='editable-card'
                        ),

                        fac.AntdDivider(
                            '不同的标签页渲染类型',
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
fac.AntdDivider('type="card"', innerTextOrientation='left'),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            tab='标签页3',
            key='标签页3'
        )
    ],
    type='card'
),

fac.AntdDivider('type="editable-card"', innerTextOrientation='left'),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab='标签页1',
            key='标签页1'
        ),
        fac.AntdTabPane(
            tab='标签页2',
            key='标签页2'
        ),
        fac.AntdTabPane(
            tab='标签页3',
            key='标签页3'
        )
    ],
    type='editable-card'
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
                    id='不同的标签页渲染类型',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdTabs(
                            [
                                fac.AntdTabPane(
                                    tab=f'标签页{i}',
                                    key=f'标签页{i}'
                                )
                                for i in range(50)
                            ]
                        ),

                        fac.AntdDivider(
                            '标签页面板众多时自动开启省略模式',
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
fac.AntdTabs(
    [
        fac.AntdTabPane(
            tab=f'标签页{i}',
            key=f'标签页{i}'
        )
        for i in range(50)
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
                    id='标签页面板众多时自动开启省略模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            [
                                fac.AntdButton(
                                    '新建标签页',
                                    id='tabs-demo-add',
                                    type='primary',
                                    style={
                                        'marginBottom': '5px'
                                    }
                                ),
                                fac.AntdTabs(
                                    [
                                        fac.AntdTabPane(
                                            '基础标签页',
                                            tab='基础标签页',
                                            key='基础标签页',
                                            closable=False
                                        ),
                                        fac.AntdTabPane(
                                            tab='禁用标签页',
                                            key='禁用标签页',
                                            disabled=True
                                        )
                                    ] + [
                                        fac.AntdTabPane(
                                            '标签页1',
                                            tab='标签页1',
                                            key='标签页1'
                                        )
                                    ],
                                    id='tabs-demo',
                                    type='editable-card'
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
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdButton(
    '新建标签页',
    id='tabs-demo-add',
    type='primary',
    style={
        'marginBottom': '5px'
    }
),
fac.AntdTabs(
    [
        fac.AntdTabPane(
            '基础标签页',
            tab='基础标签页',
            key='基础标签页',
            closable=False
        ),
        fac.AntdTabPane(
            tab='禁用标签页',
            key='禁用标签页',
            disabled=True
        )
    ] + [
        fac.AntdTabPane(
            '标签页1',
            tab='标签页1',
            key='标签页1'
        )
    ],
    id='tabs-demo',
    type='editable-card'
)
...
@app.callback(
    [Output('tabs-demo', 'children'),
     Output('tabs-demo', 'activeKey')],
    [Input('tabs-demo-add', 'nClicks'),
     Input('tabs-demo', 'latestDeletePane')],
    State('tabs-demo', 'children'),
    prevent_initial_call=True
)
def tabs_callback_demo(nClicks, latestDeletePane, children):

    ctx = dash.callback_context

    if ctx.triggered[0]['prop_id'] == 'tabs-demo-add.nClicks':
        return children + [
            fac.AntdTabPane(f'标签页{nClicks + 1}', tab=f'标签页{nClicks + 1}', key=f'标签页{nClicks + 1}')
        ], f'标签页{nClicks + 1}'

    elif ctx.triggered[0]['prop_id'] == 'tabs-demo.latestDeletePane':
        return [child for child in children if child['props']['key'] != latestDeletePane], '基础标签页'

    return dash.no_update'''
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
                'flex': 'auto',
                'width': 'calc(100vw - 625px)'
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
                            {'title': '手动设置默认激活的标签页', 'href': '#手动设置默认激活的标签页'},
                            {'title': '不同的标签页吸附位置', 'href': '#不同的标签页吸附位置'},
                            {'title': '不同的标签页渲染类型', 'href': '#不同的标签页渲染类型'},
                            {'title': '标签页面板众多时自动开启省略模式', 'href': '#标签页面板众多时自动开启省略模式'},
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
