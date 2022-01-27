from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCard(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCard.md', encoding='utf-8').read()
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

                        fac.AntdCard(
                            fac.AntdParagraph(
                                """　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
                                italic=True
                            ),
                            title='卡片示例',
                            style={
                                'width': '300px',
                                'marginBottom': '10px'
                            }
                        ),

                        fac.AntdCard(
                            fac.AntdParagraph(
                                """　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
                                italic=True
                            ),
                            bordered=False,
                            title='卡片示例（无边框）',
                            style={
                                'width': '300px'
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
fac.AntdCard(
    fac.AntdParagraph(
        """　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
        italic=True
    ),
    title='卡片示例',
    style={
        'width': '300px',
        'marginBottom': '10px'
    }
),

fac.AntdCard(
    fac.AntdParagraph(
        """　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。""",
        italic=True
    ),
    bordered=False,
    title='卡片示例（无边框）',
    style={
        'width': '300px'
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

                        fac.AntdCard(
                            fac.AntdParagraph(
                                '卡片示例',
                                italic=True
                            ),
                            extraLink={
                                'content': '链接示例',
                                'href': '/AntdCard'
                            },
                            title='卡片示例',
                            style={
                                'width': '300px',
                                'marginBottom': '10px'
                            }
                        ),

                        fac.AntdDivider(
                            '添加右上角额外链接',
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
fac.AntdCard(
    fac.AntdParagraph(
        '卡片示例',
        italic=True
    ),
    extraLink={
        'content': '链接示例',
        'href': '/AntdCard'
    },
    title='卡片示例',
    style={
        'width': '300px',
        'marginBottom': '10px'
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
                    id='添加右上角额外链接',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdCard(
                            coverImg={
                                'src': '/assets/imgs/山海情.webp'
                            },
                            title='图片封面示例',
                            bodyStyle={
                                'display': 'none'
                            },
                            hoverable=True,
                            style={
                                'width': '300px',
                                'marginBottom': '10px'
                            }
                        ),

                        fac.AntdDivider(
                            '配置封面图片',
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
fac.AntdCard(
    coverImg={
        'src': '/assets/imgs/山海情.webp'
    },
    title='图片封面示例',
    bodyStyle={
        'display': 'none'
    },
    hoverable=True,
    style={
        'width': '300px',
        'marginBottom': '10px'
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
                    id='配置封面图片',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdCard(
                            [
                                fac.AntdCardGrid(
                                    f'网格{i}',
                                    style={
                                        'width': '25%',
                                        'display': 'flex',
                                        'justifyContent': 'center',
                                        'alignItems': 'center'
                                    }
                                )
                                for i in range(10)
                            ],
                            title='卡片网格示例',
                            style={
                                'width': '400px',
                                'marginBottom': '10px'
                            }
                        ),

                        fac.AntdDivider(
                            '使用卡片网格作为子元素',
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
fac.AntdCard(
    [
        fac.AntdCardGrid(
            f'网格{i}',
            style={
                'width': '25%',
                'display': 'flex',
                'justifyContent': 'center',
                'alignItems': 'center'
            }
        )
        for i in range(10)
    ],
    title='卡片网格示例',
    style={
        'width': '400px',
        'marginBottom': '10px'
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
                    id='使用卡片网格作为子元素',
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
                            {'title': '添加右上角额外链接', 'href': '#添加右上角额外链接'},
                            {'title': '配置封面图片', 'href': '#配置封面图片'},
                            {'title': '使用卡片网格作为子元素', 'href': '#使用卡片网格作为子元素'},
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
