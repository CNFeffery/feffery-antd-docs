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
                                'title': 'AntdCompact 紧凑布局'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                '　　用于对若干内部组件进行紧凑排列，确保相邻组件之间自动合并border。')
                        ]
                    ),

                    fac.AntdParagraph(
                        '注：目前支持进行紧凑布局的组件有AntdButton、AntdCascader、AntdDatePicker、AntdInput、AntdSelect、AntdTimePicker、AntdTreeSelect',
                        type='secondary'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '基于AntdSpace',
                                innerTextOrientation='left'
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        f'按钮{i}'
                                    )
                                    for i in range(1, 6)
                                ],
                                size=0
                            ),

                            fac.AntdDivider(
                                '基于AntdCompact',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCompact(
                                [
                                    fac.AntdButton(
                                        f'按钮{i}'
                                    )
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '基于',
                                    fac.AntdText(
                                        'AntdCompact',
                                        strong=True
                                    ),
                                    '对子元素进行排列，可以实现相邻紧贴元素边框线合并效果'
                                ],
                                style={
                                    'textIndent': '2rem'
                                }
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdDivider(
    '基于AntdSpace',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdButton(
            f'按钮{i}'
        )
        for i in range(1, 6)
    ],
    size=0
),

fac.AntdDivider(
    '基于AntdCompact',
    innerTextOrientation='left'
),

fac.AntdCompact(
    [
        fac.AntdButton(
            f'按钮{i}'
        )
        for i in range(1, 6)
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
                        id='基础使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCompact(
                                [
                                    fac.AntdInput(
                                        placeholder='请输入',
                                        style={
                                            'width': 150
                                        }
                                    ),
                                    fac.AntdSelect(
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}',
                                            }
                                            for i in range(1, 4)
                                        ],
                                        defaultValue='选项1',
                                        style={
                                            'width': 80
                                        }
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '常见用法',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '输入框搭配下拉选择是',
                                    fac.AntdText(
                                        'AntdCompact',
                                        strong=True
                                    ),
                                    '的常用组合方式，你也可以针对',
                                    fac.AntdText(
                                        'AntdCompact',
                                        strong=True
                                    ),
                                    '所支持的相关组件进行自由组合'
                                ],
                                style={
                                    'textIndent': '2rem'
                                }
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdCompact(
    [
        fac.AntdInput(
            placeholder='请输入',
            style={
                'width': 150
            }
        ),
        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}',
                }
                for i in range(1, 4)
            ],
            defaultValue='选项1',
            style={
                'width': 80
            }
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
                        id='常见用法',
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
                        {'title': '常见用法', 'href': '#常见用法'}
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
                component_name='AntdCompact',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
