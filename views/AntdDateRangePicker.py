from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdDateRangePicker

docs_content = html.Div(
    [
        html.Div(
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
                                language='python',
                                 codeTheme='coy-without-shadows',
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
                        fac.AntdDateRangePicker(
                            defaultValue=['2022-01-01', None]
                        ),

                        fac.AntdDateRangePicker(
                            defaultValue=[None, '2022-01-01']
                        ),

                        fac.AntdDivider(
                            '初始化时只设置单边值',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDateRangePicker(
    defaultValue=['2022-01-01', None]
),

fac.AntdDateRangePicker(
    defaultValue=[None, '2022-01-01']
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
                    id='初始化时只设置单边值',
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
                                language='python',
                                 codeTheme='coy-without-shadows',
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
                        fac.AntdDateRangePicker(placeholder=['日期起点', '日期终点']),

                        fac.AntdDivider(
                            '自定义空白填充文字',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''fac.AntdDateRangePicker(placeholder=['日期起点', '日期终点'])'''
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
                        fac.AntdDateRangePicker(picker='quarter', placeholder=['开始季度', '结束季度']),
                        fac.AntdDateRangePicker(picker='year'),

                        fac.AntdDivider(
                            '修改时间粒度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDateRangePicker(picker='week'),
fac.AntdDateRangePicker(picker='month'),
fac.AntdDateRangePicker(picker='quarter', placeholder=['开始季度', '结束季度']),
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
                        fac.AntdDateRangePicker(disabled=[True, False]),
                        fac.AntdDateRangePicker(disabled=[False, True]),

                        fac.AntdDivider(
                            '禁用开始或结束输入框',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDateRangePicker(disabled=[True, False]),
fac.AntdDateRangePicker(disabled=[False, True])'''
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
                        fac.AntdDivider(
                            "mode='eq'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月6号', '禁用每月6号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月非6号', '禁用每月非6号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月小于等于6号', '禁用每月小于等于6号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月小于6号', '禁用每月小于6号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月大于等于6号', '禁用每月大于等于6号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月大于6号', '禁用每月大于6号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用每月的5号到25号', '禁用每月的5号到25号'],
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

                        fac.AntdDateRangePicker(
                            placeholder=['禁用非每月的5号到25号', '禁用非每月的5号到25号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月6号', '禁用每月6号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月非6号', '禁用每月非6号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月小于等于6号', '禁用每月小于等于6号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月小于6号', '禁用每月小于6号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月大于等于6号', '禁用每月大于等于6号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月大于6号', '禁用每月大于6号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用每月的5号到25号', '禁用每月的5号到25号'],
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

fac.AntdDateRangePicker(
    placeholder=['禁用非每月的5号到25号', '禁用非每月的5号到25号'],
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
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdDateRangePicker(id='date-range-picker-demo'),
html.Br(),
html.Em(id='date-range-picker-demo-output')
...
@app.callback(
    Output('date-range-picker-demo-output', 'children'),
    Input('date-range-picker-demo', 'value'),
    prevent_initial_call=True
)
def date_picker_callback_demo(value):
    if value:
        return f'{value[0]} ~ {value[1]}'

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

                html.Div(
                    [
                        fac.AntdDateRangePicker(
                            id='date-range-picker-disabled-demo'
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

fac.AntdDateRangePicker(
    id='date-range-picker-disabled-demo'
)

...


@app.callback(
    Output('date-range-picker-disabled-demo', 'disabledDatesStrategy'),
    Input('url', 'pathname')
)
def date_range_picker_disabled_callback_demo(pathname):
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
                            {'title': '基础的日期范围选择控件', 'href': '#基础的日期范围选择控件'},
                            {'title': '初始化时只设置单边值', 'href': '#初始化时只设置单边值'},
                            {'title': '添加时间选择', 'href': '#添加时间选择'},
                            {'title': '自定义空白填充文字', 'href': '#自定义空白填充文字'},
                            {'title': '修改时间粒度', 'href': '#修改时间粒度'},
                            {'title': '禁用开始或结束输入框', 'href': '#禁用开始或结束输入框'},
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
