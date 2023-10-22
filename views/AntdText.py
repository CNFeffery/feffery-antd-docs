from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

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
                                'title': '通用'
                            },
                            {
                                'title': '排版相关'
                            },
                            {
                                'title': 'AntdText 文字'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染具有丰富样式和功能的行内文字。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdParagraph(
                                [
                                    fac.AntdText('code示例', code=True),
                                    fac.AntdText('copyable示例', copyable=True),
                                    fac.AntdText('strikethrough示例',
                                                 strikethrough=True),
                                    fac.AntdText('disabled示例', disabled=True),
                                    fac.AntdText('mark示例', mark=True),
                                    fac.AntdText('strong示例', strong=True),
                                    fac.AntdText(
                                        'underline示例', underline=True),
                                    fac.AntdText('keyboard示例', keyboard=True),
                                    fac.AntdText(
                                        'secondary示例', type='secondary'),
                                    fac.AntdText('success示例', type='success'),
                                    fac.AntdText('warning示例', type='warning'),
                                    fac.AntdText('danger示例', type='danger'),
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
fac.AntdParagraph(
    [
        fac.AntdText('code示例', code=True),
        fac.AntdText('copyable示例', copyable=True),
        fac.AntdText('strikethrough示例',
                        strikethrough=True),
        fac.AntdText('disabled示例', disabled=True),
        fac.AntdText('mark示例', mark=True),
        fac.AntdText('strong示例', strong=True),
        fac.AntdText('underline示例', underline=True),
        fac.AntdText('keyboard示例', keyboard=True),
        fac.AntdText('secondary示例', type='secondary'),
        fac.AntdText('success示例', type='success'),
        fac.AntdText('warning示例', type='warning'),
        fac.AntdText('danger示例', type='danger'),
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
                                    fac.AntdText(
                                        '内容省略示例'+'巴拉巴拉巴拉巴拉'*100,
                                        ellipsis=True
                                    ),

                                    fac.AntdText(
                                        '内容省略示例'+'巴拉巴拉巴拉巴拉'*100,
                                        ellipsis={
                                            'suffix': '👉'
                                        }
                                    )
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
        fac.AntdText(
            '内容省略示例'+'巴拉巴拉巴拉巴拉'*100,
            ellipsis=True
        ),

        fac.AntdText(
            '内容省略示例'+'巴拉巴拉巴拉巴拉'*100,
            ellipsis={
                'suffix': '👉'
            }
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
                        {'title': '内容省略功能', 'href': '#内容省略功能'}
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
                component_name='AntdText',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
