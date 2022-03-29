from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTimeline(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTimeline.md', encoding='utf-8').read()
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
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
                            '不同的节点颜色状态',
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
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='不同的节点颜色状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTimeline(
                            items=[
                                {
                                    'content': '训练数据导入',
                                    'icon': 'md-cloud-upload',
                                    'iconStyle': {
                                        'fontSize': '18px'
                                    }
                                },
                                {
                                    'content': '模型训练',
                                    'icon': 'antd-clock-circle',
                                    'iconStyle': {
                                        'fontSize': '18px'
                                    }
                                },
                                {
                                    'content': '模型持久化',
                                    'icon': 'fc-accept-database',
                                    'iconStyle': {
                                        'fontSize': '18px'
                                    }
                                },
                                {
                                    'content': '模型发布',
                                    'icon': 'md-cloud-done',
                                    'iconStyle': {
                                        'fontSize': '18px'
                                    }
                                }
                            ],
                            style={
                                'marginLeft': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义节点图标及样式',
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
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': 'md-cloud-upload',
            'iconStyle': {
                'fontSize': '18px'
            }
        },
        {
            'content': '模型训练',
            'icon': 'antd-clock-circle',
            'iconStyle': {
                'fontSize': '18px'
            }
        },
        {
            'content': '模型持久化',
            'icon': 'fc-accept-database',
            'iconStyle': {
                'fontSize': '18px'
            }
        },
        {
            'content': '模型发布',
            'icon': 'md-cloud-done',
            'iconStyle': {
                'fontSize': '18px'
            }
        }
    ],
    style={
        'marginLeft': '20px'
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
                    id='自定义节点图标及样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTimeline(
                            items=[
                                {
                                    'content': '训练数据导入',
                                    'icon': 'md-cloud-upload'
                                },
                                {
                                    'content': '模型训练',
                                    'icon': 'antd-clock-circle'
                                },
                                {
                                    'content': '模型持久化',
                                    'icon': 'fc-accept-database'
                                }
                            ],
                            pending='模型发布中',
                            style={
                                'marginLeft': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '添加末端进行中节点',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　当设置了'),
                                fac.AntdText('pending', code=True),
                                fac.AntdText('时，时间轴的末尾会添加由虚线连接的表示进行中状态的节点')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': 'md-cloud-upload'
        },
        {
            'content': '模型训练',
            'icon': 'antd-clock-circle'
        },
        {
            'content': '模型持久化',
            'icon': 'fc-accept-database'
        }
    ],
    pending='模型发布中',
    style={
        'marginLeft': '20px'
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
                    id='添加末端进行中节点',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTimeline(
                            items=[
                                {
                                    'content': '训练数据导入',
                                    'icon': 'md-cloud-upload'
                                },
                                {
                                    'content': '模型训练',
                                    'icon': 'antd-clock-circle'
                                },
                                {
                                    'content': '模型持久化',
                                    'icon': 'fc-accept-database'
                                }
                            ],
                            pending='模型发布中',
                            reverse=True,
                            style={
                                'marginLeft': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '翻转坐标轴',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　默认的时间轴顺序是'),
                                fac.AntdText('自上往下', strong=True),
                                fac.AntdText('，如果你希望'),
                                fac.AntdText('自下往上', strong=True),
                                fac.AntdText('，可以设置参数'),
                                fac.AntdText('reverse=True', code=True)
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': 'md-cloud-upload'
        },
        {
            'content': '模型训练',
            'icon': 'antd-clock-circle'
        },
        {
            'content': '模型持久化',
            'icon': 'fc-accept-database'
        }
    ],
    pending='模型发布中',
    reverse=True,
    style={
        'marginLeft': '20px'
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
                    id='翻转坐标轴',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTitle('mode="left"（默认）', level=5),
                        fac.AntdTimeline(
                            items=[
                                {
                                    'content': '训练数据导入',
                                    'icon': 'md-cloud-upload',
                                    'label': '1小时前'
                                },
                                {
                                    'content': '模型训练',
                                    'icon': 'antd-clock-circle',
                                    'label': '58分钟前'
                                },
                                {
                                    'content': '模型持久化',
                                    'icon': 'fc-accept-database',
                                    'label': '17分钟前'
                                }
                            ],
                            pending='模型发布中',
                            reverse=True,
                            style={
                                'marginLeft': '20px'
                            }
                        ),

                        fac.AntdTitle('mode="right"', level=5),
                        fac.AntdTimeline(
                            items=[
                                {
                                    'content': '训练数据导入',
                                    'icon': 'md-cloud-upload',
                                    'label': '1小时前'
                                },
                                {
                                    'content': '模型训练',
                                    'icon': 'antd-clock-circle',
                                    'label': '58分钟前'
                                },
                                {
                                    'content': '模型持久化',
                                    'icon': 'fc-accept-database',
                                    'label': '17分钟前'
                                }
                            ],
                            mode='right',
                            pending='模型发布中',
                            reverse=True,
                            style={
                                'marginLeft': '20px'
                            }
                        ),

                        fac.AntdTitle('mode="alternate"', level=5),
                        fac.AntdTimeline(
                            items=[
                                {
                                    'content': '训练数据导入',
                                    'icon': 'md-cloud-upload',
                                    'label': '1小时前'
                                },
                                {
                                    'content': '模型训练',
                                    'icon': 'antd-clock-circle',
                                    'label': '58分钟前'
                                },
                                {
                                    'content': '模型持久化',
                                    'icon': 'fc-accept-database',
                                    'label': '17分钟前'
                                }
                            ],
                            mode='alternate',
                            pending='模型发布中',
                            reverse=True,
                            style={
                                'marginLeft': '20px'
                            }
                        ),

                        fac.AntdDivider(
                            '添加节点标签',
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
fac.AntdTitle('mode="left"（默认）', level=5),
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': 'md-cloud-upload',
            'label': '1小时前'
        },
        {
            'content': '模型训练',
            'icon': 'antd-clock-circle',
            'label': '58分钟前'
        },
        {
            'content': '模型持久化',
            'icon': 'fc-accept-database',
            'label': '17分钟前'
        }
    ],
    pending='模型发布中',
    reverse=True,
    style={
        'marginLeft': '20px'
    }
),

