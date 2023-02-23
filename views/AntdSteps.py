from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSteps
from .side_props import render_side_props_layout

docs_content = html.Div(
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
                            'title': '导航'
                        },
                        {
                            'title': 'AntdSteps 步骤条'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于引导用户按照流程完成一系列连贯的步骤。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}'
                                }
                                for i in range(3)
                            ]
                        ),

                        fac.AntdDivider(
                            '基础使用',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}'
        }
        for i in range(3)
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ]
                        ),

                        fac.AntdDivider(
                            '带说明信息的步骤条',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
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
                    id='带说明信息的步骤条',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ],
                            current=2
                        ),

                        fac.AntdDivider(
                            '可控的当前步骤',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
    ],
    current=2
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
                    id='可控的当前步骤',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '垂直步骤条',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
    ],
    direction='vertical'
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
                    id='垂直步骤条',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ],
                            labelPlacement='vertical'
                        ),

                        fac.AntdDivider(
                            '垂直显示步骤说明内容',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
    ],
    labelPlacement='vertical'
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
                    id='垂直显示步骤说明内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ],
                            progressDot=True
                        ),

                        fac.AntdDivider(
                            '简洁点状步骤条',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
    ],
    progressDot=True
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
                    id='简洁点状步骤条',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ]
                        ),

                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ],
                            size='small'
                        ),

                        fac.AntdDivider(
                            '不同的大小规格',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
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
        for i in range(3)
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
                    id='不同的大小规格',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
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
                                for i in range(3)
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
                                for i in range(3)
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
                                for i in range(3)
                            ],
                            status='error',
                            current=2
                        ),

                        fac.AntdDivider(
                            '设置当前步骤状态',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
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
        for i in range(3)
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
        for i in range(3)
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
        for i in range(3)
    ],
    status='error',
    current=2
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
                    id='设置当前步骤状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}的title',
                                    'subTitle': f'步骤{i + 1}的subTitle',
                                    'description': f'步骤{i + 1}的description',
                                }
                                for i in range(3)
                            ],
                            type='navigation',
                            current=2
                        ),

                        fac.AntdDivider(
                            '导航风格步骤条',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}的title',
            'subTitle': f'步骤{i + 1}的subTitle',
            'description': f'步骤{i + 1}的description',
        }
        for i in range(3)
    ],
    type='navigation',
    current=2
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
                    id='导航风格步骤条',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSteps(
                            steps=[
                                {
                                    'title': f'步骤{i + 1}'
                                }
                                for i in range(3)
                            ],
                            allowClick=True
                        ),

                        fac.AntdDivider(
                            '允许点击切换步骤',
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
fac.AntdSteps(
    steps=[
        {
            'title': f'步骤{i + 1}'
        }
        for i in range(3)
    ],
    allowClick=True
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
                    id='允许点击切换步骤',
                    className='div-highlight'
                ),

                html.Div(
                    [
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
                        fac.AntdDivider(
                            isDashed=True
                        ),
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
                        fac.AntdDivider(
                            isDashed=True
                        ),
                        fac.AntdText(
                            id='steps-demo-current'
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
fac.AntdDivider(
    isDashed=True
),
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
fac.AntdDivider(
    isDashed=True
),
fac.AntdText(
    id='steps-demo-current'
)

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
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '带说明信息的步骤条', 'href': '#带说明信息的步骤条'},
                    {'title': '可控的当前步骤', 'href': '#可控的当前步骤'},
                    {'title': '垂直步骤条', 'href': '#垂直步骤条'},
                    {'title': '垂直显示步骤说明内容', 'href': '#垂直显示步骤说明内容'},
                    {'title': '简洁点状步骤条', 'href': '#简洁点状步骤条'},
                    {'title': '不同的大小规格', 'href': '#不同的大小规格'},
                    {'title': '设置当前步骤状态', 'href': '#设置当前步骤状态'},
                    {'title': '导航风格步骤条', 'href': '#导航风格步骤条'},
                    {'title': '允许点击切换步骤', 'href': '#允许点击切换步骤'},
                    {'title': '回调示例', 'href': '#回调示例'},
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
            component_name='AntdSteps'
        )
    ],
    style={
        'display': 'flex'
    }
)
