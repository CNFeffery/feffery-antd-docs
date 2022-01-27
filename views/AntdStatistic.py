from dash import html, dcc
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdStatistic

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdStatistic(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdStatistic.md', encoding='utf-8').read()
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
                        fac.AntdStatistic(
                            title='统计数值示例',
                            value=1332971
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
fac.AntdStatistic(
    title='统计数值示例',
    value=1332971
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
                        fac.AntdStatistic(
                            title='统计数值示例',
                            value=1332971,
                            suffix={
                                'mode': 'text',
                                'content': '人次'
                            }
                        ),

                        fac.AntdStatistic(
                            title='统计数值示例',
                            value=1332971,
                            prefix={
                                'mode': 'icon',
                                'content': 'fc-statistics'
                            }
                        ),

                        fac.AntdStatistic(
                            title='统计数值示例',
                            value=1332971,
                            prefix={
                                'mode': 'icon',
                                'content': 'md-insert-chart'
                            }
                        ),

                        fac.AntdDivider(
                            '添加前后缀额外内容',
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
fac.AntdStatistic(
    title='统计数值示例',
    value=1332971,
    suffix={
        'mode': 'text',
        'content': '人次'
    }
),

fac.AntdStatistic(
    title='统计数值示例',
    value=1332971,
    prefix={
        'mode': 'icon',
        'content': 'fc-statistics'
    }
),

fac.AntdStatistic(
    title='统计数值示例',
    value=1332971,
    prefix={
        'mode': 'icon',
        'content': 'md-insert-chart'
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
                    id='添加前后缀额外内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdStatistic(
                            title='统计数值示例',
                            value=1332971,
                            valueStyle={
                                'color': 'blue',
                                'fontSize': '28px'
                            },
                            prefix={
                                'mode': 'icon',
                                'content': 'fc-statistics'
                            },
                            suffix={
                                'mode': 'text',
                                'content': '人次'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义数值样式',
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
fac.AntdStatistic(
    title='统计数值示例',
    value=1332971,
    valueStyle={
        'color': 'blue',
        'fontSize': '28px'
    },
    prefix={
        'mode': 'icon',
        'content': 'fc-statistics'
    },
    suffix={
        'mode': 'text',
        'content': '人次'
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
                    id='自定义数值样式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdStatistic(
                            id='statistic-demo',
                            precision=2,
                            title='XX股份实时股价',
                            value=675.32,
                            valueStyle={
                                'color': '#cf1322'
                            },
                            prefix={
                                'mode': 'icon',
                                'content': 'rise'
                            }
                        ),

                        dcc.Interval(
                            id='statistic-interval-demo',
                            n_intervals=0
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
fac.AntdStatistic(
    id='statistic-demo',
    precision=2,
    title='XX股份实时股价',
    value=675.32,
    valueStyle={
        'color': '#cf1322'
    },
    prefix={
        'mode': 'icon',
        'content': 'rise'
    }
),

dcc.Interval(
    id='statistic-interval-demo',
    n_intervals=0
)
...
@app.callback(
    [Output('statistic-demo', 'value'),
     Output('statistic-demo', 'prefix'),
     Output('statistic-demo', 'valueStyle')],
    Input('statistic-interval-demo', 'n_intervals'),
    State('statistic-demo', 'value')
)
def statistic_demo_callback(n_intervals, value):
    new_value = value + np.random.randn()

    if new_value >= value:
        return [
            new_value,
            {
                'mode': 'icon',
                'content': 'rise'
            },
            {
                'color': '#cf1322'
            }
        ]

    else:
        return [
            new_value,
            {
                'mode': 'icon',
                'content': 'fall'
            },
            {
                'color': '#3f8600'
            }
        ]
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
                    id='回调示例',
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
                            {'title': '添加前后缀额外内容', 'href': '#添加前后缀额外内容'},
                            {'title': '自定义数值样式', 'href': '#自定义数值样式'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
            ),
            style={
                'flex': 'none',
                'padding': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