fac.AntdTitle('mode="right"', level=5),
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': 'md-cloud-upload',
            'label': '1小时前'
        },
        {
            'content': '模型训练',
            'icon': 'antd-clock-circle',
            'label': '58分钟前'
        },
        {
            'content': '模型持久化',
            'icon': 'fc-accept-database',
            'label': '17分钟前'
        }
    ],
    mode='right',
    pending='模型发布中',
    reverse=True,
    style={
        'marginLeft': '20px'
    }
),

fac.AntdTitle('mode="alternate"', level=5),
fac.AntdTimeline(
    items=[
        {
            'content': '训练数据导入',
            'icon': 'md-cloud-upload',
            'label': '1小时前'
        },
        {
            'content': '模型训练',
            'icon': 'antd-clock-circle',
            'label': '58分钟前'
        },
        {
            'content': '模型持久化',
            'icon': 'fc-accept-database',
            'label': '17分钟前'
        }
    ],
    mode='alternate',
    pending='模型发布中',
    reverse=True,
    style={
        'marginLeft': '20px'
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
                    id='添加节点标签',
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
                            {'title': '不同的节点颜色状态', 'href': '#不同的节点颜色状态'},
                            {'title': '自定义节点图标及样式', 'href': '#自定义节点图标及样式'},
                            {'title': '添加末端进行中节点', 'href': '#添加末端进行中节点'},
                            {'title': '翻转坐标轴', 'href': '#翻转坐标轴'},
                            {'title': '添加节点标签', 'href': '#添加节点标签'},
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
