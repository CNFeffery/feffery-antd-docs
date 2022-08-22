from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdRibbon(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdRibbon.md', encoding='utf-8').read()
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
                        fac.AntdSpace(
                            [
                                fac.AntdRibbon(
                                    html.Div(
                                        style={
                                            'height': '200px',
                                            'width': '300px',
                                            'borderRadius': '16px',
                                            'boxShadow': 'rgb(102 124 145 / 9%) 0px 2px 6px 0px'
                                        }
                                    ),
                                    text='缎带示例'
                                ),
                                fac.AntdRibbon(
                                    html.Div(
                                        style={
                                            'height': '200px',
                                            'width': '300px',
                                            'borderRadius': '16px',
                                            'boxShadow': 'rgb(102 124 145 / 9%) 0px 2px 6px 0px'
                                        }
                                    ),
                                    text='缎带示例',
                                    placement='start',
                                    color='#ff4d4f'
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　缎带的使用很简单，主要用于装饰div盒子')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdRibbon(
            html.Div(
                style={
                    'height': '200px',
                    'width': '300px',
                    'borderRadius': '16px',
                    'boxShadow': 'rgb(102 124 145 / 9%) 0px 2px 6px 0px'
                }
            ),
            text='缎带示例'
        ),
        fac.AntdRibbon(
            html.Div(
                style={
                    'height': '200px',
                    'width': '300px',
                    'borderRadius': '16px',
                    'boxShadow': 'rgb(102 124 145 / 9%) 0px 2px 6px 0px'
                }
            ),
            text='缎带示例',
            placement='start',
            color='#ff4d4f'
        )
    ],
    direction='vertical'
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
