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
                                'title': 'AntdSpoiler 展开收起'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于实现对指定内容的展开收起效果。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpoiler(
                                fac.AntdParagraph(
                                    '内容示例'*100
                                ),
                                maxHeight=70
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
fac.AntdSpoiler(
    fac.AntdParagraph(
        '内容示例'*100
    ),
    maxHeight=70
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
                            fac.AntdSpoiler(
                                fac.AntdParagraph(
                                    '内容示例'*100
                                ),
                                maxHeight=70,
                                labelPosition='right'
                            ),

                            fac.AntdDivider(
                                '展开收起按钮置于右侧',
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
fac.AntdSpoiler(
    fac.AntdParagraph(
        '内容示例'*100
    ),
    maxHeight=70,
    labelPosition='right'
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
                        id='展开收起按钮置于右侧',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpoiler(
                                fac.AntdParagraph(
                                    '内容示例'*100
                                ),
                                maxHeight=70,
                                transitionDuration=0.5
                            ),

                            fac.AntdDivider(
                                '设置动画时长',
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
fac.AntdSpoiler(
    fac.AntdParagraph(
        '内容示例'*100
    ),
    maxHeight=70,
    transitionDuration=0.5
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
                        id='设置动画时长',
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
                        {'title': '展开收起按钮置于右侧', 'href': '#展开收起按钮置于右侧'},
                        {'title': '设置动画时长', 'href': '#设置动画时长'},
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
                component_name='AntdSpoiler',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
