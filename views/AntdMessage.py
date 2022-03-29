import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc
from dash.dependencies import Input, Output

from server import app

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdMessage(children, id, className, style, **kwargs)',
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
                    '主要参数说明',
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
                    markdownStr=open('documents/AntdMessage.md', encoding='utf-8').read()
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

                        fac.AntdSpin(
                            [
                                fac.AntdButton('触发全局提示框', id='message-trigger-button-demo1', type='primary'),
                                html.Div(id='message-container-demo1')
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　AntdMessage', strong=True),
                                fac.AntdText('的使用方式较为特殊，它属于'),
                                fac.AntdText('昙花一现', strong=True),
                                fac.AntdText('式的组件，相当于简化版的'),
                                fac.AntdText('AntdNotification', strong=True),
                                fac.AntdText('，不需要事先在'),
                                fac.AntdText('app.layout', strong=True),
                                fac.AntdText('中进行定义，推荐的使用方式是预先定义容纳它的容器，'
                                             '后续回调中直接将'),
                                fac.AntdText('fac.AntdMessage(...)', italic=True),
                                fac.AntdText('对象作为回调输出返回对应容器即可，譬如本例中由按钮触发通知提示框的弹出显示')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdButton('触发全局提示框', id='message-trigger-button-demo1', type='primary'),
html.Div(id='message-container-demo1')
...
@app.callback(
    Output('message-container-demo1', 'children'),
    Input('message-trigger-button-demo1', 'nClicks'),
    prevent_initial_call=True
)
def message_demo1(nClicks):
    return fac.AntdMessage(
        content='全局提示框示例'
    )'''
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

                        fac.AntdSpin(
                            [
                                fac.AntdSpace(
                                    [
                                        fac.AntdButton(
                                            'default',
                                            id='message-trigger-button-default-demo2',
                                            type='text'
                                        ),
                                        fac.AntdButton(
                                            'info',
                                            id='message-trigger-button-info-demo2',
                                            type='text',
                                            style={
                                                'backgroundColor': 'rgb(24, 144, 255)',
                                                'color': 'white'
                                            }
                                        ),
                                        fac.AntdButton(
                                            'success',
                                            id='message-trigger-button-success-demo2',
                                            type='text',
                                            style={
                                                'backgroundColor': 'rgb(82, 196, 26)',
                                                'color': 'white'
                                            }
                                        ),
                                        fac.AntdButton(
                                            'error',
                                            id='message-trigger-button-error-demo2',
                                            type='text',
                                            style={
                                                'backgroundColor': 'rgb(255, 77, 79)',
                                                'color': 'white'
                                            }
                                        ),
                                        fac.AntdButton(
                                            'warning',
                                            id='message-trigger-button-warning-demo2',
                                            type='text',
                                            style={
                                                'backgroundColor': 'rgb(250, 173, 20)',
                                                'color': 'white'
                                            }
                                        ),
                                    ]
                                ),
                                html.Div(id='message-container-demo2')
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '不同的状态',
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
fac.AntdSpace(
    [
        fac.AntdButton(
            'default',
            id='message-trigger-button-default-demo2'
        ),
        fac.AntdButton(
            'info',
            id='message-trigger-button-info-demo2',
            type='primary'
        ),
        fac.AntdButton(
            'success',
            id='message-trigger-button-success-demo2',
            style={
                'backgroundColor': 'rgb(82, 196, 26)',
                'color': 'white'
            }
        ),
        fac.AntdButton(
            'error',
            id='message-trigger-button-error-demo2',
            style={
                'backgroundColor': 'rgb(255, 77, 79)',
                'color': 'white'
            }
        ),
        fac.AntdButton(
            'warning',
            id='message-trigger-button-warning-demo2',
            style={
                'backgroundColor': 'rgb(250, 173, 20)',
                'color': 'white'
            }
        ),
    ]
),
html.Div(id='message-container-demo2')
...
@app.callback(
    Output('message-container-demo2', 'children'),
    [Input('message-trigger-button-default-demo2', 'nClicks'),
     Input('message-trigger-button-info-demo2', 'nClicks'),
     Input('message-trigger-button-success-demo2', 'nClicks'),
     Input('message-trigger-button-error-demo2', 'nClicks'),
     Input('message-trigger-button-warning-demo2', 'nClicks')],
    prevent_initial_call=True
)
def message_demo2(default_nClicks,
                  info_nClicks,
                  success_nClicks,
                  error_nClicks,
                  warning_nClicks):
    ctx = dash.callback_context

    return fac.AntdMessage(
        content='全局提示框示例',
        type=ctx.triggered[0]['prop_id'].split('-')[3]
    )'''
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
                    id='不同的状态',
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
                            {'title': '不同的状态', 'href': '#不同的状态'},
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


@app.callback(
    Output('message-container-demo1', 'children'),
    Input('message-trigger-button-demo1', 'nClicks'),
    prevent_initial_call=True
)
def message_demo1(nClicks):
    return fac.AntdMessage(
        content='全局提示框示例'
    )


@app.callback(
    Output('message-container-demo2', 'children'),
    [Input('message-trigger-button-default-demo2', 'nClicks'),
     Input('message-trigger-button-info-demo2', 'nClicks'),
     Input('message-trigger-button-success-demo2', 'nClicks'),
     Input('message-trigger-button-error-demo2', 'nClicks'),
     Input('message-trigger-button-warning-demo2', 'nClicks')],
    prevent_initial_call=True
)
def message_demo2(default_nClicks,
                  info_nClicks,
                  success_nClicks,
                  error_nClicks,
                  warning_nClicks):
    ctx = dash.callback_context

    return fac.AntdMessage(
        content='全局提示框示例',
        type=ctx.triggered[0]['prop_id'].split('-')[3]
    )
