from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdDescriptions(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdDescriptions.md', encoding='utf-8').read()
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
                        fac.AntdDivider('默认无边框', innerTextOrientation='left'),
                        fac.AntdDescriptions(
                            [
                                fac.AntdDescriptionItem(
                                    '费弗里',
                                    label='姓名'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://github.com/CNFeffery',
                                        href='https://github.com/CNFeffery'
                                    ),
                                    label='个人Github地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://www.cnblogs.com/feffery/',
                                        href='https://www.cnblogs.com/feffery/'
                                    ),
                                    label='个人博客地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'http://fac.feffery.tech/',
                                        href='http://fac.feffery.tech/'
                                    ),
                                    label='fac框架官网'
                                )
                            ],
                            title='描述列表示例',
                            labelStyle={
                                'fontWeight': 'bold'
                            }
                        ),
                        fac.AntdDivider('添加边框', innerTextOrientation='left'),
                        fac.AntdDescriptions(
                            [
                                fac.AntdDescriptionItem(
                                    '费弗里',
                                    label='姓名'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://github.com/CNFeffery',
                                        href='https://github.com/CNFeffery'
                                    ),
                                    label='个人Github地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://www.cnblogs.com/feffery/',
                                        href='https://www.cnblogs.com/feffery/'
                                    ),
                                    label='个人博客地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'http://fac.feffery.tech/',
                                        href='http://fac.feffery.tech/'
                                    ),
                                    label='fac框架官网'
                                )
                            ],
                            title='描述列表示例',
                            bordered=True,
                            labelStyle={
                                'fontWeight': 'bold'
                            }
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
fac.AntdDivider('默认无边框', innerTextOrientation='left'),
fac.AntdDescriptions(
    [
        fac.AntdDescriptionItem(
            '费弗里',
            label='姓名'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery'
            ),
            label='个人Github地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/'
            ),
            label='个人博客地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'http://fac.feffery.tech/',
                href='http://fac.feffery.tech/'
            ),
            label='fac框架官网'
        )
    ],
    title='描述列表示例',
    labelStyle={
        'fontWeight': 'bold'
    }
),
fac.AntdDivider('添加边框', innerTextOrientation='left'),
fac.AntdDescriptions(
    [
        fac.AntdDescriptionItem(
            '费弗里',
            label='姓名'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery'
            ),
            label='个人Github地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/'
            ),
            label='个人博客地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'http://fac.feffery.tech/',
                href='http://fac.feffery.tech/'
            ),
            label='fac框架官网'
        )
    ],
    title='描述列表示例',
    bordered=True,
    labelStyle={
        'fontWeight': 'bold'
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDescriptions(
                            [
                                fac.AntdDescriptionItem(
                                    '费弗里',
                                    label='姓名'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://github.com/CNFeffery',
                                        href='https://github.com/CNFeffery'
                                    ),
                                    label='个人Github地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://www.cnblogs.com/feffery/',
                                        href='https://www.cnblogs.com/feffery/'
                                    ),
                                    label='个人博客地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'http://fac.feffery.tech/',
                                        href='http://fac.feffery.tech/'
                                    ),
                                    label='fac框架官网'
                                )
                            ],
                            title='描述列表示例',
                            bordered=True,
                            layout='vertical',
                            labelStyle={
                                'fontWeight': 'bold'
                            }
                        ),

                        fac.AntdDivider(
                            '垂直布局方式',
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
fac.AntdDescriptions(
    [
        fac.AntdDescriptionItem(
            '费弗里',
            label='姓名'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery'
            ),
            label='个人Github地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/'
            ),
            label='个人博客地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'http://fac.feffery.tech/',
                href='http://fac.feffery.tech/'
            ),
            label='fac框架官网'
        )
    ],
    title='描述列表示例',
    bordered=True,
    layout='vertical',
    labelStyle={
        'fontWeight': 'bold'
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
                    id='垂直布局方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider('column=2', innerTextOrientation='left'),
                        fac.AntdDescriptions(
                            [
                                fac.AntdDescriptionItem(
                                    '费弗里',
                                    label='姓名'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://github.com/CNFeffery',
                                        href='https://github.com/CNFeffery'
                                    ),
                                    label='个人Github地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://www.cnblogs.com/feffery/',
                                        href='https://www.cnblogs.com/feffery/'
                                    ),
                                    label='个人博客地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'http://fac.feffery.tech/',
                                        href='http://fac.feffery.tech/'
                                    ),
                                    label='fac框架官网'
                                )
                            ],
                            title='描述列表示例',
                            bordered=True,
                            column=2,
                            labelStyle={
                                'fontWeight': 'bold'
                            }
                        ),

                        fac.AntdDivider('column=4', innerTextOrientation='left'),
                        fac.AntdDescriptions(
                            [
                                fac.AntdDescriptionItem(
                                    '费弗里',
                                    label='姓名'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://github.com/CNFeffery',
                                        href='https://github.com/CNFeffery'
                                    ),
                                    label='个人Github地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://www.cnblogs.com/feffery/',
                                        href='https://www.cnblogs.com/feffery/'
                                    ),
                                    label='个人博客地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'http://fac.feffery.tech/',
                                        href='http://fac.feffery.tech/'
                                    ),
                                    label='fac框架官网'
                                )
                            ],
                            title='描述列表示例',
                            bordered=True,
                            column=4,
                            labelStyle={
                                'fontWeight': 'bold'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义每行标准子项数量',
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
fac.AntdDivider('column=2', innerTextOrientation='left'),
fac.AntdDescriptions(
    [
        fac.AntdDescriptionItem(
            '费弗里',
            label='姓名'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery'
            ),
            label='个人Github地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/'
            ),
            label='个人博客地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'http://fac.feffery.tech/',
                href='http://fac.feffery.tech/'
            ),
            label='fac框架官网'
        )
    ],
    title='描述列表示例',
    bordered=True,
    column=2,
    labelStyle={
        'fontWeight': 'bold'
    }
),

