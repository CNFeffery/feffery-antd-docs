import dash_html_components as html
import dash_core_components as dcc
import feffery_antd_components as fac

import callbacks.AntdDateRangePicker

docs_content = html.Div(
    [
        html.H2(
            'AntdDateRangePicker(id, className, style, *args, **kwargs)',
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
                        {'title': '基础的日期范围选择控件', 'href': '#基础的日期范围选择控件'},
                        {'title': '添加时间选择', 'href': '#添加时间选择'},
                        {'title': '自定义空白填充文字', 'href': '#自定义空白填充文字'},
                        {'title': '修改时间粒度', 'href': '#修改时间粒度'},
                        {'title': '禁用开始或结束输入框', 'href': '#禁用开始或结束输入框'},
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

        dcc.Markdown(open('documents/AntdDateRangePicker.md', encoding='utf-8').read(),
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
                    '基础的日期范围选择控件：',
                    id='基础的日期范围选择控件',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDateRangePicker()
                ```
                '''),

                fac.AntdDateRangePicker()
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '添加时间选择：',
                    id='添加时间选择',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDateRangePicker(showTime=True)
                ```
                '''),

                fac.AntdDateRangePicker(showTime=True)
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '自定义空白填充文字：',
                    id='自定义空白填充文字',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDateRangePicker(placeholderStart='日期起点', placeholderEnd='日期终点')
                ```
                '''),

                fac.AntdDateRangePicker(placeholderStart='日期起点', placeholderEnd='日期终点')
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '修改时间粒度：',
                    id='修改时间粒度',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDateRangePicker(picker='week'),
                fac.AntdDateRangePicker(picker='month'),
                fac.AntdDateRangePicker(picker='quarter', placeholderStart='开始季度', placeholderEnd='结束季度'),
                fac.AntdDateRangePicker(picker='year')
                ```
                '''),

                fac.AntdDateRangePicker(picker='week'),
                fac.AntdDateRangePicker(picker='month'),
                fac.AntdDateRangePicker(picker='quarter', placeholderStart='开始季度', placeholderEnd='结束季度'),
                fac.AntdDateRangePicker(picker='year')
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(
            [
                html.Strong(
                    '禁用开始或结束输入框：',
                    id='禁用开始或结束输入框',
                    style={'paddingTop': '5px'}
                ),

                dcc.Markdown('''
                ```Python
                fac.AntdDateRangePicker(disabledStart=True),
                fac.AntdDateRangePicker(disabledEnd=True)
                ```
                '''),

                fac.AntdDateRangePicker(disabledStart=True),
                fac.AntdDateRangePicker(disabledEnd=True)
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
                fac.AntdDateRangePicker(id='date-range-picker-demo'),
                html.Br(),
                html.Em(id='date-range-picker-demo-output')
                ...
                @app.callback(
                    Output('date-range-picker-demo-output', 'children'),
                    [Input('date-range-picker-demo', 'selectedStartDate'),
                    Input('date-range-picker-demo', 'selectedEndDate')],
                    prevent_initial_call=True
                )
                def date_picker_callback_demo(selectedStartDate, selectedEndDate):
                    import time;time.sleep(0.5)
                    if selectedStartDate and selectedEndDate:
                        return f'{selectedStartDate} ~ {selectedEndDate}'
                
                    return dash.no_update
                ```
                '''),

                fac.AntdDateRangePicker(id='date-range-picker-demo'),
                html.Br(),
                html.Em(id='date-range-picker-demo-output')
            ],
            style={
                'marginBottom': '80px'
            }
        ),

        html.Div(style={'height': '100px'})
    ]
)
