from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

from server import app

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdAlert(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdAlert.md', encoding='utf-8').read()
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
                                fac.AntdAlert(message='这是一条alert测试')
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
html.Div(
    [
        fac.AntdAlert(message='这是一条alert测试')
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAlert(message='默认info状态'),
                                html.Br(),
                                fac.AntdAlert(message='success状态', type='success'),
                                html.Br(),
                                fac.AntdAlert(message='warning状态', type='warning'),
                                html.Br(),
                                fac.AntdAlert(message='error状态', type='error'),
                            ]
                        ),

                        fac.AntdDivider(
                            '不同的状态类型',
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
        fac.AntdAlert(message='默认info状态'),
        html.Br(),
        fac.AntdAlert(message='success状态', type='success'),
        html.Br(),
        fac.AntdAlert(message='warning状态', type='warning'),
        html.Br(),
        fac.AntdAlert(message='error状态', type='error'),
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
                    id='不同的状态类型',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAlert(message='默认info状态', showIcon=True),
                                html.Br(),
                                fac.AntdAlert(message='success状态', type='success', showIcon=True),
                                html.Br(),
                                fac.AntdAlert(message='warning状态', type='warning', showIcon=True),
                                html.Br(),
                                fac.AntdAlert(message='error状态', type='error', showIcon=True),
                            ]
                        ),

                        fac.AntdDivider(
                            '添加状态图标',
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
        fac.AntdAlert(message='默认info状态', showIcon=True),
        html.Br(),
        fac.AntdAlert(message='success状态', type='success', showIcon=True),
        html.Br(),
        fac.AntdAlert(message='warning状态', type='warning', showIcon=True),
        html.Br(),
        fac.AntdAlert(message='error状态', type='error', showIcon=True),
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
                    id='添加状态图标',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAlert(message='默认info状态', showIcon=True, closable=True)
                            ]
                        ),

                        fac.AntdDivider(
                            '添加关闭按钮',
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
        fac.AntdAlert(message='默认info状态', showIcon=True, closable=True)
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
                    id='添加关闭按钮',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAlert(
                                    '这是一段辅助说明文字',
                                    message=[
                                        '君不见黄河之水天上来',
                                        '奔流到海不复回',
                                        '君不见高堂明镜悲白发',
                                        '朝如青丝暮成雪',
                                        '人生得意须尽欢',
                                        '莫使金樽空对月',
                                        '天生我材必有用',
                                        '千金散尽还复来'
                                    ],
                                    showIcon=True,
                                    messageRenderMode='loop-text'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '轮播模式示例',
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
        fac.AntdAlert(
            '这是一段辅助说明文字',
            message=[
                '君不见黄河之水天上来',
                '奔流到海不复回',
                '君不见高堂明镜悲白发',
                '朝如青丝暮成雪',
                '人生得意须尽欢',
                '莫使金樽空对月',
                '天生我材必有用',
                '千金散尽还复来'
            ],
            showIcon=True,
            messageRenderMode='loop-text'
        )
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
                    id='轮播模式示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAlert(
                                    '这是一段辅助说明文字',
                                    message='，'.join([
                                        '君不见黄河之水天上来',
                                        '奔流到海不复回',
                                        '君不见高堂明镜悲白发',
                                        '朝如青丝暮成雪',
                                        '人生得意须尽欢',
                                        '莫使金樽空对月',
                                        '天生我材必有用',
                                        '千金散尽还复来'
                                    ]) + '。',
                                    description='这是跑马灯模式示例',
                                    showIcon=True,
                                    messageRenderMode='marquee'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            '跑马灯模式示例',
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
        fac.AntdAlert(
            '这是一段辅助说明文字',
            message='，'.join([
                '君不见黄河之水天上来',
                '奔流到海不复回',
                '君不见高堂明镜悲白发',
                '朝如青丝暮成雪',
                '人生得意须尽欢',
                '莫使金樽空对月',
                '天生我材必有用',
                '千金散尽还复来'
            ]) + '。',
            description='这是跑马灯模式示例',
            showIcon=True,
            messageRenderMode='marquee'
        )
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
                    id='跑马灯模式示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            [
                                fac.AntdAlert(
                                    showIcon=True,
                                    message=html.Span(
                                        [
                                            fac.AntdText(
                                                '这是组件型message参数示例，'
                                            ),
                                            fac.AntdButton(
                                                '点我试试',
                                                id='alert-message-button-input',
                                                type='primary',
                                                size='small'
                                            )
                                        ]
                                    ),
                                    description=html.Span(
                                        [
                                            fac.AntdText(
                                                '这是组件型description参数示例，上面的按钮被点了0次',
                                                id='alert-description-output'
                                            ),
                                        ]
                                    )
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            'message与description接受组件型输入',
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
fac.AntdAlert(
    showIcon=True,
    message=html.Span(
        [
            fac.AntdText(
                '这是组件型message参数示例，'
            ),
            fac.AntdButton(
                '点我试试',
                id='alert-message-button-input',
                type='primary',
                size='small'
            )
        ]
    ),
    description=html.Span(
        [
            fac.AntdText(
                '这是组件型description参数示例，上面的按钮被点了0次',
                id='alert-description-output'
            ),
        ]
    )
)

...

@app.callback(
    Output('alert-description-output', 'children'),
    Input('alert-message-button-input', 'nClicks'),
    prevent_initial_call=True
)
def alert_message_description_callback_demo(nClicks):
    return f'这是组件型description参数示例，上面的按钮被点了{nClicks}次'
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
                    id='message与description接受组件型输入',
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
                            {'title': '不同的状态类型', 'href': '#不同的状态类型'},
                            {'title': '添加状态图标', 'href': '#添加状态图标'},
                            {'title': '添加关闭按钮', 'href': '#添加关闭按钮'},
                            {'title': '轮播模式示例', 'href': '#轮播模式示例'},
                            {'title': '跑马灯模式示例', 'href': '#跑马灯模式示例'},
                            {'title': 'message与description接受组件型输入', 'href': '#message与description接受组件型输入'},
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


@app.callback(
    Output('alert-description-output', 'children'),
    Input('alert-message-button-input', 'nClicks'),
    prevent_initial_call=True
)
def alert_message_description_callback_demo(nClicks):
    return f'这是组件型description参数示例，上面的按钮被点了{nClicks}次'
