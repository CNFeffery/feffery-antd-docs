from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdTabs
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
                                'title': '标签页'
                            },
                            {
                                'title': 'AntdTabs 标签页'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于构建多标签页。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTabs(
                                [
                                    fac.AntdTabPane(
                                        html.Div(
                                            f'这是标签页{i}的内容示例',
                                            style={
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center',
                                                'fontSize': 18,
                                                'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                                                'height': 200
                                            }
                                        ),
                                        key=f'标签页{i}',
                                        tab=f'标签页{i}'
                                    )
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '基础使用（废弃的写法）',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '基于',
                                    fac.AntdText(
                                        'AntdTabPane',
                                        strong=True
                                    ),
                                    '的标签页构造方法将在下一个大版本',
                                    fac.AntdText(
                                        '0.3.x',
                                        code=True
                                    ),
                                    '中移除，请尽快切换到新的items构造方式'
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
fac.AntdTabs(
    [
        fac.AntdTabPane(
            html.Div(
                f'这是标签页{i}的内容示例',
                style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'fontSize': 18,
                    'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                    'height': 200
                }
            ),
            key=f'标签页{i}',
            tab=f'标签页{i}'
        )
        for i in range(1, 6)
    ]
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
                        id='基础使用（废弃的写法）',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}',
                                        'children': html.Div(
                                            f'这是标签页{i}的内容示例',
                                            style={
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center',
                                                'fontSize': 18,
                                                'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                                                'height': 200
                                            }
                                        )
                                    }
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText(
                                        '0.2.x',
                                        code=True
                                    ),
                                    '版本开始新引入的标签页构造方式'
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
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}',
            'children': html.Div(
                f'这是标签页{i}的内容示例',
                style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'fontSize': 18,
                    'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                    'height': 200
                }
            )
        }
        for i in range(1, 6)
    ]
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
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': fac.AntdSpace(
                                            [
                                                fac.AntdText(
                                                    f'标签页{i}'
                                                ),
                                                fac.AntdTooltip(
                                                    fac.AntdIcon(
                                                        icon='antd-question-circle',
                                                        style={
                                                            'color': '#9b9b9b'
                                                        }
                                                    ),
                                                    title=f'这是标签页{i}balabalabala',
                                                    placement='right'
                                                )
                                            ]
                                        )
                                    }
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '自定义标签页标题',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '参数',
                                    fac.AntdText(
                                        'label',
                                        code=True
                                    ),
                                    '支持传入任意组件作为标签页标题内容'
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
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': fac.AntdSpace(
                [
                    fac.AntdText(
                        f'标签页{i}'
                    ),
                    fac.AntdTooltip(
                        fac.AntdIcon(
                            icon='antd-question-circle',
                            style={
                                'color': '#9b9b9b'
                            }
                        ),
                        title=f'这是标签页{i}balabalabala',
                        placement='right'
                    )
                ]
            )
        }
        for i in range(1, 6)
    ]
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
                        id='自定义标签页标题',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '基于disabled参数',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}',
                                        'disabled': i in [3, 4]
                                    }
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '基于disabledTabKeys参数',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                disabledTabKeys=['标签页3', '标签页4']
                            ),

                            fac.AntdDivider(
                                '禁用部分标签页',
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
    '基于disabled参数',
    innerTextOrientation='left'
),
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}',
            'disabled': i in [3, 4]
        }
        for i in range(1, 6)
    ]
),

