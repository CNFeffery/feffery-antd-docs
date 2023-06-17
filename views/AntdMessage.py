from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdMessage
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
                                'title': 'AntdMessage 全局提示'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于渲染弹出式的全局提示框。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发全局提示',
                                id='message-basic-demo-new',
                                type='primary'
                            ),

                            html.Div(
                                id='message-basic-demo'
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '全局提示的常规使用方式是通过回调向某个容器输出，每一次输出都会触发一条新的全局提示的新增'
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
fac.AntdButton(
    '触发全局提示',
    id='message-basic-demo-new',
    type='primary'
),

html.Div(
    id='message-basic-demo'
)

...

@app.callback(
    Output('message-basic-demo', 'children'),
    Input('message-basic-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_basic_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        type='success'
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
                                    fac.AntdRadioGroup(
                                        id='message-type-demo-type',
                                        options=[
                                            {
                                                'label': type_,
                                                'value': type_
                                            }
                                            for type_ in [
                                                'default', 'info', 'success', 'warning', 'error'
                                            ]
                                        ],
                                        defaultValue='default'
                                    ),
                                    fac.AntdButton(
                                        '触发全局提示',
                                        id='message-type-demo-new',
                                        type='primary'
                                    )
                                ],
                                direction='vertical'
                            ),

                            html.Div(
                                id='message-type-demo'
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
        fac.AntdRadioGroup(
            id='message-type-demo-type',
            options=[
                {
                    'label': type_,
                    'value': type_
                }
                for type_ in [
                    'default', 'info', 'success', 'warning', 'error'
                ]
            ],
            defaultValue='default'
        ),
        fac.AntdButton(
            '触发全局提示',
            id='message-type-demo-new',
            type='primary'
        )
    ],
    direction='vertical'
),

html.Div(
    id='message-type-demo'
)

...

@app.callback(
    Output('message-type-demo', 'children'),
    Input('message-type-demo-new', 'nClicks'),
    State('message-type-demo-type', 'value'),
    prevent_initial_call=True
)
def message_type_demo(nClicks, value):

    return fac.AntdMessage(
        content='全局提示示例',
        type=value
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
                            fac.AntdButton(
                                '触发10s全局提示',
                                id='message-duration-demo-new',
                                type='primary'
                            ),

                            html.Div(
                                id='message-duration-demo'
                            ),

                            fac.AntdDivider(
                                '自定义显示持续时长',
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
fac.AntdButton(
    '触发10s全局提示',
    id='message-duration-demo-new',
    type='primary'
),

html.Div(
    id='message-duration-demo'
)

...

@app.callback(
    Output('message-duration-demo', 'children'),
    Input('message-duration-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_duration_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        duration=10,
        type='success'
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
                        id='自定义显示持续时长',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发距离顶端200px全局提示',
                                id='message-top-demo-new',
                                type='primary'
                            ),

                            html.Div(
                                id='message-top-demo'
                            ),

                            fac.AntdDivider(
                                '设置顶端最小距离',
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
fac.AntdButton(
    '触发距离顶端200px全局提示',
    id='message-top-demo-new',
    type='primary'
),

html.Div(
    id='message-top-demo'
)

...

@app.callback(
    Output('message-top-demo', 'children'),
    Input('message-top-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_top_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        top=200,
        type='success'
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
                        id='设置顶端最小距离',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发全局提示',
                                id='message-max-count-demo-new',
                                type='primary'
                            ),

                            html.Div(
                                id='message-max-count-demo'
                            ),

                            fac.AntdDivider(
                                '设置同屏最大消息数',
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
fac.AntdButton(
    '触发全局提示',
    id='message-max-count-demo-new',
    type='primary'
),

html.Div(
    id='message-max-count-demo'
)

...

@app.callback(
    Output('message-max-count-demo', 'children'),
    Input('message-max-count-demo-new', 'nClicks'),
    prevent_initial_call=True
)
def message_max_count_demo(nClicks):

    return fac.AntdMessage(
        content='全局提示示例',
        type='success',
        maxCount=3
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
                        id='设置同屏最大消息数',
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
                        {'title': '自定义显示持续时长', 'href': '#自定义显示持续时长'},
                        {'title': '设置顶端最小距离', 'href': '#设置顶端最小距离'},
                        {'title': '设置同屏最大消息数', 'href': '#设置同屏最大消息数'},
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
                component_name='AntdMessage',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
