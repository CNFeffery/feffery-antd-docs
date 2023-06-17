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
                                'title': '导航'
                            },
                            {
                                'title': 'AntdAffix 固钉'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                '　　确保内部元素原有位置在被用户滚动出视口后，仍然可以在视口范围内保持可见状态。')
                        ]
                    ),

                    html.Div(
                        [
                            html.Div(
                                fac.AntdAffix(
                                    fac.AntdButton(
                                        '向下滑动页面体验固钉锚定效果',
                                        type='primary'
                                    ),
                                    offsetTop=100
                                ),
                                style={
                                    'marginBottom': '1000px'
                                }
                            ),

                            fac.AntdDivider(
                                '下滑锚定示例',
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
    fac.AntdAffix(
        fac.AntdButton(
            '向下滑动页面体验固钉锚定效果',
            type='primary'
        ),
        offsetTop=100
    ),
    style={
        'marginBottom': '1000px'
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
                        id='下滑锚定示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            html.Div(
                                fac.AntdAffix(
                                    fac.AntdButton(
                                        '向上滑动页面体验固钉效果',
                                        type='dashed'
                                    ),
                                    offsetBottom=100,
                                    style={
                                        'float': 'right'
                                    }
                                ),
                                style={
                                    'marginTop': '1000px'
                                }
                            ),

                            fac.AntdDivider(
                                '上滑锚定示例',
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
    fac.AntdAffix(
        fac.AntdButton(
            '向上滑动页面体验固钉效果',
            type='dashed'
        ),
        offsetBottom=100,
        style={
            'float': 'right'
        }
    ),
    style={
        'marginTop': '1000px'
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
                        id='上滑锚定示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [

                            html.Div(
                                [
                                    html.Div(
                                        style={
                                            'height': '100px'
                                        }
                                    ),
                                    fac.AntdAffix(
                                        fac.AntdButton(
                                            '请在当前局部容器内下滑',
                                            danger=True
                                        ),
                                        offsetTop=50,
                                        target='affix-container-demo'
                                    ),
                                    html.Div(
                                        style={
                                            'height': '1000px'
                                        }
                                    ),
                                ],
                                id='affix-container-demo',
                                style={
                                    'border': '1px solid #f0f0f0',
                                    'maxHeight': '300px',
                                    'padding': '10px',
                                    'overflowY': 'auto',
                                    'background': '#f8f9fa'
                                }
                            ),

                            fac.AntdDivider(
                                '局部容器内锚定',
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
        html.Div(
            style={
                'height': '100px'
            }
        ),
        fac.AntdAffix(
            fac.AntdButton(
                '请在当前局部容器内下滑',
                danger=True
            ),
            offsetTop=50,
            target='affix-container-demo'
        ),
        html.Div(
            style={
                'height': '1000px'
            }
        ),
    ],
    id='affix-container-demo',
    style={
        'border': '1px solid #f0f0f0',
        'maxHeight': '300px',
        'padding': '10px',
        'overflowY': 'auto',
        'background': '#f8f9fa'
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
                        id='局部容器内锚定',
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
                        {'title': '下滑锚定示例', 'href': '#下滑锚定示例'},
                        {'title': '上滑锚定示例', 'href': '#上滑锚定示例'},
                        {'title': '局部容器内锚定', 'href': '#局部容器内锚定'},
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
                component_name='AntdAffix',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