fac.AntdDivider(
    '基于disabledTabKeys参数',
    innerTextOrientation='left'
),
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}'
        }
        for i in range(1, 6)
    ],
    disabledTabKeys=['标签页3', '标签页4']
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
                        id='禁用部分标签页',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'key': f'标签页{i}',
                                                'label': f'标签页{i}',
                                                'children': html.Div(
                                                    f'这是标签页{i}的内容示例',
                                                    style={
                                                        'display': 'flex',
                                                        'justifyContent': 'center',
                                                        'alignItems': 'center',
                                                        'fontSize': 18,
                                                        'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                                                        'height': 260
                                                    }
                                                ),
                                            }
                                            for i in range(1, 6)
                                        ],
                                        tabPosition=position
                                    )
                                    for position in [
                                        'top', 'left', 'bottom', 'right'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '不同的标签页显示方位',
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
        fac.AntdTabs(
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}',
                    'children': html.Div(
                        f'这是标签页{i}的内容示例',
                        style={
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center',
                            'fontSize': 18,
                            'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                            'height': 260
                        }
                    ),
                }
                for i in range(1, 6)
            ],
            tabPosition=position
        )
        for position in [
            'top', 'left', 'bottom', 'right'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                        id='不同的标签页显示方位',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'key': f'标签页{i}',
                                                'label': f'标签页{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        size=size
                                    )
                                    for size in [
                                        'small', 'default', 'large'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '不同的尺寸规格',
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
        fac.AntdTabs(
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}'
                }
                for i in range(1, 6)
            ],
            size=size
        )
        for size in [
            'small', 'default', 'large'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                        id='不同的尺寸规格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                centered=True
                            ),

                            fac.AntdDivider(
                                '居中的标签栏',
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
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}'
        }
        for i in range(1, 6)
    ],
    centered=True
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
                        id='居中的标签栏',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSlider(
                                id='tabs-gutter-demo-slider',
                                min=20,
                                max=60,
                                step=5,
                                defaultValue=20,
                                tooltipVisible=True,
                                marks={
                                    i*5: f'{i*5}px'
                                    for i in range(1, 13)
                                }
                            ),
                            fac.AntdTabs(
                                id='tabs-gutter-demo',
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}'
                                    }
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '设置标签之间的间距',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString="""
fac.AntdSlider(
    id='tabs-gutter-demo-slider',
    min=20,
    max=60,
    step=5,
    defaultValue=20,
    tooltipVisible=True,
    marks={
        i*5: f'{i*5}px'
        for i in range(1, 13)
    }
),
fac.AntdTabs(
    id='tabs-gutter-demo',
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}'
        }
        for i in range(1, 6)
    ]
)

...

app.clientside_callback(
    '''(value) => value''',
    Output('tabs-gutter-demo', 'tabBarGutter'),
    Input('tabs-gutter-demo-slider', 'value')
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
                        id='设置标签之间的间距',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdForm(
                                [
                                    fac.AntdFormItem(
                                        fac.AntdSwitch(
                                            id='tabs-animation-demo-inkBarAnimated',
                                            checked=True,
                                            checkedChildren='True',
                                            unCheckedChildren='False'
                                        ),
                                        label='inkBarAnimated'
                                    ),
                                    fac.AntdFormItem(
                                        fac.AntdSwitch(
                                            id='tabs-animation-demo-tabPaneAnimated',
                                            checked=False,
                                            checkedChildren='True',
                                            unCheckedChildren='False'
                                        ),
                                        label='tabPaneAnimated'
                                    )
                                ],
                                layout='inline'
                            ),
                            fac.AntdTabs(
                                id='tabs-animation-demo',
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}',
                                        'children': html.Div(
                                            f'这是标签页{i}的内容示例',
                                            style={
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center',
                                                'fontSize': 18,
                                                'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                                                'height': 200
                                            }
                                        )
                                    }
                                    for i in range(1, 6)
                                ]
                            ),

                            fac.AntdDivider(
                                '控制切换动画',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString="""
fac.AntdForm(
    [
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='tabs-animation-demo-inkBarAnimated',
                checked=True,
                checkedChildren='True',
                unCheckedChildren='False'
            ),
            label='inkBarAnimated'
        ),
        fac.AntdFormItem(
            fac.AntdSwitch(
                id='tabs-animation-demo-tabPaneAnimated',
                checked=False,
                checkedChildren='True',
                unCheckedChildren='False'
            ),
            label='tabPaneAnimated'
        )
    ],
    layout='inline'
),
fac.AntdTabs(
    id='tabs-animation-demo',
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}',
            'children': html.Div(
                f'这是标签页{i}的内容示例',
                style={
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    'fontSize': 18,
                    'background': f'rgba(28, 126, 214, calc(1 - 0.2 * {i}))',
                    'height': 200
                }
            )
        }
        for i in range(1, 6)
    ]
)

...

