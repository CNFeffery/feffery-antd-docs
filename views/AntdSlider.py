from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSlider
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
                                'title': '数据录入'
                            },
                            {
                                'title': 'AntdSlider 滑动输入条'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供基于滑动交互的单值或范围设置功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=33,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdSlider(
                                range=True,
                                min=0,
                                max=100,
                                defaultValue=[10, 90],
                                style={
                                    'width': 300
                                }
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
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=33,
    style={
        'width': 300
    }
),

fac.AntdSlider(
    range=True,
    min=0,
    max=100,
    defaultValue=[10, 90],
    style={
        'width': 300
    }
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
                            fac.AntdSpace(
                                [
                                    fac.AntdSlider(
                                        vertical=True,
                                        min=0,
                                        max=100,
                                        defaultValue=33,
                                        style={
                                            'height': 200
                                        }
                                    ),

                                    fac.AntdSlider(
                                        vertical=True,
                                        range=True,
                                        min=0,
                                        max=100,
                                        defaultValue=[10, 90],
                                        style={
                                            'height': 200
                                        }
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '垂直模式',
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
fac.AntdSpace(
    [
        fac.AntdSlider(
            vertical=True,
            min=0,
            max=100,
            defaultValue=33,
            style={
                'height': 200
            }
        ),

        fac.AntdSlider(
            vertical=True,
            range=True,
            min=0,
            max=100,
            defaultValue=[10, 90],
            style={
                'height': 200
            }
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
                        id='垂直模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=50,
                                step=10,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '自定义滑动步长',
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
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=50,
    step=10,
    style={
        'width': 300
    }
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
                        id='自定义滑动步长',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=50,
                                marks={
                                    i*10: f'{i*10}%'
                                    for i in range(0, 11)
                                },
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '自定义刻度',
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
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=50,
    marks={
        i*10: f'{i*10}%'
        for i in range(0, 11)
    },
    style={
        'width': 300
    }
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
                        id='自定义刻度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'tooltipVisible=True',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=50,
                                tooltipVisible=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'tooltipVisible=False',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=50,
                                tooltipVisible=False,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '滑动提示内容显示策略',
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
    'tooltipVisible=True',
    innerTextOrientation='left'
),
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=50,
    tooltipVisible=True,
    style={
        'width': 300
    }
),

fac.AntdDivider(
    'tooltipVisible=False',
    innerTextOrientation='left'
),
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=50,
    tooltipVisible=False,
    style={
        'width': 300
    }
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
                        id='滑动提示内容显示策略',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=50,
                                tooltipPrefix='当前值：',
                                tooltipSuffix='%',
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '滑动提示内容前后缀',
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
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=50,
    tooltipPrefix='当前值：',
    tooltipSuffix='%',
    style={
        'width': 300
    }
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
                        id='滑动提示内容前后缀',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=33,
                                disabled=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdSlider(
                                range=True,
                                min=0,
                                max=100,
                                defaultValue=[10, 90],
                                disabled=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '禁用状态',
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
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=33,
    disabled=True,
    style={
        'width': 300
    }
),

fac.AntdSlider(
    range=True,
    min=0,
    max=100,
    defaultValue=[10, 90],
    disabled=True,
    style={
        'width': 300
    }
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                min=0,
                                max=100,
                                defaultValue=33,
                                style={
                                    'width': 300
                                },
                                railStyle={
                                    'background': '#d0ebff'
                                }
                            ),

                            fac.AntdSlider(
                                range=True,
                                min=0,
                                max=100,
                                defaultValue=[10, 90],
                                style={
                                    'width': 300
                                },
                                railStyle={
                                    'background': '#d0ebff'
                                }
                            ),

                            fac.AntdDivider(
                                '自定义滑轨样式',
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
fac.AntdSlider(
    min=0,
    max=100,
    defaultValue=33,
    style={
        'width': 300
    },
    railStyle={
        'background': '#d0ebff'
    }
),

fac.AntdSlider(
    range=True,
    min=0,
    max=100,
    defaultValue=[10, 90],
    style={
        'width': 300
    },
    railStyle={
        'background': '#d0ebff'
    }
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
                        id='自定义滑轨样式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                id='slider-demo',
                                min=0,
                                max=100,
                                defaultValue=33,
                                style={
                                    'width': 300
                                }
                            ),
                            fac.AntdText(
                                id='slider-demo-output'
                            ),

                            fac.AntdSlider(
                                id='slider-range-demo',
                                range=True,
                                min=0,
                                max=100,
                                defaultValue=[10, 90],
                                style={
                                    'width': 300
                                }
                            ),
                            fac.AntdText(
                                id='slider-range-demo-output'
                            ),

                            fac.AntdDivider(
                                '回调示例',
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
fac.AntdSlider(
    id='slider-demo',
    min=0,
    max=100,
    defaultValue=33,
    style={
        'width': 300
    }
),
fac.AntdText(
    id='slider-demo-output'
),

fac.AntdSlider(
    id='slider-range-demo',
    range=True,
    min=0,
    max=100,
    defaultValue=[10, 90],
    style={
        'width': 300
    }
),
fac.AntdText(
    id='slider-range-demo-output'
)

...

@app.callback(
    Output('slider-demo-output', 'children'),
    Input('slider-demo', 'value')
)
def slider_demo(value):

    return f'value: {value}'


@app.callback(
    Output('slider-range-demo-output', 'children'),
    Input('slider-range-demo', 'value')
)
def slider_range_demo(value):

    return f'value: {value}'
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
                        id='回调示例',
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
                        {'title': '垂直模式', 'href': '#垂直模式'},
                        {'title': '自定义滑动步长', 'href': '#自定义滑动步长'},
                        {'title': '自定义刻度', 'href': '#自定义刻度'},
                        {'title': '滑动提示内容显示策略', 'href': '#滑动提示内容显示策略'},
                        {'title': '滑动提示内容前后缀', 'href': '#滑动提示内容前后缀'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '自定义滑轨样式', 'href': '#自定义滑轨样式'},
                        {'title': '回调示例', 'href': '#回调示例'},
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
                component_name='AntdSlider',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
