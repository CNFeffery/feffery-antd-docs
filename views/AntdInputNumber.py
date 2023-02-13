from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

# import callbacks.AntdButton
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
                            '添加内嵌前后缀元素',
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
                    id='添加内嵌前后缀元素',
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
                    {'title': '添加内嵌前后缀元素', 'href': '#添加内嵌前后缀元素'},
                    {'title': '限制上下限', 'href': '#限制上下限'},
                    {'title': '设置指定步长', 'href': '#设置指定步长'},
                    {'title': '设置指定精度', 'href': '#设置指定精度'},
                    {'title': '高精度模式', 'href': '#高精度模式'},
                    {'title': '禁用状态', 'href': '#禁用状态'},
                    {'title': '只读状态', 'href': '#只读状态'},
                    {'title': '强制状态渲染', 'href': '#强制状态渲染'},
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
