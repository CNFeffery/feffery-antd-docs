from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCopyText
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
                                'title': 'AntdCopyText 文本复制'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于帮助用户快速复制指定文本内容。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdCopyText(
                                text='AntdCopyText复制示例'
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
fac.AntdCopyText(
    text='AntdCopyText复制示例'
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
                            fac.AntdCopyText(
                                text='AntdCopyText复制示例',
                                beforeIcon='点我复制',
                                afterIcon='复制成功'
                            ),

                            fac.AntdCopyText(
                                text='AntdCopyText复制示例',
                                beforeIcon=fac.AntdIcon(icon='antd-smile'),
                                afterIcon=fac.AntdIcon(icon='antd-like')
                            ),

                            fac.AntdDivider(
                                '自定义复制前后渲染内容',
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
fac.AntdCopyText(
    text='AntdCopyText复制示例',
    beforeIcon='点我复制',
    afterIcon='复制成功'
),

fac.AntdCopyText(
    text='AntdCopyText复制示例',
    beforeIcon=fac.AntdIcon(icon='antd-smile'),
    afterIcon=fac.AntdIcon(icon='antd-like')
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
                        id='自定义复制前后渲染内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        id='copy-text-input',
                                        maxLength=20,
                                        style={
                                            'width': '150px'
                                        }
                                    ),
                                    fac.AntdCopyText(
                                        id='copy-text-output',
                                        text='无内容'
                                    )
                                ]
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
fac.AntdSpace(
    [
        fac.AntdInput(
            id='copy-text-input',
            maxLength=20,
            style={
                'width': '150px'
            }
        ),
        fac.AntdCopyText(
            id='copy-text-output',
            text='无内容'
        )
    ]
)

...

@app.callback(
    Output('copy-text-output', 'text'),
    Input('copy-text-input', 'value')
)
def copy_text_callback(value):
    return value or '无内容'
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
                        {'title': '自定义复制前后渲染内容', 'href': '#自定义复制前后渲染内容'},
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
                component_name='AntdCopyText',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
