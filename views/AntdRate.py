from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdRate
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
                                'title': 'AntdRate 评分'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供美观的星级打分功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRate(),
                                    fac.AntdRate(
                                        count=10,
                                        defaultValue=7
                                    )
                                ],
                                direction='vertical'
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
        fac.AntdRate(),
        fac.AntdRate(
            count=10,
            defaultValue=5
        )
    ],
    direction='vertical'
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
                            fac.AntdRate(
                                allowHalf=True,
                                defaultValue=3.5
                            ),

                            fac.AntdDivider(
                                '半星选择',
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
fac.AntdRate(
    allowHalf=True,
    defaultValue=3.5
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
                        id='半星选择',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdRate(
                                count=10,
                                tooltips=[f'等级{i + 1}' for i in range(10)]
                            ),

                            fac.AntdDivider(
                                '各星级提示文字',
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
fac.AntdRate(
    count=10,
    tooltips=[f'等级{i + 1}' for i in range(10)]
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
                        id='各星级提示文字',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdRate(
                                count=10,
                                defaultValue=7.5,
                                allowHalf=True,
                                disabled=True
                            ),

                            fac.AntdDivider(
                                '只读模式',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '　　设置参数',
                                    fac.AntdText('defaultValue', code=True),
                                    fac.AntdText('及'),
                                    fac.AntdText('disabled=True', code=True),
                                    '之后，即等价于只读模式，适合单纯的星级展示'
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdRate(
    count=10,
    defaultValue=7.5,
    allowHalf=True,
    disabled=True
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
                        id='只读模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdRate(
                                id='rate-demo',
                                count=10,
                                allowHalf=True,
                                defaultValue=1
                            ),

                            fac.AntdParagraph(
                                id='rate-demo-output'
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
fac.AntdRate(
    id='rate-demo',
    count=10,
    allowHalf=True,
    defaultValue=1
),

fac.AntdParagraph(
    id='rate-demo-output'
)

...

@app.callback(
    Output('rate-demo-output', 'children'),
    Input('rate-demo', 'value')
)
def rate_demo(value):

    return f'value: {value}'
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
                        {'title': '半星选择', 'href': '#半星选择'},
                        {'title': '各星级提示文字', 'href': '#各星级提示文字'},
                        {'title': '只读模式', 'href': '#只读模式'},
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
                component_name='AntdRate',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
