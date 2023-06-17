from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.use_key_to_refresh_c


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
                                'title': '强制刷新组件'
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
                            '中的全部组件都具有参数',
                            fac.AntdText(
                                'key',
                                code=True
                            ),
                            '，对其进行更新可以实现对该组件的强制重载，譬如在下面的例子中，切换上面的类型，会对下方内容区的内容进行更新，',
                            '但当类型发生切换后，先前的滚动条位置会残留：'
                        ],
                        style={
                            'textIndent': '2rem'
                        }
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        id='key-demo1-type',
                                        options=[
                                            {
                                                'label': f'类型{i}',
                                                'value': f'类型{i}',
                                            }
                                            for i in range(1, 6)
                                        ],
                                        defaultValue='类型1'
                                    ),

                                    fac.AntdSpace(
                                        id='key-demo1-output',
                                        style={
                                            'width': 200,
                                            'height': 100,
                                            'overflowY': 'auto',
                                            'border': '1px solid #dee2e6'
                                        }
                                    )
                                ],
                                direction='vertical'
                            )
                        ],
                        style={
                            'padding': 25
                        }
                    ),

                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString='''
html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdRadioGroup(
                    id='key-demo1-type',
                    options=[
                        {
                            'label': f'类型{i}',
                            'value': f'类型{i}',
                        }
                        for i in range(1, 6)
                    ],
                    defaultValue='类型1'
                ),

                fac.AntdSpace(
                    id='key-demo1-output',
                    style={
                        'width': 200,
                        'height': 100,
                        'overflowY': 'auto',
                        'border': '1px solid #dee2e6'
                    }
                )
            ],
            direction='vertical'
        )
    ],
    style={
        'padding': 25
    }
)

...

@app.callback(
    Output('key-demo1-output', 'children'),
    Input('key-demo1-type', 'value')
)
def key_demo1(value):

    return value * 100
'''
                    ),

                    fac.AntdParagraph(
                        [
                            '这时我们就可以使用',
                            fac.AntdText(
                                'key',
                                code=True
                            ),
                            '来辅助强制重置：'
                        ],
                        style={
                            'textIndent': '2rem'
                        }
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        id='key-demo2-type',
                                        options=[
                                            {
                                                'label': f'类型{i}',
                                                'value': f'类型{i}',
                                            }
                                            for i in range(1, 6)
                                        ],
                                        defaultValue='类型1'
                                    ),

                                    fac.AntdSpace(
                                        id='key-demo2-output',
                                        style={
                                            'width': 200,
                                            'height': 100,
                                            'overflowY': 'auto',
                                            'border': '1px solid #dee2e6'
                                        }
                                    )
                                ],
                                direction='vertical'
                            )
                        ],
                        style={
                            'padding': 25
                        }
                    ),

                    fmc.FefferySyntaxHighlighter(
                        showCopyButton=True,
                        showLineNumbers=True,
                        language='python',
                        codeTheme='coy-without-shadows',
                        codeString='''
html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdRadioGroup(
                    id='key-demo2-type',
                    options=[
                        {
                            'label': f'类型{i}',
                            'value': f'类型{i}',
                        }
                        for i in range(1, 6)
                    ],
                    defaultValue='类型1'
                ),

                fac.AntdSpace(
                    id='key-demo2-output',
                    style={
                        'width': 200,
                        'height': 100,
                        'overflowY': 'auto',
                        'border': '1px solid #dee2e6'
                    }
                )
            ],
            direction='vertical'
        )
    ],
    style={
        'padding': 25
    }
)

...

import uuid

...

@app.callback(
    [Output('key-demo2-output', 'children'),
     Output('key-demo2-output', 'key')],
    Input('key-demo2-type', 'value')
)
def key_demo2(value):

    return [value * 100, str(uuid.uuid4())]
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
