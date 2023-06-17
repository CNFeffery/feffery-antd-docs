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
                                'title': 'AntdTimeline 时间轴'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染美观的时间轴内容。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'content': '模型训练'
                                    },
                                    {
                                        'content': '模型持久化'
                                    },
                                    {
                                        'content': '模型发布'
                                    }
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
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入'
        },
        {
            'content': '模型训练'
        },
        {
            'content': '模型持久化'
        },
        {
            'content': '模型发布'
        }
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
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'content': '训练数据导入',
                                        'color': 'blue'
                                    },
                                    {
                                        'content': '模型训练',
                                        'color': 'green'
                                    },
                                    {
                                        'content': '模型持久化',
                                        'color': 'grey'
                                    },
                                    {
                                        'content': '模型发布',
                                        'color': 'red'
                                    }
                                ]
                            ),

                            fac.AntdDivider(
                                '不同的节点状态色',
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
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'color': 'blue'
        },
        {
            'content': '模型训练',
            'color': 'green'
        },
        {
            'content': '模型持久化',
            'color': 'grey'
        },
        {
            'content': '模型发布',
            'color': 'red'
        }
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
                        id='不同的节点状态色',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'content': '训练数据导入',
                                        'icon': fac.AntdIcon(
                                            icon='md-cloud-upload',
                                            style={
                                                'fontSize': '18px'
                                            }
                                        )
                                    },
                                    {
                                        'content': '模型训练',
                                        'icon': fac.AntdIcon(
                                            icon='antd-clock-circle',
                                            style={
                                                'fontSize': '18px'
                                            }
                                        )
                                    },
                                    {
                                        'content': '模型持久化',
                                        'icon': fac.AntdIcon(
                                            icon='fc-accept-database',
                                            style={
                                                'fontSize': '18px'
                                            }
                                        )
                                    },
                                    {
                                        'content': '模型发布',
                                        'icon': fac.AntdIcon(
                                            icon='md-cloud-done',
                                            style={
                                                'fontSize': '18px'
                                            }
                                        )
                                    }
                                ]
                            ),

                            fac.AntdDivider(
                                '自定义节点图标',
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
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': fac.AntdIcon(
                icon='md-cloud-upload',
                style={
                    'fontSize': '18px'
                }
            )
        },
        {
            'content': '模型训练',
            'icon': fac.AntdIcon(
                icon='antd-clock-circle',
                style={
                    'fontSize': '18px'
                }
            )
        },
        {
            'content': '模型持久化',
            'icon': fac.AntdIcon(
                icon='fc-accept-database',
                style={
                    'fontSize': '18px'
                }
            )
        },
        {
            'content': '模型发布',
            'icon': fac.AntdIcon(
                icon='md-cloud-done',
                style={
                    'fontSize': '18px'
                }
            )
        }
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
                        id='自定义节点图标',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'content': '模型训练'
                                    },
                                    {
                                        'content': '模型持久化'
                                    },
                                    {
                                        'content': '模型发布'
                                    }
                                ],
                                pending='处理中'
                            ),

                            fac.AntdDivider(
                                '末尾添加加载中状态节点',
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
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入'
        },
        {
            'content': '模型训练'
        },
        {
            'content': '模型持久化'
        },
        {
            'content': '模型发布'
        }
    ],
    pending='处理中'
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
                        id='末尾添加加载中状态节点',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'content': '模型训练'
                                    },
                                    {
                                        'content': '模型持久化'
                                    },
                                    {
                                        'content': '模型发布'
                                    }
                                ],
                                pending='处理中',
                                reverse=True
                            ),

                            fac.AntdDivider(
                                '翻转时间轴',
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
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入'
        },
        {
            'content': '模型训练'
        },
        {
            'content': '模型持久化'
        },
        {
            'content': '模型发布'
        }
    ],
    pending='处理中',
    reverse=True
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
                        id='翻转时间轴',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'label': '1小时前',
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'label': '58分钟前',
                                        'content': '模型训练'
                                    },
                                    {
                                        'label': '9分钟前',
                                        'content': '模型持久化'
                                    },
                                    {
                                        'label': '1分钟前',
                                        'content': '模型发布'
                                    }
                                ],
                                pending='处理中'
                            ),

                            fac.AntdDivider(
                                '为节点添加标签',
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
fac.AntdTimeline(
    items=[
        {
            'label': '1小时前',
            'content': '训练数据导入'
        },
        {
            'label': '58分钟前',
            'content': '模型训练'
        },
        {
            'label': '9分钟前',
            'content': '模型持久化'
        },
        {
            'label': '1分钟前',
            'content': '模型发布'
        }
    ],
    pending='处理中'
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
                        id='为节点添加标签',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'mode="right"（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'label': '1小时前',
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'label': '58分钟前',
                                        'content': '模型训练'
                                    },
                                    {
                                        'label': '9分钟前',
                                        'content': '模型持久化'
                                    },
                                    {
                                        'label': '1分钟前',
                                        'content': '模型发布'
                                    }
                                ],
                                pending='处理中'
                            ),

                            fac.AntdDivider(
                                'mode="alternate"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'label': '1小时前',
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'label': '58分钟前',
                                        'content': '模型训练'
                                    },
                                    {
                                        'label': '9分钟前',
                                        'content': '模型持久化'
                                    },
                                    {
                                        'label': '1分钟前',
                                        'content': '模型发布'
                                    }
                                ],
                                pending='处理中',
                                mode='alternate'
                            ),

                            fac.AntdDivider(
                                'mode="right"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTimeline(
                                items=[
                                    {
                                        'label': '1小时前',
                                        'content': '训练数据导入'
                                    },
                                    {
                                        'label': '58分钟前',
                                        'content': '模型训练'
                                    },
                                    {
                                        'label': '9分钟前',
                                        'content': '模型持久化'
                                    },
                                    {
                                        'label': '1分钟前',
                                        'content': '模型发布'
                                    }
                                ],
                                pending='处理中',
                                mode='right'
                            ),

                            fac.AntdDivider(
                                '不同的整体显示模式',
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
    'mode="right"（默认）',
    innerTextOrientation='left'
),
fac.AntdTimeline(
    items=[
        {
            'label': '1小时前',
            'content': '训练数据导入'
        },
        {
            'label': '58分钟前',
            'content': '模型训练'
        },
        {
            'label': '9分钟前',
            'content': '模型持久化'
        },
        {
            'label': '1分钟前',
            'content': '模型发布'
        }
    ],
    pending='处理中'
),

