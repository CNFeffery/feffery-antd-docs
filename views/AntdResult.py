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
                                'title': '反馈'
                            },
                            {
                                'title': 'AntdResult 结果'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供不同场景下的状态提示。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdResult(
                                title='标题示例',
                                subTitle='副标题示例'
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
fac.AntdResult(
    title='标题示例',
    subTitle='副标题示例'
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
                            fac.AntdSpace(
                                [
                                    fac.AntdResult(
                                        title='标题示例',
                                        subTitle=f'status="{status}"',
                                        status=status
                                    )
                                    for status in [
                                        'info', 'success', 'warning', 'error',
                                        '404', '403', '500', 'loading'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '不同的状态类型',
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
        fac.AntdResult(
            title='标题示例',
            subTitle=f'status="{status}"',
            status=status
        )
        for status in [
            'info', 'success', 'warning', 'error',
            '404', '403', '500', 'loading'
        ]
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
                        id='不同的状态类型',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdResult(
                                title='标题示例',
                                subTitle='副标题示例',
                                icon=fac.AntdIcon(
                                    icon='antd-bulb',
                                    style={
                                        'fontSize': 60,
                                        'color': '#fcd53f'
                                    }
                                )
                            ),

                            fac.AntdDivider(
                                '自定义图标',
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
fac.AntdResult(
    title='标题示例',
    subTitle='副标题示例',
    icon=fac.AntdIcon(
        icon='antd-bulb',
        style={
            'fontSize': 60,
            'color': '#fcd53f'
        }
    )
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
                        id='自定义图标',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdResult(
                                status='success',
                                title='任务创建成功',
                                subTitle=fac.AntdSpace(
                                    [
                                        fac.AntdText(
                                            '创建时间：2023-01-01 12:00:00',
                                            type='secondary'
                                        ),
                                        fac.AntdSpace(
                                            [
                                                fac.AntdButton(
                                                    '查看详情',
                                                    type='primary'
                                                ),
                                                fac.AntdButton(
                                                    '回到首页'
                                                )
                                            ]
                                        )
                                    ],
                                    direction='vertical',
                                    align='center'
                                )
                            ),

                            fac.AntdDivider(
                                '更复杂的使用',
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
fac.AntdResult(
    status='success',
    title='任务创建成功',
    subTitle=fac.AntdSpace(
        [
            fac.AntdText(
                '创建时间：2023-01-01 12:00:00',
                type='secondary'
            ),
            fac.AntdSpace(
                [
                    fac.AntdButton(
                        '查看详情',
                        type='primary'
                    ),
                    fac.AntdButton(
                        '回到首页'
                    )
                ]
            )
        ],
        direction='vertical',
        align='center'
    )
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
                        id='更复杂的使用',
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
                        {'title': '不同的状态类型', 'href': '#不同的状态类型'},
                        {'title': '自定义图标', 'href': '#自定义图标'},
                        {'title': '更复杂的使用', 'href': '#更复杂的使用'},
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
                component_name='AntdResult',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
