from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdCalendar

docs_content = html.Div(
    [
        html.Div(
            [

                html.H2(
                    'AntdCalendar(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCalendar.md', encoding='utf-8').read()
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
                        fac.AntdDivider('size="default"（默认）', innerTextOrientation='left'),
                        fac.AntdCalendar(),
                        fac.AntdDivider('size="large"', innerTextOrientation='left'),
                        fac.AntdCalendar(
                            size='large'
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
fac.AntdDivider('size="default"（默认）', innerTextOrientation='left'),
fac.AntdCalendar(),
fac.AntdDivider('size="large"', innerTextOrientation='left'),
fac.AntdCalendar(
    size='large'
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
                        html.Div(
                            fac.AntdCalendar(),
                            style={
                                'width': '300px'
                            }
                        ),

                        html.Div(
                            fac.AntdCalendar(),
                            style={
                                'width': '500px'
                            }
                        ),

                        fac.AntdDivider(
                            '默认尺寸下日历宽度自适应容器大小',
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
    fac.AntdCalendar(),
    style={
        'width': '300px'
    }
),

html.Div(
    fac.AntdCalendar(),
    style={
        'width': '500px'
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
                    id='默认尺寸下日历宽度自适应容器大小',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdCalendar(
                                id='calendar-demo',
                                defaultValue='2022-01-01'
                            ),
                            style={
                                'width': '300px'
                            }
                        ),

                        html.Div(
                            id='calendar-demo-output'
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
html.Div(
    fac.AntdCalendar(
        id='calendar-demo',
        defaultValue='2022-01-01'
    ),
    style={
        'width': '300px'
    }
),

html.Div(
    id='calendar-demo-output'
)
...
@app.callback(
    Output('calendar-demo-output', 'children'),
    Input('calendar-demo', 'value')
)
def calendar_demo_callback(value):
    return [
        fac.AntdText('value: ', strong=True),
        fac.AntdText(value)
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
                            {'title': '默认尺寸下日历宽度自适应容器大小', 'href': '#默认尺寸下日历宽度自适应容器大小'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
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
