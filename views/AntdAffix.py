from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdAffix(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdAffix.md', encoding='utf-8').read()
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
                            fac.AntdAffix(
                                fac.AntdButton(
                                    '向下滑动页面体验固钉效果',
                                    type='primary'
                                ),
                                offsetTop=100,
                                target='docs-content'
                            ),
                            style={
                                'marginBottom': '1000px'
                            }
                        ),

                        fac.AntdDivider(
                            '下滑固钉示例',
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
    fac.AntdAffix(
        fac.AntdButton(
            '向下滑动页面体验固钉效果',
            type='primary'
        ),
        offsetTop=100,
        target='docs-content'
    ),
    style={
        'marginBottom': '1000px'
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
                    id='下滑固钉示例',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        html.Div(
                            fac.AntdAffix(
                                fac.AntdButton(
                                    '向上滑动页面体验固钉效果',
                                    type='dashed'
                                ),
                                offsetBottom=100,
                                target='docs-content',
                                style={
                                    'float': 'right'
                                }
                            ),
                            style={
                                'marginTop': '1000px'
                            }
                        ),

                        fac.AntdDivider(
                            '上滑固钉示例',
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
    fac.AntdAffix(
        fac.AntdButton(
            '向上滑动页面体验固钉效果',
            type='dashed'
        ),
        offsetBottom=100,
        target='docs-content',
        style={
            'float': 'right'
        }
    ),
    style={
        'marginTop': '1000px'
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
                    id='上滑固钉示例',
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
                            {'title': '下滑固钉示例', 'href': '#下滑固钉示例'},
                            {'title': '上滑固钉示例', 'href': '#上滑固钉示例'},
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
