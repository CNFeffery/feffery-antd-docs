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
                                'title': '其他'
                            },
                            {
                                'title': 'AntdBackTop 回到顶部'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于帮助用户在长页面中快速回到顶部。')
                        ]
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    fac.AntdBackTop(
                                        containerId='back-top-container-demo',
                                        duration=1
                                    ),
                                    fac.AntdTitle(
                                        '向下滑动一段距离',
                                        level=4
                                    )
                                ] + [
                                    html.Div(
                                        [
                                            i if i % 2 == 0 else html.Br()
                                            for i in range(200)
                                        ]
                                    )
                                ],
                                id='back-top-container-demo',
                                style={
                                    'maxHeight': '500px',
                                    'overflowY': 'auto',
                                    'position': 'relative',
                                    'backgroundColor': 'rgba(240, 240, 240, 0.2)',
                                    'padding': '20px'
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
html.Div(
    [
        fac.AntdBackTop(
            containerId='back-top-container-demo',
            duration=1
        ),
        fac.AntdTitle(
            '向下滑动一段距离',
            level=4
        )
    ] + [
        html.Div(
            [
                i if i % 2 == 0 else html.Br()
                for i in range(200)
            ]
        )
    ],
    id='back-top-container-demo',
    style={
        'maxHeight': '500px',
        'overflowY': 'auto',
        'position': 'relative',
        'backgroundColor': 'rgba(240, 240, 240, 0.2)',
        'padding': '20px'
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
                component_name='AntdBackTop',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
