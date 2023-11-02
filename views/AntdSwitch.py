from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSwitch
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
                                'title': 'AntdSwitch 开关'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供在两种状态之间进行切换的功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSwitch(),

                                    fac.AntdSwitch(
                                        checked=True
                                    )
                                ]
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
        fac.AntdSwitch(),

        fac.AntdSwitch(
            checked=True
        )
    ]
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
                            fac.AntdSwitch(
                                checkedChildren='打开',
                                unCheckedChildren='关闭'
                            ),

                            fac.AntdDivider(
                                '自定义状态标签',
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
fac.AntdSwitch(
    checkedChildren='打开',
    unCheckedChildren='关闭'
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
                        id='自定义状态标签',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSwitch(
                                checked=True,
                                size='small'
                            ),

                            fac.AntdDivider(
                                '迷你尺寸',
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
fac.AntdSwitch(
    checked=True,
    size='small'
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
                        id='迷你尺寸',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSwitch(
                                        disabled=True
                                    ),
                                    fac.AntdSwitch(
                                        checked=True,
                                        disabled=True
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '禁用状态',
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
        fac.AntdSwitch(
            disabled=True
        ),
        fac.AntdSwitch(
            checked=True,
            disabled=True
        )
    ]
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSwitch(
                                        readOnly=True
                                    ),
                                    fac.AntdSwitch(
                                        checked=True,
                                        readOnly=True
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '只读状态',
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
        fac.AntdSwitch(
            readOnly=True
        ),
        fac.AntdSwitch(
            checked=True,
            readOnly=True
        )
    ]
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
                        id='只读状态',
                        className='div-highlight'
                    ),
                    
                    html.Div(
                        [
                            fac.AntdSwitch(
                                autoFocus=True
                            ),

                            fac.AntdDivider(
                                '自动获取焦点',
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
fac.AntdSwitch(
    autoFocus=True
),
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
                        id='自动获取焦点',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSwitch(
                                        loading=True
                                    ),
                                    fac.AntdSwitch(
                                        checked=True,
                                        loading=True
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '加载中状态',
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
        fac.AntdSwitch(
            loading=True
        ),
        fac.AntdSwitch(
            checked=True,
            loading=True
        )
    ]
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
                        id='加载中状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSwitch(
                                id='switch-demo'
                            ),

                            fac.AntdParagraph(
                                id='switch-demo-output'
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
fac.AntdSwitch(
    id='switch-demo'
),

fac.AntdParagraph(
    id='switch-demo-output'
)

...

@app.callback(
    Output('switch-demo-output', 'children'),
    Input('switch-demo', 'checked')
)
def switch_demo(checked):

    return f'checked: {checked}'
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
                        {'title': '自定义状态标签', 'href': '#自定义状态标签'},
                        {'title': '迷你尺寸', 'href': '#迷你尺寸'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '自动获取焦点', 'href': '#自动获取焦点'},
                        {'title': '加载中状态', 'href': '#加载中状态'},
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
                component_name='AntdSwitch',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
