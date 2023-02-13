from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from .side_props import render_side_props_layout

docs_content = html.Div(
    [
        html.Div(
            [
                fac.AntdBackTop(
                    duration=0.3
                ),

                fac.AntdBreadcrumb(
                    items=[
                        {
                            'title': '组件介绍'
                        },
                        {
                            'title': '布局'
                        },
                        {
                            'title': '网格系统'
                        },
                        {
                            'title': 'AntdRow 行'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在网格系统中构建每个行。')
                    ]
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
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
                            '响应式布局',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText(
                                    '在不同的屏幕尺寸下呈现出不同规格的布局效果'
                                )
                            ],
                            style={
                                'textIndent': '2rem'
                            }
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
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
                    id='响应式布局',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            'span之和溢出24单位时',
                            innerTextOrientation='left'
                        ),
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
                            '像素宽度之和溢出父容器100%时',
                            innerTextOrientation='left'
                        ),
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        'width: 200px',
                                        style={
                                            'backgroundColor': 'rgba(0, 146, 255, 1)',
                                            'color': 'white',
                                            'height': '100px',
                                            'display': 'flex',
                                            'justifyContent': 'center',
                                            'alignItems': 'center',
                                            'width': '200px'
                                        }
                                    ),
                                    flex='none'
                                )
                            ] * 10,
                            gutter=[5, 5]
                        ),

                        fac.AntdDivider(
                            '宽度溢出时自动换行',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider(
    'span之和溢出24单位时',
    innerTextOrientation='left'
),
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
    '像素宽度之和溢出父容器100%时',
    innerTextOrientation='left'
),
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                'width: 200px',
                style={
                    'backgroundColor': 'rgba(0, 146, 255, 1)',
                    'color': 'white',
                    'height': '100px',
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'width': '200px'
                }
            ),
            flex='none'
        )
    ] * 10,
    gutter=[5, 5]
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
                    id='宽度溢出时自动换行',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            'justify="start"',
                            innerTextOrientation='left'
                        ),
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

                        fac.AntdDivider(
                            'justify="end"',
                            innerTextOrientation='left'
                        ),
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

                        fac.AntdDivider(
                            'justify="center"',
                            innerTextOrientation='left'
                        ),
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

                        fac.AntdDivider(
                            'justify="space-around"',
                            innerTextOrientation='left'
                        ),
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

                        fac.AntdDivider(
                            'justify="space-between"',
                            innerTextOrientation='left'
                        ),
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
                            '不同的水平布局方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider(
    'justify="start"',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'justify="end"',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'justify="center"',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'justify="space-around"',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'justify="space-between"',
    innerTextOrientation='left'
),
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
                    id='不同的水平布局方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            'align="top"',
                            innerTextOrientation='left'
                        ),
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

                        fac.AntdDivider(
                            'align="middle"',
                            innerTextOrientation='left'
                        ),
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

                        fac.AntdDivider(
                            'align="bottom"',
                            innerTextOrientation='left'
                        ),
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider(
    'align="top"',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'align="middle"',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'align="bottom"',
    innerTextOrientation='left'
),
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
                            '基于flex自由控制列宽度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
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
                    id='基于flex自由控制列宽度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdRow(
                            [
                                fac.AntdCol(
                                    html.Div(
                                        style={
                                            'backgroundColor': 'rgba(64, 173, 255, 1)',
                                            'height': '100px'
                                        }
                                    ),
                                    span=6
                                )
                            ] * 4,
                            gutter={
                                'xs': 5,
                                'sm': 8,
                                'md': 10,
                                'lg': 12,
                                'xl': 15,
                                'xxl': 25
                            }
                        ),

                        fac.AntdDivider(
                            '响应式gutter',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdRow(
    [
        fac.AntdCol(
            html.Div(
                style={
                    'backgroundColor': 'rgba(64, 173, 255, 1)',
                    'height': '100px'
                }
            ),
            span=6
        )
    ] * 4,
    gutter={
        'xs': 5,
        'sm': 8,
        'md': 10,
        'lg': 12,
        'xl': 15,
        'xxl': 25
    }
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
                    id='响应式gutter',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '响应式布局', 'href': '#响应式布局'},
                    {'title': '宽度溢出时自动换行', 'href': '#宽度溢出时自动换行'},
                    {'title': '不同的水平布局方式', 'href': '#不同的水平布局方式'},
                    {'title': '不同的垂直对齐方式', 'href': '#不同的垂直对齐方式'},
                    {'title': '基于flex自由控制列宽度', 'href': '#基于flex自由控制列宽度'},
                    {'title': '响应式gutter', 'href': '#响应式gutter'},
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'padding': '25px'
            }
        ),
        # 侧边参数栏
        render_side_props_layout(
            component_name='AntdRow'
        )
    ],
    style={
        'display': 'flex'
    }
)
