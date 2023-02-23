from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCollapse
from .side_props import render_side_props_layout

docs_content = html.Div(
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
                            'title': 'AntdCollapse 折叠面板'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于渲染单个可折叠展开的特殊容器，典型如本网站所有示例代码所在容器。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdCollapse(
                            fac.AntdParagraph(
                                '内容示例'*20
                            ),
                            title='折叠面板示例',
                            style={
                                'width': 300
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
fac.AntdCollapse(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    title='折叠面板示例',
    style={
        'width': 300
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

                html.Div(
                    [
                        fac.AntdCollapse(
                            fac.AntdParagraph(
                                '内容示例'*20
                            ),
                            isOpen=False,
                            title='折叠面板示例',
                            style={
                                'width': 300
                            }
                        ),

                        fac.AntdDivider(
                            '初始化折叠',
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
fac.AntdCollapse(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    isOpen=False,
    title='折叠面板示例',
    style={
        'width': 300
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
                    id='初始化折叠',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCollapse(
                            fac.AntdParagraph(
                                '内容示例'*20
                            ),
                            bordered=False,
                            title='折叠面板示例',
                            style={
                                'width': 300
                            }
                        ),

                        fac.AntdDivider(
                            '无边框',
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
fac.AntdCollapse(
    fac.AntdParagraph(
        '内容示例'*20
    ),
    bordered=False,
    title='折叠面板示例',
    style={
        'width': 300
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
                    id='无边框',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdCollapse(
                                fac.AntdParagraph(
                                    '内容示例'*20
                                ),
                                ghost=True,
                                title='折叠面板示例'
                            ),
                            style={
                                'background': '#e7f5ff',
                                'width': 300
                            }
                        ),

                        fac.AntdDivider(
                            '透明面板模式',
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
    fac.AntdCollapse(
        fac.AntdParagraph(
            '内容示例'*20
        ),
        ghost=True,
        title='折叠面板示例'
    ),
    style={
        'background': '#e7f5ff',
        'width': 300
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
                    id='透明面板模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdCollapse(
                                    fac.AntdParagraph(
                                        '内容示例'*20
                                    ),
                                    title='collapsible="header"',
                                    collapsible='header',
                                    isOpen=False,
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdCollapse(
                                    fac.AntdParagraph(
                                        '内容示例'*20
                                    ),
                                    title='collapsible="disabled"',
                                    collapsible='disabled',
                                    isOpen=False,
                                    style={
                                        'width': 300
                                    }
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '不同的折叠触发策略',
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
        fac.AntdCollapse(
            fac.AntdParagraph(
                '内容示例'*20
            ),
            title='collapsible="header"',
            collapsible='header',
            isOpen=False,
            style={
                'width': 300
            }
        ),
        fac.AntdCollapse(
            fac.AntdParagraph(
                '内容示例'*20
            ),
            title='collapsible="disabled"',
            collapsible='disabled',
            isOpen=False,
            style={
                'width': 300
            }
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
                    id='不同的折叠触发策略',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            'forceRender=False（默认）',
                            innerTextOrientation='left'
                        ),

                        fac.AntdSpace(
                            [
                                fac.AntdCollapse(
                                    fac.AntdInput(
                                        id='collapse-child-demo1',
                                        defaultValue='内容测试',
                                        style={
                                            'width': '100%'
                                        }
                                    ),
                                    isOpen=False,
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdText(
                                    id='collapse-child-demo1-output'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            'forceRender=True',
                            innerTextOrientation='left'
                        ),

                        fac.AntdSpace(
                            [
                                fac.AntdCollapse(
                                    fac.AntdInput(
                                        id='collapse-child-demo2',
                                        defaultValue='内容测试',
                                        style={
                                            'width': '100%'
                                        }
                                    ),
                                    isOpen=False,
                                    forceRender=True,
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdText(
                                    id='collapse-child-demo2-output'
                                )
                            ]
                        ),

                        fac.AntdDivider(
                            'forceRender的应用场景',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '在设置参数',
                                fac.AntdText(
                                    'forceRender=True',
                                    code=True
                                ),
                                '后，即使折叠面板初始化时处于折叠状态，也会强制提前将内部元素渲染到页面中，从而便于一些初始化回调的正常赋值'
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
fac.AntdDivider(
    'forceRender=False（默认）',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdCollapse(
            fac.AntdInput(
                id='collapse-child-demo1',
                defaultValue='内容测试',
                style={
                    'width': '100%'
                }
            ),
            isOpen=False,
            style={
                'width': 300
            }
        ),
        fac.AntdText(
            id='collapse-child-demo1-output'
        )
    ]
),

fac.AntdDivider(
    'forceRender=True',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdCollapse(
            fac.AntdInput(
                id='collapse-child-demo2',
                defaultValue='内容测试',
                style={
                    'width': '100%'
                }
            ),
            isOpen=False,
            forceRender=True,
            style={
                'width': 300
            }
        ),
        fac.AntdText(
            id='collapse-child-demo2-output'
        )
    ]
)

...

@app.callback(
    Output('collapse-child-demo1-output', 'children'),
    Input('collapse-child-demo1', 'value')
)
def collapse_child_demo1(value):

    return value

@app.callback(
    Output('collapse-child-demo2-output', 'children'),
    Input('collapse-child-demo2', 'value')
)
def collapse_child_demo2(value):

    return value
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
                    id='forceRender的应用场景',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdCollapse(
                                    fac.AntdParagraph(
                                        '内容示例'*20
                                    ),
                                    id='collapse-demo',
                                    isOpen=True,
                                    title='回调示例',
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdText(
                                    id='collapse-demo-output'
                                )
                            ],
                            direction='vertical'
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
        fac.AntdCollapse(
            fac.AntdParagraph(
                '内容示例'*20
            ),
            id='collapse-demo',
            isOpen=True,
            title='回调示例',
            style={
                'width': 300
            }
        ),
        fac.AntdText(
            id='collapse-demo-output'
        )
    ],
    direction='vertical'
)

...

@app.callback(
    Output('collapse-demo-output', 'children'),
    Input('collapse-demo', 'isOpen')
)
def collapse_demo(isOpen):

    return f'isOpen={isOpen}'
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
                    {'title': '初始化折叠', 'href': '#初始化折叠'},
                    {'title': '无边框', 'href': '#无边框'},
                    {'title': '透明面板模式', 'href': '#透明面板模式'},
                    {'title': '不同的折叠触发策略', 'href': '#不同的折叠触发策略'},
                    {'title': 'forceRender的应用场景', 'href': '#forceRender的应用场景'},
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
            component_name='AntdCollapse'
        )
    ],
    style={
        'display': 'flex'
    }
)
