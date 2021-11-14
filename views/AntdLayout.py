import dash
from dash import html
from dash import dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc

from dash.dependencies import Input, Output, State

from server import app

docs_content = html.Div(
    [
        html.H2(
            'AntdLayout(children, id, className, style, **kwargs)',
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

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '经典布局', 'href': '#经典布局'},
                        {'title': '不同的侧边栏位置', 'href': '#不同的侧边栏位置'},
                        {'title': '可折叠的侧边栏', 'href': '#可折叠的侧边栏'},
                        {'title': '将其他组件整合入侧边栏', 'href': '#将其他组件整合入侧边栏'},
                        {'title': '自定义侧边栏折叠触发器', 'href': '#自定义侧边栏折叠触发器'},
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
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

        fuc.FefferyMarkdown(
            markdownStr=open('documents/AntdLayout.md', encoding='utf-8').read()
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
                        fac.AntdLayout(
                            [
                                fac.AntdHeader(
                                    fac.AntdTitle(
                                        '页首示例',
                                        level=2,
                                        style={
                                            'color': 'white',
                                            'margin': '0'
                                        }
                                    ),
                                    style={
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                ),
                                fac.AntdLayout(
                                    [
                                        fac.AntdSider(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '侧边栏示例',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'alignItems': 'center',
                                                    'display': 'flex',
                                                    'height': '100%'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)',
                                                'display': 'flex',
                                                'justifyContent': 'center'
                                            }
                                        ),
                                        fac.AntdLayout(
                                            [
                                                fac.AntdContent(
                                                    html.Div(
                                                        fac.AntdTitle(
                                                            '内容区示例',
                                                            level=2,
                                                            style={
                                                                'margin': '0'
                                                            }
                                                        ),
                                                        style={
                                                            'display': 'flex',
                                                            'height': '100%',
                                                            'justifyContent': 'center',
                                                            'alignItems': 'center'
                                                        }
                                                    ),
                                                    style={
                                                        'backgroundColor': 'white'
                                                    }
                                                ),
                                                fac.AntdFooter(
                                                    html.Div(
                                                        fac.AntdTitle(
                                                            '页尾示例',
                                                            level=2,
                                                            style={
                                                                'margin': '0'
                                                            }
                                                        ),
                                                        style={
                                                            'display': 'flex',
                                                            'height': '100%',
                                                            'justifyContent': 'center',
                                                            'alignItems': 'center'
                                                        }
                                                    ),
                                                    style={
                                                        'backgroundColor': 'rgb(193, 193, 193)',
                                                        'height': '40px'
                                                    }
                                                )
                                            ]
                                        )
                                    ],
                                    style={
                                        'height': '536px'
                                    }
                                )
                            ]
                        )
                    ],
                    style={
                        'height': '600px',
                        'border': '1px solid rgb(241, 241, 241)'
                    }
                ),

                fac.AntdDivider(
                    '经典布局',
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
        fac.AntdLayout(
            [
                fac.AntdHeader(
                    fac.AntdTitle(
                        '页首示例',
                        level=2,
                        style={
                            'color': 'white',
                            'margin': '0'
                        }
                    ),
                    style={
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                ),
                fac.AntdLayout(
                    [
                        fac.AntdSider(
                            html.Div(
                                fac.AntdTitle(
                                    '侧边栏示例',
                                    level=2,
                                    style={
                                        'margin': '0'
                                    }
                                ),
                                style={
                                    'alignItems': 'center',
                                    'display': 'flex',
                                    'height': '100%'
                                }
                            ),
                            style={
                                'backgroundColor': 'rgb(240, 242, 245)',
                                'display': 'flex',
                                'justifyContent': 'center'
                            }
                        ),
                        fac.AntdLayout(
                            [
                                fac.AntdContent(
                                    html.Div(
                                        fac.AntdTitle(
                                            '内容区示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'white'
                                    }
                                ),
                                fac.AntdFooter(
                                    html.Div(
                                        fac.AntdTitle(
                                            '页尾示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'rgb(193, 193, 193)',
                                        'height': '40px'
                                    }
                                )
                            ]
                        )
                    ],
                    style={
                        'height': '536px'
                    }
                )
            ]
        )
    ],
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
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
            id='经典布局',
            className='div-highlight'
        ),

        html.Div(
            [
                html.Div(
                    [
                        fac.AntdLayout(
                            [
                                fac.AntdContent(
                                    html.Div(
                                        fac.AntdTitle(
                                            '内容区示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'white'
                                    }
                                ),

                                fac.AntdSider(
                                    html.Div(
                                        fac.AntdTitle(
                                            '右侧侧边栏',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'rgb(240, 242, 245)'
                                    }
                                )
                            ],
                            style={
                                'height': '600px'
                            }
                        )
                    ],
                    style={
                        'height': '600px',
                        'border': '1px solid rgb(241, 241, 241)'
                    }
                ),

                fac.AntdDivider(
                    '不同的侧边栏位置',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　若需要侧边栏位于右侧，只需要将'),
                        fac.AntdText('AntdSider', strong=True),
                        fac.AntdText('在'),
                        fac.AntdText('AntdLayout', strong=True),
                        fac.AntdText('中的位置从列表第一调整至列表最后即可'),
                    ]
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
                                fac.AntdLayout(
                                    [
                                        fac.AntdContent(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '内容区示例',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'white'
                                            }
                                        ),
        
                                        fac.AntdSider(
                                            html.Div(
                                                fac.AntdTitle(
                                                    '右侧侧边栏',
                                                    level=2,
                                                    style={
                                                        'margin': '0'
                                                    }
                                                ),
                                                style={
                                                    'display': 'flex',
                                                    'height': '100%',
                                                    'justifyContent': 'center',
                                                    'alignItems': 'center'
                                                }
                                            ),
                                            style={
                                                'backgroundColor': 'rgb(240, 242, 245)'
                                            }
                                        )
                                    ],
                                    style={
                                        'height': '600px'
                                    }
                                )
                            ],
                            style={
                                'height': '600px',
                                'border': '1px solid rgb(241, 241, 241)'
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
            id='不同的侧边栏位置',
            className='div-highlight'
        ),

        html.Div(
            [
                html.Div(
                    [
                        fac.AntdLayout(
                            [
                                fac.AntdSider(
                                    collapsible=True,
                                    style={
                                        'backgroundColor': 'rgb(240, 242, 245)'
                                    }
                                ),

                                fac.AntdContent(
                                    html.Div(
                                        fac.AntdTitle(
                                            '内容区示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'white'
                                    }
                                )
                            ],
                            style={
                                'height': '600px'
                            }
                        )
                    ],
                    id='sider-demo',
                    style={
                        'height': '600px',
                        'border': '1px solid rgb(241, 241, 241)'
                    }
                ),

                fac.AntdDivider(
                    '可折叠的侧边栏',
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
        fac.AntdLayout(
            [
                fac.AntdSider(
                    collapsible=True,
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                ),

                fac.AntdContent(
                    html.Div(
                        fac.AntdTitle(
                            '内容区示例',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    id='sider-demo',
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
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
            id='可折叠的侧边栏',
            className='div-highlight'
        ),

        html.Div(
            [
                html.Div(
                    [
                        fac.AntdLayout(
                            [
                                fac.AntdSider(
                                    [
                                        html.Div(
                                            fac.AntdInput(placeholder='输入搜索内容', mode='search'),
                                            style={
                                                'padding': '5px'
                                            }
                                        ),
                                        html.Div(
                                            [
                                                fac.AntdMenu(
                                                    menuItems=[
                                                        {
                                                            'component': 'Item',
                                                            'props': {
                                                                'key': f'图标{icon}',
                                                                'title': f'图标{icon}',
                                                                'icon': icon
                                                            }
                                                        }
                                                        for icon in [
                                                            'home',
                                                            'upload',
                                                            'bar-chart',
                                                            'pie-chart',
                                                            'dot-chart',
                                                            'line-chart',
                                                            'apartment',
                                                            'app-store',
                                                            'app-store-add',
                                                            'bell',
                                                            'calculator',
                                                            'calendar',
                                                            'database',
                                                            'history'
                                                        ]
                                                    ],
                                                    mode='inline'
                                                )
                                            ],
                                            style={
                                                'height': '100%',
                                                'overflowY': 'auto'
                                            }
                                        )
                                    ],
                                    collapsible=True,
                                    style={
                                        'backgroundColor': 'rgb(240, 242, 245)'
                                    }
                                ),

                                fac.AntdContent(
                                    html.Div(
                                        fac.AntdTitle(
                                            '内容区示例',
                                            level=2,
                                            style={
                                                'margin': '0'
                                            }
                                        ),
                                        style={
                                            'display': 'flex',
                                            'height': '100%',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    style={
                                        'backgroundColor': 'white'
                                    }
                                )
                            ],
                            style={
                                'height': '600px'
                            }
                        )
                    ],
                    id='sider-demo',
                    style={
                        'height': '600px',
                        'border': '1px solid rgb(241, 241, 241)'
                    }
                ),

                fac.AntdDivider(
                    '将其他组件整合入侧边栏',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　侧边栏中放入的其他组件，在侧边栏折叠时会自适应压缩，典型如'),
                        fac.AntdText('AntdMenu', strong=True),
                    ]
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
        fac.AntdLayout(
            [
                fac.AntdSider(
                    [
                        html.Div(
                            fac.AntdInput(placeholder='输入搜索内容', mode='search'),
                            style={
                                'padding': '5px'
                            }
                        ),
                        html.Div(
                            [
                                fac.AntdMenu(
                                    menuItems=[
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': f'图标{icon}',
                                                'title': f'图标{icon}',
                                                'icon': icon
                                            }
                                        }
                                        for icon in [
                                            'home',
                                            'upload',
                                            'bar-chart',
                                            'pie-chart',
                                            'dot-chart',
                                            'line-chart',
                                            'apartment',
                                            'app-store',
                                            'app-store-add',
                                            'bell',
                                            'calculator',
                                            'calendar',
                                            'database',
                                            'history'
                                        ]
                                    ],
                                    mode='inline'
                                )
                            ],
                            style={
                                'height': '100%',
                                'overflowY': 'auto'
                            }
                        )
                    ],
                    collapsible=True,
                    style={
                        'backgroundColor': 'rgb(240, 242, 245)'
                    }
                ),

                fac.AntdContent(
                    html.Div(
                        fac.AntdTitle(
                            '内容区示例',
                            level=2,
                            style={
                                'margin': '0'
                            }
                        ),
                        style={
                            'display': 'flex',
                            'height': '100%',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    ),
                    style={
                        'backgroundColor': 'white'
                    }
                )
            ],
            style={
                'height': '600px'
            }
        )
    ],
    id='sider-demo',
    style={
        'height': '600px',
        'border': '1px solid rgb(241, 241, 241)'
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
            id='将其他组件整合入侧边栏',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdSpin(
                    html.Div(
                        [
                            fac.AntdLayout(
                                [
                                    fac.AntdSider(
                                        id='sider-custom-trigger-demo',
                                        collapsible=True,
                                        trigger=None,
                                        style={
                                            'backgroundColor': 'rgb(240, 242, 245)'
                                        }
                                    ),

                                    fac.AntdContent(
                                        fac.AntdButton(
                                            '自定义折叠按钮',
                                            id='sider-custom-trigger-button-demo',
                                            type='primary'
                                        ),
                                        style={
                                            'backgroundColor': 'white'
                                        }
                                    )
                                ],
                                style={
                                    'height': '600px'
                                }
                            )
                        ],
                        style={
                            'height': '600px',
                            'border': '1px solid rgb(241, 241, 241)'
                        }
                    ),
                    text='回调中'
                ),

                fac.AntdDivider(
                    '自定义侧边栏折叠触发器',
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
    html.Div(
        [
            fac.AntdLayout(
                [
                    fac.AntdSider(
                        id='sider-custom-trigger-demo',
                        collapsible=True,
                        trigger=None,
                        style={
                            'backgroundColor': 'rgb(240, 242, 245)'
                        }
                    ),

                    fac.AntdContent(
                        fac.AntdButton(
                            '自定义折叠按钮',
                            id='sider-custom-trigger-button-demo',
                            type='primary'
                        ),
                        style={
                            'backgroundColor': 'white'
                        }
                    )
                ],
                style={
                    'height': '600px'
                }
            )
        ],
        style={
            'height': '600px',
            'border': '1px solid rgb(241, 241, 241)'
        }
    ),
    text='回调中'
)
...
@app.callback(
    Output('sider-custom-trigger-demo', 'collapsed'),
    Input('sider-custom-trigger-button-demo', 'nClicks'),
    State('sider-custom-trigger-demo', 'collapsed'),
    prevent_initial_call=True
)
def sider_custom_trigger_demo(nClicks, collapsed):
    if nClicks:
        return not collapsed

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
            id='自定义侧边栏折叠触发器',
            className='div-highlight'
        ),

        html.Div(style={'height': '100px'})
    ]
)


@app.callback(
    Output('sider-custom-trigger-demo', 'collapsed'),
    Input('sider-custom-trigger-button-demo', 'nClicks'),
    State('sider-custom-trigger-demo', 'collapsed'),
    prevent_initial_call=True
)
def sider_custom_trigger_demo(nClicks, collapsed):
    if nClicks:
        return not collapsed

    return dash.no_update