fac.AntdDivider('column=4', innerTextOrientation='left'),
fac.AntdDescriptions(
    [
        fac.AntdDescriptionItem(
            '费弗里',
            label='姓名'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery'
            ),
            label='个人Github地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/'
            ),
            label='个人博客地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'http://fac.feffery.tech/',
                href='http://fac.feffery.tech/'
            ),
            label='fac框架官网'
        )
    ],
    title='描述列表示例',
    bordered=True,
    column=4,
    labelStyle={
        'fontWeight': 'bold'
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
                    id='自定义每行标准子项数量',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDescriptions(
                            [
                                fac.AntdDescriptionItem(
                                    '费弗里',
                                    label='姓名',
                                    span=2
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://github.com/CNFeffery',
                                        href='https://github.com/CNFeffery'
                                    ),
                                    label='个人Github地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'https://www.cnblogs.com/feffery/',
                                        href='https://www.cnblogs.com/feffery/'
                                    ),
                                    label='个人博客地址'
                                ),
                                fac.AntdDescriptionItem(
                                    html.A(
                                        'http://fac.feffery.tech/',
                                        href='http://fac.feffery.tech/'
                                    ),
                                    label='fac框架官网'
                                )
                            ],
                            title='描述列表示例',
                            bordered=True,
                            labelStyle={
                                'fontWeight': 'bold'
                            }
                        ),

                        fac.AntdDivider(
                            '令部分子项占据多个标准宽度',
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
fac.AntdDescriptions(
    [
        fac.AntdDescriptionItem(
            '费弗里',
            label='姓名',
            span=2
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://github.com/CNFeffery',
                href='https://github.com/CNFeffery'
            ),
            label='个人Github地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'https://www.cnblogs.com/feffery/',
                href='https://www.cnblogs.com/feffery/'
            ),
            label='个人博客地址'
        ),
        fac.AntdDescriptionItem(
            html.A(
                'http://fac.feffery.tech/',
                href='http://fac.feffery.tech/'
            ),
            label='fac框架官网'
        )
    ],
    title='描述列表示例',
    bordered=True,
    labelStyle={
        'fontWeight': 'bold'
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
                    id='令部分子项占据多个标准宽度',
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
                            {'title': '垂直布局方式', 'href': '#垂直布局方式'},
                            {'title': '自定义每行标准子项数量', 'href': '#自定义每行标准子项数量'},
                            {'title': '令部分子项占据多个标准宽度', 'href': '#令部分子项占据多个标准宽度'},
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
