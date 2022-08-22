from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdRow(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdRow.md', encoding='utf-8').read()
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
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col4',
                                        style={
                                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=6
                                ),
                            ],
                            gutter=10
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
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=6
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=6
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=6
        ),
        fac.AntdCol(
            html.Div(
                'col4',
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=6
        ),
    ],
    gutter=10
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
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    xs=12,
                                    sm=12,
                                    md=8,
                                    lg=8,
                                    xl=6,
                                    xxl=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    xs=12,
                                    sm=12,
                                    md=8,
                                    lg=8,
                                    xl=6,
                                    xxl=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    xs=12,
                                    sm=12,
                                    md=8,
                                    lg=8,
                                    xl=6,
                                    xxl=6
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col4',
                                        style={
                                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    xs=12,
                                    sm=12,
                                    md=8,
                                    lg=8,
                                    xl=6,
                                    xxl=6
                                ),
                            ],
                            gutter=[10, 10]
                        ),

                        fac.AntdDivider(
                            '响应式示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            xs=12,
            sm=12,
            md=8,
            lg=8,
            xl=6,
            xxl=6
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            xs=12,
            sm=12,
            md=8,
            lg=8,
            xl=6,
            xxl=6
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            xs=12,
            sm=12,
            md=8,
            lg=8,
            xl=6,
            xxl=6
        ),
        fac.AntdCol(
            html.Div(
                'col4',
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            xs=12,
            sm=12,
            md=8,
            lg=8,
            xl=6,
            xxl=6
        ),
    ],
    gutter=[10, 10]
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
                    id='响应式示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        f'col{col + 1}',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=2
                                )
                                if col % 2 == 0
                                else fac.AntdCol(
                                    html.Div(
                                        f'col{col + 1}',
                                        style={
                                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=2
                                )
                                for col in range(14)
                            ],
                            gutter=[5, 5]
                        ),

                        fac.AntdDivider(
                            '行组件内部列组件的span之和大于24时自动换行',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                f'col{col + 1}',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=2
        )
        if col % 2 == 0
        else fac.AntdCol(
            html.Div(
                f'col{col + 1}',
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=2
        )
        for col in range(14)
    ],
    gutter=[5, 5]
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
                    id='行组件内部列组件的span之和大于24时自动换行',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('justify="start"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10
                        ),

                        fac.AntdDivider('justify="end"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10,
                            justify='end'
                        ),

                        fac.AntdDivider('justify="center"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10,
                            justify='center'
                        ),

                        fac.AntdDivider('justify="space-around"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10,
                            justify='space-around'
                        ),

                        fac.AntdDivider('justify="space-between"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10,
                            justify='space-between'
                        ),

                        fac.AntdDivider(
                            '不同的水平对齐方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('justify="start"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10
),

fac.AntdDivider('justify="end"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10,
    justify='end'
),

fac.AntdDivider('justify="center"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10,
    justify='center'
),

fac.AntdDivider('justify="space-around"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10,
    justify='space-around'
),

fac.AntdDivider('justify="space-between"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10,
    justify='space-between'
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
                    id='不同的水平对齐方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('align="top"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '50px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10
                        ),

                        fac.AntdDivider('align="middle"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '50px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10,
                            align='middle'
                        ),

                        fac.AntdDivider('align="bottom"', innerTextOrientation='left'),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'col1',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '50px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col2',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '25px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        'col3',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    span=4
                                )
                            ],
                            gutter=10,
                            align='bottom'
                        ),

                        fac.AntdDivider(
                            '不同的垂直对齐方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider('align="top"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '50px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10
),

fac.AntdDivider('align="middle"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '50px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10,
    align='middle'
),

fac.AntdDivider('align="bottom"', innerTextOrientation='left'),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'col1',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '50px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col2',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '25px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        ),
        fac.AntdCol(
            html.Div(
                'col3',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            span=4
        )
    ],
    gutter=10,
    align='bottom'
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
                    id='不同的垂直对齐方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        '1/7',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '50px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    flex='1'
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        '2/7',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '50px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    flex='2'
                                ),
                                fac.AntdCol(
                                    html.Div(
                                        '4/7',
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'color': 'white',
                                            'height': '50px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center'
                                        }
                                    ),
                                    flex='4'
                                )
                            ],
                            gutter=10
                        ),

                        fac.AntdDivider(
                            '使用flex更灵活地配置列宽度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                '1/7',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '50px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            flex='1'
        ),
        fac.AntdCol(
            html.Div(
                '2/7',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '50px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            flex='2'
        ),
        fac.AntdCol(
            html.Div(
                '4/7',
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'color': 'white',
                    'height': '50px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            flex='4'
        )
    ],
    gutter=10
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
                    id='使用flex更灵活地配置列宽度',
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
                            {'title': '响应式示例', 'href': '#响应式示例'},
                            {'title': '行组件内部列组件的span之和大于24时自动换行', 'href': '#行组件内部列组件的span之和大于24时自动换行'},
                            {'title': '不同的水平对齐方式', 'href': '#不同的水平对齐方式'},
                            {'title': '不同的垂直对齐方式', 'href': '#不同的垂直对齐方式'},
                            {'title': '使用flex更灵活地配置列宽度', 'href': '#使用flex更灵活地配置列宽度'},
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
