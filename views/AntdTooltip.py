from dash import html
import feffery_utils_components as fuc
import feffery_antd_components as fac

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTooltip(children, id, className, style, *args, **kwargs)',
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

                fuc.FefferyMarkdown(
                    markdownStr=open('documents/AntdTooltip.md', encoding='utf-8').read()
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
                        fac.AntdTooltip(
                            fac.AntdButton(
                                '请将鼠标悬浮于此',
                                type='primary'
                            ),
                            title='这是一段AntdTooltip提示示例'
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
fac.AntdTooltip(
    fac.AntdButton(
        '请将鼠标悬浮于此',
        type='primary'
    ),
    title='这是一段AntdTooltip提示示例'
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
                                fac.AntdTooltip(
                                    fac.AntdButton(
                                        'hover事件',
                                        type='primary'
                                    ),
                                    title='这是一段AntdTooltip提示示例'
                                ),

                                fac.AntdTooltip(
                                    fac.AntdButton(
                                        'click事件',
                                        type='primary'
                                    ),
                                    title='这是一段AntdTooltip提示示例',
                                    trigger='click'
                                ),

                                fac.AntdTooltip(
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
        fac.AntdTooltip(
            fac.AntdButton(
                'hover事件',
                type='primary'
            ),
            title='这是一段AntdTooltip提示示例'
        ),

        fac.AntdTooltip(
            fac.AntdButton(
                'click事件',
                type='primary'
            ),
            title='这是一段AntdTooltip提示示例',
            trigger='click'
        ),

        fac.AntdTooltip(
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
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
            ),
            style={
                'flex': 'none',
                'margin': 'none'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
