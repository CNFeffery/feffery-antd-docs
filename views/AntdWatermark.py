from dash import html
import feffery_markdown_components as fmc
import feffery_antd_components as fac
import feffery_utils_components as fuc

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdWatermark(children, id, className, style, *args, **kwargs)',
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
                    markdownStr=open('documents/AntdWatermark.md', encoding='utf-8').read()
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
                        fac.AntdWatermark(
                            html.Div(
                                style={
                                    'height': '500px',
                                    'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                    'marginBottom': '25px'
                                }
                            ),
                            content='水印内容测试',
                            fontSize=28
                        ),

                        fac.AntdWatermark(
                            html.Div(
                                fac.AntdForm(
                                    [
                                        fac.AntdFormItem(
                                            fac.AntdInput(
                                                autoComplete='off'
                                            ),
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
                                style={
                                    'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                    'padding': '25px'
                                }
                            ),
                            content='水印内容测试',
                            fontSize=22,
                            rotate=22,
                            gapX=50,
                            gapY=50
                        ),

                        fac.AntdDivider(
                            '基础使用',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　'),
                                fac.AntdText('AntdWatermark', code=True),
                                fac.AntdText('可为嵌套进其中的子元素覆盖上自定义水印文字内容，适用于敏感信息页面的防泄密')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdWatermark(
    html.Div(
        style={
            'height': '500px',
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'marginBottom': '25px'
        }
    ),
    content='水印内容测试',
    fontSize=28
),

fac.AntdWatermark(
    html.Div(
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdInput(
                        autoComplete='off'
                    ),
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
        style={
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'padding': '25px'
        }
    ),
    content='水印内容测试',
    fontSize=22,
    rotate=22,
    gapX=50,
    gapY=50
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
                    id='基础使用',
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
                            {'title': '基础使用', 'href': '#基础使用'},
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
