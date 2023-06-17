from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdForm
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
                                'title': '表单'
                            },
                            {
                                'title': 'AntdForm 表单'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            '　　用于通过嵌套若干',
                            fac.AntdText('AntdFormItem', strong=True),
                            '的方式构建现代化表单。'
                        ]
                    ),

                    html.Div(
                        [
                            html.Div(
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
                                        'span': 20
                                    },
                                    style={
                                        'width': '300px',
                                        'margin': '0 auto'  # 以快捷实现居中布局效果
                                    }
                                )
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
html.Div(
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
            'span': 20
        },
        style={
            'width': '300px',
            'margin': '0 auto'  # 以快捷实现居中布局效果
        }
    )
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
                            fac.AntdDivider(
                                'layout="vertical"',
                                innerTextOrientation='left'
                            ),
                            html.Div(
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
                                    layout='vertical',
                                    style={
                                        'width': 300,
                                        'margin': '0 auto'
                                    }
                                )
                            ),

                            fac.AntdDivider(
                                'layout="inline"',
                                innerTextOrientation='left'
                            ),
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
                                layout='inline',
                                style={
                                    'justifyContent': 'center'
                                }
                            ),

                            fac.AntdDivider(
                                '其他布局模式',
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
    'layout="vertical"',
    innerTextOrientation='left'
),
html.Div(
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
        layout='vertical',
        style={
            'width': 300,
            'margin': '0 auto'
        }
    )
),

