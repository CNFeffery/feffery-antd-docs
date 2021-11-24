from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdSpin

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdSpin(children, id, className, style, *args, **kwargs)',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5'
                    }
                ),

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                html.Span(
                    '主要参数说明：',
                    id='主要参数说明',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5',
                        'fontWeight': 'bold',
                        'fontSize': '1.2rem'
                    }
                ),

                fuc.FefferyMarkdown(
                    markdownStr=open('documents/AntdSpin.md', encoding='utf-8').read()
                ),

                html.Div(
                    html.Span(
                        '使用示例',
                        id='使用示例',
                        style={
                            'borderLeft': '4px solid grey',
                            'padding': '3px 0 3px 10px',
                            'backgroundColor': '#f5f5f5',
                            'fontWeight': 'bold',
                            'fontSize': '1.2rem'
                        }
                    ),
                    style={
                        'marginBottom': '10px'
                    }
                ),

                html.Div(
                    [
                        fac.AntdButton('触发2秒加载动画', id='spin-basic-demo-input', type='primary'),

                        fac.AntdSpin(
                            fac.AntdText('nClicks: 0', id='spin-basic-demo-output', strong=True),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　默认模式下，被'),
                                fac.AntdText('AntdSpin', strong=True),
                                fac.AntdText('作为children参数传入的所有后代组件，在作为回调过程的'),
                                fac.AntdText('Output', strong=True),
                                fac.AntdText('处于回调中状态时，都会触发加载动画过程'),
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdButton('触发2秒加载动画', id='spin-basic-demo-input', type='primary'),

fac.AntdSpin(
    fac.AntdText('nClicks: 0', id='spin-basic-demo-output', strong=True),
    text='回调中'
)
...
@app.callback(
    Output('spin-basic-demo-output', 'children'),
    Input('spin-basic-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def spin_basic_callback_demo(nClicks):
    import time
    time.sleep(2)

    return f'nClicks: {nClicks}'
'''
                            ),
                            title='点击查看代码',
                            is_open=False,
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
                                fac.AntdButton('触发耗时0.5秒的回调过程', id='spin-delay-demo-input1', type='primary'),
                                fac.AntdButton('触发耗时2秒的回调过程', id='spin-delay-demo-input2', type='primary')
                            ]
                        ),

                        fac.AntdSpin(
                            fac.AntdText('0.5秒回调 nClicks: 0', id='spin-delay-demo-output1', strong=True),
                            delay=1000,
                            text='回调中'
                        ),

                        fac.AntdSpin(
                            fac.AntdText('2s回调 nClicks: 0', id='spin-delay-demo-output2', strong=True),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '延迟加载',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('当监听的后代组件实际加载耗时低于'),
                                fac.AntdText('delay', strong=True),
                                fac.AntdText('所设置的时长时，加载动画不会被触发')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdButton('触发耗时0.5秒的回调过程', id='spin-delay-demo-input1', type='primary'),
        fac.AntdButton('触发耗时2秒的回调过程', id='spin-delay-demo-input2', type='primary')
    ]
),

fac.AntdSpin(
    fac.AntdText('0.5秒回调 nClicks: 0', id='spin-delay-demo-output1', strong=True),
    delay=1000,
    text='回调中'
),

fac.AntdSpin(
    fac.AntdText('2s回调 nClicks: 0', id='spin-delay-demo-output2', strong=True),
    text='回调中'
)
...
@app.callback(
    Output('spin-delay-demo-output1', 'children'),
    Input('spin-delay-demo-input1', 'nClicks'),
    prevent_initial_call=True
)
def spin_delay_callback_demo1(nClicks):
    import time
    time.sleep(0.5)

    return f'0.5秒回调 nClicks: {nClicks}'


@app.callback(
    Output('spin-delay-demo-output2', 'children'),
    Input('spin-delay-demo-input2', 'nClicks'),
    prevent_initial_call=True
)
def spin_delay_callback_demo2(nClicks):
    import time
    time.sleep(2)

    return f'2秒回调 nClicks: {nClicks}'
'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='延迟加载',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton('未被includeProps指定', id='spin-include-demo-input1', type='primary'),
                                fac.AntdButton('被includeProps指定', id='spin-include-demo-input2', type='primary')
                            ]
                        ),

                        fac.AntdSpin(
                            fac.AntdSpace(
                                [
                                    fac.AntdText('未被includeProps指定 nClicks: 0', id='spin-include-demo-output1',
                                                 strong=True),
                                    fac.AntdText('被includeProps指定 nClicks: 0', id='spin-include-demo-output2',
                                                 strong=True)
                                ],
                                direction='vertical'
                            ),
                            listenPropsMode='include',
                            includeProps=['spin-include-demo-output2.children'],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            'include模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText("　　listenPropsMode='include'", strong=True),
                                fac.AntdText("时，由"),
                                fac.AntdText('includeProps', strong=True),
                                fac.AntdText('指定的组件属性对应的'),
                                fac.AntdText('Output', strong=True),
                                fac.AntdText('回调过程才会触发加载动画'),
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdButton('未被includeProps指定', id='spin-include-demo-input1', type='primary'),
        fac.AntdButton('被includeProps指定', id='spin-include-demo-input2', type='primary')
    ]
),

fac.AntdSpin(
    fac.AntdSpace(
        [
            fac.AntdText('未被includeProps指定 nClicks: 0', id='spin-include-demo-output1', strong=True),
            fac.AntdText('被includeProps指定 nClicks: 0', id='spin-include-demo-output2', strong=True)
        ],
        direction='vertical'
    ),
    listenPropsMode='include',
    includeProps=['spin-include-demo-output2.children'],
    text='回调中'
)
...
@app.callback(
    Output('spin-include-demo-output1', 'children'),
    Input('spin-include-demo-input1', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_callback_demo1(nClicks):
    import time
    time.sleep(1)

    return f'未被includeProps指定 nClicks: {nClicks}'


@app.callback(
    Output('spin-include-demo-output2', 'children'),
    Input('spin-include-demo-input2', 'nClicks'),
    prevent_initial_call=True
)
def spin_include_callback_demo2(nClicks):
    import time
    time.sleep(1)

    return f'被includeProps指定 nClicks: {nClicks}'
'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='include模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton('未被excludeProps指定', id='spin-exclude-demo-input1', type='primary'),
                                fac.AntdButton('被excludeProps指定', id='spin-exclude-demo-input2', type='primary')
                            ]
                        ),

                        fac.AntdSpin(
                            fac.AntdSpace(
                                [
                                    fac.AntdText('未被excludeProps指定 nClicks: 0', id='spin-exclude-demo-output1',
                                                 strong=True),
                                    fac.AntdText('被excludeProps指定 nClicks: 0', id='spin-exclude-demo-output2',
                                                 strong=True)
                                ],
                                direction='vertical'
                            ),
                            listenPropsMode='exclude',
                            excludeProps=['spin-exclude-demo-output2.children'],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            'exclude模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText("　　listenPropsMode='exclude'", strong=True),
                                fac.AntdText("时，由"),
                                fac.AntdText('excludeProps', strong=True),
                                fac.AntdText('指定的组件属性对应的'),
                                fac.AntdText('Output', strong=True),
                                fac.AntdText('回调过程不会触发加载动画'),
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpace(
    [
        fac.AntdButton('未被excludeProps指定', id='spin-exclude-demo-input1', type='primary'),
        fac.AntdButton('被excludeProps指定', id='spin-exclude-demo-input2', type='primary')
    ]
),

fac.AntdSpin(
    fac.AntdSpace(
        [
            fac.AntdText('未被excludeProps指定 nClicks: 0', id='spin-exclude-demo-output1', strong=True),
            fac.AntdText('被excludeProps指定 nClicks: 0', id='spin-exclude-demo-output2', strong=True)
        ],
        direction='vertical'
    ),
    listenPropsMode='exclude',
    excludeProps=['spin-exclude-demo-output2.children'],
    text='回调中'
)
...
@app.callback(
    Output('spin-exclude-demo-output1', 'children'),
    Input('spin-exclude-demo-input1', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_callback_demo1(nClicks):
    import time
    time.sleep(1)

    return f'未被excludeProps指定 nClicks: {nClicks}'


@app.callback(
    Output('spin-exclude-demo-output2', 'children'),
    Input('spin-exclude-demo-input2', 'nClicks'),
    prevent_initial_call=True
)
def spin_exclude_callback_demo2(nClicks):
    import time
    time.sleep(1)

    return f'被excludeProps指定 nClicks: {nClicks}'
                        '''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )
                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='exclude模式',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '主要参数说明', 'href': '#主要参数说明'},
                    {
                        'title': '使用示例',
                        'href': '#使用示例',
                        'children': [
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '延迟加载', 'href': '#延迟加载'},
                            {'title': 'include模式', 'href': '#include模式'},
                            {'title': 'exclude模式', 'href': '#exclude模式'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
