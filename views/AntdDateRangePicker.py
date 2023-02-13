from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdDateRangePicker
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
                            'title': 'AntdDateRangePicker 日期范围选择框'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于进行各种常见粒度下的日期时间范围选择。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdDateRangePicker(),
                        fac.AntdDateRangePicker(
                            placeholder=['开始日期时间', '结束日期时间'],
                            showTime=True
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
fac.AntdDateRangePicker(),
fac.AntdDateRangePicker(
    placeholder=['开始日期时间', '结束日期时间'],
    showTime=True
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'placement=',
                                        f'"{placement}"'
                                    ],
                                    placement=placement,
                                    style={
                                        'width': 275
                                    }
                                )
                                for placement in [
                                    'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
                                ]
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '不同的悬浮层展开方位',
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
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(
            placeholder=[
                'placement=',
                f'"{placement}"'
            ],
            placement=placement,
            style={
                'width': 275
            }
        )
        for placement in [
            'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
        ]
    ],
    direction='vertical'
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
                    id='不同的悬浮层展开方位',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'picker=',
                                        f'"{picker}"'
                                    ],
                                    picker=picker,
                                    style={
                                        'width': 200
                                    }
                                )
                                for picker in
                                ['date', 'week', 'month', 'quarter', 'year']
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '不同的日期范围选择粒度',
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
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(
            placeholder=[
                'picker=',
                f'"{picker}"'
            ],
            picker=picker,
            style={
                'width': 200
            }
        )
        for picker in
        ['date', 'week', 'month', 'quarter', 'year']
    ],
    direction='vertical'
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
                    id='不同的日期范围选择粒度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'picker="date"', ''
                                    ],
                                    format='YYYY年MM月DD日',
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'picker="week"', ''
                                    ],
                                    picker='week',
                                    format='YYYY-第W周',
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'picker="month"', ''
                                    ],
                                    picker='month',
                                    format='YYYY-MM',
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'picker="quarter"', ''
                                    ],
                                    picker='quarter',
                                    format='YYYY-第Q季度',
                                    style={
                                        'width': 300
                                    }
                                ),
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        'picker="year"', ''
                                    ],
                                    picker='year',
                                    format='YYYY年',
                                    style={
                                        'width': 300
                                    }
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '自定义format',
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
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(
            placeholder=[
                'picker="date"', ''
            ],
            format='YYYY年MM月DD日',
            style={
                'width': 300
            }
        ),
        fac.AntdDateRangePicker(
            placeholder=[
                'picker="week"', ''
            ],
            picker='week',
            format='YYYY-第W周',
            style={
                'width': 300
            }
        ),
        fac.AntdDateRangePicker(
            placeholder=[
                'picker="month"', ''
            ],
            picker='month',
            format='YYYY-MM',
            style={
                'width': 300
            }
        ),
        fac.AntdDateRangePicker(
            placeholder=[
                'picker="quarter"', ''
            ],
            picker='quarter',
            format='YYYY-第Q季度',
            style={
                'width': 300
            }
        ),
        fac.AntdDateRangePicker(
            placeholder=[
                'picker="year"', ''
            ],
            picker='year',
            format='YYYY年',
            style={
                'width': 300
            }
        )
    ],
    direction='vertical'
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
                    id='自定义format',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDateRangePicker(
                            disabled=[True, True]
                        ),

                        fac.AntdDateRangePicker(
                            disabled=[True, False]
                        ),

                        fac.AntdDateRangePicker(
                            disabled=[False, True]
                        ),

                        fac.AntdDivider(
                            '禁用状态',
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
fac.AntdDateRangePicker(
    disabled=[True, True]
),

fac.AntdDateRangePicker(
    disabled=[True, False]
),

fac.AntdDateRangePicker(
    disabled=[False, True]
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
                    id='禁用状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDateRangePicker(
                            value=['2023-01-01', '2023-01-20'],
                            readOnly=True
                        ),

                        fac.AntdDivider(
                            '只读状态',
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
fac.AntdDateRangePicker(
    value=['2023-01-01', '2023-01-20'],
    readOnly=True
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
                    id='只读状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        f'status="{status}"',
                                        ''
                                    ],
                                    status=status,
                                    style={
                                        'width': 300
                                    }
                                )
                                for status in ['warning', 'error']
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '强制状态渲染',
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
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(
            placeholder=[
                f'status="{status}"',
                ''
            ],
            status=status,
            style={
                'width': 300
            }
        )
        for status in ['warning', 'error']
    ],
    direction='vertical'
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
                    id='强制状态渲染',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdDateRangePicker(
                                    defaultPickerValue='1999-12-31',
                                    style={
                                        'width': 300
                                    }
                                ),

                                fac.AntdDateRangePicker(
                                    placeholder=[
                                        '配合自定义format',
                                        ''
                                    ],
                                    defaultPickerValue='1999年12月31日',
                                    format='YYYY年MM月DD日',
                                    style={
                                        'width': 300
                                    }
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '初始化停留日期位置',
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
fac.AntdSpace(
    [
        fac.AntdDateRangePicker(
            defaultPickerValue='1999-12-31',
            style={
                'width': 300
            }
        ),

        fac.AntdDateRangePicker(
            placeholder=[
                '配合自定义format',
                ''
            ],
            defaultPickerValue='1999年12月31日',
            format='YYYY年MM月DD日',
            style={
                'width': 300
            }
        )
    ],
    direction='vertical'
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
                    id='初始化停留日期位置',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdDivider(
                            "mode='eq'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDateRangePicker(
                            placeholder=[
                                '禁用每月6号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用每月非6号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用每月小于等于6号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用每月小于6号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用每月大于等于6号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用每月大于6号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用每月的5号到25号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
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
                            placeholder=[
                                '禁用非每月的5号到25号',
                                ''
                            ],
                            style={
                                'width': 400
                            },
                            disabledDatesStrategy=[
                                {
                                    'mode': 'not-in',
                                    'target': 'day',
                                    'value': list(range(5, 26))
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            "mode='in-enumerate-dates'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDateRangePicker(
                            placeholder=[
                                '禁用枚举列表中的日期',
                                ''
                            ],
                            style={
                                'width': 400
                            },
                            disabledDatesStrategy=[
                                {
                                    'mode': 'in-enumerate-dates',
                                    'value': [
                                        f'2023-01-0{i}'
                                        for i in range(1, 10)
                                    ]
                                }
                            ],
                            defaultPickerValue='2023-01-01'
                        ),

                        fac.AntdDivider(
                            "mode='not-in-enumerate-dates'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDateRangePicker(
                            placeholder=[
                                '禁用非枚举列表中的日期',
                                ''
                            ],
                            style={
                                'width': 400
                            },
                            disabledDatesStrategy=[
                                {
                                    'mode': 'not-in-enumerate-dates',
                                    'value': [
                                        f'2023-01-0{i}'
                                        for i in range(1, 10)
                                    ]
                                }
                            ],
                            defaultPickerValue='2023-01-01'
                        ),

                        fac.AntdDivider(
                            "target='specific-date'",
                            innerTextOrientation='left'
                        ),

                        fac.AntdDateRangePicker(
                            placeholder=[
                                '禁用指定日期之前的日期',
                                ''
                            ],
                            style={
                                'width': 400
                            },
                            disabledDatesStrategy=[
                                {
                                    'mode': 'lt',
                                    'target': 'specific-date',
                                    'value': '2023-01-15'
                                }
                            ],
                            defaultPickerValue='2023-01-01'
                        ),

                        fac.AntdDivider(
                            '自定义日期禁用策略',
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
    "mode='eq'",
    innerTextOrientation='left'
),

fac.AntdDateRangePicker(
    placeholder=[
        '禁用每月6号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用每月非6号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用每月小于等于6号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用每月小于6号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用每月大于等于6号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用每月大于6号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用每月的5号到25号',
        ''
    ],
    style={
        'width': 400
    },
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
    placeholder=[
        '禁用非每月的5号到25号',
        ''
    ],
    style={
        'width': 400
    },
    disabledDatesStrategy=[
        {
            'mode': 'not-in',
            'target': 'day',
            'value': list(range(5, 26))
        }
    ]
),

fac.AntdDivider(
    "mode='in-enumerate-dates'",
    innerTextOrientation='left'
),

fac.AntdDateRangePicker(
    placeholder=[
        '禁用枚举列表中的日期',
        ''
    ],
    style={
        'width': 400
    },
    disabledDatesStrategy=[
        {
            'mode': 'in-enumerate-dates',
            'value': [
                f'2023-01-0{i}'
                for i in range(1, 10)
            ]
        }
    ],
    defaultPickerValue='2023-01-01'
),

fac.AntdDivider(
    "mode='not-in-enumerate-dates'",
    innerTextOrientation='left'
),

fac.AntdDateRangePicker(
    placeholder=[
        '禁用非枚举列表中的日期',
        ''
    ],
    style={
        'width': 400
    },
    disabledDatesStrategy=[
        {
            'mode': 'not-in-enumerate-dates',
            'value': [
                f'2023-01-0{i}'
                for i in range(1, 10)
            ]
        }
    ],
    defaultPickerValue='2023-01-01'
),

fac.AntdDivider(
    "target='specific-date'",
    innerTextOrientation='left'
),

fac.AntdDateRangePicker(
    placeholder=[
        '禁用指定日期之前的日期',
        ''
    ],
    style={
        'width': 400
    },
    disabledDatesStrategy=[
        {
            'mode': 'lt',
            'target': 'specific-date',
            'value': '2023-01-15'
        }
    ],
    defaultPickerValue='2023-01-01'
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
                        fac.AntdSpace(
                            [
                                fac.AntdSpace(
                                    [
                                        fac.AntdDateRangePicker(
                                            id='date-range-picker-demo1',
                                            style={
                                                'width': 300
                                            },
                                        ),
                                        fac.AntdText(
                                            id='date-range-picker-demo1-output'
                                        )
                                    ],
                                    align='center'
                                ),

                                fac.AntdSpace(
                                    [
                                        fac.AntdDateRangePicker(
                                            id='date-range-picker-demo2',
                                            placeholder=[
                                                '开始日期时间',
                                                '结束日期时间'
                                            ],
                                            style={
                                                'width': 350
                                            },
                                            showTime=True
                                        ),
                                        fac.AntdText(
                                            id='date-range-picker-demo2-output'
                                        )
                                    ],
                                    align='center'
                                ),

                                fac.AntdSpace(
                                    [
                                        fac.AntdDateRangePicker(
                                            id='date-range-picker-demo3',
                                            placeholder=[
                                                '配合自定义format',
                                                ''
                                            ],
                                            format='YYYY年MM月DD日',
                                            style={
                                                'width': 300
                                            },
                                        ),
                                        fac.AntdText(
                                            id='date-range-picker-demo3-output'
                                        )
                                    ],
                                    align='center'
                                ),
                            ],
                            direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdDateRangePicker(
                    id='date-range-picker-demo1',
                    style={
                        'width': 300
                    },
                ),
                fac.AntdText(
                    id='date-range-picker-demo1-output'
                )
            ],
            align='center'
        ),

        fac.AntdSpace(
            [
                fac.AntdDateRangePicker(
                    id='date-range-picker-demo2',
                    placeholder=[
                        '开始日期时间',
                        '结束日期时间'
                    ],
                    style={
                        'width': 350
                    },
                    showTime=True
                ),
                fac.AntdText(
                    id='date-range-picker-demo2-output'
                )
            ],
            align='center'
        ),

        fac.AntdSpace(
            [
                fac.AntdDateRangePicker(
                    id='date-range-picker-demo3',
                    placeholder=[
                        '配合自定义format',
                        ''
                    ],
                    format='YYYY年MM月DD日',
                    style={
                        'width': 300
                    },
                ),
                fac.AntdText(
                    id='date-range-picker-demo3-output'
                )
            ],
            align='center'
        ),
    ],
    direction='vertical'
)

...


@app.callback(
    Output('date-range-picker-demo1-output', 'children'),
    Input('date-range-picker-demo1', 'value')
)
def date_range_picker_demo1(value):

    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo2-output', 'children'),
    Input('date-range-picker-demo2', 'value')
)
def date_range_picker_demo2(value):

    return f'value: {value}'


@app.callback(
    Output('date-range-picker-demo3-output', 'children'),
    Input('date-range-picker-demo3', 'value')
)
def date_range_picker_demo3(value):

    return f'value: {value}'
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
                'flex': 'auto',
                'padding': '25px'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '基础使用', 'href': '#基础使用'},
                    {'title': '不同的悬浮层展开方位', 'href': '#不同的悬浮层展开方位'},
                    {'title': '不同的日期范围选择粒度', 'href': '#不同的日期范围选择粒度'},
                    {'title': '自定义format', 'href': '#自定义format'},
                    {'title': '禁用状态', 'href': '#禁用状态'},
                    {'title': '只读状态', 'href': '#只读状态'},
                    {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                    {'title': '初始化停留日期位置', 'href': '#初始化停留日期位置'},
                    {'title': '自定义日期禁用策略', 'href': '#自定义日期禁用策略'},
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
            component_name='AntdDateRangePicker'
        )
    ],
    style={
        'display': 'flex'
    }
)
