import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdSteps

docs_content = html.Div(
    [
        html.H2(
            'AntdSteps(id, className, style, *args, **kwargs)',
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
                        {'title': '步骤条中的说明信息', 'href': '#步骤条中的说明信息'},
                        {'title': '设置当前停留的步骤序号', 'href': '#设置当前停留的步骤序号'},
                        {'title': '设置步骤条的显示方向', 'href': '#设置步骤条的显示方向'},
                        {'title': '设置步骤条说明文字的放置位置', 'href': '#设置步骤条说明文字的放置位置'},
                        {'title': '点状步骤条模式', 'href': '#点状步骤条模式'},
                        {'title': '设置不同的步骤条尺寸模式', 'href': '#设置不同的步骤条尺寸模式'},
                        {'title': '自定义当前步骤的显示状态', 'href': '#自定义当前步骤的显示状态'},
                        {'title': '设置步骤条整体渲染形式', 'href': '#设置步骤条整体渲染形式'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ]
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

        dcc.Markdown(open('documents/AntdSteps.md', encoding='utf-8').read(),
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
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}'
                        }
                        for i in range(5)
                    ]
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}'
                        }
                        for i in range(5)
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '步骤条中的说明信息：',
                    id='步骤条中的说明信息',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ]
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ]
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置当前停留的步骤序号：',
                    id='设置当前停留的步骤序号',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    current=2
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    current=2
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置步骤条的显示方向：',
                    id='设置步骤条的显示方向',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    direction='vertical'
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    direction='vertical'
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置步骤条说明文字的放置位置：',
                    id='设置步骤条说明文字的放置位置',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    labelPlacement='vertical'
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    labelPlacement='vertical'
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '点状步骤条模式：',
                    id='点状步骤条模式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    progressDot=True
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    progressDot=True
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置不同的步骤条尺寸模式：',
                    id='设置不同的步骤条尺寸模式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ]
                ),
                fac.AntdDivider(),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    size='small'
                )
                ```
                '''),

                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ]
                ),
                fac.AntdDivider(),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    size='small'
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '自定义当前步骤的显示状态：',
                    id='自定义当前步骤的显示状态',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    status='wait',
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    status='finish',
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    status='error',
                    current=2
                )
                ```
                '''),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    status='wait',
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    status='finish',
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    status='error',
                    current=2
                )
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '设置步骤条整体渲染形式：',
                    id='设置步骤条整体渲染形式',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    type='navigation',
                    current=2
                )
                ```
                '''),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    current=2
                ),
                fac.AntdSteps(
                    steps=[
                        {
                            'title': f'步骤{i + 1}的title',
                            'subTitle': f'步骤{i + 1}的subTitle',
                            'description': f'步骤{i + 1}的description',
                        }
                        for i in range(5)
                    ],
                    type='navigation',
                    current=2
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
                fac.AntdSteps(
                    id='steps-demo',
                    steps=[
                        {
                            'title': f'步骤{i}'
                        }
                        for i in range(5)
                    ],
                    direction='horizontal',
                    type='navigation'
                ),
                fac.AntdDivider(),
                fac.AntdButton(
                    '下一步',
                    id='steps-demo-go-next',
                    type='primary'
                ),
                fac.AntdDivider(direction='vertical'),
                fac.AntdButton(
                    '上一步',
                    id='steps-demo-go-last',
                    type='primary'
                ),
                fac.AntdDivider(direction='vertical'),
                fac.AntdButton(
                    '重置',
                    id='steps-demo-restart',
                    type='primary'
                ),
                fac.AntdDivider(),
                html.Em(id='steps-demo-current')
                ...
                @app.callback(
                    Output('steps-demo', 'current'),
                    [Input('steps-demo-go-next', 'nClicks'),
                     Input('steps-demo-go-last', 'nClicks'),
                     Input('steps-demo-restart', 'nClicks')],
                    State('steps-demo', 'current'),
                    prevent_initial_call=True
                )
                def steps_callback_demo_part1(go_next, go_last, restart, current):

                    ctx = dash.callback_context
                
                    if ctx.triggered[0]['prop_id'].startswith('steps-demo-go-next'):
                        return current + 1
                
                    elif ctx.triggered[0]['prop_id'].startswith('steps-demo-go-last'):
                        return max(current - 1, 0)
                
                    else:
                        return 0
                
                
                @app.callback(
                    Output('steps-demo-current', 'children'),
                    Input('steps-demo', 'current'),
                    prevent_initial_call=True
                )
                def steps_callback_demo_part2(current):
                
                    return f'当前步骤为：步骤{current}'
                ```
                '''),
                fac.AntdSteps(
                    id='steps-demo',
                    steps=[
                        {
                            'title': f'步骤{i}'
                        }
                        for i in range(5)
                    ],
                    direction='horizontal',
                    type='navigation'
                ),
                fac.AntdDivider(),
                fac.AntdButton(
                    '下一步',
                    id='steps-demo-go-next',
                    type='primary'
                ),
                fac.AntdDivider(direction='vertical'),
                fac.AntdButton(
                    '上一步',
                    id='steps-demo-go-last',
                    type='primary'
                ),
                fac.AntdDivider(direction='vertical'),
                fac.AntdButton(
                    '重置',
                    id='steps-demo-restart',
                    type='primary'
                ),
                fac.AntdDivider(),
                html.Em(id='steps-demo-current')
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
