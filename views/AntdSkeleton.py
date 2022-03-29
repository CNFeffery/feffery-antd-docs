from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdSkeleton

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdSkeleton(children, id, className, style, *args, **kwargs)',
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

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdSkeleton.md', encoding='utf-8').read()
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
                        fac.AntdButton('触发2秒骨骼屏动画', id='skeleton-basic-demo-input', type='primary'),

                        html.Br(),

                        fac.AntdSkeleton(
                            fac.AntdText('nClicks: 0', id='skeleton-basic-demo-output', strong=True),
                            active=True
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　默认模式下，被'),
                                fac.AntdText('AntdSkeleton', strong=True),
                                fac.AntdText('作为children参数传入的所有后代组件，在作为回调过程的'),
                                fac.AntdText('Output', strong=True),
                                fac.AntdText('处于回调中状态时，都会触发骨骼屏动画过程'),
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdButton('触发2秒骨骼屏动画', id='skeleton-basic-demo-input', type='primary'),

html.Br(),

fac.AntdSkeleton(
    fac.AntdText('nClicks: 0', id='skeleton-basic-demo-output', strong=True),
    active=True
)
...
@app.callback(
    Output('skeleton-basic-demo-output', 'children'),
    Input('skeleton-basic-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_basic_callback_demo(nClicks):
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
                        fac.AntdButton('触发2秒骨骼屏动画', id='skeleton-custom-demo-input', type='primary'),

                        html.Br(),

                        fac.AntdSkeleton(
                            fac.AntdText('nClicks: 0', id='skeleton-custom-demo-output', strong=True),
                            active=True,
                            avatar=True,
                            paragraph={
                                'rows': 3,
                                'width': '95%'
                            },
                            title={
                                'width': '4rem'
                            }
                        ),

                        fac.AntdDivider(
                            '自定义头像、段落及标题占位效果',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdButton('触发2秒骨骼屏动画', id='skeleton-custom-demo-input', type='primary'),

html.Br(),

fac.AntdSkeleton(
    fac.AntdText('nClicks: 0', id='skeleton-custom-demo-output', strong=True),
    active=True,
    avatar=True,
    paragraph={
        'rows': 3,
        'width': '95%'
    },
    title={
        'width': '4rem'
    }
)
...
@app.callback(
    Output('skeleton-custom-demo-output', 'children'),
    Input('skeleton-custom-demo-input', 'nClicks'),
    prevent_initial_call=True
)
def skeleton_custom_callback_demo(nClicks):
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
                    id='自定义头像、段落及标题占位效果',
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
                            {'title': '自定义头像、段落及标题占位效果', 'href': '#自定义头像、段落及标题占位效果'},
                        ]
                    },
                ],
                offsetTop=0
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
