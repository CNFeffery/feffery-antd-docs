from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdDatePicker

docs_content = html.Div(
    [
        html.Div(
            [

                html.H2(
                    'AntdDatePicker(id, className, style, *args, **kwargs)',
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

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdDatePicker.md', encoding='utf-8').read()
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
                        fac.AntdDatePicker(
                            picker='date',
                            placeholder='请选择日期',
                            defaultPickerValue='2020/01/01'
                        ),

                        fac.AntdDivider(
                            '常规的日期选择',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDatePicker(
    picker='date',
    placeholder='请选择日期',
    defaultPickerValue='2020/01/01'
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
                    id='常规的日期选择',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDatePicker(
                            picker='date',
                            placeholder='请选择日期+时间',
                            defaultPickerValue='2020/01/01',
                            showTime=True
                        ),

                        fac.AntdDivider(
                            '添加时间选择功能',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDatePicker(
    picker='date',
    placeholder='请选择日期+时间',
    defaultPickerValue='2020/01/01',
    showTime=True
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
                    id='添加时间选择功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDatePicker(
                            picker='week',
                            placeholder='请选择周：',
                            format='YYYY-第W周'
                        ),
                        fac.AntdDatePicker(
                            picker='month',
                            placeholder='请选择月份：',
                            format='YYYY-MM'
                        ),
                        fac.AntdDatePicker(
                            picker='quarter',
                            placeholder='请选择季度：',
                            format='YYYY-第Q季度'
                        ),
                        fac.AntdDatePicker(
                            picker='year',
                            placeholder='请选择年份',
                            format='YYYY'
                        ),

                        fac.AntdDivider(
                            '其他时间粒度选择',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDatePicker(
    picker='week',
    placeholder='请选择周：',
    format='YYYY-第W周'
),
fac.AntdDatePicker(
    picker='month',
    placeholder='请选择月份：',
    format='YYYY-MM'
),
fac.AntdDatePicker(
    picker='quarter',
    placeholder='请选择季度：',
    format='YYYY-第Q季度'
),
fac.AntdDatePicker(
    picker='year',
    placeholder='请选择年份',
    format='YYYY'
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
                    id='其他时间粒度选择',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            "mode='eq'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月6号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'eq',
                                    'target': 'day',
                                    'value': 6
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='ne'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月非6号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'ne',
                                    'target': 'day',
                                    'value': 6
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='le'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月小于等于6号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'le',
                                    'target': 'day',
                                    'value': 6
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='lt'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月小于6号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'lt',
                                    'target': 'day',
                                    'value': 6
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='ge'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月大于等于6号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'ge',
                                    'target': 'day',
                                    'value': 6
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='gt'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月大于6号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'gt',
                                    'target': 'day',
                                    'value': 6
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='in'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用每月的5号到25号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'in',
                                    'target': 'day',
                                    'value': list(range(5, 26))
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='not-in'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDatePicker(
                            placeholder='禁用非每月的5号到25号',
                            disabledDatesStrategy=[
                                {
                                    'mode': 'not-in',
                                    'target': 'day',
                                    'value': list(range(5, 26))
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '自定义日期禁用策略',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDivider(
    "mode='eq'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月6号',
    disabledDatesStrategy=[
        {
            'mode': 'eq',
            'target': 'day',
            'value': 6
        }
    ]
),

fac.AntdDivider(
    "mode='ne'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月非6号',
    disabledDatesStrategy=[
        {
            'mode': 'ne',
            'target': 'day',
            'value': 6
        }
    ]
),

fac.AntdDivider(
    "mode='le'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月小于等于6号',
    disabledDatesStrategy=[
        {
            'mode': 'le',
            'target': 'day',
            'value': 6
        }
    ]
),

fac.AntdDivider(
    "mode='lt'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月小于6号',
    disabledDatesStrategy=[
        {
            'mode': 'lt',
            'target': 'day',
            'value': 6
        }
    ]
),

fac.AntdDivider(
    "mode='ge'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月大于等于6号',
    disabledDatesStrategy=[
        {
            'mode': 'ge',
            'target': 'day',
            'value': 6
        }
    ]
),

fac.AntdDivider(
    "mode='gt'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月大于6号',
    disabledDatesStrategy=[
        {
            'mode': 'gt',
            'target': 'day',
            'value': 6
        }
    ]
),

fac.AntdDivider(
    "mode='in'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用每月的5号到25号',
    disabledDatesStrategy=[
        {
            'mode': 'in',
            'target': 'day',
            'value': list(range(5, 26))
        }
    ]
),

fac.AntdDivider(
    "mode='not-in'",
    innerTextOrientation='left'
),

fac.AntdDatePicker(
    placeholder='禁用非每月的5号到25号',
    disabledDatesStrategy=[
        {
            'mode': 'not-in',
            'target': 'day',
            'value': list(range(5, 26))
        }
    ]
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
                    id='自定义日期禁用策略',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDatePicker(
                            id='date-picker-demo',
                            picker='date',
                            placeholder='请选择日期+时间',
                            defaultPickerValue='2020/01/01',
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
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDatePicker(
    id='date-picker-demo',
    picker='date',
    placeholder='请选择日期+时间',
    defaultPickerValue='2020/01/01',
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
    Input('date-picker-demo', 'value'),
    prevent_initial_call=True
)
def date_picker_callback_demo(value):
    if value:
        return value

    return dash.no_update
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
                        fac.AntdDatePicker(
                            id='date-picker-disabled-demo'
                        ),

                        fac.AntdDivider(
                            '禁用今天往后七天',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
from datetime import datetime, timedelta

fac.AntdDatePicker(
    id='date-picker-disabled-demo'
)

...

@app.callback(
    Output('date-picker-disabled-demo', 'disabledDatesStrategy'),
    Input('url', 'pathname')
)
def date_picker_disabled_callback_demo(pathname):
    return [
        {
            'mode': 'in-enumerate-dates',
            'value': [
                (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
                for day in range(7)
            ]
        }
    ]
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
                    id='禁用今天往后七天',
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
                            {'title': '常规的日期选择', 'href': '#常规的日期选择'},
                            {'title': '添加时间选择功能', 'href': '#添加时间选择功能'},
                            {'title': '其他时间粒度选择', 'href': '#其他时间粒度选择'},
                            {'title': '自定义日期禁用策略', 'href': '#自定义日期禁用策略'},
                            {'title': '回调示例', 'href': '#回调示例'},
                            {'title': '禁用今天往后七天', 'href': '#禁用今天往后七天'},
                        ]
                    },
                ],
                offsetTop=0
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
