from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCheckboxGroup
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
                            'title': '数据录入'
                        },
                        {
                            'title': 'AntdCheckboxGroup 组合选择框'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于在一组可选项中进行多项选择。')
                    ]
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
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdCheckboxGroup(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
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
                        fac.AntdDivider(
                            '禁用部分选项',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCheckboxGroup(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}',
                                    'disabled': i % 2 != 0
                                }
                                for i in range(5)
                            ]
                        ),

                        fac.AntdDivider(
                            '禁用整体',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCheckboxGroup(
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ],
                            disabled=True
                        ),

                        fac.AntdDivider(
                            '部分选项及整体的禁用',
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
fac.AntdDivider(
    '禁用部分选项',
    innerTextOrientation='left'
),

fac.AntdCheckboxGroup(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}',
            'disabled': i % 2 != 0
        }
        for i in range(5)
    ]
),

fac.AntdDivider(
    '禁用整体',
    innerTextOrientation='left'
),

fac.AntdCheckboxGroup(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ],
    disabled=True
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
                    id='部分选项及整体的禁用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdCheckboxGroup(
                            id='checkbox-group-demo1',
                            options=[
                                {
                                    'label': f'选项{i}',
                                    'value': f'选项{i}'
                                }
                                for i in range(5)
                            ]
                        ),

                        fac.AntdParagraph(
                            id='checkbox-group-demo1-output'
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
fac.AntdCheckboxGroup(
    id='checkbox-group-demo1',
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(5)
    ]
),

fac.AntdParagraph(
    id='checkbox-group-demo1-output'
)

...

@app.callback(
    Output('checkbox-group-demo1-output', 'children'),
    Input('checkbox-group-demo1', 'value')
)
def checkbox_group_demo1(value):

    return f'value: {value}'
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
                            ],
                            value=[]
                        ),

                        fac.AntdDivider(
                            '基于回调实现全选',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '　　本例中使用了浏览器端回调以实现更流畅的交互响应速度'
                            ]
                        ),

                        fac.AntdCollapse(
                            fmc.FefferySyntaxHighlighter(
                                showCopyButton=True,
                                showLineNumbers=True,
                                language='python',
                                codeTheme='coy-without-shadows',
                                codeString="""
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
    '''(checked, value, options) => {
        let ctx = dash_clientside.callback_context;
        value = value || []
        if ( ctx?.triggered[0].prop_id === 'checkbox-group-demo-client-side.value' ) {
            return [
                value.length === options.length ? true : false,
                value,
                value.length > 0 && value.length < options.length ? true : false
            ]
        } else if ( ctx?.triggered[0].prop_id === 'checkbox-demo-client-side.checked' ) {
            return [
                checked,
                checked ? options.map(item => item.value) : [],
                !checked && value.length > 0 && value.length < options.length ? true : false
            ]
        }
        return dash_clientside.no_update;
    }''',
    [Output('checkbox-demo-client-side', 'checked'),
     Output('checkbox-group-demo-client-side', 'value'),
     Output('checkbox-demo-client-side', 'indeterminate')],
    [Input('checkbox-demo-client-side', 'checked'),
     Input('checkbox-group-demo-client-side', 'value')],
    State('checkbox-group-demo-client-side', 'options'),
    prevent_initial_call=True
)
"""
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
                    id='基于回调实现全选',
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
                    {'title': '部分选项及整体的禁用', 'href': '#部分选项及整体的禁用'},
                    {'title': '回调示例', 'href': '#回调示例'},
                    {'title': '基于回调实现全选', 'href': '#基于回调实现全选'},
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
            component_name='AntdCheckboxGroup'
        )
    ],
    style={
        'display': 'flex'
    }
)
