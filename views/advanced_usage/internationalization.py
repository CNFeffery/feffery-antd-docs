from i18n import localized_output, translator
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Component


@localized_output
def render() -> Component:
    """渲染“国际化”文档页"""

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(duration=0.3),
                    fac.AntdBreadcrumb(
                        items=[{'title': '进阶使用'}, {'title': '国际化'}]
                    ),
                    fac.AntdDivider(isDashed=True),
                    fac.AntdParagraph(
                        [
                            fac.AntdText('fac', strong=True),
                            '针对部分组件，具有切换组件自带文案信息语种的功能，基于相关组件的参数',
                            fac.AntdText('locale', code=True),
                            '（默认为',
                            fac.AntdText('"zh-cn"', code=True),
                            '，即简体中文），也可以设置为',
                            fac.AntdText('"en-us"', code=True),
                            '切换到英文文案模式，典型例子如下：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdForm(
                        [
                            fac.AntdFormItem(
                                fac.AntdConfigProvider(
                                    fac.AntdSpace(
                                        [
                                            fac.AntdDatePicker(locale='zh-cn'),
                                            fac.AntdDateRangePicker(
                                                locale='zh-cn'
                                            ),
                                        ]
                                    ),
                                    locale='zh-cn',
                                ),
                                label='locale="zh-cn"（默认）',
                            ),
                            fac.AntdFormItem(
                                fac.AntdConfigProvider(
                                    fac.AntdSpace(
                                        [
                                            fac.AntdDatePicker(locale='en-us'),
                                            fac.AntdDateRangePicker(
                                                locale='en-us'
                                            ),
                                        ]
                                    ),
                                    locale='en-us',
                                ),
                                label='locale="en-us"',
                            ),
                        ],
                        layout='vertical',
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdConfigProvider(
                fac.AntdSpace(
                    [
                        fac.AntdDatePicker(locale='zh-cn'),
                        fac.AntdDateRangePicker(locale='zh-cn')
                    ]
                ),
                locale='zh-cn'
            ),
            label='locale="zh-cn"（默认）'
        ),

        fac.AntdFormItem(
            fac.AntdConfigProvider(
                fac.AntdSpace(
                    [
                        fac.AntdDatePicker(locale='en-us'),
                        fac.AntdDateRangePicker(locale='en-us')
                    ]
                ),
                locale='en-us'
            ),
            label='locale="en-us"'
        )
    ],
    layout='vertical'
)
""",
                    ),
                    fac.AntdParagraph(
                        translator.t(
                            '配置提供器的语种设置优先于后代组件自身的 locale。为避免本官网页面外层的配置影响上述对比，示例分别使用中文和英文的嵌套配置提供器；没有配置提供器覆盖时，可以直接使用组件自身的 locale。',
                            locale_topic='advanced_usage',
                        )
                    ),
                    fac.AntdParagraph(
                        [
                            '上面介绍的例子是针对每个组件单独控制语种，而如果你的应用中存在着大量的需要设置为其他语种的组件，则可以将相关组件全部嵌套在全局配置组件',
                            fac.AntdText('AntdConfigProvider', strong=True),
                            '中，并为其设置参数',
                            fac.AntdText('locale="en-us"', code=True),
                            '，从而批量快捷覆盖设置内部元素的国际化语种',
                            '（更多内容请参考',
                            html.A(
                                'AntdConfigProvider',
                                href='/AntdConfigProvider',
                                target='_blank',
                            ),
                            '文档）：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdConfigProvider(
                        fac.AntdSpace(
                            [fac.AntdDatePicker(), fac.AntdDateRangePicker()]
                        ),
                        locale='en-us',
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
fac.AntdConfigProvider(
    fac.AntdSpace(
        [
            fac.AntdDatePicker(),
            fac.AntdDateRangePicker()
        ]
    ),
    locale='en-us'
)
""",
                    ),
                    fac.AntdParagraph(
                        translator.t(
                            'FAC 组件内置文案还支持 de-de（德语）、ru-ru（俄语）和 fr-fr（法语）。这些设置只控制组件内置文案，不会自动翻译传入的标题、说明和其他自定义内容。本官网的文档语种目前为中文和英文，页首语言按钮通过 Cookie 保存选择并重载页面，与示例中组件内置文案的语种设置相互独立。',
                            locale_topic='advanced_usage',
                        )
                    ),
                    html.Div(style={'height': '100px'}),
                ],
                style={'flex': 'auto', 'padding': '25px'},
            )
        ],
        style={'display': 'flex', 'marginRight': 40},
    )
