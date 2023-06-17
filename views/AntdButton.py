from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdButton
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
                                'title': '通用'
                            },
                            {
                                'title': 'AntdButton 按钮'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于在各种场景下作为功能逻辑的触发点。')
                        ]
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    fac.AntdButton('default'),
                                    fac.AntdButton('primary', type='primary'),
                                    fac.AntdButton('ghost', type='ghost'),
                                    fac.AntdButton('dashed', type='dashed'),
                                    fac.AntdButton('link', type='link'),
                                    fac.AntdButton('text', type='text')
                                ]
                            ),

                            fac.AntdDivider(
                                '不同type对应按钮样式风格',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText('注：'),
                                    fac.AntdText('ghost', strong=True),
                                    fac.AntdText('模式相当于透明背景的'),
                                    fac.AntdText('default', strong=True),
                                    fac.AntdText('模式')
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
        fac.AntdButton('default'),
        fac.AntdButton('primary', type='primary'),
        fac.AntdButton('ghost', type='ghost'),
        fac.AntdButton('dashed', type='dashed'),
        fac.AntdButton('link', type='link'),
        fac.AntdButton('text', type='text')
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
                        id='不同type对应按钮样式风格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                'feffery-antd-components',
                                href='https://github.com/CNFeffery/feffery-antd-components',
                                target='_blank',
                                type='primary'
                            ),

                            fac.AntdDivider(
                                '充当链接跳转功能',
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
    'feffery-antd-components',
    href='https://github.com/CNFeffery/feffery-antd-components',
    target='_blank',
    type='primary'
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
                        id='充当链接跳转功能',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdButton(
                                'feffery-antd-components',
                                block=True,
                                type='primary'
                            ),

                            fac.AntdDivider(
                                '撑满父级元素宽度',
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
    'feffery-antd-components',
    block=True,
    type='primary'
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
                        id='撑满父级元素宽度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        'default',
                                        danger=True
                                    ),
                                    fac.AntdButton(
                                        'primary',
                                        type='primary',
                                        danger=True
                                    ),
                                    fac.AntdButton(
                                        'ghost',
                                        type='ghost',
                                        danger=True
                                    ),
                                    fac.AntdButton(
                                        'dashed',
                                        type='dashed',
                                        danger=True
                                    ),
                                    fac.AntdButton(
                                        'link',
                                        type='link',
                                        danger=True
                                    ),
                                    fac.AntdButton(
                                        'text',
                                        type='text',
                                        danger=True
                                    )
                                ],
                                size='small'
                            ),

                            fac.AntdDivider(
                                '渲染为危险警告状态',
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
            'default',
            danger=True
        ),
        fac.AntdButton(
            'primary',
            type='primary',
            danger=True
        ),
        fac.AntdButton(
            'ghost',
            type='ghost',
            danger=True
        ),
        fac.AntdButton(
            'dashed',
            type='dashed',
            danger=True
        ),
        fac.AntdButton(
            'link',
            type='link',
            danger=True
        ),
        fac.AntdButton(
            'text',
            type='text',
            danger=True
        )
    ],
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
                        id='渲染为危险警告状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        'default',
                                        disabled=True
                                    ),
                                    fac.AntdButton(
                                        'primary',
                                        type='primary',
                                        disabled=True
                                    ),
                                    fac.AntdButton(
                                        'ghost',
                                        type='ghost',
                                        disabled=True
                                    ),
                                    fac.AntdButton(
                                        'dashed',
                                        type='dashed',
                                        disabled=True
                                    ),
                                    fac.AntdButton(
                                        'link',
                                        type='link',
                                        disabled=True
                                    ),
                                    fac.AntdButton(
                                        'text',
                                        type='text',
                                        disabled=True
                                    )
                                ],
                                size='small'
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
        fac.AntdButton(
            'default',
            disabled=True
        ),
        fac.AntdButton(
            'primary',
            type='primary',
            disabled=True
        ),
        fac.AntdButton(
            'ghost',
            type='ghost',
            disabled=True
        ),
        fac.AntdButton(
            'dashed',
            type='dashed',
            disabled=True
        ),
        fac.AntdButton(
            'link',
            type='link',
            disabled=True
        ),
        fac.AntdButton(
            'text',
            type='text',
            disabled=True
        )
    ],
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '默认',
                                        type='primary'
                                    ),
                                    fac.AntdButton(
                                        'circle',
                                        shape='circle',
                                        type='primary'
                                    ),
                                    fac.AntdButton(
                                        'round',
                                        shape='round',
                                        type='primary'
                                    )
                                ],
                                size='small'
                            ),

                            fac.AntdDivider(
                                '不同的按钮形状',
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
            '默认',
            type='primary'
        ),
        fac.AntdButton(
            'circle',
            shape='circle',
            type='primary'
        ),
        fac.AntdButton(
            'round',
            shape='round',
            type='primary'
        )
    ],
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
                        id='不同的按钮形状',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        'antd-reload',
                                        type='dashed',
                                        icon=fac.AntdIcon(
                                            icon='antd-reload'
                                        )
                                    ),
                                    fac.AntdButton(
                                        'md-power-settings-new',
                                        icon=fac.AntdIcon(
                                            icon='md-power-settings-new'
                                        )
                                    ),
                                    fac.AntdButton(
                                        'md-layers',
                                        type='primary',
                                        icon=fac.AntdIcon(
                                            icon='md-layers'
                                        )
                                    ),
                                    fac.AntdButton(
                                        'fc-repair',
                                        type='dashed',
                                        icon=fac.AntdIcon(
                                            icon='fc-repair'
                                        )
                                    )
                                ],
                                size='small'
                            ),

                            fac.AntdDivider(
                                '设置内嵌前缀元素',
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
            'antd-reload',
            type='dashed',
            icon=fac.AntdIcon(
                icon='antd-reload'
            )
        ),
        fac.AntdButton(
            'md-power-settings-new',
            icon=fac.AntdIcon(
                icon='md-power-settings-new'
            )
        ),
        fac.AntdButton(
            'md-layers',
            type='primary',
            icon=fac.AntdIcon(
                icon='md-layers'
            )
        ),
        fac.AntdButton(
            'fc-repair',
            type='dashed',
            icon=fac.AntdIcon(
                icon='fc-repair'
            )
        )
    ],
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
                        id='设置内嵌前缀元素',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '常规点击',
                                innerTextOrientation='left'
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '点击',
                                        id='button-click-demo'
                                    ),
                                    fac.AntdText(
                                        id='button-click-demo-output'
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '500ms防抖',
                                innerTextOrientation='left'
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '点击',
                                        id='button-debounce-click-demo',
                                        debounceWait=500
                                    ),
                                    fac.AntdText(
                                        id='button-debounce-click-demo-output'
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
fac.AntdDivider(
    '常规点击',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdButton(
            '点击',
            id='button-click-demo'
        ),
        fac.AntdText(
            id='button-click-demo-output'
        )
    ]
),

