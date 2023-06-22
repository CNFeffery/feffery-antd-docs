from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdTooltip
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
                                'title': '数据展示'
                            },
                            {
                                'title': 'AntdTooltip 信息提示'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为指定元素添加额外信息提示。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTooltip(
                                fac.AntdButton(
                                    '锚点元素'
                                ),
                                title='信息提示示例'
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
fac.AntdTooltip(
    fac.AntdButton(
        '锚点元素'
    ),
    title='信息提示示例'
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
                                    fac.AntdTooltip(
                                        fac.AntdButton(
                                            placement
                                        ),
                                        title=placement,
                                        placement=placement
                                    )
                                    for placement in [
                                        'top', 'left', 'right', 'bottom',
                                        'topLeft', 'topRight', 'bottomLeft',
                                        'bottomRight'
                                    ]
                                ],
                                wrap=True
                            ),

                            fac.AntdDivider(
                                '不同的悬浮层展开方向',
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
        fac.AntdTooltip(
            fac.AntdButton(
                placement
            ),
            title=placement,
            placement=placement
        )
        for placement in [
            'top', 'left', 'right', 'bottom',
            'topLeft', 'topRight', 'bottomLeft',
            'bottomRight'
        ]
    ],
    wrap=True
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
                        id='不同的悬浮层展开方向',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fuc.FefferyHexColorPicker(
                                        id='tooltip-color-demo-input',
                                        showAlpha=True,
                                        color='#f6f7f866'
                                    ),

                                    fac.AntdTooltip(
                                        fac.AntdButton(
                                            '锚点示例'
                                        ),
                                        id='tooltip-color-demo',
                                        title='信息提示示例'
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '自定义背景色',
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
        fuc.FefferyHexColorPicker(
            id='tooltip-color-demo-input',
            showAlpha=True,
            color='#f6f7f866'
        ),

        fac.AntdTooltip(
            fac.AntdButton(
                '锚点示例'
            ),
            id='tooltip-color-demo',
            title='信息提示示例'
        )
    ]
)

...

