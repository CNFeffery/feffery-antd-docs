import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdTransfer

docs_content = html.Div(
    [
        html.H2(
            'AntdTransfer(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

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
                        {'title': '修改左右区域标题及双向按钮文字', 'href': '#修改左右区域标题及双向按钮文字'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ]
        ),
        html.Span(
            '主要参数说明：',
            id='#主要参数说明',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        dcc.Markdown(open('documents/AntdTransfer.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

        html.Span(
            '使用示例：',
            id='使用示例',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5',
                'fontWeight': 'bold',
                'fontSize': '1.2rem'
            }
        ),

        html.Hr(),

        html.Div(
            [
                html.Strong(
                    '基础使用方式：',
                    id='基础使用方式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                )
                ```
                '''),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '调节总体宽度：',
                    id='调节总体宽度',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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

                html.Hr(),

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

                html.Hr(),

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
                )
                ```
                '''),

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

                html.Hr(),

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

                html.Hr(),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '自定义高度：',
                    id='自定义高度',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                )
                ```
                '''),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '分页显示：',
                    id='分页显示',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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

                html.Hr(),

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
                )
                ```
                '''),

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

                html.Hr(),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '添加搜索框：',
                    id='添加搜索框',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                )
                ```
                '''),

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

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '修改左右区域标题及双向按钮文字：',
                    id='修改左右区域标题及双向按钮文字',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                )
                ```
                '''),

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
                )

            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '回调示例：',
                    id='回调示例',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
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
                    ]
                
                ```
                '''),

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
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