app.clientside_callback(
    '''(inkBarAnimated, tabPaneAnimated) => [inkBarAnimated, tabPaneAnimated]''',
    [Output('tabs-animation-demo', 'inkBarAnimated'),
     Output('tabs-animation-demo', 'tabPaneAnimated')],
    [Input('tabs-animation-demo-inkBarAnimated', 'checked'),
     Input('tabs-animation-demo-tabPaneAnimated', 'checked')]
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
                        id='控制切换动画',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTabs(
                                        items=[
                                            {
                                                'key': f'标签页{i}',
                                                'label': f'标签页{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        type=type_
                                    )
                                    for type_ in [
                                        'line', 'card', 'editable-card'
                                    ]
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '不同的标签栏类型',
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
        fac.AntdTabs(
            items=[
                {
                    'key': f'标签页{i}',
                    'label': f'标签页{i}'
                }
                for i in range(1, 6)
            ],
            type=type_
        )
        for type_ in [
            'line', 'card', 'editable-card'
        ]
    ],
    direction='vertical',
    style={
        'width': '100%'
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
                        id='不同的标签栏类型',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': f'标签页{i}',
                                        'label': f'标签页{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                tabBarLeftExtraContent=fac.AntdButton(
                                    '示例1'
                                ),
                                tabBarRightExtraContent=fac.AntdButton(
                                    '示例2'
                                ),
                                centered=True
                            ),

                            fac.AntdDivider(
                                '添加额外的前后缀内容',
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
fac.AntdTabs(
    items=[
        {
            'key': f'标签页{i}',
            'label': f'标签页{i}'
        }
        for i in range(1, 6)
    ],
    tabBarLeftExtraContent=fac.AntdButton(
        '示例1'
    ),
    tabBarRightExtraContent=fac.AntdButton(
        '示例2'
    ),
    centered=True
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
                        id='添加额外的前后缀内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTabs(
                                id='tabs-demo',
                                items=[
                                    {
                                        'label': f'标签页{i}',
                                        'key': f'标签页{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                defaultActiveKey='标签页3'
                            ),
                            fac.AntdText(
                                id='tabs-demo-output'
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
fac.AntdTabs(
    id='tabs-demo',
    items=[
        {
            'label': f'标签页{i}',
            'key': f'标签页{i}'
        }
        for i in range(1, 6)
    ],
    defaultActiveKey='标签页3'
),
fac.AntdText(
    id='tabs-demo-output'
)

...

@app.callback(
    Output('tabs-demo-output', 'children'),
    Input('tabs-demo', 'activeKey')
)
def tabs_demo(activeKey):

    return f'activeKey: {activeKey}'
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
                            fac.AntdTabs(
                                id='tabs-add-delete-demo',
                                type='editable-card',
                                items=[
                                    {
                                        'label': f'标签页{i}',
                                        'key': str(i),
                                        'children': html.Div(
                                            f'标签页{i}',
                                            style={
                                                'height': 200,
                                                'fontSize': 28,
                                                'display': 'flex',
                                                'justifyContent': 'center',
                                                'alignItems': 'center'
                                            }
                                        ),
                                        'closable': not (i == 1)
                                    }
                                    for i in range(1, 6)
                                ],
                                tabBarRightExtraContent=fac.AntdIcon(
                                    id='tabs-add-delete-demo-add',
                                    icon='antd-plus-circle-two-tone',
                                    style={
                                        'fontSize': 20,
                                        'cursor': 'pointer'
                                    }
                                )
                            ),

                            fac.AntdDivider(
                                '标签页自由增删示例',
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
fac.AntdTabs(
    id='tabs-add-delete-demo',
    type='editable-card',
    items=[
        {
            'label': f'标签页{i}',
            'key': str(i),
            'children': html.Div(
                f'标签页{i}',
                style={
                    'height': 200,
                    'fontSize': 28,
                    'display': 'flex',
                    'justifyContent': 'center',
                    'alignItems': 'center'
                }
            ),
            'closable': not (i == 1)
        }
        for i in range(1, 6)
    ],
    tabBarRightExtraContent=fac.AntdIcon(
        id='tabs-add-delete-demo-add',
        icon='antd-plus-circle-two-tone',
        style={
            'fontSize': 20,
            'cursor': 'pointer'
        }
    )
)

...

@app.callback(
    [Output('tabs-add-delete-demo', 'items'),
     Output('tabs-add-delete-demo', 'activeKey')],
    [Input('tabs-add-delete-demo-add', 'nClicks'),
     Input('tabs-add-delete-demo', 'latestDeletePane')],
    [State('tabs-add-delete-demo', 'items'),
     State('tabs-add-delete-demo', 'activeKey')]
)
def tabs_add_delete_demo(nClicks,
                         latestDeletePane,
                         origin_items,
                         activeKey):

    if dash.ctx.triggered_id == 'tabs-add-delete-demo-add':

        # 提取已有items中的最大key值
        origin_max_key = max([int(item['key']) for item in origin_items])

        return [
            [
                *origin_items,
                {
                    'label': f'标签页{origin_max_key+1}',
                    'key': str(origin_max_key+1),
                    'children': html.Div(
                        f'标签页{origin_max_key+1}',
                        style={
                            'height': 200,
                            'fontSize': 28,
                            'display': 'flex',
                            'justifyContent': 'center',
                            'alignItems': 'center'
                        }
                    )
                }
            ],
            str(origin_max_key+1)
        ]

    elif dash.ctx.triggered_id == 'tabs-add-delete-demo':

        return [
            [
                item
                for item in origin_items
                if item['key'] != latestDeletePane
            ],
            '1' if latestDeletePane == activeKey else dash.no_update
        ]

    return dash.no_update
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
                        id='标签页自由增删示例',
                        className='div-highlight'
                    ),

                    html.Div(style={'height': '100px'})
                ],
                style={
                    'flex': 'auto',
                    'padding': '25px',
                    'width': 0
                }
            ),
            html.Div(
                fac.AntdAnchor(
                    linkDict=[
                        {'title': '基础使用（废弃的写法）', 'href': '#基础使用（废弃的写法）'},
                        {'title': '基础使用', 'href': '#基础使用'},
                        {'title': '自定义标签页标题', 'href': '#自定义标签页标题'},
                        {'title': '禁用部分标签页', 'href': '#禁用部分标签页'},
                        {'title': '不同的标签页显示方位', 'href': '#不同的标签页显示方位'},
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                        {'title': '居中的标签栏', 'href': '#居中的标签栏'},
                        {'title': '设置标签之间的间距', 'href': '#设置标签之间的间距'},
                        {'title': '控制切换动画', 'href': '#控制切换动画'},
                        {'title': '不同的标签栏类型', 'href': '#不同的标签栏类型'},
                        {'title': '添加额外的前后缀内容', 'href': '#添加额外的前后缀内容'},
                        {'title': '回调示例', 'href': '#回调示例'},
                        {'title': '标签页自由增删示例', 'href': '#标签页自由增删示例'},
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
                component_name='AntdTabs',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
