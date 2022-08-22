from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTimePicker

docs_content = html.Div(
    [
        html.Div(
            [

                html.H2(
                    'AntdTimePicker(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTimePicker.md', encoding='utf-8').read()
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
                        fac.AntdTimePicker(
                            allowClear=True
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
fac.AntdTimePicker(
    allowClear=True
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
                        fac.AntdTimePicker(
                            allowClear=True,
                            hourStep=3,
                            minuteStep=10,
                            secondStep=10
                        ),

                        fac.AntdDivider(
                            '调整时间粒度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTimePicker(
    allowClear=True,
    hourStep=3,
    minuteStep=10,
    secondStep=10
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
                    id='调整时间粒度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTimePicker(
                            allowClear=True,
                            use12Hours=True
                        ),

                        fac.AntdDivider(
                            '12小时制',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTimePicker(
    allowClear=True,
    use12Hours=True
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
                    id='12小时制',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTimePicker(
                            allowClear=True,
                            format='hh时mm分ss秒',
                            defaultValue='18时16分21秒'
                        ),

                        fac.AntdDivider(
                            '自定义format',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdTimePicker(
    allowClear=True,
    format='hh时mm分ss秒',
    defaultValue='18时16分21秒'
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
                    id='自定义format',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdSpin(
                            [
                                html.Div(
                                    id='time-picker-demo-output'
                                ),
                                fac.AntdTimePicker(
                                    id='time-picker-demo',
                                    allowClear=True,
                                    format='hh时mm分ss秒'
                                )
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        html.Div(
            id='time-picker-demo-output'
        ),
        fac.AntdTimePicker(
            id='time-picker-demo',
            allowClear=True,
            format='hh时mm分ss秒'
        )
    ],
    text='回调中'
)
...
@app.callback(
    Output('time-picker-demo-output', 'children'),
    Input('time-picker-demo', 'value'),
    prevent_initial_call=True
)
def time_picker_demo_callback(value):
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
                            {'title': '调整时间粒度', 'href': '#调整时间粒度'},
                            {'title': '12小时制', 'href': '#12小时制'},
                            {'title': '自定义format', 'href': '#自定义format'},
                            {'title': '回调示例', 'href': '#回调示例'},
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
