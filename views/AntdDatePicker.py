import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdDatePicker

docs_content = html.Div(
    [

        html.H2(
            'AntdDatePicker(id, className, style, *args, **kwargs)',
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
                        {'title': '常规的日期选择', 'href': '#常规的日期选择'},
                        {'title': '添加时间选择功能', 'href': '#添加时间选择功能'},
                        {'title': '其他时间粒度选择', 'href': '#其他时间粒度选择'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
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

        dcc.Markdown(open('documents/AntdDatePicker.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

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
                fac.AntdDatePicker(
                    picker='date',
                    placeholder='请选择日期',
                    defaultPickerValue={
                        'value': '2020/01/01',
                        'format': 'YYYY/MM/DD'
                    }
                ),

                fac.AntdDivider(
                    '常规的日期选择',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdDatePicker(
                                    picker='date',
                                    placeholder='请选择日期',
                                    defaultPickerValue={
                                        'value': '2020/01/01',
                                        'format': 'YYYY/MM/DD'
                                    },
                                    showTime=False
                                )
                                ```
                                '''),
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
            id='常规的日期选择',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDatePicker(
                    picker='date',
                    placeholder='请选择日期+时间',
                    defaultPickerValue={
                        'value': '2020/01/01',
                        'format': 'YYYY/MM/DD'
                    },
                    showTime=True
                ),

                fac.AntdDivider(
                    '添加时间选择功能',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdDatePicker(
                                    picker='date',
                                    placeholder='请选择日期+时间',
                                    defaultPickerValue={
                                        'value': '2020/01/01',
                                        'format': 'YYYY/MM/DD'
                                    },
                                    showTime=True
                                )
                                ```
                                '''),
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
            id='添加时间选择功能',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDatePicker(
                    picker='month',
                    placeholder='请选择月份：',
                    defaultPickerValue={
                        'value': '2020/01',
                        'format': 'YYYY/MM'
                    }
                ),

                html.Div(style={'height': '25px'}),

                fac.AntdDatePicker(
                    picker='year',
                    placeholder='请选择年份',
                    defaultPickerValue={
                        'value': '2020',
                        'format': 'YYYY'
                    }
                ),

                fac.AntdDivider(
                    '其他时间粒度选择',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdDatePicker(
                                    picker='month',
                                    placeholder='请选择月份：',
                                    defaultPickerValue={
                                        'value': '2020/01',
                                        'format': 'YYYY/MM'
                                    }
                                ),

                                html.Div(style={'height': '25px'}),

                                fac.AntdDatePicker(
                                    picker='year',
                                    placeholder='请选择年份',
                                    defaultPickerValue={
                                        'value': '2020',
                                        'format': 'YYYY'
                                    }
                                )
                                ```
                                '''),
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
            id='其他时间粒度选择',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDatePicker(
                    id='date-picker-demo',
                    picker='date',
                    placeholder='请选择日期+时间',
                    defaultPickerValue={
                        'value': '2020/01/01',
                        'format': 'YYYY/MM/DD'
                    },
                    showTime=True
                ),
                html.Br(),
                fac.AntdSpin(
                    html.Em(id='date-picker-demo-output'),
                    text='回调中'
                ),

                fac.AntdDivider(
                    '回调示例',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdDatePicker(
                                    id='date-picker-demo',
                                    picker='date',
                                    placeholder='请选择日期+时间',
                                    defaultPickerValue={
                                        'value': '2020/01/01',
                                        'format': 'YYYY/MM/DD'
                                    },
                                    showTime=True
                                ),
                                html.Br(),
                                fac.AntdSpin(
                                    html.Em(id='date-picker-demo-output'),
                                    text='回调中'
                                )
                                ...
                                @app.callback(
                                    Output('date-picker-demo-output', 'children'),
                                    Input('date-picker-demo', 'selectedDate'),
                                    prevent_initial_call=True
                                )
                                def date_picker_callback_demo(selectedDate):
                                    if selectedDate:
                                        return selectedDate

                                    return ''

                                ```
                                '''),
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
    ]
)
