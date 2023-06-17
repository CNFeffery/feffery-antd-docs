from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdAlert
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
                                'title': 'AntdAlert 警告提示'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染不同状态类型的警告提示信息。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdAlert(
                                        message='这是一条警告提示示例'
                                    ),
                                    fac.AntdAlert(
                                        message='这是一条警告提示示例',
                                        description='这是一段辅助说明文字'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
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
fac.AntdSpace(
    [
        fac.AntdAlert(
            message='这是一条警告提示示例'
        ),
        fac.AntdAlert(
            message='这是一条警告提示示例',
            description='这是一段辅助说明文字'
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
                        id='基础使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdAlert(
                                        message=f'type="{type_}"示例',
                                        type=type_
                                    )
                                    for type_ in [
                                        'info', 'success', 'warning', 'error'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '不同的状态类型',
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
        fac.AntdAlert(
            message=f'type="{type_}"示例',
            type=type_
        )
        for type_ in [
            'info', 'success', 'warning', 'error'
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
                        id='不同的状态类型',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdAlert(
                                        message=f'type="{type_}"示例',
                                        type=type_,
                                        showIcon=True
                                    )
                                    for type_ in [
                                        'info', 'success', 'warning', 'error'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '添加状态图标',
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
        fac.AntdAlert(
            message=f'type="{type_}"示例',
            type=type_,
            showIcon=True
        )
        for type_ in [
            'info', 'success', 'warning', 'error'
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
                        id='添加状态图标',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAlert(
                                message=f'可关闭警告提示示例',
                                showIcon=True,
                                closable=True
                            ),

                            fac.AntdDivider(
                                '添加关闭按钮',
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
fac.AntdAlert(
    message=f'可关闭警告提示示例',
    showIcon=True,
    closable=True
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
                        id='添加关闭按钮',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAlert(
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
                                description='轮播模式示例',
                                showIcon=True,
                                messageRenderMode='loop-text'
                            ),

                            fac.AntdDivider(
                                '轮播模式',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '当开启轮播模式时，参数',
                                    fac.AntdText(
                                        'message',
                                        code=True
                                    ),
                                    '需要传入数组型以便进行轮播'
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
fac.AntdAlert(
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
    description='轮播模式示例',
    showIcon=True,
    messageRenderMode='loop-text'
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
                        id='轮播模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAlert(
                                message='，'.join(
                                    [
                                        '君不见黄河之水天上来',
                                        '奔流到海不复回',
                                        '君不见高堂明镜悲白发',
                                        '朝如青丝暮成雪',
                                        '人生得意须尽欢',
                                        '莫使金樽空对月',
                                        '天生我材必有用',
                                        '千金散尽还复来。'
                                    ]
                                ),
                                description='这是走马灯模式示例',
                                showIcon=True,
                                messageRenderMode='marquee'
                            ),

                            fac.AntdDivider(
                                '走马灯模式',
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
fac.AntdAlert(
    message='，'.join(
        [
            '君不见黄河之水天上来',
            '奔流到海不复回',
            '君不见高堂明镜悲白发',
            '朝如青丝暮成雪',
            '人生得意须尽欢',
            '莫使金樽空对月',
            '天生我材必有用',
            '千金散尽还复来。'
        ]
    ),
    description='这是走马灯模式示例',
    showIcon=True,
    messageRenderMode='marquee'
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
                        id='走马灯模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAlert(
                                showIcon=True,
                                message=fac.AntdSpace(
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
                                    ],
                                    size=0
                                ),
                                description=fac.AntdText(
                                    '这是组件型description参数示例，上面的按钮被点了0次',
                                    id='alert-description-output'
                                )
                            ),

                            fac.AntdDivider(
                                '组件型message与description',
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
fac.AntdAlert(
    showIcon=True,
    message=fac.AntdSpace(
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
        ],
        size=0
    ),
    description=fac.AntdText(
        '这是组件型description参数示例，上面的按钮被点了0次',
        id='alert-description-output'
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
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='组件型message与description',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdAlert(
                                message='这是一条警告提示示例',
                                action=fac.AntdButton(
                                    'action示例',
                                    type='primary'
                                )
                            ),

                            fac.AntdDivider(
                                '右上角添加额外元素',
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
fac.AntdAlert(
    message='这是一条警告提示示例',
    action=fac.AntdButton(
        'action示例',
        type='primary'
    )
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
                        id='右上角添加额外元素',
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
                        {'title': '不同的状态类型', 'href': '#不同的状态类型'},
                        {'title': '添加状态图标', 'href': '#添加状态图标'},
                        {'title': '添加关闭按钮', 'href': '#添加关闭按钮'},
                        {'title': '轮播模式', 'href': '#轮播模式'},
                        {'title': '走马灯模式', 'href': '#走马灯模式'},
                        {
                            'title': '组件型message与description',
                            'href': '#组件型message与description'
                        },
                        {'title': '右上角添加额外元素', 'href': '#右上角添加额外元素'},
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
                component_name='AntdAlert',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
