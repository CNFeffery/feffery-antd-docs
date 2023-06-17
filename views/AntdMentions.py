from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdMentions
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
                                'title': '数据录入'
                            },
                            {
                                'title': 'AntdMentions 提及'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                '　　用于实现在输入内容中对不同角色进行提及的功能，常用于构建论坛、协同办公等平台中的评论功能。'
                            )
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdMentions(
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '  输入子项菜单默认触发关键字',
                                    fac.AntdText(
                                        '@',
                                        strong=True
                                    ),
                                    '后可进行目标角色的选中和提及'
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    style={
        'width': 200
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
                            fac.AntdDivider(
                                'autoSize=False（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdMentions(
                                defaultValue='示例内容'*20,
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'autoSize=True',
                                innerTextOrientation='left'
                            ),
                            fac.AntdMentions(
                                defaultValue='示例内容'*20,
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                autoSize=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '配置minRows、maxRows参数',
                                innerTextOrientation='left'
                            ),
                            fac.AntdMentions(
                                defaultValue='示例内容'*20,
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                autoSize={
                                    'minRows': 2,
                                    'maxRows': 6
                                },
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '自适应高度',
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
    'autoSize=False（默认）',
    innerTextOrientation='left'
),
fac.AntdMentions(
    defaultValue='示例内容'*20,
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    style={
        'width': 300
    }
),

fac.AntdDivider(
    'autoSize=True',
    innerTextOrientation='left'
),
fac.AntdMentions(
    defaultValue='示例内容'*20,
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    autoSize=True,
    style={
        'width': 300
    }
),

fac.AntdDivider(
    '配置minRows、maxRows参数',
    innerTextOrientation='left'
),
fac.AntdMentions(
    defaultValue='示例内容'*20,
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    autoSize={
        'minRows': 2,
        'maxRows': 6
    },
    style={
        'width': 300
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
                        id='自适应高度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdMentions(
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                placement='top',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '子项菜单向上展开',
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
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    placement='top',
    style={
        'width': 200
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
                        id='子项菜单向上展开',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdMentions(
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                disabled=True,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '禁用状态',
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
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    disabled=True,
    style={
        'width': 200
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'status="warning"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdMentions(
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                status='warning',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                'status="error"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdMentions(
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                status='error',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '强制状态渲染',
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
    'status="warning"',
    innerTextOrientation='left'
),
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    status='warning',
    style={
        'width': 200
    }
),

fac.AntdDivider(
    'status="error"',
    innerTextOrientation='left'
),
fac.AntdMentions(
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    status='error',
    style={
        'width': 200
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
                        id='强制状态渲染',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdMentions(
                                id='mentions-demo',
                                autoSize={
                                    'minRows': 2,
                                    'maxRows': 4
                                },
                                options=[
                                    {
                                        'label': f'用户{c}',
                                        'value': f'用户{c}'
                                    }
                                    for c in list('abcdef')
                                ],
                                style={
                                    'width': 300
                                }
                            ),

                            html.Br(),

                            fac.AntdSpace(
                                id='mentions-demo-output',
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '回调示例',
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
fac.AntdMentions(
    id='mentions-demo',
    autoSize={
        'minRows': 2,
        'maxRows': 4
    },
    options=[
        {
            'label': f'用户{c}',
            'value': f'用户{c}'
        }
        for c in list('abcdef')
    ],
    style={
        'width': 300
    }
),

html.Br(),

fac.AntdSpace(
    id='mentions-demo-output',
    direction='vertical'
)

...

@app.callback(
    Output('mentions-demo-output', 'children'),
    [Input('mentions-demo', 'value'),
     Input('mentions-demo', 'selectedOptions')]
)
def mentions_demo(value, selectedOptions):

    return [
        fac.AntdText(
            f'value: {value}'
        ),
        fac.AntdText(
            f'selectedOptions: {selectedOptions}'
        )
    ]
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
                        id='回调示例',
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
                        {'title': '自适应高度', 'href': '#自适应高度'},
                        {'title': '子项菜单向上展开', 'href': '#子项菜单向上展开'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                        {'title': '回调示例', 'href': '#回调示例'},
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
                component_name='AntdMentions',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
