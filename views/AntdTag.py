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
                                'title': 'AntdTag 标签'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染美观的小标签。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTag(
                                        content=f'标签{i}'
                                    )
                                    for i in range(1, 4)
                                ],
                                size='small'
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
fac.AntdSpace(
    [
        fac.AntdTag(
            content=f'标签{i}'
        )
        for i in range(1, 4)
    ],
    size='small'
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
                            fac.AntdDivider(
                                '使用内置色彩主题',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdTag(
                                        content=color,
                                        color=color
                                    )
                                    for color in [
                                        'magenta',
                                        'red',
                                        'volcano',
                                        'orange',
                                        'gold',
                                        'lime',
                                        'green',
                                        'cyan',
                                        'blue',
                                        'geekblue',
                                        'purple'
                                    ]
                                ],
                                wrap=True,
                                size='small'
                            ),

                            fac.AntdDivider(
                                '使用任意css颜色值',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdTag(
                                        content=color,
                                        color=color
                                    )
                                    for color in [
                                        '#c5f6fa',
                                        '#99e9f2',
                                        '#66d9e8',
                                        '#3bc9db',
                                        '#22b8cf',
                                        '#15aabf',
                                        '#1098ad',
                                        '#0c8599',
                                        '#0b7285'
                                    ]
                                ],
                                wrap=True,
                                size='small'
                            ),

                            fac.AntdDivider(
                                '不同的色彩风格',
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
    '使用内置色彩主题',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdTag(
            content=color,
            color=color
        )
        for color in [
            'magenta',
            'red',
            'volcano',
            'orange',
            'gold',
            'lime',
            'green',
            'cyan',
            'blue',
            'geekblue',
            'purple'
        ]
    ],
    wrap=True,
    size='small'
),

fac.AntdDivider(
    '使用任意css颜色值',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdTag(
            content=color,
            color=color
        )
        for color in [
            '#c5f6fa',
            '#99e9f2',
            '#66d9e8',
            '#3bc9db',
            '#22b8cf',
            '#15aabf',
            '#1098ad',
            '#0c8599',
            '#0b7285'
        ]
    ],
    wrap=True,
    size='small'
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
                        id='不同的色彩风格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTag(
                                content='fuc官网',
                                href='https://fuc.feffery.tech',
                                color='cyan'
                            ),

                            fac.AntdTag(
                                content='fmc官网',
                                href='https://fmc.feffery.tech',
                                color='green'
                            ),

                            fac.AntdDivider(
                                '充当链接使用',
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
fac.AntdTag(
    content='fuc官网',
    href='https://fuc.feffery.tech',
    color='cyan'
),

fac.AntdTag(
    content='fmc官网',
    href='https://fmc.feffery.tech',
    color='green'
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
                        id='充当链接使用',
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
                        {'title': '不同的色彩风格', 'href': '#不同的色彩风格'},
                        {'title': '充当链接使用', 'href': '#充当链接使用'},
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
                component_name='AntdTag',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
