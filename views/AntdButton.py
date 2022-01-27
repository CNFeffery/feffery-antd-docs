from dash import html
from dash import dcc
import feffery_antd_components as fac
import feffery_markdown_components as fmc
import feffery_utils_components as fuc

import callbacks.AntdButton

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdButton(children, id, className, style, **kwargs)',
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
                    '主要参数说明',
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
                    markdownStr=open('documents/AntdButton.md', encoding='utf-8').read()
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
                        html.Div(
                            [
                                fac.AntdButton('default'),
                                fac.AntdButton('primary', type='primary'),
                                fac.AntdButton('dashed', type='dashed'),
                                fac.AntdButton('link', type='link'),
                                fac.AntdButton('text', type='text')
                            ]
                        ),

                        fac.AntdDivider(
                            '不同type对应按钮样式风格',
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
    [
        fac.AntdButton('default'),
        fac.AntdButton('primary', type='primary'),
        fac.AntdButton('dashed', type='dashed'),
        fac.AntdButton('link', type='link'),
        fac.AntdButton('text', type='text')
    ]
)'''
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
                    id='不同type对应按钮样式风格',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdButton('feffery-antd-components',
                                       href='https://github.com/CNFeffery/feffery-antd-components',
                                       target='_blank',
                                       type='primary'),

                        fac.AntdDivider(
                            '充当跳转功能使用',
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
fac.AntdButton(href='https://github.com/CNFeffery/feffery-antd-components',
               target='_blank')'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='充当跳转功能使用',
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdButton('feffery-antd-components',
                                       block=True,
                                       type='primary'),

                        fac.AntdDivider(
                            '撑满父级元素宽度',
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
fac.AntdButton('feffery-antd-components',
               block=True,
               type='primary')'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='撑满父级元素宽度',
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdButton('default', danger=True),
                                fac.AntdButton('primary', type='primary', danger=True),
                                fac.AntdButton('dashed', type='dashed', danger=True),
                                fac.AntdButton('link', type='link', danger=True),
                                fac.AntdButton('text', type='text', danger=True)
                            ]
                        ),

                        fac.AntdDivider(
                            '显示为危险警告状态',
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
    [
        fac.AntdButton('default', danger=True),
        fac.AntdButton('primary', type='primary', danger=True),
        fac.AntdButton('dashed', type='dashed', danger=True),
        fac.AntdButton('link', type='link', danger=True),
        fac.AntdButton('text', type='text', danger=True)
    ]
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='显示为危险警告状态',
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdButton('default', disabled=True),
                                fac.AntdButton('primary', type='primary', disabled=True),
                                fac.AntdButton('dashed', type='dashed', disabled=True),
                                fac.AntdButton('link', type='link', disabled=True),
                                fac.AntdButton('text', type='text', disabled=True)
                            ]
                        ),

                        fac.AntdDivider(
                            '显示为不可点击状态',
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
    [
        fac.AntdButton('default', disabled=True),
        fac.AntdButton('primary', type='primary', disabled=True),
        fac.AntdButton('dashed', type='dashed', disabled=True),
        fac.AntdButton('link', type='link', disabled=True),
        fac.AntdButton('text', type='text', disabled=True)
    ]
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='显示为不可点击状态',
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    className='div-highlight'
                ),

                html.Div(
                    [

                        html.Div(
                            [
                                fac.AntdButton('默认', type='primary'),
                                fac.AntdButton('circle', shape='circle', type='primary'),
                                fac.AntdButton('round', shape='round', type='primary')
                            ]
                        ),

                        fac.AntdDivider(
                            '修改按钮形状',
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
    [
        fac.AntdButton('默认'),
        fac.AntdButton('circle', shape='circle'),
        fac.AntdButton('round', shape='round')
    ]
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='修改按钮形状',
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    [
                                        fac.AntdIcon(
                                            icon='md-power-settings-new'
                                        ),
                                        'md-power-settings-new'
                                    ]
                                ),
                                fac.AntdButton(
                                    [
                                        fac.AntdIcon(
                                            icon='md-layers'
                                        ),
                                        'md-layers'
                                    ],
                                    type='primary'
                                ),
                                fac.AntdButton(
                                    [
                                        fac.AntdIcon(
                                            icon='fc-repair'
                                        ),
                                        'fc-repair'
                                    ],
                                    type='dashed'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '配合AntdIcon添加图标',
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
fac.AntdSpace(
    [
        fac.AntdButton(
            [
                fac.AntdIcon(
                    icon='md-power-settings-new'
                ),
                'md-power-settings-new'
            ]
        ),
        fac.AntdButton(
            [
                fac.AntdIcon(
                    icon='md-layers'
                ),
                'md-layers'
            ],
            type='primary'
        ),
        fac.AntdButton(
            [
                fac.AntdIcon(
                    icon='fc-repair'
                ),
                'fc-repair'
            ],
            type='dashed'
        )
    ]
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='配合AntdIcon添加图标',
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdButton('点我点我', type='primary', id='button-demo'),
                        html.Br(),
                        fac.AntdSpin(
                            html.Em(id='button-demo-output'),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            innerTextOrientation='left',
                            lineColor='#f0f0f0'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdButton('点我点我', type='primary', id='button-demo'),
html.Br(),
html.Em(id='button-demo-output')
...
@app.callback(
    Output('button-demo-output', 'children'),
    Input('button-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_callback_demo(nClicks):

    return nClicks'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    id='回调示例',
                    style={
                        'marginBottom': '80px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
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
                            {'title': '不同type对应按钮样式风格', 'href': '#不同type对应按钮样式风格'},
                            {'title': '充当跳转功能使用', 'href': '#充当跳转功能使用'},
                            {'title': '撑满父级元素宽度', 'href': '#撑满父级元素宽度'},
                            {'title': '显示为危险警告状态', 'href': '#显示为危险警告状态'},
                            {'title': '显示为不可点击状态', 'href': '#显示为不可点击状态'},
                            {'title': '修改按钮形状', 'href': '#修改按钮形状'},
                            {'title': '配合AntdIcon添加图标', 'href': '#配合AntdIcon添加图标'},
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
