from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdTimePicker
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
                                'title': 'AntdTimePicker 时间选择框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供时间选择功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTimePicker(
                                placeholder='请选择时间'
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
fac.AntdTimePicker(
    placeholder='请选择时间'
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
                                    fac.AntdTimePicker(
                                        placeholder=f'placement="{placement}"',
                                        placement=placement,
                                        style={
                                            'width': 220
                                        }
                                    )
                                    for placement in [
                                        'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
                                    ]
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '不同的悬浮层展开方位',
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
        fac.AntdTimePicker(
            placeholder=f'placement="{placement}"',
            placement=placement,
            style={
                'width': 220
            }
        )
        for placement in [
            'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
        ]
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
                        id='不同的悬浮层展开方位',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimePicker(
                                format='HH点mm分ss秒',
                                defaultValue='12点18分17秒'
                            ),

                            fac.AntdDivider(
                                '自定义format',
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
fac.AntdTimePicker(
    format='HH点mm分ss秒',
    defaultValue='12点18分17秒'
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
                        id='自定义format',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimePicker(
                                defaultValue='12:00:19',
                                disabled=True
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
fac.AntdTimePicker(
    defaultValue='12:00:19',
    disabled=True
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
                            fac.AntdTimePicker(
                                defaultValue='12:00:19',
                                readOnly=True
                            ),

                            fac.AntdDivider(
                                '只读状态',
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
fac.AntdTimePicker(
    defaultValue='12:00:19',
    readOnly=True
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
                        id='只读状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTimePicker(
                                        placeholder='status="warning"',
                                        status='warning',
                                        style={
                                            'width': 200
                                        }
                                    ),

                                    fac.AntdTimePicker(
                                        placeholder='status="error"',
                                        status='error',
                                        style={
                                            'width': 200
                                        }
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '强制状态渲染',
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
        fac.AntdTimePicker(
            placeholder='status="warning"',
            status='warning',
            style={
                'width': 200
            }
        ),

        fac.AntdTimePicker(
            placeholder='status="error"',
            status='error',
            style={
                'width': 200
            }
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
                        id='强制状态渲染',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimePicker(
                                hourStep=3,
                                minuteStep=10,
                                secondStep=20
                            ),

                            fac.AntdDivider(
                                '设置各部分时间间隔',
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
fac.AntdTimePicker(
    hourStep=3,
    minuteStep=10,
    secondStep=20
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
                        id='设置各部分时间间隔',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTimePicker(
                                use12Hours=True
                            ),

                            fac.AntdDivider(
                                '12小时制',
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
fac.AntdTimePicker(
    use12Hours=True
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
                        id='12小时制',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSpace(
                                        [
                                            fac.AntdTimePicker(
                                                id='time-picker-demo',
                                                defaultValue='06:00:00'
                                            ),
                                            fac.AntdText(
                                                id='time-picker-demo-output'
                                            )
                                        ],
                                        align='center'
                                    ),

                                    fac.AntdSpace(
                                        [
                                            fac.AntdTimePicker(
                                                id='time-picker-format-demo',
                                                defaultValue='06时00分00秒',
                                                format='HH时mm分ss秒'
                                            ),
                                            fac.AntdText(
                                                id='time-picker-format-demo-output'
                                            )
                                        ],
                                        align='center'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
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
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdTimePicker(
                    id='time-picker-demo',
                    defaultValue='06:00:00'
                ),
                fac.AntdText(
                    id='time-picker-demo-output'
                )
            ],
            align='center'
        ),

        fac.AntdSpace(
            [
                fac.AntdTimePicker(
                    id='time-picker-format-demo',
                    defaultValue='06时00分00秒',
                    format='HH时mm分ss秒'
                ),
                fac.AntdText(
                    id='time-picker-format-demo-output'
                )
            ],
            align='center'
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

@app.callback(
    Output('time-picker-demo-output', 'children'),
    Input('time-picker-demo', 'value')
)
def time_picker_demo(value):

    return f'value: {value}'


@app.callback(
    Output('time-picker-format-demo-output', 'children'),
    Input('time-picker-format-demo', 'value')
)
def time_picker_format_demo(value):

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
                        {'title': '不同的悬浮层展开方位', 'href': '#不同的悬浮层展开方位'},
                        {'title': '自定义format', 'href': '#自定义format'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                        {'title': '设置各部分时间间隔', 'href': '#设置各部分时间间隔'},
                        {'title': '12小时制', 'href': '#12小时制'},
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
                component_name='AntdTimePicker',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
