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
                                'title': '数据展示'
                            },
                            {
                                'title': '描述列表'
                            },
                            {
                                'title': 'AntdDescriptions 描述列表'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于配合AntdDescriptionItem进行一组属性的展示。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '默认无边框',
                                innerTextOrientation='left'
                            ),
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

                            fac.AntdDivider(
                                '添加边框',
                                innerTextOrientation='left'
                            ),
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
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdDivider(
    '默认无边框',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    '添加边框',
    innerTextOrientation='left'
),
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
                                '垂直布局模式',
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
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='垂直布局模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'column=2',
                                innerTextOrientation='left'
                            ),
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

                            fac.AntdDivider(
                                'column=4',
                                innerTextOrientation='left'
                            ),
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
                                '设置每行宽度单位数量',
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
fac.AntdDivider(
    'column=2',
    innerTextOrientation='left'
),
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

fac.AntdDivider(
    'column=4',
    innerTextOrientation='left'
),
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
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置每行宽度单位数量',
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
                                '设置描述列表项单位宽度',
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
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='设置描述列表项单位宽度',
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
                        {'title': '垂直布局模式', 'href': '#垂直布局模式'},
                        {'title': '设置每行宽度单位数量', 'href': '#设置每行宽度单位数量'},
                        {'title': '设置描述列表项单位宽度', 'href': '#设置描述列表项单位宽度'},
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
                component_name='AntdDescriptions',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
