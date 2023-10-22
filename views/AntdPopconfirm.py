from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdPopconfirm
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
                                'title': 'AntdPopconfirm 气泡确认框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于实现二次确认功能，相较于对话框更加简便。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdPopconfirm(
                                fac.AntdButton(
                                    '触发'
                                ),
                                title='确认继续'
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '触发'
    ),
    title='确认继续'
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
                                    fac.AntdPopconfirm(
                                        fac.AntdButton(
                                            placement
                                        ),
                                        title=f'placement="{placement}"',
                                        placement=placement
                                    )
                                    for placement in [
                                        'top', 'left', 'right', 'bottom',
                                        'topLeft', 'topRight', 'bottomLeft',
                                        'bottomRight', 'leftTop', 'leftBottom',
                                        'rightTop', 'rightBottom'
                                    ]
                                ],
                                size='small',
                                wrap=True
                            ),

                            fac.AntdDivider(
                                '不同的展开方向',
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
        fac.AntdPopconfirm(
            fac.AntdButton(
                placement
            ),
            title=f'placement="{placement}"',
            placement=placement
        )
        for placement in [
            'top', 'left', 'right', 'bottom',
            'topLeft', 'topRight', 'bottomLeft',
            'bottomRight', 'leftTop', 'leftBottom',
            'rightTop', 'rightBottom'
        ]
    ],
    size='small',
    wrap=True
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
                        id='不同的展开方向',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdPopconfirm(
                                fac.AntdButton(
                                    '触发'
                                ),
                                title='气泡确认框',
                                okText='Ok',
                                cancelText='Cancel',
                                cancelButtonProps={
                                    'danger': True,
                                    'type': 'primary'
                                }
                            ),

                            fac.AntdDivider(
                                '自定义按钮',
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '触发'
    ),
    title='气泡确认框',
    okText='Ok',
    cancelText='Cancel',
    cancelButtonProps={
        'danger': True,
        'type': 'primary'
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
                        id='自定义按钮',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdPopconfirm(
                                fac.AntdButton(
                                    '点击触发'
                                ),
                                title='trigger="click"',
                                trigger='click'
                            ),

                            fac.AntdDivider(
                                '点击触发',
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '点击触发'
    ),
    title='trigger="click"',
    trigger='click'
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
                        id='点击触发',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '手动展开',
                                        id='popconfirm-open'
                                    ),
                                    fac.AntdPopconfirm(
                                        fac.AntdButton(
                                            '点击触发'
                                        ),
                                        id='popconfirm-open-demo',
                                        title='可控展开状态示例'
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '展开状态可控',
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
        fac.AntdButton(
            '手动展开',
            id='popconfirm-open'
        ),
        fac.AntdPopconfirm(
            fac.AntdButton(
                '点击触发'
            ),
            id='popconfirm-open-demo',
            title='可控展开状态示例'
        )
    ]
)

...

@app.callback(
    Output('popconfirm-open-demo', 'open'),
    Input('popconfirm-open', 'nClicks'),
    prevent_initial_call=True
)
def popconfirm_open_demo(nClicks):

    return True
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
                        id='展开状态可控',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdPopconfirm(
                                fac.AntdButton(
                                    '触发'
                                ),
                                id='popconfirm-demo',
                                title='回调示例'
                            ),

                            html.Pre(
                                id='popconfirm-demo-output'
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
fac.AntdPopconfirm(
    fac.AntdButton(
        '触发'
    ),
    id='popconfirm-demo',
    title='回调示例'
),

html.Pre(
    id='popconfirm-demo-output'
)

...

import json

...

@app.callback(
    Output('popconfirm-demo-output', 'children'),
    [Input('popconfirm-demo', 'confirmCounts'),
     Input('popconfirm-demo', 'cancelCounts')],
    prevent_initial_call=True
)
def popconfirm_demo(confirmCounts, cancelCounts):

    return json.dumps(
        dict(
            confirmCounts=confirmCounts,
            cancelCounts=cancelCounts
        ),
        indent=4,
        ensure_ascii=False
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
                        id='回调示例',
                        className='div-highlight'
                    ),

                    fac.AntdTitle(
                        '常见问题',
                        id='常见问题',
                        level=3,
                        className='common-problem-demo',
                        style={
                            'margin': '25px 0'
                        }
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Span(
                                        fac.AntdPopconfirm(
                                            fac.AntdButton(
                                                '示例1',
                                                type='primary'
                                            ),
                                            title='示例内容'
                                        ),
                                        style={
                                            'position': 'absolute',
                                            'left': 15,
                                            'bottom': 15
                                        }
                                    ),
                                    html.Span(
                                        fac.AntdPopconfirm(
                                            fac.AntdButton(
                                                '示例2',
                                                type='primary'
                                            ),
                                            title='示例内容'
                                        ),
                                        style={
                                            'position': 'absolute',
                                            'right': 15,
                                            'top': 15
                                        }
                                    ),
                                    html.Span(
                                        fac.AntdPopconfirm(
                                            fac.AntdButton(
                                                '示例3',
                                                type='primary'
                                            ),
                                            title='示例内容'
                                        ),
                                        style={
                                            'position': 'absolute',
                                            'right': 15,
                                            'bottom': 15
                                        }
                                    )
                                ],
                                style={
                                    'position': 'relative',
                                    'height': 300,
                                    'background': '#dee2e6'
                                }
                            ),

                            fac.AntdDivider(
                                '配合绝对定位',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '当直接将',
                                    fac.AntdText(
                                        'AntdPopconfirm',
                                        strong=True
                                    ),
                                    '施加于具有绝对定位样式的元素之上时，可能会遇到悬浮层位置显示异常的问题，推荐的稳定做法是为对应的',
                                    fac.AntdText(
                                        'AntdPopconfirm',
                                        strong=True
                                    ),
                                    '添加一层',
                                    fac.AntdText(
                                        'Span',
                                        strong=True
                                    ),
                                    '父元素，并将原先的绝对定位相关样式转而施加于此父元素之上'
                                ],
                                style={
                                    'textIndent': '2rem'
                                }
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
        html.Span(
            fac.AntdPopconfirm(
                fac.AntdButton(
                    '示例1',
                    type='primary'
                ),
                title='示例内容'
            ),
            style={
                'position': 'absolute',
                'left': 15,
                'bottom': 15
            }
        ),
        html.Span(
            fac.AntdPopconfirm(
                fac.AntdButton(
                    '示例2',
                    type='primary'
                ),
                title='示例内容'
            ),
            style={
                'position': 'absolute',
                'right': 15,
                'top': 15
            }
        ),
        html.Span(
            fac.AntdPopconfirm(
                fac.AntdButton(
                    '示例3',
                    type='primary'
                ),
                title='示例内容'
            ),
            style={
                'position': 'absolute',
                'right': 15,
                'bottom': 15
            }
        )
    ],
    style={
        'position': 'relative',
        'height': 300,
        'background': '#dee2e6'
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
                        id='常见问题|配合绝对定位',
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
                        {'title': '不同的展开方向', 'href': '#不同的展开方向'},
                        {'title': '自定义按钮', 'href': '#自定义按钮'},
                        {'title': '点击触发', 'href': '#点击触发'},
                        {'title': '展开状态可控', 'href': '#展开状态可控'},
                        {'title': '回调示例', 'href': '#回调示例'},
                        {
                            'title': '常见问题',
                            'href': '#常见问题',
                            'children': [
                                {
                                    'title': '配合绝对定位',
                                    'href': '#常见问题|配合绝对定位'
                                }
                            ]
                        }
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
                component_name='AntdPopconfirm',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
