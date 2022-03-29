from dash import html
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdPopover(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdPopover.md', encoding='utf-8').read()
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
                        fac.AntdPopover(
                            fac.AntdButton(
                                '请将鼠标悬浮于此',
                                type='primary'
                            ),
                            title='这是一段AntdTooltip提示示例',
                            content=[
                                fac.AntdParagraph(
                                    [
                                        fac.AntdText('　　配合'),
                                        fac.AntdText('AntdPopover', strong=True),
                                        fac.AntdText('的'),
                                        fac.AntdText('content', code=True),
                                        fac.AntdText('参数，可实现比'),
                                        fac.AntdText('AntdTooltip', strong=True),
                                        fac.AntdText('更加丰富自由的提示框内容渲染')
                                    ]
                                )
                            ],
                            overlayStyle={
                                'width': '350px'
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdPopover', strong=True),
                                fac.AntdText('中可通过'),
                                fac.AntdText('content', strong=True),
                                fac.AntdText('参数传入列表格式的'),
                                fac.AntdText('其他组件元素，作为气泡卡片中内容区元素进行渲染')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdPopover(
    fac.AntdButton(
        '请将鼠标悬浮于此',
        type='primary'
    ),
    title='这是一段AntdTooltip提示示例',
    content=[
        fac.AntdParagraph(
            [
                fac.AntdText('　　配合'),
                fac.AntdText('AntdPopover', strong=True),
                fac.AntdText('的'),
                fac.AntdText('content', code=True),
                fac.AntdText('参数，可实现比'),
                fac.AntdText('AntdTooltip', strong=True),
                fac.AntdText('更加丰富自由的提示框内容渲染')
            ]
        )
    ],
    overlayStyle={
        'width': '350px'
    }
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
                        fac.AntdSpace(
                            [
                                fac.AntdPopover(
                                    fac.AntdButton(
                                        'hover事件',
                                        type='primary'
                                    ),
                                    title='这是一段AntdTooltip提示示例'
                                ),

                                fac.AntdPopover(
                                    fac.AntdButton(
                                        'click事件',
                                        type='primary'
                                    ),
                                    title='这是一段AntdTooltip提示示例',
                                    trigger='click'
                                ),

                                fac.AntdPopover(
                                    fac.AntdInput(
                                        placeholder='focus事件',
                                        style={
                                            'width': '150px'
                                        }
                                    ),
                                    title='这是一段AntdTooltip提示示例',
                                    trigger='focus'
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '不同的触发行为',
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
        fac.AntdPopover(
            fac.AntdButton(
                'hover事件',
                type='primary'
            ),
            title='这是一段AntdTooltip提示示例'
        ),

        fac.AntdPopover(
            fac.AntdButton(
                'click事件',
                type='primary'
            ),
            title='这是一段AntdTooltip提示示例',
            trigger='click'
        ),

        fac.AntdPopover(
            fac.AntdInput(
                placeholder='focus事件',
                style={
                    'width': '150px'
                }
            ),
            title='这是一段AntdTooltip提示示例',
            trigger='focus'
        )
    ],
    direction='vertical'
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
                    id='不同的触发行为',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPopover(
                            fac.AntdButton(
                                '鼠标悬浮于此',
                                type='primary'
                            ),
                            title={
                                'content': '标题前缀图标测试',
                                'prefixIcon': 'antd-search'
                            }
                        ),

                        fac.AntdDivider(
                            '为title自定义前缀图标',
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
fac.AntdPopover(
    fac.AntdButton(
        '鼠标悬浮于此',
        type='primary'
    ),
    title={
        'content': '标题前缀图标测试',
        'prefixIcon': 'antd-search'
    }
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
                    id='为title自定义前缀图标',
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
                            {'title': '不同的触发行为', 'href': '#不同的触发行为'},
                            {'title': '为title自定义前缀图标', 'href': '#为title自定义前缀图标'},
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