fac.AntdDivider(
    'layout="inline"',
    innerTextOrientation='left'
),
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
    layout='inline',
    style={
        'justifyContent': 'center'
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
                        id='其他布局模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            html.Div(
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
                                        'span': 20
                                    },
                                    labelAlign='left',
                                    style={
                                        'width': 300,
                                        'margin': '0 auto'
                                    }
                                )
                            ),

                            fac.AntdDivider(
                                '表单项标签左对齐',
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
html.Div(
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
            'span': 20
        },
        labelAlign='left',
        style={
            'width': 300,
            'margin': '0 auto'
        }
    )
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
                        id='表单项标签左对齐',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            html.Div(
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
                                                'offset': 5
                                            }
                                        )
                                    ],
                                    labelCol={
                                        'span': 5
                                    },
                                    wrapperCol={
                                        'span': 19
                                    },
                                    style={
                                        'width': 300,
                                        'margin': '0 auto'
                                    }
                                )
                            ),

                            fac.AntdDivider(
                                '添加必填项标识',
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
html.Div(
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
                    'offset': 5
                }
            )
        ],
        labelCol={
            'span': 5
        },
        wrapperCol={
            'span': 19
        },
        style={
            'width': 300,
            'margin': '0 auto'
        }
    )
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
                        id='添加必填项标识',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            html.Div(
                                fac.AntdForm(
                                    [
                                        fac.AntdFormItem(
                                            fac.AntdInput(),
                                            label='用户名',
                                            tooltip='输入您的用户名信息'
                                        ),
                                        fac.AntdFormItem(
                                            fac.AntdInput(
                                                mode='password'
                                            ),
                                            label='密码',
                                            tooltip='输入您的账户密码信息'
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
                                        'span': 6
                                    },
                                    wrapperCol={
                                        'span': 18
                                    },
                                    style={
                                        'width': 300,
                                        'margin': '0 auto'
                                    }
                                )
                            ),

                            fac.AntdDivider(
                                '添加额外提示信息框',
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
html.Div(
    fac.AntdForm(
        [
            fac.AntdFormItem(
                fac.AntdInput(),
                label='用户名',
                tooltip='输入您的用户名信息'
            ),
            fac.AntdFormItem(
                fac.AntdInput(
                    mode='password'
                ),
                label='密码',
                tooltip='输入您的账户密码信息'
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
            'span': 20
        },
        style={
            'width': 300,
            'margin': '0 auto'
        }
    )
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
                        id='添加额外提示信息框',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdForm(
                                [
                                    fac.AntdFormItem(
                                        fac.AntdRadioGroup(
                                            id='form-item-status-switch',
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
                                        id='form-item-status-demo',
                                        label='用户名'
                                    )
                                ],
                                labelCol={
                                    'span': 4
                                },
                                wrapperCol={
                                    'span': 20
                                },
                                style={
                                    'width': 500,
                                    'margin': '0 auto'
                                }
                            ),

                            fac.AntdDivider(
                                '不同的校验状态',
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
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdRadioGroup(
                id='form-item-status-switch',
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
            id='form-item-status-demo',
            label='用户名'
        )
    ],
    labelCol={
        'span': 4
    },
    wrapperCol={
        'span': 20
    },
    style={
        'width': 500,
        'margin': '0 auto'
    }
)

...

@app.callback(
    [Output('form-item-status-demo', 'validateStatus'),
     Output('form-item-status-demo', 'help')],
    Input('form-item-status-switch', 'value')
)
def form_item_status_demo(value):
    if not value or value == 'None':
        return None, None

    return value, f'validateStatus="{value}"'
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
                        id='不同的校验状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
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
                                                fac.AntdInput(
                                                    id='form-item-validate-demo-username'
                                                ),
                                                id='form-item-validate-demo-username-container',
                                                label='用户名'
                                            ),
                                            fac.AntdFormItem(
                                                fac.AntdInput(
                                                    id='form-item-validate-demo-password',
                                                    mode='password'
                                                ),
                                                id='form-item-validate-demo-password-container',
                                                label='密码'
                                            ),
                                            fac.AntdFormItem(
                                                fac.AntdButton(
                                                    '登录',
                                                    id='form-item-validate-demo-submit',
                                                    type='primary'
                                                )
                                            )
                                        ],
                                        layout='vertical'
                                    )
                                ],
                                style={
                                    'width': 400,
                                    'margin': '0 auto'
                                }
                            ),

                            fac.AntdDivider(
                                '基于回调的状态校验示例',
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
                    fac.AntdInput(
                        id='form-item-validate-demo-username'
                    ),
                    id='form-item-validate-demo-username-container',
                    label='用户名'
                ),
                fac.AntdFormItem(
                    fac.AntdInput(
                        id='form-item-validate-demo-password',
                        mode='password'
                    ),
                    id='form-item-validate-demo-password-container',
                    label='密码'
                ),
                fac.AntdFormItem(
                    fac.AntdButton(
                        '登录',
                        id='form-item-validate-demo-submit',
                        type='primary'
                    )
                )
            ],
            layout='vertical'
        )
    ],
    style={
        'width': 400,
        'margin': '0 auto'
    }
)

...

@app.callback(
    [Output('form-item-validate-demo-username-container', 'validateStatus'),
     Output('form-item-validate-demo-password-container', 'validateStatus'),
     Output('form-item-validate-demo-username-container', 'help'),
     Output('form-item-validate-demo-password-container', 'help')],
    Input('form-item-validate-demo-submit', 'nClicks'),
    [State('form-item-validate-demo-username', 'value'),
     State('form-item-validate-demo-password', 'value')],
    prevent_initial_call=True
)
def form_item_validate_demo(nClicks, username, password):

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
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id='基于回调的状态校验示例',
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
                        {'title': '其他布局模式', 'href': '#其他布局模式'},
                        {'title': '表单项标签左对齐', 'href': '#表单项标签左对齐'},
                        {'title': '添加必填项标识', 'href': '#添加必填项标识'},
                        {'title': '添加额外提示信息框', 'href': '#添加额外提示信息框'},
                        {'title': '不同的校验状态', 'href': '#不同的校验状态'},
                        {'title': '基于回调的状态校验示例', 'href': '#基于回调的状态校验示例'},
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
                component_name='AntdForm',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
