from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCheckCard
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
                                'title': '选择卡片'
                            },
                            {
                                'title': 'AntdCheckCard 选择卡片'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染具有状态切换功能的内容卡片。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdCheckCard(
                                        fac.AntdText(
                                            '选择卡片示例' * 10
                                        )
                                    ),
                                    fac.AntdCheckCard(
                                        fac.AntdStatistic(
                                            title='统计数值示例',
                                            value=1332971
                                        ),
                                        defaultChecked=True
                                    ),
                                    fac.AntdCheckCard(
                                        html.Div(
                                            [
                                                html.Div(
                                                    fac.AntdAvatar(
                                                        mode='image',
                                                        size=48,
                                                        src='/assets/imgs/avatar-demo.jpg'
                                                    ),
                                                    style={
                                                        'flex': 'none',
                                                        'marginRight': '10px'
                                                    }
                                                ),
                                                html.Div(
                                                    fac.AntdText(
                                                        '选择卡片示例' * 20
                                                    ),
                                                    style={
                                                        'flex': 'auto'
                                                    }
                                                )
                                            ],
                                            style={
                                                'display': 'flex'
                                            }
                                        )
                                    )
                                ],
                                direction='vertical',
                                size='small',
                                style={
                                    'width': '100%'
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
fac.AntdSpace(
    [
        fac.AntdCheckCard(
            fac.AntdText(
                '选择卡片示例' * 10
            )
        ),
        fac.AntdCheckCard(
            fac.AntdStatistic(
                title='统计数值示例',
                value=1332971,
                defaultChecked=True
            )
        ),
        fac.AntdCheckCard(
            html.Div(
                [
                    html.Div(
                        fac.AntdAvatar(
                            mode='image',
                            size=48,
                            src='/assets/imgs/avatar-demo.jpg'
                        ),
                        style={
                            'flex': 'none',
                            'marginRight': '10px'
                        }
                    ),
                    html.Div(
                        fac.AntdText(
                            '选择卡片示例' * 20
                        ),
                        style={
                            'flex': 'auto'
                        }
                    )
                ],
                style={
                    'display': 'flex'
                }
            )
        )
    ],
    direction='vertical',
    size='small',
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
                        id='基础使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCheckCard(
                                fac.AntdText(
                                    '选择卡片示例' * 10
                                ),
                                readOnly=True,
                                checked=True
                            ),

                            fac.AntdDivider(
                                '只读状态',
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
fac.AntdCheckCard(
    fac.AntdText(
        '选择卡片示例' * 10
    ),
    readOnly=True,
    checked=True
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
                        id='只读状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdCheckCard(
                                        f'size="{size}"',
                                        size=size
                                    )
                                    for size in [
                                        'small', 'default', 'large'
                                    ]
                                ],
                                direction='vertical',
                                size='small',
                                style={
                                    'width': '100%'
                                }
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
        fac.AntdCheckCard(
            f'size="{size}"',
            size=size
        )
        for size in [
            'small', 'default', 'large'
        ]
    ],
    direction='vertical',
    size='small',
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
                        id='不同的尺寸规格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCheckCard(
                                fac.AntdText(
                                    '选择卡片示例' * 10
                                ),
                                id='check-card-demo',
                                defaultChecked=False
                            ),

                            fac.AntdParagraph(
                                id='check-card-demo-output'
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
fac.AntdCheckCard(
    fac.AntdText(
        '选择卡片示例' * 10
    ),
    id='check-card-demo',
    defaultChecked=False
),

fac.AntdParagraph(
    id='check-card-demo-output'
)

...

@app.callback(
    Output('check-card-demo-output', 'children'),
    Input('check-card-demo', 'checked')
)
def check_card_demo(checked):

    return f'checked: {checked}'
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
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
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
                component_name='AntdCheckCard',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
