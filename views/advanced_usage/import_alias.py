from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
from dash.dependencies import Component


def render() -> Component:
    """渲染“组件按别名导入”文档页"""

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdBackTop(duration=0.3),
                    fac.AntdBreadcrumb(
                        items=[
                            {'title': '进阶使用'},
                            {'title': '组件按别名导入'},
                        ]
                    ),
                    fac.AntdDivider(isDashed=True),
                    fac.AntdParagraph(
                        [
                            '除了常规的',
                            fac.AntdText(
                                'import feffery_antd_components as fac',
                                code=True,
                            ),
                            '导入方式外，还可以使用',
                            fac.AntdText(
                                'import feffery_antd_components.alias as fac',
                                code=True,
                            ),
                            '进行组件的按别名导入，从而省略各组件名的',
                            fac.AntdText('Antd', code=True),
                            '前缀信息，譬如下面的示例代码：',
                        ],
                        style={'textIndent': '2rem'},
                    ),
                    fac.AntdSpace(
                        [
                            fac.AntdButton(f'按钮{i}', type='primary')
                            for i in range(1, 6)
                        ]
                    ),
                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString="""
import feffery_antd_components.alias as fac

...

fac.Space(
    [
        fac.Button(
            f'按钮{i}',
            type='primary'
        )
        for i in range(1, 6)
    ]
)
""",
                    ),
                    html.Div(style={'height': 'calc(100vh - 800px)'}),
                ],
                style={'flex': 'auto', 'padding': '25px'},
            )
        ],
        style={'display': 'flex', 'paddingRight': 40},
    )
