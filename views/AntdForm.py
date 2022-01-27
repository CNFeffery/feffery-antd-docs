from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.AntdForm

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdForm(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdForm.md', encoding='utf-8').read()
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

                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdCheckbox(
                                        label='记住密码'
                                    ),
                                    wrapperCol={
                                        'offset': 4
                                    }
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    ),
                                    wrapperCol={
                                        'offset': 4
                                    }
                                )
                            ],
                            labelCol={
                                'span': 4
                            },
                            wrapperCol={
                                'span': 8
                            }
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　在默认的'),
                                fac.AntdText('layout="horizontal"', code=True),
                                fac.AntdText('布局模式下，我们可以通过妥善使用参数'),
                                fac.AntdText('labelCol', code=True),
                                fac.AntdText('与'),
                                fac.AntdText('wrapperCol', code=True),
                                fac.AntdText('来将若干个表单输入类组件组合为一张经典的表单')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码'
        ),
        fac.AntdFormItem(
            fac.AntdCheckbox(
                label='记住密码'
            ),
            wrapperCol={
                'offset': 4
            }
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            ),
            wrapperCol={
                'offset': 4
            }
        )
    ],
    labelCol={
        'span': 4
    },
    wrapperCol={
        'span': 8
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
                    id='基础使用',
                    className='div-highlight'
                ),

                html.Div(
                    [

                        fac.AntdDivider('layout="vertical"', innerTextOrientation='left'),
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    )
                                )
                            ],
                            wrapperCol={
                                'span': 12
                            },
                            layout='vertical'
                        ),

                        fac.AntdDivider('layout="inline"', innerTextOrientation='left'),
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    )
                                )
                            ],
                            layout='inline'
                        ),

                        fac.AntdDivider(
                            '其他布局模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　布局模式'),
                                fac.AntdText('layout="vertical"', code=True),
                                fac.AntdText('及'),
                                fac.AntdText('layout="inline"', code=True),
                                fac.AntdText('属于特殊布局模式，部分参数的效果与'),
                                fac.AntdText('layout="horizontal"', code=True),
                                fac.AntdText('模式有所不同')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True,
                                showInlineLineNumbers=True,
                                language='python',
                                codeStyle='coy-without-shadows',
                                codeString='''
fac.AntdDivider('layout="vertical"', innerTextOrientation='left'),
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码'
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            )
        )
    ],
    wrapperCol={
        'span': 12
    },
    layout='vertical'
),

fac.AntdDivider('layout="inline"', innerTextOrientation='left'),
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码'
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            )
        )
    ],
    layout='inline'
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
                    id='其他布局模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    ),
                                    wrapperCol={
                                        'offset': 4
                                    }
                                )
                            ],
                            labelCol={
                                'span': 4
                            },
                            wrapperCol={
                                'span': 8
                            },
                            labelAlign='left'
                        ),

                        fac.AntdDivider(
                            '不同的标签对齐方式',
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
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码'
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            ),
            wrapperCol={
                'offset': 4
            }
        )
    ],
    labelCol={
        'span': 4
    },
    wrapperCol={
        'span': 8
    },
    labelAlign='left'
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
                    id='不同的标签对齐方式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名',
                                    required=True
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码',
                                    required=True
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    ),
                                    wrapperCol={
                                        'offset': 4
                                    }
                                )
                            ],
                            labelCol={
                                'span': 4
                            },
                            wrapperCol={
                                'span': 8
                            }
                        ),

                        fac.AntdDivider(
                            '添加必填标识',
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
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名',
            required=True
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码',
            required=True
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            ),
            wrapperCol={
                'offset': 4
            }
        )
    ],
    labelCol={
        'span': 4
    },
    wrapperCol={
        'span': 8
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
                    id='添加必填标识',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名',
                                    tooltip='这个输入框用于输入用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码',
                                    tooltip='这个输入框用于输入密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    ),
                                    wrapperCol={
                                        'offset': 4
                                    }
                                )
                            ],
                            labelCol={
                                'span': 4
                            },
                            wrapperCol={
                                'span': 8
                            }
                        ),

                        fac.AntdDivider(
                            '添加鼠标悬浮提示信息',
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
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名',
            tooltip='这个输入框用于输入用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码',
            tooltip='这个输入框用于输入密码'
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            ),
            wrapperCol={
                'offset': 4
            }
        )
    ],
    labelCol={
        'span': 4
    },
    wrapperCol={
        'span': 8
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
                    id='添加鼠标悬浮提示信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(),
                                    label='用户名',
                                    extra='提示：这个输入框用于输入用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        mode='password'
                                    ),
                                    label='密码',
                                    extra='提示：这个输入框用于输入密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        type='primary'
                                    ),
                                    wrapperCol={
                                        'offset': 4
                                    }
                                )
                            ],
                            labelCol={
                                'span': 4
                            },
                            wrapperCol={
                                'span': 8
                            }
                        ),

                        fac.AntdDivider(
                            '添加额外提示信息',
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
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(),
            label='用户名',
            extra='提示：这个输入框用于输入用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                mode='password'
            ),
            label='密码',
            extra='提示：这个输入框用于输入密码'
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                type='primary'
            ),
            wrapperCol={
                'offset': 4
            }
        )
    ],
    labelCol={
        'span': 4
    },
    wrapperCol={
        'span': 8
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
                    id='添加额外提示信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdForm(
                                [
                                    fac.AntdFormItem(
                                        fac.AntdRadioGroup(
                                            id='form-demo-1-status',
                                            options=[
                                                {
                                                    'label': 'None',
                                                    'value': 'None'
                                                },
                                                {
                                                    'label': 'success',
                                                    'value': 'success',
                                                },
                                                {
                                                    'label': 'warning',
                                                    'value': 'warning',
                                                },
                                                {
                                                    'label': 'error',
                                                    'value': 'error',
                                                },
                                                {
                                                    'label': 'validating',
                                                    'value': 'validating',
                                                }
                                            ],
                                            optionType='button',
                                            defaultValue='None'
                                        ),
                                        label='切换状态'
                                    ),
                                    fac.AntdFormItem(
                                        fac.AntdInput(),
                                        id='form-demo-1',
                                        label='用户名'
                                    )
                                ],
                                labelCol={
                                    'span': 4
                                },
                                wrapperCol={
                                    'span': 8
                                }
                            ),
                            text='回调中',
                            delay=300
                        ),

                        fac.AntdDivider(
                            '不同的校验状态',
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
fac.AntdSpin(
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdRadioGroup(
                    id='form-demo-1-status',
                    options=[
                        {
                            'label': 'None',
                            'value': 'None'
                        },
                        {
                            'label': 'success',
                            'value': 'success',
                        },
                        {
                            'label': 'warning',
                            'value': 'warning',
                        },
                        {
                            'label': 'error',
                            'value': 'error',
                        },
                        {
                            'label': 'validating',
                            'value': 'validating',
                        }
                    ],
                    optionType='button',
                    defaultValue='None'
                ),
                label='切换状态'
            ),
            fac.AntdFormItem(
                fac.AntdInput(),
                id='form-demo-1',
                label='用户名'
            )
        ],
        labelCol={
            'span': 4
        },
        wrapperCol={
            'span': 8
        }
    ),
    text='回调中',
    delay=300
)
...
@app.callback(
    [Output('form-demo-1', 'validateStatus'),
     Output('form-demo-1', 'help')],
    Input('form-demo-1-status', 'value')
)
def form_demo_1_callback(value):
    if not value or value == 'None':
        return None, None

    return value, f'validateStatus="{value}"'
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
                    id='不同的校验状态',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdAlert(
                            message='示例用户名：fac  密码：123456 你可以故意输错用户名或密码来查看不同的校验反馈结果',
                            type='info',
                            showIcon=True,
                            messageRenderMode='marquee',
                            style={
                                'marginBottom': '10px'
                            }
                        ),
                        fac.AntdForm(
                            [
                                fac.AntdFormItem(
                                    fac.AntdInput(id='form-validate-demo-username'),
                                    id='form-item-validate-demo-username',
                                    label='用户名'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdInput(
                                        id='form-validate-demo-password',
                                        mode='password'
                                    ),
                                    id='form-item-validate-demo-password',
                                    label='密码'
                                ),
                                fac.AntdFormItem(
                                    fac.AntdButton(
                                        '登录',
                                        id='form-validate-demo-submit',
                                        type='primary'
                                    )
                                )
                            ],
                            labelCol={
                                'offset': 8
                            },
                            wrapperCol={
                                'span': 8,
                                'offset': 8
                            },
                            layout='vertical'
                        ),

                        fac.AntdDivider(
                            '回调状态校验示例',
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
fac.AntdAlert(
    message='示例用户名：fac  密码：123456 你可以故意输错用户名或密码来查看不同的校验反馈结果',
    type='info',
    showIcon=True,
    messageRenderMode='marquee',
    style={
        'marginBottom': '10px'
    }
),
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdInput(id='form-validate-demo-username'),
            id='form-item-validate-demo-username',
            label='用户名'
        ),
        fac.AntdFormItem(
            fac.AntdInput(
                id='form-validate-demo-password',
                mode='password'
            ),
            id='form-item-validate-demo-password',
            label='密码'
        ),
        fac.AntdFormItem(
            fac.AntdButton(
                '登录',
                id='form-validate-demo-submit',
                type='primary'
            )
        )
    ],
    labelCol={
        'offset': 8
    },
    wrapperCol={
        'span': 8,
        'offset': 8
    },
    layout='vertical'
)
...
@app.callback(
    [Output('form-item-validate-demo-username', 'validateStatus'),
     Output('form-item-validate-demo-password', 'validateStatus'),
     Output('form-item-validate-demo-username', 'help'),
     Output('form-item-validate-demo-password', 'help')],
    Input('form-validate-demo-submit', 'nClicks'),
    [State('form-validate-demo-username', 'value'),
     State('form-validate-demo-password', 'value')],
    prevent_initial_call=True
)
def form_demo_2_callback(nClicks, username, password):
    if username and password:
        return [
            None if username == 'fac' else 'error',
            ('success' if password == '123456' else 'error')
            if username == 'fac' else None,
            None if username == 'fac' else '用户不存在！',
            ('密码正确！' if password == '123456' else '密码错误！')
            if username == 'fac' else None
        ]

    return [
        None if username else 'error',
        None if password else 'error',
        None if username else '用户名不能为空！',
        None if password else '密码不能为空！'
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
                    id='回调状态校验示例',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto',
                'width': 0
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
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '其他布局模式', 'href': '#其他布局模式'},
                            {'title': '不同的标签对齐方式', 'href': '#不同的标签对齐方式'},
                            {'title': '添加必填标识', 'href': '#添加必填标识'},
                            {'title': '添加鼠标悬浮提示信息', 'href': '#添加鼠标悬浮提示信息'},
                            {'title': '添加额外提示信息', 'href': '#添加额外提示信息'},
                            {'title': '不同的校验状态', 'href': '#不同的校验状态'},
                            {'title': '回调状态校验示例', 'href': '#回调状态校验示例'},
                        ]
                    },
                ],
                containerId='docs-content',
                targetOffset=200
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
