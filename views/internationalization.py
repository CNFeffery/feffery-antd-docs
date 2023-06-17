from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc


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
                                'title': '进阶使用'
                            },
                            {
                                'title': '国际化'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                'fac',
                                strong=True
                            ),
                            '针对部分组件，具有切换组件自带文案信息语种的功能，基于相关组件的参数',
                            fac.AntdText(
                                'locale',
                                code=True
                            ),
                            '（默认为',
                            fac.AntdText(
                                '"zh-cn"',
                                code=True
                            ),
                            '，即简体中文），也可以设置为',
                            fac.AntdText(
                                '"en-us"',
                                code=True
                            ),
                            '切换到英文文案模式，典型例子如下：'
                        ],
                        style={
                            'textIndent': '2rem'
                        }
                    ),

                    fac.AntdForm(
                        [
                            fac.AntdFormItem(
                                fac.AntdSpace(
                                    [
                                        fac.AntdDatePicker(),
                                        fac.AntdDateRangePicker()
                                    ]
                                ),
                                label='locale="zh-cn"（默认）'
                            ),

                            fac.AntdFormItem(
                                fac.AntdSpace(
                                    [
                                        fac.AntdDatePicker(
                                            locale='en-us'
                                        ),
                                        fac.AntdDateRangePicker(
                                            locale='en-us'
                                        )
                                    ]
                                ),
                                label='locale="en-us"'
                            )
                        ],
                        layout='vertical'
                    ),

                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString='''
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdSpace(
                [
                    fac.AntdDatePicker(),
                    fac.AntdDateRangePicker()
                ]
            ),
            label='locale="zh-cn"（默认）'
        ),

        fac.AntdFormItem(
            fac.AntdSpace(
                [
                    fac.AntdDatePicker(
                        locale='en-us'
                    ),
                    fac.AntdDateRangePicker(
                        locale='en-us'
                    )
                ]
            ),
            label='locale="en-us"'
        )
    ],
    layout='vertical'
)
'''
                    ),

                    fac.AntdParagraph(
                        [
                            '上面介绍的例子是针对每个组件单独控制语种，而如果你的应用中存在着大量的需要设置为其他语种的组件，则可以将相关组件全部嵌套在全局配置组件',
                            fac.AntdText(
                                'AntdConfigProvider',
                                strong=True
                            ),
                            '中，并为其设置参数',
                            fac.AntdText(
                                'locale="en-us"',
                                code=True
                            ),
                            '，从而批量快捷覆盖设置内部元素的国际化语种',
                            '（更多内容请参考',
                            html.A(
                                'AntdConfigProvider',
                                href='/AntdConfigProvider',
                                target='_blank'
                            ),
                            '文档）：'
                        ],
                        style={
                            'textIndent': '2rem'
                        }
                    ),

                    fac.AntdConfigProvider(
                        fac.AntdSpace(
                            [
                                fac.AntdDatePicker(),
                                fac.AntdDateRangePicker()
                            ]
                        ),
                        locale='en-us'
                    ),

                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString='''
fac.AntdConfigProvider(
    fac.AntdSpace(
        [
            fac.AntdDatePicker(),
            fac.AntdDateRangePicker()
        ]
    ),
    locale='en-us'
)
'''
                    ),

                    html.Div(style={'height': '100px'})
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px'
                }
            )
        ],
        style={
            'display': 'flex'
        }
    )
