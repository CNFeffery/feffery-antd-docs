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
                                'title': '布局'
                            },
                            {
                                'title': 'AntdCenter 居中'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于快捷实现内部元素水平竖直方向上居中。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdCenter(
                                        '常规居中',
                                        style={
                                            'width': 300,
                                            'height': 150,
                                            'background': '#f0f0f0'
                                        }
                                    ),
                                    fac.AntdParagraph(
                                        [
                                            '测试内容',
                                            fac.AntdCenter(
                                                '行内居中',
                                                style={
                                                    'width': 100,
                                                    'height': 100,
                                                    'background': '#f0f0f0'
                                                },
                                                inline=True
                                            ),
                                            '测试内容',
                                        ]
                                    )
                                ],
                                direction='vertical',
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
        fac.AntdCenter(
            '常规居中',
            style={
                'width': 300,
                'height': 150,
                'background': '#f0f0f0'
            }
        ),
        fac.AntdParagraph(
            [
                '测试内容',
                fac.AntdCenter(
                    '行内居中',
                    style={
                        'width': 100,
                        'height': 100,
                        'background': '#f0f0f0'
                    },
                    inline=True
                ),
                '测试内容',
            ]
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
                        id='基础使用',
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
                component_name='AntdCenter',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