@app.callback(
    [Output('tooltip-color-demo', 'color'),
     Output('tooltip-color-demo', 'title')],
    Input('tooltip-color-demo-input', 'color')
)
def tooltip_color_demo(color):

    return [
        color,
        fac.AntdParagraph(
            [
                '当前color: ',
                fac.AntdText(
                    color,
                    copyable=True
                )
            ]
        )
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
                        id='自定义背景色',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTooltip(
                                fac.AntdButton(
                                    '锚点示例'
                                ),
                                title='内容示例'*50,
                                overlayStyle={
                                    'width': 250
                                },
                                overlayInnerStyle={
                                    'maxHeight': 150,
                                    'overflowY': 'auto'
                                }
                            ),

                            fac.AntdDivider(
                                '自定义样式',
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
fac.AntdTooltip(
    fac.AntdButton(
        '锚点示例'
    ),
    title='内容示例'*50,
    overlayStyle={
        'width': 250
    },
    overlayInnerStyle={
        'maxHeight': 150,
        'overflowY': 'auto'
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
                        id='自定义样式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdForm(
                                        [
                                            fac.AntdFormItem(
                                                fac.AntdSwitch(
                                                    id='tooltip-open-demo-open',
                                                    checkedChildren='True',
                                                    unCheckedChildren='False',
                                                    checked=False
                                                ),
                                                label='open'
                                            ),
                                            fac.AntdFormItem(
                                                fac.AntdSwitch(
                                                    id='tooltip-open-demo-permanent',
                                                    checkedChildren='True',
                                                    unCheckedChildren='False',
                                                    checked=False
                                                ),
                                                label='permanent'
                                            )
                                        ],
                                        layout='inline'
                                    ),
                                    fac.AntdTooltip(
                                        fac.AntdButton(
                                            '锚点元素'
                                        ),
                                        id='tooltip-open-demo',
                                        placement='right'
                                    )
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '可控的展开行为',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '仅设置',
                                    fac.AntdText(
                                        'open=True',
                                        code=True
                                    ),
                                    '时，文字提示会默认展开，但随着用户后续的鼠标动作，展开状态会照常被切换'
                                ],
                                style={
                                    'textIndent': '2rem'
                                }
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString="""
fac.AntdSpace(
    [
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdSwitch(
                        id='tooltip-open-demo-open',
                        checkedChildren='True',
                        unCheckedChildren='False',
                        checked=False
                    ),
                    label='open'
                ),
                fac.AntdFormItem(
                    fac.AntdSwitch(
                        id='tooltip-open-demo-permanent',
                        checkedChildren='True',
                        unCheckedChildren='False',
                        checked=False
                    ),
                    label='permanent'
                )
            ],
            layout='inline'
        ),
        fac.AntdTooltip(
            fac.AntdButton(
                '锚点元素'
            ),
            id='tooltip-open-demo',
            placement='right'
        )
    ],
    direction='vertical'
)

...

app.clientside_callback(
    '''(open, permanent) => {
        return [
            open,
            permanent,
            `open=${open} permanent=${permanent}`
        ];
    }''',
    [Output('tooltip-open-demo', 'open'),
     Output('tooltip-open-demo', 'permanent'),
     Output('tooltip-open-demo', 'title')],
    [Input('tooltip-open-demo-open', 'checked'),
     Input('tooltip-open-demo-permanent', 'checked')]
)
"""
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
                        id='可控的展开行为',
                        className='div-highlight'
                    ),

                    fac.AntdTitle(
                        '常见问题',
                        id='常见问题',
                        level=3,
                        className='common-problem-demo',
                        style={
                            'margin': '25px 0'
                        }
                    ),

                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Span(
                                        fac.AntdTooltip(
                                            fac.AntdButton(
                                                '示例1',
                                                type='primary'
                                            ),
                                            title='示例内容'
                                        ),
                                        style={
                                            'position': 'absolute',
                                            'left': 15,
                                            'bottom': 15
                                        }
                                    ),
                                    html.Span(
                                        fac.AntdTooltip(
                                            fac.AntdButton(
                                                '示例2',
                                                type='primary'
                                            ),
                                            title='示例内容'
                                        ),
                                        style={
                                            'position': 'absolute',
                                            'right': 15,
                                            'top': 15
                                        }
                                    ),
                                    html.Span(
                                        fac.AntdTooltip(
                                            fac.AntdButton(
                                                '示例3',
                                                type='primary'
                                            ),
                                            title='示例内容'
                                        ),
                                        style={
                                            'position': 'absolute',
                                            'right': 15,
                                            'bottom': 15
                                        }
                                    )
                                ],
                                style={
                                    'position': 'relative',
                                    'height': 300,
                                    'background': '#dee2e6'
                                }
                            ),

                            fac.AntdDivider(
                                '配合绝对定位',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '当直接将',
                                    fac.AntdText(
                                        'AntdTooltip',
                                        strong=True
                                    ),
                                    '施加于具有绝对定位样式的元素之上时，可能会遇到悬浮层位置显示异常的问题，推荐的稳定做法是为对应的',
                                    fac.AntdText(
                                        'AntdTooltip',
                                        strong=True
                                    ),
                                    '添加一层',
                                    fac.AntdText(
                                        'Span',
                                        strong=True
                                    ),
                                    '父元素，并将原先的绝对定位相关样式转而施加于此父元素之上'
                                ],
                                style={
                                    'textIndent': '2rem'
                                }
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
        html.Span(
            fac.AntdTooltip(
                fac.AntdButton(
                    '示例1',
                    type='primary'
                ),
                title='示例内容'
            ),
            style={
                'position': 'absolute',
                'left': 15,
                'bottom': 15
            }
        ),
        html.Span(
            fac.AntdTooltip(
                fac.AntdButton(
                    '示例2',
                    type='primary'
                ),
                title='示例内容'
            ),
            style={
                'position': 'absolute',
                'right': 15,
                'top': 15
            }
        ),
        html.Span(
            fac.AntdTooltip(
                fac.AntdButton(
                    '示例3',
                    type='primary'
                ),
                title='示例内容'
            ),
            style={
                'position': 'absolute',
                'right': 15,
                'bottom': 15
            }
        )
    ],
    style={
        'position': 'relative',
        'height': 300,
        'background': '#dee2e6'
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
                        id='常见问题|配合绝对定位',
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
                        {'title': '不同的悬浮层展开方向', 'href': '#不同的悬浮层展开方向'},
                        {'title': '自定义背景色', 'href': '#自定义背景色'},
                        {'title': '自定义样式', 'href': '#自定义样式'},
                        {'title': '可控的展开行为', 'href': '#可控的展开行为'},
                        {
                            'title': '常见问题',
                            'href': '#常见问题',
                            'children': [
                                {
                                    'title': '配合绝对定位',
                                    'href': '#常见问题|配合绝对定位'
                                }
                            ]
                        }
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
                component_name='AntdTooltip',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
