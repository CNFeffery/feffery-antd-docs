from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdSpin
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
                                'title': 'AntdSpin 加载动画'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为正在加载中的内容添加加载动画。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例',
                                id='spin-basic-demo-trigger',
                                style={
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSpin(
                                fac.AntdText(
                                    id='spin-basic-demo-output'
                                ),
                                text='回调中'
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
fac.AntdButton(
    '触发示例',
    id='spin-basic-demo-trigger',
    style={
        'marginBottom': 10
    }
),

fac.AntdSpin(
    fac.AntdText(
        id='spin-basic-demo-output'
    ),
    text='回调中'
)

...

import time

...

@app.callback(
    Output('spin-basic-demo-output', 'children'),
    Input('spin-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def spin_basic_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'
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
                                    fac.AntdButton(
                                        '按钮1',
                                        id='spin-exclude-demo-trigger1'
                                    ),
                                    fac.AntdButton(
                                        '按钮2',
                                        id='spin-exclude-demo-trigger2'
                                    )
                                ],
                                style={
                                    'width': '100%',
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSpin(
                                [
                                    fac.AntdParagraph(
                                        id='spin-exclude-demo-output1'
                                    ),
                                    fac.AntdParagraph(
                                        id='spin-exclude-demo-output2'
                                    )
                                ],
                                text='回调中',
                                listenPropsMode='exclude',
                                excludeProps=[
                                    'spin-exclude-demo-output1.children'
                                ]
                            ),

                            fac.AntdDivider(
                                '排除监听模式',
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
            '按钮1',
            id='spin-exclude-demo-trigger1'
        ),
        fac.AntdButton(
            '按钮2',
            id='spin-exclude-demo-trigger2'
        )
    ],
    style={
        'width': '100%',
        'marginBottom': 10
    }
),

fac.AntdSpin(
    [
        fac.AntdParagraph(
            id='spin-exclude-demo-output1'
        ),
        fac.AntdParagraph(
            id='spin-exclude-demo-output2'
        )
    ],
    text='回调中',
    listenPropsMode='exclude',
    excludeProps=[
        'spin-exclude-demo-output1.children'
    ]
)

...

import time

...

@app.callback(
    Output('spin-exclude-demo-output1', 'children'),
    Input('spin-exclude-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('spin-exclude-demo-output2', 'children'),
    Input('spin-exclude-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_demo2(nClicks):

    time.sleep(1)

    return f'按钮2: {nClicks}'
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
                        id='排除监听模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '按钮1',
                                        id='spin-include-demo-trigger1'
                                    ),
                                    fac.AntdButton(
                                        '按钮2',
                                        id='spin-include-demo-trigger2'
                                    )
                                ],
                                style={
                                    'width': '100%',
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSpin(
                                [
                                    fac.AntdParagraph(
                                        id='spin-include-demo-output1'
                                    ),
                                    fac.AntdParagraph(
                                        id='spin-include-demo-output2'
                                    )
                                ],
                                text='回调中',
                                listenPropsMode='include',
                                includeProps=[
                                    'spin-include-demo-output1.children'
                                ]
                            ),

                            fac.AntdDivider(
                                '包含监听模式',
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
            '按钮1',
            id='spin-include-demo-trigger1'
        ),
        fac.AntdButton(
            '按钮2',
            id='spin-include-demo-trigger2'
        )
    ],
    style={
        'width': '100%',
        'marginBottom': 10
    }
),

fac.AntdSpin(
    [
        fac.AntdParagraph(
            id='spin-include-demo-output1'
        ),
        fac.AntdParagraph(
            id='spin-include-demo-output2'
        )
    ],
    text='回调中',
    listenPropsMode='include',
    includeProps=[
        'spin-include-demo-output1.children'
    ]
)

...

import time

...

@app.callback(
    Output('spin-include-demo-output1', 'children'),
    Input('spin-include-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('spin-include-demo-output2', 'children'),
    Input('spin-include-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_demo2(nClicks):

    time.sleep(1)

    return f'按钮2: {nClicks}'
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
                        id='包含监听模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例',
                                id='spin-custom-demo-trigger',
                                style={
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSpin(
                                fac.AntdText(
                                    'nClicks: 0',
                                    id='spin-custom-demo-output'
                                ),
                                indicator=fuc.FefferyExtraSpinner(
                                    type='ring'
                                )
                            ),

                            fac.AntdDivider(
                                '自定义加载动画',
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
    '触发示例',
    id='spin-custom-demo-trigger',
    style={
        'marginBottom': 10
    }
),

fac.AntdSpin(
    fac.AntdText(
        'nClicks: 0',
        id='spin-custom-demo-output'
    ),
    indicator=fuc.FefferyExtraSpinner(
        type='ring'
    )
)

...

import time

...

@app.callback(
    Output('spin-custom-demo-output', 'children'),
    Input('spin-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def spin_custom_demo(nClicks):

    time.sleep(2)

    return f'nClicks: {nClicks}'
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
                        id='自定义加载动画',
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
                        {'title': '排除监听模式', 'href': '#排除监听模式'},
                        {'title': '包含监听模式', 'href': '#包含监听模式'},
                        {'title': '自定义加载动画', 'href': '#自定义加载动画'},
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
                component_name='AntdSpin',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
