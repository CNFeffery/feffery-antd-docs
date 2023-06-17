from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from .side_props import render_side_props_layout


def docs_content(language: str = '中文'):

    return html.Div(
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
                                'title': '数据展示'
                            },
                            {
                                'title': 'AntdCarousel 走马灯'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于以轮播切换的形式展示多个内容。')
                        ]
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
                                    enumerate(
                                        [
                                            '#0050b3', '#096dd9', '#1890ff',
                                            '#69c0ff', '#91d5ff'
                                        ]
                                    )
                                ]
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
        enumerate(
            [
                '#0050b3', '#096dd9', '#1890ff',
                '#69c0ff', '#91d5ff'
            ]
        )
    ]
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
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
                                    enumerate(
                                        [
                                            '#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'
                                        ]
                                    )
                                ],
                                autoplay=True
                            ),

                            fac.AntdDivider(
                                '自动轮播',
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
                        enumerate(
                            [
                                '#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'
                            ]
                        )
                    ],
                    autoplay=True
                )
                '''
                                ),
                                title='点击查看代码',
                                isOpen=False,
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
                                            enumerate(
                                                ['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
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
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
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
                                enumerate(
                                    ['#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'])
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
                                isOpen=False,
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
                                    enumerate(
                                        [
                                            '#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'
                                        ]
                                    )
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
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
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
                        enumerate(
                            [
                                '#0050b3', '#096dd9', '#1890ff', '#69c0ff', '#91d5ff'
                            ]
                        )
                    ],
                    autoplay=True,
                    effect='fade'
                )
                '''
                                ),
                                title='点击查看代码',
                                isOpen=False,
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
                                    enumerate(
                                        [
                                            '#0050b3', '#096dd9', '#1890ff',
                                            '#69c0ff', '#91d5ff'
                                        ]
                                    )
                                ],
                                autoplaySpeed=1000,
                                autoplay=True
                            ),

                            fac.AntdDivider(
                                '设置轮播间隔',
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
        enumerate(
            [
                '#0050b3', '#096dd9', '#1890ff',
                '#69c0ff', '#91d5ff'
            ]
        )
    ],
    autoplaySpeed=1000,
    autoplay=True
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置轮播间隔',
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
                                    enumerate(
                                        [
                                            '#0050b3', '#096dd9', '#1890ff',
                                            '#69c0ff', '#91d5ff'
                                        ]
                                    )
                                ],
                                speed=2000,
                                autoplay=True
                            ),

                            fac.AntdDivider(
                                '设置过渡动画耗时',
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
        enumerate(
            [
                '#0050b3', '#096dd9', '#1890ff',
                '#69c0ff', '#91d5ff'
            ]
        )
    ],
    speed=2000,
    autoplay=True
)
'''
                                ),
                                title='点击查看代码',
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置过渡动画耗时',
                        className='div-highlight'
                    ),

                    html.Div(style={'height': '100px'})
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px',
                    'width': 0
                }
            ),

            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '基础使用', 'href': '#基础使用'},
                        {'title': '自动轮播', 'href': '#自动轮播'},
                        {'title': '不同的轮播指示器方位', 'href': '#不同的轮播指示器方位'},
                        {'title': '不同的轮播切换效果', 'href': '#不同的轮播切换效果'},
                        {'title': '设置轮播间隔', 'href': '#设置轮播间隔'},
                        {'title': '设置过渡动画耗时', 'href': '#设置过渡动画耗时'},
                    ],
                    offsetTop=0
                ),
                style={
                    'flex': 'none',
                    'padding': '25px',
                    'flexShrink': 0
                }
            ),
            # 侧边参数栏
            render_side_props_layout(
                component_name='AntdCarousel',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
