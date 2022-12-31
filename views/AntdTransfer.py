from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTransfer

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdTransfer(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdTransfer.md',
                                     encoding='utf-8').read()
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
                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ]
                            )
                        ),

                        fac.AntdDivider(
                            '基础使用方式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ]
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
                    id='基础使用方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        # AntdTransfer自动会撑满父元素的宽度
                        # 因此可以通过设定父级Div的style宽度
                        # 来实现对AntdTransfer整体宽度的调节
                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ]
                            ),
                            style={
                                'width': '600px'
                            }
                        ),

                        fac.AntdDivider(),

                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ]
                            ),
                            style={
                                'width': '400px'
                            }
                        ),

                        fac.AntdDivider(),

                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ]
                            ),
                            style={
                                'width': '500px'
                            }
                        ),

                        fac.AntdDivider(
                            '调节总体宽度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ]
    ),
    style={
        'width': '600px'
    }
),

fac.AntdDivider(),

html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ]
    ),
    style={
        'width': '400px'
    }
),

fac.AntdDivider(),

html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ]
    ),
    style={
        'width': '500px'
    }
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
                    id='调节总体宽度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ],
                                height='500px'
                            )
                        ),

                        fac.AntdDivider(
                            '自定义高度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ],
        height='500px'
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
                    id='自定义高度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ],
                                pagination=True
                            )
                        ),

                        fac.AntdDivider(),

                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ],
                                pagination={
                                    'pageSize': 5
                                }
                            )
                        ),

                        fac.AntdDivider(
                            '分页显示',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ],
        pagination=True
    )
),

fac.AntdDivider(),

html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ],
        pagination={
            'pageSize': 5
        }
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
                    id='分页显示',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ],
                                showSearch=True
                            )
                        ),

                        fac.AntdDivider(
                            '添加搜索框',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ],
        showSearch=True
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
                    id='添加搜索框',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdTransfer(
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ],
                                operations=['新增', '移除'],
                                titles=['待选指标区', '已选指标区']
                            )
                        ),

                        fac.AntdDivider(
                            '修改左右区域标题及双向按钮文字',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ],
        operations=['新增', '移除'],
        titles=['待选指标区', '已选指标区']
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
                    id='修改左右区域标题及双向按钮文字',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        html.Div(
                            fac.AntdTransfer(
                                id='transfer-demo',
                                dataSource=[
                                    {
                                        'key': str(i),
                                        'title': f'选项{i}'
                                    }
                                    for i in range(20)
                                ]
                            )
                        ),

                        html.Br(),
                        fac.AntdSpin(
                            html.Em(id='transfer-demo-output'),
                            text='回调中'
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
html.Div(
    fac.AntdTransfer(
        id='transfer-demo',
        dataSource=[
            {
                'key': str(i),
                'title': f'选项{i}'
            }
            for i in range(20)
        ]
    )
),

html.Br(),
html.Em(id='transfer-demo-output')
...
@app.callback(
    Output('transfer-demo-output', 'children'),
    [Input('transfer-demo', 'targetKeys'),
     Input('transfer-demo', 'moveDirection'),
     Input('transfer-demo', 'moveKeys')],
    prevent_initial_call=True
)
def transfer_callback_demo(targetKeys, moveDirection, moveKeys):

    return [
        f'targetKeys: {targetKeys}',
        html.Br(),
        f'moveDirection: {moveDirection}',
        html.Br(),
        f'moveKeys: {moveKeys}'
    ]'''
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
                            {'title': '基础使用方式', 'href': '#基础使用方式'},
                            {'title': '调节总体宽度', 'href': '#调节总体宽度'},
                            {'title': '自定义高度', 'href': '#自定义高度'},
                            {'title': '分页显示', 'href': '#分页显示'},
                            {'title': '添加搜索框', 'href': '#添加搜索框'},
                            {'title': '修改左右区域标题及双向按钮文字',
                                'href': '#修改左右区域标题及双向按钮文字'},
                            {'title': '回调示例', 'href': '#回调示例'},
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
