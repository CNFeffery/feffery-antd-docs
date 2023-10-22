from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
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
                                'title': '反馈'
                            },
                            {
                                'title': 'AntdProrgess 进度条'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染常用形式的进度条。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'type="line"（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdProgress(
                                percent=80,
                                style={
                                    'width': 200
                                }
                            ),
                            fac.AntdDivider(
                                'type="circle"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdProgress(
                                percent=80,
                                type='circle'
                            ),
                            fac.AntdDivider(
                                'type="dashboard"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdProgress(
                                percent=80,
                                type='dashboard'
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
fac.AntdDivider(
    'type="line"（默认）',
    innerTextOrientation='left'
),
fac.AntdProgress(
    percent=80,
    style={
        'width': 200
    }
),
fac.AntdDivider(
    'type="circle"',
    innerTextOrientation='left'
),
fac.AntdProgress(
    percent=80,
    type='circle'
),
fac.AntdDivider(
    'type="dashboard"',
    innerTextOrientation='left'
),
fac.AntdProgress(
    percent=80,
    type='dashboard'
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
                                    fac.AntdProgress(
                                        percent=100,
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdProgress(
                                        percent=100,
                                        type='circle'
                                    ),
                                    fac.AntdProgress(
                                        percent=100,
                                        type='dashboard'
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '100%状态样式',
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
        fac.AntdProgress(
            percent=100,
            style={
                'width': 200
            }
        ),
        fac.AntdProgress(
            percent=100,
            type='circle'
        ),
        fac.AntdProgress(
            percent=100,
            type='dashboard'
        )
    ],
    direction='vertical'
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
                        id='100%状态样式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        status=status,
                                        style={
                                            'width': 425
                                        }
                                    )
                                    for status in [
                                        'normal', 'success', 'exception', 'active'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        status=status,
                                        type='circle'
                                    )
                                    for status in [
                                        'normal', 'success', 'exception'
                                    ]
                                ],
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        status=status,
                                        type='dashboard'
                                    )
                                    for status in [
                                        'normal', 'success', 'exception'
                                    ]
                                ],
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '强制状态类型',
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
        fac.AntdProgress(
            percent=80,
            status=status,
            style={
                'width': 425
            }
        )
        for status in [
            'normal', 'success', 'exception', 'active'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
),

fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=80,
            status=status,
            type='circle'
        )
        for status in [
            'normal', 'success', 'exception'
        ]
    ],
    style={
        'width': '100%'
    }
),

fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=80,
            status=status,
            type='dashboard'
        )
        for status in [
            'normal', 'success', 'exception'
        ]
    ],
    style={
        'width': '100%'
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
                        id='强制状态类型',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        status=status,
                                        size='small',
                                        style={
                                            'width': 425
                                        }
                                    )
                                    for status in [
                                        'normal', 'success', 'exception', 'active'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '迷你尺寸进度条',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '针对',
                                    fac.AntdText(
                                        'line',
                                        strong=True
                                    ),
                                    '型进度条可设置迷你尺寸规格'
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
fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=80,
            status=status,
            size='small',
            style={
                'width': 425
            }
        )
        for status in [
            'normal', 'success', 'exception', 'active'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                        id='迷你尺寸进度条',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        format={
                                            'prefix': '进度'
                                        },
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        format={
                                            'suffix': '分'
                                        },
                                        type='circle'
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        format={
                                            'content': '🚀🚀🚀'
                                        },
                                        type='dashboard'
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '自定义百分比内容',
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
        fac.AntdProgress(
            percent=80,
            format={
                'prefix': '进度'
            },
            style={
                'width': 200
            }
        ),
        fac.AntdProgress(
            percent=80,
            format={
                'suffix': '分'
            },
            type='circle'
        ),
        fac.AntdProgress(
            percent=80,
            format={
                'content': '🚀🚀🚀'
            },
            type='dashboard'
        )
    ],
    direction='vertical'
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
                        id='自定义百分比内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        strokeColor={
                                            'from': '#f067b4',
                                            'to': '#81ffef'
                                        },
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        strokeColor={
                                            'from': '#f067b4',
                                            'to': '#81ffef'
                                        },
                                        type='circle'
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        strokeColor={
                                            'from': '#f067b4',
                                            'to': '#81ffef'
                                        },
                                        type='dashboard'
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '设置渐变色',
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
        fac.AntdProgress(
            percent=80,
            strokeColor={
                'from': '#f067b4',
                'to': '#81ffef'
            },
            style={
                'width': 200
            }
        ),
        fac.AntdProgress(
            percent=80,
            strokeColor={
                'from': '#f067b4',
                'to': '#81ffef'
            },
            type='circle'
        ),
        fac.AntdProgress(
            percent=80,
            strokeColor={
                'from': '#f067b4',
                'to': '#81ffef'
            },
            type='dashboard'
        )
    ],
    direction='vertical'
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
                        id='设置渐变色',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTooltip(
                                        fac.AntdProgress(
                                            percent=60,
                                            success={
                                                'percent': 30
                                            }
                                        ),
                                        title='3 done / 3 in progress / 4 to do'
                                    ),

                                    fac.AntdTooltip(
                                        fac.AntdProgress(
                                            percent=60,
                                            success={
                                                'percent': 30
                                            },
                                            type='circle'
                                        ),
                                        title='3 done / 3 in progress / 4 to do'
                                    ),

                                    fac.AntdTooltip(
                                        fac.AntdProgress(
                                            percent=60,
                                            success={
                                                'percent': 30
                                            },
                                            type='dashboard'
                                        ),
                                        title='3 done / 3 in progress / 4 to do'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '多阶段进度条',
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
        fac.AntdTooltip(
            fac.AntdProgress(
                percent=60,
                success={
                    'percent': 30
                }
            ),
            title='3 done / 3 in progress / 4 to do'
        ),

        fac.AntdTooltip(
            fac.AntdProgress(
                percent=60,
                success={
                    'percent': 30
                },
                type='circle'
            ),
            title='3 done / 3 in progress / 4 to do'
        ),

        fac.AntdTooltip(
            fac.AntdProgress(
                percent=60,
                success={
                    'percent': 30
                },
                type='dashboard'
            ),
            title='3 done / 3 in progress / 4 to do'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                        id='多阶段进度条',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        trailColor='#a5d8ff',
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        trailColor='#a5d8ff',
                                        type='circle'
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        trailColor='#a5d8ff',
                                        type='dashboard'
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '设置未完成部分颜色',
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
        fac.AntdProgress(
            percent=80,
            trailColor='#a5d8ff',
            style={
                'width': 200
            }
        ),
        fac.AntdProgress(
            percent=80,
            trailColor='#a5d8ff',
            type='circle'
        ),
        fac.AntdProgress(
            percent=80,
            trailColor='#a5d8ff',
            type='dashboard'
        )
    ],
    direction='vertical'
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
                        id='设置未完成部分颜色',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=80,
                                        type='dashboard',
                                        gapPosition=position
                                    )
                                    for position in [
                                        'left', 'top', 'right', 'bottom'
                                    ]
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '设置仪表盘开口方向',
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
                        id='设置仪表盘开口方向',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '默认分段宽度',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=40,
                                        steps=10
                                    ),
                                    fac.AntdProgress(
                                        percent=100,
                                        steps=5,
                                        strokeColor='#52c41a'
                                    ),
                                    fac.AntdProgress(
                                        percent=80,
                                        steps=10,
                                        size='small'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '自定义分段宽度',
                                innerTextOrientation='left'
                            ),
                            fuc.FefferyStyle(
                                rawStyle='''
#progress-custom-step-width .ant-progress-steps-item {
    width: 30px !important;
}
'''
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdProgress(
                                        percent=40,
                                        steps=10
                                    ),
                                    fac.AntdProgress(
                                        percent=100,
                                        steps=5,
                                        strokeColor='#52c41a'
                                    )
                                ],
                                id='progress-custom-step-width',
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '分段line型进度条',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString="""
fac.AntdDivider(
    '默认分段宽度',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=40,
            steps=10
        ),
        fac.AntdProgress(
            percent=100,
            steps=5,
            strokeColor='#52c41a'
        ),
        fac.AntdProgress(
            percent=80,
            steps=10,
            size='small'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
),

fac.AntdDivider(
    '自定义分段宽度',
    innerTextOrientation='left'
),
fuc.FefferyStyle(
    rawStyle='''
#progress-custom-step-width .ant-progress-steps-item {
    width: 30px !important;
}
'''
),
fac.AntdSpace(
    [
        fac.AntdProgress(
            percent=40,
            steps=10
        ),
        fac.AntdProgress(
            percent=100,
            steps=5,
            strokeColor='#52c41a'
        )
    ],
    id='progress-custom-step-width',
    direction='vertical',
    style={
        'width': '100%'
    }
)
"""
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
                        id='分段line型进度条',
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
                        {'title': '100%状态样式', 'href': '#100%状态样式'},
                        {'title': '强制状态类型', 'href': '#强制状态类型'},
                        {'title': '迷你尺寸进度条', 'href': '#迷你尺寸进度条'},
                        {'title': '自定义百分比内容', 'href': '#自定义百分比内容'},
                        {'title': '设置渐变色', 'href': '#设置渐变色'},
                        {'title': '多阶段进度条', 'href': '#多阶段进度条'},
                        {'title': '设置未完成部分颜色', 'href': '#设置未完成部分颜色'},
                        {'title': '设置仪表盘开口方向', 'href': '#设置仪表盘开口方向'},
                        {'title': '分段line型进度条', 'href': '#分段line型进度条'}
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
                component_name='AntdProgress',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
