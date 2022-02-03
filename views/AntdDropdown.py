from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdDropdown

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdDropdown(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdDropdown.md', encoding='utf-8').read()
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

                        fac.AntdDropdown(
                            title='触发点',
                            menuItems=[
                                {
                                    'title': '子页面1'
                                },
                                {
                                    'title': '子页面2'
                                },
                                {
                                    'isDivider': True
                                },
                                {
                                    'title': '子页面3-1'
                                },
                                {
                                    'title': '子页面3-2'
                                }
                            ]
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
fac.AntdDropdown(
    title='触发点',
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
    ]
)
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

                        fac.AntdDropdown(
                            title='触发点',
                            buttonMode=True,
                            menuItems=[
                                {
                                    'title': '子页面1'
                                },
                                {
                                    'title': '子页面2'
                                },
                                {
                                    'isDivider': True
                                },
                                {
                                    'title': '子页面3-1'
                                },
                                {
                                    'title': '子页面3-2'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '按钮模式',
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
fac.AntdDropdown(
    title='触发点',
    buttonMode=True,
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
    ]
)
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
                    id='按钮模式',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdDropdown(
                            title='触发点',
                            trigger='click',
                            menuItems=[
                                {
                                    'title': '子页面1'
                                },
                                {
                                    'title': '子页面2'
                                },
                                {
                                    'isDivider': True
                                },
                                {
                                    'title': '子页面3-1'
                                },
                                {
                                    'title': '子页面3-2'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '点击触发',
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
fac.AntdDropdown(
    title='触发点',
    trigger='click',
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
    ]
)
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
                    id='点击触发',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdDropdown(
                            title='触发点',
                            arrow=True,
                            menuItems=[
                                {
                                    'title': '子页面1'
                                },
                                {
                                    'title': '子页面2'
                                },
                                {
                                    'isDivider': True
                                },
                                {
                                    'title': '子页面3-1'
                                },
                                {
                                    'title': '子页面3-2'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '添加连接箭头',
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
fac.AntdDropdown(
    title='触发点',
    arrow=True,
    menuItems=[
        {
            'title': '子页面1'
        },
        {
            'title': '子页面2'
        },
        {
            'isDivider': True
        },
        {
            'title': '子页面3-1'
        },
        {
            'title': '子页面3-2'
        }
    ]
)
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
                    id='添加连接箭头',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdSpace(
                            [
                                fac.AntdDropdown(
                                    title=placement,
                                    arrow=True,
                                    placement=placement,
                                    menuItems=[
                                        {
                                            'title': '子页面1'
                                        },
                                        {
                                            'title': '子页面2'
                                        },
                                        {
                                            'isDivider': True
                                        },
                                        {
                                            'title': '子页面3-1'
                                        },
                                        {
                                            'title': '子页面3-2'
                                        }
                                    ]
                                )
                                for placement in [
                                'bottomLeft', 'bottomCenter', 'bottomRight',
                                'topLeft', 'topCenter', 'topRight']
                            ],
                            size=20
                        ),

                        fac.AntdDivider(
                            '不同的弹出方位',
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
        fac.AntdDropdown(
            title=placement,
            arrow=True,
            placement=placement,
            menuItems=[
                {
                    'title': '子页面1'
                },
                {
                    'title': '子页面2'
                },
                {
                    'isDivider': True
                },
                {
                    'title': '子页面3-1'
                },
                {
                    'title': '子页面3-2'
                }
            ]
        )
        for placement in [
        'bottomLeft', 'bottomCenter', 'bottomRight',
        'topLeft', 'topCenter', 'topRight']
    ],
    size=20
)
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
                    id='不同的弹出方位',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdSpin(
                            [
                                fac.AntdDropdown(
                                    id='dropdown-demo',
                                    title='触发点',
                                    arrow=True,
                                    placement='topCenter',
                                    menuItems=[
                                        {
                                            'title': '子页面1',
                                            'key': '子页面1',
                                        },
                                        {
                                            'title': '子页面2',
                                            'key': '子页面2',
                                        },
                                        {
                                            'isDivider': True
                                        },
                                        {
                                            'title': '子页面3-1',
                                            'key': '子页面3-1'
                                        },
                                        {
                                            'title': '子页面3-2',
                                            'key': '子页面3-2'
                                        }
                                    ]
                                ),

                                html.Div(
                                    id='dropdown-demo-output'
                                )
                            ],
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　除了在构造选项时传入href等参数令选项充当链接跳转功能之外，'),
                                fac.AntdText('AntdDropdown', strong=True),
                                fac.AntdText('还可通过为选项设置key值，从而在回调中监听'),
                                fac.AntdText('clickedKey', strong=True),
                                fac.AntdText('随着选项点击事件的变化')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        fac.AntdDropdown(
            id='dropdown-demo',
            title='触发点',
            arrow=True,
            placement='topCenter',
            menuItems=[
                {
                    'title': '子页面1',
                    'key': '子页面1',
                },
                {
                    'title': '子页面2',
                    'key': '子页面2',
                },
                {
                    'isDivider': True
                },
                {
                    'title': '子页面3-1',
                    'key': '子页面3-1'
                },
                {
                    'title': '子页面3-2',
                    'key': '子页面3-2'
                }
            ]
        ),

        html.Div(
            id='dropdown-demo-output'
        )
    ],
    text='回调中'
)
...
@app.callback(
    Output('dropdown-demo-output', 'children'),
    Input('dropdown-demo', 'clickedKey'),
    prevent_initial_call=True
)
def dropdown_demo_callback(clickedKey):
    return [
        fac.AntdText('clickedKey: ', strong=True),
        fac.AntdText(clickedKey)
    ]
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
                    id='回调示例',
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
                            {'title': '按钮模式', 'href': '#按钮模式'},
                            {'title': '点击触发', 'href': '#点击触发'},
                            {'title': '添加连接箭头', 'href': '#添加连接箭头'},
                            {'title': '不同的弹出方位', 'href': '#不同的弹出方位'},
                            {'title': '回调示例', 'href': '#回调示例'}
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
            ),
            style={
                'flex': 'none',
                'padding': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
