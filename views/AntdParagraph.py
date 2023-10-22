from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

from .side_props import render_side_props_layout

paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'


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
                                'title': '通用'
                            },
                            {
                                'title': '排版相关'
                            },
                            {
                                'title': 'AntdParagraph 段落'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染具有丰富样式和功能的段落文字。')
                        ]
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    fac.AntdDivider(
                                        '默认模式',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo
                                    ),
                                    fac.AntdDivider(
                                        'code=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        code=True
                                    ),
                                    fac.AntdDivider(
                                        'copyable=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        copyable=True
                                    ),
                                    fac.AntdDivider(
                                        'strikethrough=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        strikethrough=True
                                    ),
                                    fac.AntdDivider(
                                        'disabled=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        disabled=True
                                    ),
                                    fac.AntdDivider(
                                        'mark=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        mark=True
                                    ),
                                    fac.AntdDivider(
                                        'strong=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        strong=True
                                    ),
                                    fac.AntdDivider(
                                        'italic=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        italic=True
                                    ),
                                    fac.AntdDivider(
                                        'underline=True',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        underline=True
                                    ),
                                    fac.AntdDivider(
                                        'type="secondary"',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        type="secondary"
                                    ),
                                    fac.AntdDivider(
                                        'type="success"',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        type="success"
                                    ),
                                    fac.AntdDivider(
                                        'type="warning"',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        type="warning"
                                    ),
                                    fac.AntdDivider(
                                        'type="danger"',
                                        innerTextOrientation='left'
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        type="danger"
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '不同的渲染模式',
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
paragraph_demo = '　　君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。'

...

html.Div(
    [
        fac.AntdDivider(
            '默认模式',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo
        ),
        fac.AntdDivider(
            'code=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            code=True
        ),
        fac.AntdDivider(
            'copyable=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            copyable=True
        ),
        fac.AntdDivider(
            'strikethrough=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            strikethrough=True
        ),
        fac.AntdDivider(
            'disabled=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            disabled=True
        ),
        fac.AntdDivider(
            'mark=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            mark=True
        ),
        fac.AntdDivider(
            'strong=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            strong=True
        ),
        fac.AntdDivider(
            'italic=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            italic=True
        ),
        fac.AntdDivider(
            'underline=True',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            underline=True
        ),
        fac.AntdDivider(
            'type="secondary"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="secondary"
        ),
        fac.AntdDivider(
            'type="success"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="success"
        ),
        fac.AntdDivider(
            'type="warning"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="warning"
        ),
        fac.AntdDivider(
            'type="danger"',
            innerTextOrientation='left'
        ),
        fac.AntdParagraph(
            paragraph_demo,
            type="danger"
        )
    ]
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
                        id='不同的渲染模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        ellipsis=True
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        ellipsis={
                                            'expandable': True
                                        }
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        ellipsis={
                                            'expandable': True,
                                            'rows': 3
                                        }
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        ellipsis={
                                            'suffix': '👉'
                                        }
                                    ),
                                    fac.AntdParagraph(
                                        paragraph_demo,
                                        ellipsis={
                                            'expandable': True,
                                            'rows': 3,
                                            'symbol': fac.AntdText(
                                                '点我展开',
                                                type='secondary'
                                            )
                                        }
                                    ),
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '内容省略功能',
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
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis=True
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': True
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': True,
                'rows': 3
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'suffix': '👉'
            }
        ),
        fac.AntdParagraph(
            paragraph_demo,
            ellipsis={
                'expandable': True,
                'rows': 3,
                'symbol': fac.AntdText(
                    '点我展开',
                    type='secondary'
                )
            }
        ),
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
                        id='内容省略功能',
                        className='div-highlight'
                    ),

                    html.Div(style={'height': '100px'})
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px',
                    'width': 0
                }
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '不同的渲染模式', 'href': '#不同的渲染模式'},
                        {'title': '内容省略功能', 'href': '#内容省略功能'},
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
                component_name='AntdParagraph',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
