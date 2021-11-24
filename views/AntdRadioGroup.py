from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdRadioGroup

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdRadioGroup(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdRadioGroup.md', encoding='utf-8').read()
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
                        fac.AntdRadioGroup(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ],
                            defaultValue='选项1'
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
fac.AntdRadioGroup(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ],
    defaultValue='选项1'
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
                        fac.AntdDivider('direction="vertical"', innerTextOrientation='left'),
                        fac.AntdRadioGroup(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ],
                            direction='vertical',
                            defaultValue='选项1'
                        ),

                        fac.AntdDivider(
                            '不同的排列方向',
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
fac.AntdRadioGroup(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ],
    direction='vertical',
    defaultValue='选项1'
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
                    id='不同的排列方向',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdRadioGroup(
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ],
                                    optionType='button',
                                    defaultValue='选项1'
                                ),

                                fac.AntdRadioGroup(
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ],
                                    optionType='button',
                                    buttonStyle='solid',
                                    defaultValue='选项1'
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '按钮渲染模式',
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
        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            optionType='button',
            defaultValue='选项1'
        ),

        fac.AntdRadioGroup(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            optionType='button',
            buttonStyle='solid',
            defaultValue='选项1'
        )
    ],
    direction='vertical'
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
                    id='按钮渲染模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            [
                                fac.AntdRadioGroup(
                                    id='radio-group-demo',
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ],
                                    defaultValue='选项1'
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('value：', strong=True),
                                        fac.AntdText(id='radio-group-demo-output')
                                    ]
                                )
                            ],
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
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdSpin(
    [
        fac.AntdRadioGroup(
            id='radio-group-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ],
            defaultValue='选项1'
        ),
        html.Div(
            [
                fac.AntdText('value：', strong=True),
                fac.AntdText(id='radio-group-demo-output')
            ]
        )
    ],
    text='回调中'
)
...
@app.callback(
    Output('radio-group-demo-output', 'children'),
    Input('radio-group-demo', 'value')
)
def radio_group_demo_callback(value):
    return str(value)
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
                            {'title': '不同的排列方向', 'href': '#不同的排列方向'},
                            {'title': '按钮渲染模式', 'href': '#按钮渲染模式'},
                            {'title': '回调示例', 'href': '#回调示例'},
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
