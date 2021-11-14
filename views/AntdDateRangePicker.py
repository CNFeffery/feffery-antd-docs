from dash import html
from dash import dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc

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

        fac.AntdBackTop(
            containerId='docs-content',
            duration=0.6
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

        fuc.FefferyMarkdown(
            markdownStr=open('documents/AntdDateRangePicker.md', encoding='utf-8').read()
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
                fac.AntdDateRangePicker(),

                fac.AntdDivider(
                    '基础的日期范围选择控件',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    fuc.FefferySyntaxHighlighter(
                        showLineNumbers=True,
                        showInlineLineNumbers=True,
                        language='python',
                        codeStyle='coy-without-shadows',
                        codeString='''fac.AntdDateRangePicker()'''
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
            id='基础的日期范围选择控件',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDateRangePicker(showTime=True),

                fac.AntdDivider(
                    '添加时间选择',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    fuc.FefferySyntaxHighlighter(
                        showLineNumbers=True,
                        showInlineLineNumbers=True,
                        language='python',
                        codeStyle='coy-without-shadows',
                        codeString='''fac.AntdDateRangePicker(showTime=True)'''
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
            id='添加时间选择',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDateRangePicker(placeholderStart='日期起点', placeholderEnd='日期终点'),

                fac.AntdDivider(
                    '自定义空白填充文字',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    fuc.FefferySyntaxHighlighter(
                        showLineNumbers=True,
                        showInlineLineNumbers=True,
                        language='python',
                        codeStyle='coy-without-shadows',
                        codeString='''fac.AntdDateRangePicker(placeholderStart='日期起点', placeholderEnd='日期终点')'''
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
            id='自定义空白填充文字',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDateRangePicker(picker='week'),
                fac.AntdDateRangePicker(picker='month'),
                fac.AntdDateRangePicker(picker='quarter', placeholderStart='开始季度', placeholderEnd='结束季度'),
                fac.AntdDateRangePicker(picker='year'),

                fac.AntdDivider(
                    '修改时间粒度',
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
fac.AntdDateRangePicker(picker='week'),
fac.AntdDateRangePicker(picker='month'),
fac.AntdDateRangePicker(picker='quarter', placeholderStart='开始季度', placeholderEnd='结束季度'),
fac.AntdDateRangePicker(picker='year')'''
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
            id='修改时间粒度',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDateRangePicker(disabledStart=True),
                fac.AntdDateRangePicker(disabledEnd=True),

                fac.AntdDivider(
                    '禁用开始或结束输入框',
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
fac.AntdDateRangePicker(disabledStart=True),
fac.AntdDateRangePicker(disabledEnd=True)'''
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
            id='禁用开始或结束输入框',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdDateRangePicker(id='date-range-picker-demo'),
                html.Br(),
                fac.AntdSpin(
                    html.Em(id='date-range-picker-demo-output'),
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
    if selectedStartDate and selectedEndDate:
        return f'{selectedStartDate} ~ {selectedEndDate}'

    return dash.no_update'''
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
    ]
)
