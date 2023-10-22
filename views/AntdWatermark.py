from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

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
                                'title': '其他'
                            },
                            {
                                'title': 'AntdWatermark 水印'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于在指定内容上叠加水印内容。')
                        ]
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

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
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
                            fac.AntdWatermark(
                                html.Div(
                                    style={
                                        'height': '500px',
                                        'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
                                        'marginBottom': '25px'
                                    }
                                ),
                                content=[
                                    '第一行水印',
                                    '第二行水印',
                                    '第三行水印'
                                ],
                                fontSize=28
                            ),

                            fac.AntdDivider(
                                '多行文字水印',
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
fac.AntdWatermark(
    html.Div(
        style={
            'height': '500px',
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'marginBottom': '25px'
        }
    ),
    content=[
        '第一行水印',
        '第二行水印',
        '第三行水印'
    ],
    fontSize=28
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
                        id='多行文字水印',
                        className='div-highlight'
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
                                image='assets/imgs/fac-logo.svg',
                                width=48,
                                height=48,
                                rotate=0
                            ),

                            fac.AntdDivider(
                                '图片型水印',
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
fac.AntdWatermark(
    html.Div(
        style={
            'height': '500px',
            'boxShadow': '0 6px 16px rgb(107 147 224 / 14%)',
            'marginBottom': '25px'
        }
    ),
    image='assets/imgs/fac-logo.svg',
    width=48,
    height=48,
    rotate=0
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
                        id='图片型水印',
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
                        {'title': '多行文字水印', 'href': '#多行文字水印'},
                        {'title': '图片型水印', 'href': '#图片型水印'},
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
                component_name='AntdWatermark',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