fac.AntdDivider(
    'mode="alternate"',
    innerTextOrientation='left'
),
fac.AntdTimeline(
    items=[
        {
            'label': '1小时前',
            'content': '训练数据导入'
        },
        {
            'label': '58分钟前',
            'content': '模型训练'
        },
        {
            'label': '9分钟前',
            'content': '模型持久化'
        },
        {
            'label': '1分钟前',
            'content': '模型发布'
        }
    ],
    pending='处理中',
    mode='alternate'
),

fac.AntdDivider(
    'mode="right"',
    innerTextOrientation='left'
),
fac.AntdTimeline(
    items=[
        {
            'label': '1小时前',
            'content': '训练数据导入'
        },
        {
            'label': '58分钟前',
            'content': '模型训练'
        },
        {
            'label': '9分钟前',
            'content': '模型持久化'
        },
        {
            'label': '1分钟前',
            'content': '模型发布'
        }
    ],
    pending='处理中',
    mode='right'
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
                        id='不同的整体显示模式',
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
                        {'title': '不同的节点状态色', 'href': '#不同的节点状态色'},
                        {'title': '自定义节点图标', 'href': '#自定义节点图标'},
                        {'title': '末尾添加加载中状态节点', 'href': '#末尾添加加载中状态节点'},
                        {'title': '翻转时间轴', 'href': '#翻转时间轴'},
                        {'title': '为节点添加标签', 'href': '#为节点添加标签'},
                        {'title': '不同的整体显示模式', 'href': '#不同的整体显示模式'}
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
                component_name='AntdTimeline',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