fac.AntdDivider(
    '500ms防抖',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdButton(
            '点击',
            id='button-debounce-click-demo',
            debounceWait=500
        ),
        fac.AntdText(
            id='button-debounce-click-demo-output'
        )
    ]
)

...

@app.callback(
    Output('button-click-demo-output', 'children'),
    Input('button-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_click_demo(nClicks):

    return f'nClicks: {nClicks}'


@app.callback(
    Output('button-debounce-click-demo-output', 'children'),
    Input('button-debounce-click-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_debounce_click_demo(nClicks):

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
                        id='回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        '请点击',
                                        id='button-auto-loading-demo',
                                        type='primary',
                                        loadingChildren='运算中',
                                        autoSpin=True
                                    ),
                                    fac.AntdText(
                                        id='button-auto-loading-demo-output'
                                    )
                                ],
                                align='center'
                            ),

                            fac.AntdDivider(
                                '利用loading展示回调中状态',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '在设置参数',
                                    fac.AntdText('autoSpin=True', code=True),
                                    '后，每次按钮被点击后都会立即自动进入loading中状态，配合此特性以及参数loadingChildren、loading，',
                                    '可以像本例一样更好地向用户展示运算中状态'
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
fac.AntdSpace(
    [
        fac.AntdButton(
            '请点击',
            id='button-auto-loading-demo',
            type='primary',
            loadingChildren='运算中',
            autoSpin=True
        ),
        fac.AntdText(
            id='button-auto-loading-demo-output'
        )
    ],
    align='center'
)

...

import time

@app.callback(
    [Output('button-auto-loading-demo-output', 'children'),
     Output('button-auto-loading-demo', 'loading')],
    Input('button-auto-loading-demo', 'nClicks'),
    prevent_initial_call=True
)
def button_auto_loading_demo(nClicks):

    time.sleep(3)

    return f'nClicks: {nClicks}', False
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
                        id='利用loading展示回调中状态',
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
                        {'title': '不同type对应按钮样式风格', 'href': '#不同type对应按钮样式风格'},
                        {'title': '充当链接跳转功能', 'href': '#充当链接跳转功能'},
                        {'title': '撑满父级元素宽度', 'href': '#撑满父级元素宽度'},
                        {'title': '渲染为危险警告状态', 'href': '#渲染为危险警告状态'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '不同的按钮形状', 'href': '#不同的按钮形状'},
                        {'title': '设置内嵌前缀元素', 'href': '#设置内嵌前缀元素'},
                        {'title': '回调示例', 'href': '#回调示例'},
                        {'title': '利用loading展示回调中状态', 'href': '#利用loading展示回调中状态'},
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
                component_name='AntdButton',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
