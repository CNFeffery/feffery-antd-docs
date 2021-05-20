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

        html.Span(
            '主要参数说明：',
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

        html.Span(
            '使用示例：',
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
                html.Strong('常规的日期选择：', style={'paddingTop': '5px'}),

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

                fac.AntdDatePicker(
                    picker='date',
                    placeholder='请选择日期',
                    defaultPickerValue={
                        'value': '2020/01/01',
                        'format': 'YYYY/MM/DD'
                    }
                ),
            ],
            style={
                'marginBottom': '20px'
            }
        ),

        html.Div(
            [
                html.Strong('添加时间选择功能：', style={'paddingTop': '5px'}),

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

                fac.AntdDatePicker(
                    picker='date',
                    placeholder='请选择日期+时间',
                    defaultPickerValue={
                        'value': '2020/01/01',
                        'format': 'YYYY/MM/DD'
                    },
                    showTime=True
                )
            ],
            style={
                'marginBottom': '20px'
            }
        ),

        html.Div(
            [
                html.Strong('其他时间粒度选择：', style={'paddingTop': '5px'}),

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
            ],
            style={
                'marginBottom': '20px'
            }
        ),

        html.Div(
            [
                html.Strong('回调示例：', style={'paddingTop': '5px'}),

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
                html.Em(id='date-picker-demo-output')

                ...

                @app.callback(
                    Output('date-picker-demo-output', 'children'),
                    Input('date-picker-demo', 'selectedDate')
                )
                def date_picker_callback_demo(selectedDate):
                    if selectedDate:
                        return selectedDate
                
                    return ''

                ```
                '''),

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
                html.Em(id='date-picker-demo-output')
            ],
            style={
                'marginBottom': '20px'
            }
        ),

        html.Div(style={'height': '50px'})
    ]
)
