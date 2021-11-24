from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdDrawer

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdDrawer(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdDrawer.md', encoding='utf-8').read()
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
                        fac.AntdButton(
                            '触发抽屉',
                            type='primary',
                            id='drawer-demo-trigger-1'
                        ),

                        fac.AntdDrawer(
                            fac.AntdText('抽屉内容测试' * 200),
                            id='drawer-demo-1'
                        ),

                        fac.AntdDivider(
                            '基础使用',
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
fac.AntdButton(
    '触发抽屉',
    type='primary',
    id='drawer-demo-trigger-1'
),

fac.AntdDrawer(
    fac.AntdText('抽屉内容测试' * 200),
    id='drawer-demo-1'
)
...
@app.callback(
    Output('drawer-demo-1', 'visible'),
    Input('drawer-demo-trigger-1', 'nClicks'),
    prevent_initial_call=True
)
def drawer_demo_callback1(nClicks):
    return True
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
                                fac.AntdButton(
                                    'top方向',
                                    type='primary',
                                    id='drawer-demo-trigger-2-top'
                                ),
                                fac.AntdButton(
                                    'left方向',
                                    type='primary',
                                    id='drawer-demo-trigger-2-left'
                                ),
                                fac.AntdButton(
                                    'bottom方向',
                                    type='primary',
                                    id='drawer-demo-trigger-2-bottom'
                                ),
                            ]
                        ),

                        fac.AntdDrawer(
                            fac.AntdText('抽屉内容测试' * 100),
                            id='drawer-demo-2-top',
                            placement='top',
                            mask=False
                        ),

                        fac.AntdDrawer(
                            fac.AntdText('抽屉内容测试' * 100),
                            id='drawer-demo-2-left',
                            placement='left',
                            mask=False
                        ),

                        fac.AntdDrawer(
                            fac.AntdText('抽屉内容测试' * 100),
                            id='drawer-demo-2-bottom',
                            placement='bottom',
                            mask=False
                        ),

                        fac.AntdDivider(
                            '不同的抽屉弹出方向',
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
            'top方向',
            type='primary',
            id='drawer-demo-trigger-2-top'
        ),
        fac.AntdButton(
            'left方向',
            type='primary',
            id='drawer-demo-trigger-2-left'
        ),
        fac.AntdButton(
            'bottom方向',
            type='primary',
            id='drawer-demo-trigger-2-bottom'
        ),
    ]
),

fac.AntdDrawer(
    fac.AntdText('抽屉内容测试' * 100),
    id='drawer-demo-2-top',
    placement='top',
    mask=False
),

fac.AntdDrawer(
    fac.AntdText('抽屉内容测试' * 100),
    id='drawer-demo-2-left',
    placement='left',
    mask=False
),

fac.AntdDrawer(
    fac.AntdText('抽屉内容测试' * 100),
    id='drawer-demo-2-bottom',
    placement='bottom',
    mask=False
)
...
@app.callback(
    [Output('drawer-demo-2-top', 'visible'),
     Output('drawer-demo-2-left', 'visible'),
     Output('drawer-demo-2-bottom', 'visible')],
    [Input('drawer-demo-trigger-2-top', 'nClicks'),
     Input('drawer-demo-trigger-2-left', 'nClicks'),
     Input('drawer-demo-trigger-2-bottom', 'nClicks')],
    prevent_initial_call=True
)
def drawer_demo_callback2(_, __, ___):
    ctx = dash.callback_context

    placement = ctx.triggered[0]['prop_id'].split('.')[0].split('-')[-1]

    if placement == 'top':
        return True, False, False

    elif placement == 'left':
        return False, True, False

    else:
        return False, False, True
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
                    id='不同的抽屉弹出方向',
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
                            {'title': '不同的抽屉弹出方向', 'href': '#不同的抽屉弹出方向'},
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
