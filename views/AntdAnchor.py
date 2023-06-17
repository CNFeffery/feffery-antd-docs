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
                                'title': 'AntdAnchor 锚点'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染页面内导航目录。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdAnchor(
                                linkDict=[
                                    {
                                        'title': '章节1',
                                        'href': '#章节1',
                                        'children': [
                                            {
                                                'title': '章节1-1',
                                                'href': '#章节1-1'
                                            },
                                            {
                                                'title': '章节1-2',
                                                'href': '#章节1-2'
                                            }
                                        ]
                                    },
                                    {
                                        'title': '章节2',
                                        'href': '#章节2',
                                        'children': [
                                            {
                                                'title': '章节2-1',
                                                'href': '#章节2-1'
                                            },
                                            {
                                                'title': '章节2-2',
                                                'href': '#章节2-2'
                                            }
                                        ]
                                    }
                                ],
                                align='left'
                            ),

                            fac.AntdDivider(
                                '章节1',
                                id='章节1',
                                innerTextOrientation='right'
                            ),
                            html.Div(
                                style={
                                    'height': 300
                                }
                            ),
                            fac.AntdDivider(
                                '章节1-1',
                                id='章节1-1',
                                innerTextOrientation='right'
                            ),
                            html.Div(
                                style={
                                    'height': 300
                                }
                            ),
                            fac.AntdDivider(
                                '章节1-2',
                                id='章节1-2',
                                innerTextOrientation='right'
                            ),
                            html.Div(
                                style={
                                    'height': 300
                                }
                            ),
                            fac.AntdDivider(
                                '章节2',
                                id='章节2',
                                innerTextOrientation='right'
                            ),
                            html.Div(
                                style={
                                    'height': 300
                                }
                            ),
                            fac.AntdDivider(
                                '章节2-1',
                                id='章节2-1',
                                innerTextOrientation='right'
                            ),
                            html.Div(
                                style={
                                    'height': 300
                                }
                            ),
                            fac.AntdDivider(
                                '章节2-2',
                                id='章节2-2',
                                innerTextOrientation='right'
                            ),
                            html.Div(
                                style={
                                    'height': 300
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
fac.AntdAnchor(
    linkDict=[
        {
            'title': '章节1',
            'href': '#章节1',
            'children': [
                {
                    'title': '章节1-1',
                    'href': '#章节1-1'
                },
                {
                    'title': '章节1-2',
                    'href': '#章节1-2'
                }
            ]
        },
        {
            'title': '章节2',
            'href': '#章节2',
            'children': [
                {
                    'title': '章节2-1',
                    'href': '#章节2-1'
                },
                {
                    'title': '章节2-2',
                    'href': '#章节2-2'
                }
            ]
        }
    ],
    align='left'
),

fac.AntdDivider(
    '章节1',
    id='章节1',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节1-1',
    id='章节1-1',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节1-2',
    id='章节1-2',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节2',
    id='章节2',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节2-1',
    id='章节2-1',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
    }
),
fac.AntdDivider(
    '章节2-2',
    id='章节2-2',
    innerTextOrientation='right'
),
html.Div(
    style={
        'height': 300
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
                component_name='AntdAnchor',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
