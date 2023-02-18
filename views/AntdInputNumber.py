from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdInputNumber
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
                            'title': 'AntdInputNumber 数字输入框'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　用于为用户提供纯数字类型的信息录入功能。')
                    ]
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdInputNumber(
                                    size='small',
                                    style={
                                        'width': 150
                                    }
                                ),
                                fac.AntdInputNumber(
                                    style={
                                        'width': 150
                                    }
                                ),
                                fac.AntdInputNumber(
                                    size='large',
                                    style={
                                        'width': 150
                                    }
                                )
                            ],
                            direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdInputNumber(
            size='small',
            style={
                'width': 150
            }
        ),
        fac.AntdInputNumber(
            style={
                'width': 150
            }
        ),
        fac.AntdInputNumber(
            size='large',
            style={
                'width': 150
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdInputNumber(
                                    addonBefore='前缀元素',
                                    addonAfter='后缀元素',
                                    style={
                                        'width': 300
                                    }
                                ),

                                fac.AntdInputNumber(
                                    addonBefore=fac.AntdSelect(
                                        defaultValue='a',
                                        options=[
                                            {
                                                'label': option,
                                                'value': option
                                            }
                                            for option in ['a', 'b']
                                        ],
                                        allowClear=False
                                    ),
                                    addonAfter=fac.AntdSelect(
                                        defaultValue='m',
                                        options=[
                                            {
                                                'label': option,
                                                'value': option
                                            }
                                            for option in [
                                                'mm', 'cm', 'dm', 'm'
                                            ]
                                        ],
                                        allowClear=False
                                    ),
                                    style={
                                        'width': 300
                                    }
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '添加前后置额外元素',
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
        fac.AntdInputNumber(
            addonBefore='前缀元素',
            addonAfter='后缀元素',
            style={
                'width': 300
            }
        ),

        fac.AntdInputNumber(
            addonBefore=fac.AntdSelect(
                defaultValue='a',
                options=[
                    {
                        'label': option,
                        'value': option
                    }
                    for option in ['a', 'b']
                ],
                allowClear=False
            ),
            addonAfter=fac.AntdSelect(
                defaultValue='m',
                options=[
                    {
                        'label': option,
                        'value': option
                    }
                    for option in [
                        'mm', 'cm', 'dm', 'm'
                    ]
                ],
                allowClear=False
            ),
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
                    id='添加前后置额外元素',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            prefix=fac.AntdIcon(
                                icon='antd-control'
                            ),
                            style={
                                'width': 200
                            }
                        ),

                        fac.AntdDivider(
                            '添加内嵌前缀元素',
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
fac.AntdInputNumber(
    prefix=fac.AntdIcon(
        icon='antd-control'
    ),
    style={
        'width': 200
    }
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
                    id='添加内嵌前缀元素',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            min=0,
                            max=100,
                            placeholder='请尝试输入0~100以外的数值查看效果',
                            style={
                                'width': 275
                            }
                        ),

                        fac.AntdDivider(
                            '限制上下限',
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
fac.AntdInputNumber(
    min=0,
    max=100,
    placeholder='请尝试输入0~100以外的数值查看效果',
    style={
        'width': 275
    }
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
                    id='限制上下限',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdInputNumber(
                                    step=0.1,
                                    defaultValue=0,
                                    placeholder='step=0.1'
                                ),

                                fac.AntdInputNumber(
                                    step=0.001,
                                    defaultValue=0,
                                    placeholder='step=0.001'
                                )
                            ],
                            direction='vertical'
                        ),

                        fac.AntdDivider(
                            '设置指定步长',
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
        fac.AntdInputNumber(
            step=0.1,
            defaultValue=0,
            placeholder='step=0.1'
        ),

        fac.AntdInputNumber(
            step=0.001,
            defaultValue=0,
            placeholder='step=0.001'
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
                    id='设置指定步长',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            precision=5,
                            placeholder='precision=5',
                            style={
                                'width': 150
                            }
                        ),

                        fac.AntdDivider(
                            '设置指定精度',
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
fac.AntdInputNumber(
    precision=5,
    placeholder='precision=5',
    style={
        'width': 150
    }
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
                    id='设置指定精度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            stringMode=True,
                            defaultValue='0.1312312314124123124124123123123312312321312312312312',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '高精度模式',
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
fac.AntdInputNumber(
    stringMode=True,
    defaultValue='0.1312312314124123124124123123123312312321312312312312',
    style={
        'width': '100%'
    }
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
                    id='高精度模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            disabled=True,
                            style={
                                'width': 150
                            }
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
fac.AntdInputNumber(
    disabled=True,
    style={
        'width': 150
    }
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
                        fac.AntdInputNumber(
                            defaultValue=3.1415926,
                            readOnly=True,
                            style={
                                'width': 150
                            }
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
fac.AntdInputNumber(
    defaultValue=3.1415926,
    readOnly=True,
    style={
        'width': 150
    }
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
                                fac.AntdInputNumber(
                                    defaultValue=3.1415926,
                                    status='warning',
                                    style={
                                        'width': 150
                                    }
                                ),

                                fac.AntdInputNumber(
                                    defaultValue=3.1415926,
                                    status='error',
                                    style={
                                        'width': 150
                                    }
                                )
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
        fac.AntdInputNumber(
            defaultValue=3.1415926,
            status='warning',
            style={
                'width': 150
            }
        ),

        fac.AntdInputNumber(
            defaultValue=3.1415926,
            status='error',
            style={
                'width': 150
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
                    id='强制状态渲染',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdInputNumber(
                            id='input-number-demo',
                            defaultValue=0.999,
                            style={
                                'width': 200
                            }
                        ),

                        fac.AntdParagraph(
                            id='input-number-demo-output'
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
fac.AntdInputNumber(
    id='input-number-demo',
    defaultValue=0.999,
    style={
        'width': 200
    }
),

fac.AntdParagraph(
    id='input-number-demo-output'
)

...

@app.callback(
    Output('input-number-demo-output', 'children'),
    Input('input-number-demo', 'value')
)
def input_number_demo(value):

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

                html.Div(
                    [
                        fac.AntdInputNumber(
                            id='input-number-debounce-demo',
                            defaultValue=0.999,
                            debounceWait=500,
                            style={
                                'width': 200
                            }
                        ),

                        fac.AntdParagraph(
                            id='input-number-debounce-demo-output'
                        ),

                        fac.AntdDivider(
                            '防抖回调示例',
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
fac.AntdInputNumber(
    id='input-number-debounce-demo',
    defaultValue=0.999,
    debounceWait=500,
    style={
        'width': 200
    }
),

fac.AntdParagraph(
    id='input-number-debounce-demo-output'
)

...

@app.callback(
    Output('input-number-debounce-demo-output', 'children'),
    Input('input-number-debounce-demo', 'debounceValue')
)
def input_number_debounce_demo(debounceValue):

    return f'debounceValue: {debounceValue}'
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
                    id='防抖回调示例',
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
                    {'title': '添加前后置额外元素', 'href': '#添加前后置额外元素'},
                    {'title': '添加内嵌前缀元素', 'href': '#添加内嵌前缀元素'},
                    {'title': '限制上下限', 'href': '#限制上下限'},
                    {'title': '设置指定步长', 'href': '#设置指定步长'},
                    {'title': '设置指定精度', 'href': '#设置指定精度'},
                    {'title': '高精度模式', 'href': '#高精度模式'},
                    {'title': '禁用状态', 'href': '#禁用状态'},
                    {'title': '只读状态', 'href': '#只读状态'},
                    {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                    {'title': '回调示例', 'href': '#回调示例'},
                    {'title': '防抖回调示例', 'href': '#防抖回调示例'},
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
            component_name='AntdInputNumber'
        )
    ],
    style={
        'display': 'flex'
    }
)
