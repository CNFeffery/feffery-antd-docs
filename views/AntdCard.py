from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from .side_props import render_side_props_layout

docs_content = html.Div(
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
                            'title': 'AntdCard 卡片'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于构建美观的内容展示卡片。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdCard(
                            '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
                            title='卡片示例',
                            style={
                                'width': 300,
                                'marginBottom': 10
                            }
                        ),

                        fac.AntdCard(
                            '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
                            title='无边框卡片示例',
                            bordered=False,
                            style={
                                'width': 300
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
                                codeString="""
fac.AntdCard(
    '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
    title='卡片示例',
    style={
        'width': 300,
        'marginBottom': 10
    }
),

fac.AntdCard(
    '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
    title='无边框卡片示例',
    bordered=False,
    style={
        'width': 300
    }
)
"""
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
                        fac.AntdCard(
                            '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
                            title='卡片示例',
                            extraLink={
                                'content': '链接示例',
                                'href': 'https://zh.wikipedia.org/zh-hans/国际歌'
                            },
                            style={
                                'width': 300,
                                'marginBottom': 10
                            }
                        ),

                        fac.AntdDivider(
                            '添加右上角链接',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fac.AntdCard(
    '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
    title='卡片示例',
    extraLink={
        'content': '链接示例',
        'href': 'https://zh.wikipedia.org/zh-hans/国际歌'
    },
    style={
        'width': 300,
        'marginBottom': 10
    }
)
"""
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
                    id='添加右上角链接',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCard(
                            coverImg={
                                'src': '/assets/imgs/流浪地球2海报.jpg'
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
                            '使用封面图片',
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
fac.AntdCard(
    coverImg={
        'src': '/assets/imgs/流浪地球2海报.jpg'
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
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='使用封面图片',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdCard(
                                    'size="default"',
                                    title='卡片示例'
                                ),

                                fac.AntdCard(
                                    'size="small"',
                                    title='卡片示例',
                                    size='small'
                                )
                            ],
                            direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdCard(
            'size="default"',
            title='卡片示例'
        ),

        fac.AntdCard(
            'size="small"',
            title='卡片示例',
            size='small'
        )
    ],
    direction='vertical'
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
                            '内嵌卡片网格',
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
                            isOpen=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='内嵌卡片网格',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCard(
                            '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
                            title='卡片示例',
                            headStyle={
                                'display': 'none'
                            },
                            hoverable=True,
                            style={
                                'width': 300,
                                'marginBottom': 10
                            }
                        ),

                        fac.AntdDivider(
                            '隐藏标题栏',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
fac.AntdCard(
    '''
　　从来就没有什么救世主，
也不靠神仙皇帝。
要创造人类的幸福，
全靠我们自己。
我们要夺回劳动果实，
让思想冲破牢笼。
快把那炉火烧得通红，
趁热打铁才能成功！
这是最后的斗争，
团结起来，到明天，
英特纳雄耐尔就一定要实现。
''',
    title='卡片示例',
    headStyle={
        'display': 'none'
    },
    hoverable=True,
    style={
        'width': 300,
        'marginBottom': 10
    }
)
"""
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
                    id='隐藏标题栏',
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
                    {'title': '添加右上角链接', 'href': '#添加右上角链接'},
                    {'title': '使用封面图片', 'href': '#使用封面图片'},
                    {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                    {'title': '内嵌卡片网格', 'href': '#内嵌卡片网格'},
                    {'title': '隐藏标题栏', 'href': '#隐藏标题栏'},
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
            component_name='AntdCard'
        )
    ],
    style={
        'display': 'flex'
    }
)
