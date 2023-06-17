from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSkeleton
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
                                'title': 'AntdSkeleton 骨骼屏'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为正在加载中的内容添加骨骼屏加载动画。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例',
                                id='skeleton-basic-demo-trigger',
                                style={
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSkeleton(
                                fac.AntdParagraph(
                                    id='skeleton-basic-demo-output'
                                )
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
    id='skeleton-basic-demo-trigger',
    style={
        'marginBottom': 10
    }
),

fac.AntdSkeleton(
    fac.AntdParagraph(
        id='skeleton-basic-demo-output'
    )
)

...

import time

...

@app.callback(
    Output('skeleton-basic-demo-output', 'children'),
    Input('skeleton-basic-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_basic_demo(nClicks):

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
                            fac.AntdButton(
                                '触发示例',
                                id='skeleton-active-demo-trigger',
                                style={
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSkeleton(
                                fac.AntdParagraph(
                                    id='skeleton-active-demo-output'
                                ),
                                active=True
                            ),

                            fac.AntdDivider(
                                '启用扫屏动画',
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
    id='skeleton-active-demo-trigger',
    style={
        'marginBottom': 10
    }
),

fac.AntdSkeleton(
    fac.AntdParagraph(
        id='skeleton-active-demo-output'
    ),
    active=True
)

...

import time

...

@app.callback(
    Output('skeleton-active-demo-output', 'children'),
    Input('skeleton-active-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_active_demo(nClicks):

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
                        id='启用扫屏动画',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                '触发示例',
                                id='skeleton-custom-demo-trigger',
                                style={
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSkeleton(
                                fac.AntdParagraph(
                                    id='skeleton-custom-demo-output'
                                ),
                                active=True,
                                avatar={
                                    'size': 'large',
                                    'shape': 'square'
                                },
                                paragraph={
                                    'rows': 10,
                                    'width': '20%'
                                },
                                title={
                                    'width': '4rem'
                                }
                            ),

                            fac.AntdDivider(
                                '定制化各部件',
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
    id='skeleton-custom-demo-trigger',
    style={
        'marginBottom': 10
    }
),

fac.AntdSkeleton(
    fac.AntdParagraph(
        id='skeleton-custom-demo-output'
    ),
    active=True,
    avatar={
        'size': 'large',
        'shape': 'square'
    },
    paragraph={
        'rows': 10,
        'width': '20%'
    },
    title={
        'width': '4rem'
    }
)

...

import time

...

@app.callback(
    Output('skeleton-custom-demo-output', 'children'),
    Input('skeleton-custom-demo-trigger', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_custom_demo(nClicks):

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
                        id='定制化各部件',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '按钮1',
                                        id='skeleton-exclude-demo-trigger1'
                                    ),
                                    fac.AntdButton(
                                        '按钮2',
                                        id='skeleton-exclude-demo-trigger2'
                                    )
                                ],
                                style={
                                    'width': '100%',
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSkeleton(
                                [
                                    fac.AntdParagraph(
                                        id='skeleton-exclude-demo-output1'
                                    ),
                                    fac.AntdParagraph(
                                        id='skeleton-exclude-demo-output2'
                                    )
                                ],
                                active=True,
                                listenPropsMode='exclude',
                                excludeProps=[
                                    'skeleton-exclude-demo-output1.children'
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
            id='skeleton-exclude-demo-trigger1'
        ),
        fac.AntdButton(
            '按钮2',
            id='skeleton-exclude-demo-trigger2'
        )
    ],
    style={
        'width': '100%',
        'marginBottom': 10
    }
),

fac.AntdSkeleton(
    [
        fac.AntdParagraph(
            id='skeleton-exclude-demo-output1'
        ),
        fac.AntdParagraph(
            id='skeleton-exclude-demo-output2'
        )
    ],
    active=True,
    listenPropsMode='exclude',
    excludeProps=[
        'skeleton-exclude-demo-output1.children'
    ]
)

...

import time

...

@app.callback(
    Output('skeleton-exclude-demo-output1', 'children'),
    Input('skeleton-exclude-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_exclude_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('skeleton-exclude-demo-output2', 'children'),
    Input('skeleton-exclude-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_exclude_demo2(nClicks):

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
                                        id='skeleton-include-demo-trigger1'
                                    ),
                                    fac.AntdButton(
                                        '按钮2',
                                        id='skeleton-include-demo-trigger2'
                                    )
                                ],
                                style={
                                    'width': '100%',
                                    'marginBottom': 10
                                }
                            ),

                            fac.AntdSkeleton(
                                [
                                    fac.AntdParagraph(
                                        id='skeleton-include-demo-output1'
                                    ),
                                    fac.AntdParagraph(
                                        id='skeleton-include-demo-output2'
                                    )
                                ],
                                active=True,
                                listenPropsMode='include',
                                includeProps=[
                                    'skeleton-include-demo-output1.children'
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
            id='skeleton-include-demo-trigger1'
        ),
        fac.AntdButton(
            '按钮2',
            id='skeleton-include-demo-trigger2'
        )
    ],
    style={
        'width': '100%',
        'marginBottom': 10
    }
),

fac.AntdSkeleton(
    [
        fac.AntdParagraph(
            id='skeleton-include-demo-output1'
        ),
        fac.AntdParagraph(
            id='skeleton-include-demo-output2'
        )
    ],
    active=True,
    listenPropsMode='include',
    includeProps=[
        'skeleton-include-demo-output1.children'
    ]
)

...

@app.callback(
    Output('skeleton-include-demo-output1', 'children'),
    Input('skeleton-include-demo-trigger1', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_include_demo1(nClicks):

    time.sleep(1)

    return f'按钮1: {nClicks}'


@app.callback(
    Output('skeleton-include-demo-output2', 'children'),
    Input('skeleton-include-demo-trigger2', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_include_demo2(nClicks):

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
                        {'title': '启用扫屏动画', 'href': '#启用扫屏动画'},
                        {'title': '定制化各部件', 'href': '#定制化各部件'},
                        {'title': '排除监听模式', 'href': '#排除监听模式'},
                        {'title': '包含监听模式', 'href': '#包含监听模式'},
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
                component_name='AntdSkeleton',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
