from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCarousel(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCarousel.md', encoding='utf-8').read()
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
                        fac.AntdCarousel(
                            [
                                html.Div(
                                    f'子元素{i}',
                                    style={
                                        'color': 'white',
                                        'fontSize': '36px',
                                        'height': '400px',
                                        'backgroundColor': color,
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                                for i, color in
                                enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
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
fac.AntdCarousel(
    [
        html.Div(
            f'子元素{i}',
            style={
                'color': 'white',
                'fontSize': '36px',
                'height': '400px',
                'backgroundColor': color,
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
        for i, color in
        enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCarousel(
                            [
                                html.Div(
                                    f'子元素{i}',
                                    style={
                                        'color': 'white',
                                        'fontSize': '36px',
                                        'height': '400px',
                                        'backgroundColor': color,
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                                for i, color in
                                enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
                            ],
                            autoplay=True
                        ),

                        fac.AntdDivider(
                            '自动轮播',
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
fac.AntdCarousel(
    [
        html.Div(
            f'子元素{i}',
            style={
                'color': 'white',
                'fontSize': '36px',
                'height': '400px',
                'backgroundColor': color,
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
        for i, color in
        enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
    ],
    autoplay=True
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
                    id='自动轮播',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdCarousel(
                                    [
                                        html.Div(
                                            f'dotPosition={position} 子元素{i}',
                                            style={
                                                'color': 'white',
                                                'fontSize': '36px',
                                                'height': '400px',
                                                'backgroundColor': color,
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center'
                                            }
                                        )
                                        for i, color in
                                        enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
                                    ],
                                    dotPosition=position,
                                    autoplay=True,
                                    style={
                                        'marginBottom': '10px'
                                    }
                                )
                                for position in ['top', 'bottom', 'left', 'right']
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的轮播指示器方位',
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
        fac.AntdCarousel(
            [
                html.Div(
                    f'dotPosition={position} 子元素{i}',
                    style={
                        'color': 'white',
                        'fontSize': '36px',
                        'height': '400px',
                        'backgroundColor': color,
                        'display': 'flex',
                        'justifyContent': 'center',
                        'alignItems': 'center'
                    }
                )
                for i, color in
                enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
            ],
            dotPosition=position,
            autoplay=True,
            style={
                'marginBottom': '10px'
            }
        )
        for position in ['top', 'bottom', 'left', 'right']
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
                    id='不同的轮播指示器方位',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCarousel(
                            [
                                html.Div(
                                    f'子元素{i}',
                                    style={
                                        'color': 'white',
                                        'fontSize': '36px',
                                        'height': '400px',
                                        'backgroundColor': color,
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                                for i, color in
                                enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
                            ],
                            autoplay=True,
                            effect='fade'
                        ),

                        fac.AntdDivider(
                            '不同的轮播切换效果',
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
fac.AntdCarousel(
    [
        html.Div(
            f'子元素{i}',
            style={
                'color': 'white',
                'fontSize': '36px',
                'height': '400px',
                'backgroundColor': color,
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
        for i, color in
        enumerate(['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
    ],
    autoplay=True,
    effect='fade'
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
                    id='不同的轮播切换效果',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'width': 0
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
                            {'title': '自动轮播', 'href': '#自动轮播'},
                            {'title': '不同的轮播指示器方位', 'href': '#不同的轮播指示器方位'},
                            {'title': '不同的轮播切换效果', 'href': '#不同的轮播切换效果'},
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
