from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdInput
from .side_props import render_side_props_layout


def docs_content(language: str = '中文'):

    return html.Div(
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
                                'title': 'AntdInput 输入框'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供不同形式的文本信息录入功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        placeholder='mode="default"（默认）'
                                    ),

                                    fac.AntdInput(
                                        placeholder='mode="search"',
                                        mode='search'
                                    ),

                                    fac.AntdInput(
                                        placeholder='mode="text-area"',
                                        mode='text-area'
                                    ),

                                    fac.AntdInput(
                                        placeholder='mode="password"',
                                        mode='password'
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '350px'
                                }
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
        fac.AntdInput(
            placeholder='mode="default"（默认）'
        ),

        fac.AntdInput(
            placeholder='mode="search"',
            mode='search'
        ),

        fac.AntdInput(
            placeholder='mode="text-area"',
            mode='text-area'
        ),

        fac.AntdInput(
            placeholder='mode="password"',
            mode='password'
        )
    ],
    direction='vertical',
    style={
        'width': '350px'
    }
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
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        addonBefore='前缀元素示例',
                                        addonAfter='后缀元素示例',
                                        style={
                                            'width': 300
                                        }
                                    ),

                                    fac.AntdInput(
                                        addonBefore=fac.AntdSelect(
                                            defaultValue='http://',
                                            options=[
                                                {
                                                    'label': option,
                                                    'value': option
                                                }
                                                for option in [
                                                    'http://', 'https://'
                                                ]
                                            ],
                                            allowClear=False
                                        ),
                                        addonAfter=fac.AntdSelect(
                                            defaultValue='.com',
                                            options=[
                                                {
                                                    'label': option,
                                                    'value': option
                                                }
                                                for option in [
                                                    '.com', '.cn'
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

                            fac.AntdParagraph(
                                [
                                    '　　针对默认模式下的输入框，可以通过参数',
                                    fac.AntdText(
                                        'addonBefore',
                                        strong=True
                                    ),
                                    '、',
                                    fac.AntdText(
                                        'addonAfter',
                                        strong=True
                                    ),
                                    '为输入框添加前后置额外内容，实现功能的一体化'
                                ]
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
        fac.AntdInput(
            addonBefore='前缀元素示例',
            addonAfter='后缀元素示例',
            style={
                'width': 300
            }
        ),

        fac.AntdInput(
            addonBefore=fac.AntdSelect(
                defaultValue='http://',
                options=[
                    {
                        'label': option,
                        'value': option
                    }
                    for option in [
                        'http://', 'https://'
                    ]
                ],
                allowClear=False
            ),
            addonAfter=fac.AntdSelect(
                defaultValue='.com',
                options=[
                    {
                        'label': option,
                        'value': option
                    }
                    for option in [
                        '.com', '.cn'
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
                                isOpen=False,
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
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        prefix=fac.AntdIcon(
                                            icon='antd-user'
                                        ),
                                        placeholder='请输入用户名',
                                        style={
                                            'width': 200
                                        }
                                    ),

                                    fac.AntdInput(
                                        suffix=fac.AntdIcon(
                                            icon='antd-lock'
                                        ),
                                        placeholder='请输入密码',
                                        style={
                                            'width': 200
                                        }
                                    )
                                ],
                                direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdInput(
            prefix=fac.AntdIcon(
                icon='antd-user'
            ),
            placeholder='请输入用户名',
            style={
                'width': 200
            }
        ),

        fac.AntdInput(
            suffix=fac.AntdIcon(
                icon='antd-lock'
            ),
            placeholder='请输入密码',
            style={
                'width': 200
            }
        )
    ],
    direction='vertical'
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
                        id='添加内嵌前后缀元素',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '以maxLength=10为例',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        mode=mode,
                                        maxLength=10,
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for mode in [
                                        'default', 'search', 'text-area', 'password'
                                    ]
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '限制输入框最大内容长度',
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
    '以maxLength=10为例',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdInput(
            mode=mode,
            maxLength=10,
            style={
                'width': 200
            }
        )
        for mode in [
            'default', 'search', 'text-area', 'password'
        ]
    ],
    direction='vertical'
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
                        id='限制输入框最大内容长度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdInput(
                                mode='text-area',
                                showCount=True,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '展示已输入文字数量',
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
fac.AntdInput(
    mode='text-area',
    showCount=True,
    style={
        'width': 200
    }
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
                        id='展示已输入文字数量',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdInput(
                                value='Some demo words.',
                                mode='text-area',
                                showCount=True,
                                countFormat='[a-zA-Z]+',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '自定义文字计数规则',
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
fac.AntdInput(
    value='Some demo words.',
    mode='text-area',
    showCount=True,
    countFormat='[a-zA-Z]+',
    style={
        'width': 200
    }
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
                        id='自定义文字计数规则',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'autoSize=False（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdInput(
                                mode='text-area',
                                defaultValue='示例内容'*20,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'autoSize=True',
                                innerTextOrientation='left'
                            ),
                            fac.AntdInput(
                                mode='text-area',
                                defaultValue='示例内容'*20,
                                autoSize=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '配置minRows、maxRows参数',
                                innerTextOrientation='left'
                            ),
                            fac.AntdInput(
                                mode='text-area',
                                defaultValue='示例内容'*20,
                                autoSize={
                                    'minRows': 2,
                                    'maxRows': 3
                                },
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                '文本域输入框自适应高度',
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
    'autoSize=False（默认）',
    innerTextOrientation='left'
),
fac.AntdInput(
    mode='text-area',
    defaultValue='示例内容'*20,
    style={
        'width': 300
    }
),

fac.AntdDivider(
    'autoSize=True',
    innerTextOrientation='left'
),
fac.AntdInput(
    mode='text-area',
    defaultValue='示例内容'*20,
    autoSize=True,
    style={
        'width': 300
    }
),

fac.AntdDivider(
    '配置minRows、maxRows参数',
    innerTextOrientation='left'
),
fac.AntdInput(
    mode='text-area',
    defaultValue='示例内容'*20,
    autoSize={
        'minRows': 2,
        'maxRows': 3
    },
    style={
        'width': 300
    }
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
                        id='文本域输入框自适应高度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        mode=mode,
                                        disabled=True,
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for mode in [
                                        'default', 'search', 'text-area', 'password'
                                    ]
                                ],
                                direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdInput(
            mode=mode,
            disabled=True,
            style={
                'width': 200
            }
        )
        for mode in [
            'default', 'search', 'text-area', 'password'
        ]
    ],
    direction='vertical'
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        mode=mode,
                                        readOnly=True,
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for mode in [
                                        'default', 'search', 'text-area', 'password'
                                    ]
                                ],
                                direction='vertical'
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
fac.AntdSpace(
    [
        fac.AntdInput(
            mode=mode,
            readOnly=True,
            style={
                'width': 200
            }
        )
        for mode in [
            'default', 'search', 'text-area', 'password'
        ]
    ],
    direction='vertical'
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
                        id='只读状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'status="warning"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        mode=mode,
                                        status='warning',
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for mode in [
                                        'default', 'search', 'text-area', 'password'
                                    ]
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                'status="error"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        mode=mode,
                                        status='error',
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for mode in [
                                        'default', 'search', 'text-area', 'password'
                                    ]
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
fac.AntdDivider(
    'status="warning"',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdInput(
            mode=mode,
            status='warning',
            style={
                'width': 200
            }
        )
        for mode in [
            'default', 'search', 'text-area', 'password'
        ]
    ],
    direction='vertical'
),

fac.AntdDivider(
    'status="error"',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdInput(
            mode=mode,
            status='error',
            style={
                'width': 200
            }
        )
        for mode in [
            'default', 'search', 'text-area', 'password'
        ]
    ],
    direction='vertical'
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
                        id='强制状态渲染',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdInput(
                                        id=f'input-{mode}-mode-demo',
                                        mode=mode,
                                        maxLength=10,
                                        style={
                                            'width': 300
                                        }
                                    )
                                    for mode in [
                                        'default', 'search', 'text-area', 'password'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            html.Div(
                                id='input-demo-output'
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
        fac.AntdInput(
            id=f'input-{mode}-mode-demo',
            mode=mode,
            maxLength=10,
            style={
                'width': 300
            }
        )
        for mode in [
            'default', 'search', 'text-area', 'password'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
),

html.Div(
    id='input-demo-output'
)

...

@app.callback(
    Output('input-demo-output', 'children'),
    [Input(f'input-{mode}-mode-demo', 'value')
     for mode in ['default', 'search', 'text-area', 'password']]
)
def input_mode_demo(*value_list):

    return fac.AntdSpace(
        [
            fac.AntdText(
                f'{mode}模式value：{value_list[i]}'
            )
            for i, mode in enumerate(
                ['default', 'search', 'text-area', 'password']
            )
        ],
        direction='vertical'
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
                        id='回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdInput(
                                id='input-debounce-demo',
                                debounceWait=500,
                                maxLength=10,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdParagraph(
                                id='input-debounce-demo-output'
                            ),

                            fac.AntdDivider(
                                '防抖回调示例',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '　　在回调函数中用',
                                    fac.AntdText(
                                        'debounceValue',
                                        strong=True
                                    ),
                                    '代替',
                                    fac.AntdText(
                                        'value',
                                        strong=True
                                    ),
                                    '可以实现对用户实时输入值变化的防抖监听，避免回调函数被频繁触发执行'
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdInput(
    id='input-debounce-demo',
    debounceWait=500,
    maxLength=10,
    style={
        'width': 200
    }
),

fac.AntdParagraph(
    id='input-debounce-demo-output'
)

...

@app.callback(
    Output('input-debounce-demo-output', 'children'),
    Input('input-debounce-demo', 'debounceValue')
)
def input_debounce_demo(debounceValue):

    return f'debounceValue: {debounceValue}'
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
                        id='防抖回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdInput(
                                id='input-enter-demo',
                                placeholder='聚焦于此后按下enter',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdParagraph(
                                id='input-enter-demo-output'
                            ),

                            fac.AntdDivider(
                                '监听输入框内enter键盘事件',
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
fac.AntdInput(
    id='input-enter-demo',
    placeholder='聚焦于此后按下enter',
    style={
        'width': 200
    }
),

fac.AntdParagraph(
    id='input-enter-demo-output'
)

...

@app.callback(
    Output('input-enter-demo-output', 'children'),
    Input('input-enter-demo', 'nSubmit')
)
def input_enter_dmeo(nSubmit):

    return f'nSubmit: {nSubmit}'
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
                        id='监听输入框内enter键盘事件',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdInput(
                                id='input-search-demo',
                                placeholder='点击右侧搜索按钮',
                                mode='search',
                                style={
                                    'width': 220
                                }
                            ),

                            fac.AntdParagraph(
                                id='input-search-demo-output'
                            ),

                            fac.AntdDivider(
                                '监听搜索按钮点击事件',
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
fac.AntdInput(
    id='input-search-demo',
    placeholder='点击右侧搜索按钮',
    mode='search',
    style={
        'width': 220
    }
),

fac.AntdParagraph(
    id='input-search-demo-output'
)

...

@app.callback(
    Output('input-search-demo-output', 'children'),
    Input('input-search-demo', 'nClicksSearch')
)
def input_search_dmeo(nClicksSearch):

    return f'nClicksSearch: {nClicksSearch}'
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
                        id='监听搜索按钮点击事件',
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
                        {'title': '限制输入框最大内容长度', 'href': '#限制输入框最大内容长度'},
                        {'title': '展示已输入文字数量', 'href': '#展示已输入文字数量'},
                        {'title': '自定义文字计数规则', 'href': '#自定义文字计数规则'},
                        {'title': '文本域输入框自适应高度', 'href': '#文本域输入框自适应高度'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                        {'title': '回调示例', 'href': '#回调示例'},
                        {'title': '防抖回调示例', 'href': '#防抖回调示例'},
                        {'title': '监听输入框内enter键盘事件', 'href': '#监听输入框内enter键盘事件'},
                        {'title': '监听搜索按钮点击事件', 'href': '#监听搜索按钮点击事件'},
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
                component_name='AntdInput',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
