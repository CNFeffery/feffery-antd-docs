from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCalendar
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
                                'title': 'AntdCalendar 日历'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染可交互的日历。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdCalendar(),

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
fac.AntdCalendar()
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
                            fac.AntdCalendar(
                                size='large'
                            ),

                            fac.AntdDivider(
                                '不同的尺寸规格',
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
fac.AntdCalendar(
    size='large'
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
                        id='不同的尺寸规格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdCalendar(
                                        id='calendar-demo',
                                        defaultValue='2023-01-01',
                                        style={
                                            'width': '300px'
                                        }
                                    ),
                                    fac.AntdParagraph(
                                        id='calendar-demo-output'
                                    )
                                ]
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdCalendar(
                                        id='calendar-format-demo',
                                        defaultValue='2023年01月01日',
                                        format='YYYY年MM月DD日',
                                        style={
                                            'width': '300px'
                                        }
                                    ),
                                    fac.AntdParagraph(
                                        id='calendar-format-demo-output'
                                    )
                                ]
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
        fac.AntdCalendar(
            id='calendar-demo',
            defaultValue='2023-01-01',
            style={
                'width': '300px'
            }
        ),
        fac.AntdParagraph(
            id='calendar-demo-output'
        )
    ]
),

fac.AntdSpace(
    [
        fac.AntdCalendar(
            id='calendar-format-demo',
            defaultValue='2023年01月01日',
            format='YYYY年MM月DD日',
            style={
                'width': '300px'
            }
        ),
        fac.AntdParagraph(
            id='calendar-format-demo-output'
        )
    ]
)

...

@app.callback(
    Output('calendar-demo-output', 'children'),
    Input('calendar-demo', 'value')
)
def calendar_demo(value):

    return f'value: {value}'


@app.callback(
    Output('calendar-format-demo-output', 'children'),
    Input('calendar-format-demo', 'value')
)
def calendar_format_demo(value):

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
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
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
                component_name='AntdCalendar',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
