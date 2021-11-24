from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdCheckboxGroup

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdCheckboxGroup(id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdCheckboxGroup.md', encoding='utf-8').read()
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
                        fac.AntdCheckboxGroup(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
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
fac.AntdCheckboxGroup(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ]
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
                                fac.AntdCheckboxGroup(
                                    id='checkbox-group-demo',
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        }
                                        for i in range(5)
                                    ]
                                ),
                                html.Div(
                                    [
                                        fac.AntdText('value：', strong=True),
                                        fac.AntdText(id='checkbox-group-demo-output')
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
        fac.AntdCheckboxGroup(
            id='checkbox-group-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(5)
            ]
        ),
        html.Div(
            [
                fac.AntdText('value：', strong=True),
                fac.AntdText(id='checkbox-group-demo-output')
            ]
        )
    ],
    text='回调中'
)
...
@app.callback(
    Output('checkbox-group-demo-output', 'children'),
    Input('checkbox-group-demo', 'value')
)
def checkbox_group_demo_callback(value):

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

                html.Div(
                    [
                        fac.AntdCheckbox(
                            id='checkbox-demo-client-side',
                            label='全选',
                            style={
                                'marginRight': '8px'
                            }
                        ),
                        fac.AntdCheckboxGroup(
                            id='checkbox-group-demo-client-side',
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ]
                        ),

                        fac.AntdDivider(
                            '利用浏览器端回调实现全选效果',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　利用dash的浏览器端回调，配合'),
                                fac.AntdText('AntdCheckbox', strong=True),
                                fac.AntdText('组件，可以实现浏览器端丝滑的全选/非全选效果')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdCheckbox(
    id='checkbox-demo-client-side',
    label='全选',
    style={
        'marginRight': '8px'
    }
),
fac.AntdCheckboxGroup(
    id='checkbox-group-demo-client-side',
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ]
)
...
app.clientside_callback(
    """
    function(checked, value, options) {

        const ctx = dash_clientside.callback_context;

        if ( ctx?.triggered[0].prop_id === 'checkbox-group-demo-client-side.value' ) {
            return [
                value.length === options.length ? true : false,
                value
            ]
        } else if ( ctx?.triggered[0].prop_id === 'checkbox-demo-client-side.checked' ) {
            return [
                checked,
                checked ? options.map(item => item.value) : []
            ]
        }
        return dash_clientside.no_update;
    }
    """,
    [Output('checkbox-demo-client-side', 'checked'),
     Output('checkbox-group-demo-client-side', 'value')],
    [Input('checkbox-demo-client-side', 'checked'),
     Input('checkbox-group-demo-client-side', 'value')],
    State('checkbox-group-demo-client-side', 'options'),
    prevent_initial_call=True
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
                    id='利用浏览器端回调实现全选效果',
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
                            {'title': '回调示例', 'href': '#回调示例'},
                            {'title': '利用浏览器端回调实现全选效果', 'href': '#利用浏览器端回调实现全选效果'},
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
