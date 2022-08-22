from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdPageHeader

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdPageHeader(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdPageHeader.md', encoding='utf-8').read()
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
                        fac.AntdPageHeader(
                            title='页头标题示例',
                            subTitle='页头副标题示例'
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　最基础的页头包含了自带浏览器后退功能的返回按钮、主标题及副标题信息')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPageHeader(
    title='页头标题示例',
    subTitle='页头副标题示例'
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
                        fac.AntdPageHeader(
                            fac.AntdSpace(
                                [
                                    fac.AntdButton('按钮1'),
                                    fac.AntdButton('按钮2', type='primary'),
                                    fac.AntdSwitch(checkedChildren='打开', unCheckedChildren='关闭'),
                                    fac.AntdBadge(status='processing')
                                ]
                            ),
                            title='页头标题示例',
                            subTitle='页头副标题示例'
                        ),

                        fac.AntdDivider(
                            '带有子元素的页头',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPageHeader(
    fac.AntdSpace(
        [
            fac.AntdButton('按钮1'),
            fac.AntdButton('按钮2', type='primary'),
            fac.AntdSwitch(checkedChildren='打开', unCheckedChildren='关闭'),
            fac.AntdBadge(status='processing')
        ]
    ),
    title='页头标题示例',
    subTitle='页头副标题示例'
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
                    id='带有子元素的页头',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdPageHeader(
                            id='page-header-demo',
                            title='页头标题示例',
                            subTitle='页头副标题示例',
                            historyBackDisabled=True
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　设置'),
                                fac.AntdText('historyBackDisabled=True', code=True),
                                fac.AntdText('之后，页头的返回按钮就不再具有原生浏览器后退功能，而是可以用来记录返回按钮的点击次数从而实现更多交互')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPageHeader(
    id='page-header-demo',
    title='页头标题示例',
    subTitle='页头副标题示例',
    historyBackDisabled=True
)
...
@app.callback(
    Output('page-header-demo', 'children'),
    Input('page-header-demo', 'backClicks')
)
def page_header_demo_callback(backClicks):
    return [
        fac.AntdText('backClicks: ', strong=True),
        fac.AntdText(backClicks)
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

                html.Div(
                    [
                        fac.AntdPageHeader(
                            title=fac.AntdText(
                                '组件型title示例',
                                italic=True,
                                copyable=True,
                                strong=True,
                                style={
                                    'fontSize': '28px'
                                }
                            ),
                            subTitle=fac.AntdText(
                                '组件型subTitle示例',
                                italic=True,
                                copyable=True
                            )
                        ),

                        fac.AntdDivider(
                            'title与subTitle接受组件型输入',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdPageHeader(
    title=fac.AntdText(
        '组件型title示例',
        italic=True,
        copyable=True,
        strong=True,
        style={
            'fontSize': '28px'
        }
    ),
    subTitle=fac.AntdText(
        '组件型subTitle示例',
        italic=True,
        copyable=True
    )
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
                    id='title与subTitle接受组件型输入',
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
                            {'title': '带有子元素的页头', 'href': '#带有子元素的页头'},
                            {'title': '回调示例', 'href': '#回调示例'},
                            {'title': 'title与subTitle接受组件型输入', 'href': '#title与subTitle接受组件型输入'},
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
