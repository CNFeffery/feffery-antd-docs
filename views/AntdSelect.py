from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdSelect
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
                                'title': 'AntdSelect 下拉选择'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供一组选项进行选择。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                style={
                                    'width': 200
                                }
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
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    style={
        'width': 200
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
                        id='基础使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                mode='multiple',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '多选模式',
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
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    mode='multiple',
    style={
        'width': 200
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
                        id='多选模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                mode='tags',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '自由新增模式',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '　　自由新增模式下，在输入框中输入内容后按下',
                                    fac.AntdText(
                                        'enter',
                                        keyboard=True
                                    ),
                                    '键，可以进行新选项的添加'
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    mode='tags',
    style={
        'width': 200
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
                        id='自由新增模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'group': '分组1',
                                        'options': [
                                            {
                                                'label': f'选项1-{i}',
                                                'value': f'选项1-{i}'
                                            }
                                            for i in range(1, 4)
                                        ]
                                    },
                                    {
                                        'group': '分组2',
                                        'options': [
                                            {
                                                'label': f'选项2-{i}',
                                                'value': f'选项2-{i}'
                                            }
                                            for i in range(1, 4)
                                        ]
                                    }
                                ],
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '下拉选项分组',
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
fac.AntdSelect(
    options=[
        {
            'group': '分组1',
            'options': [
                {
                    'label': f'选项1-{i}',
                    'value': f'选项1-{i}'
                }
                for i in range(1, 4)
            ]
        },
        {
            'group': '分组2',
            'options': [
                {
                    'label': f'选项2-{i}',
                    'value': f'选项2-{i}'
                }
                for i in range(1, 4)
            ]
        }
    ],
    style={
        'width': 200
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
                        id='下拉选项分组',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 26)
                                        ],
                                        listHeight=400,
                                        style={
                                            'width': 200
                                        }
                                    ),

                                    fac.AntdSelect(
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 10)
                                        ],
                                        listHeight=100,
                                        style={
                                            'width': 200
                                        }
                                    )
                                ]
                            ),

                            fac.AntdDivider(
                                '下拉菜单最大高度',
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
        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 26)
            ],
            listHeight=400,
            style={
                'width': 200
            }
        ),

        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 10)
            ],
            listHeight=100,
            style={
                'width': 200
            }
        )
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
                        id='下拉菜单最大高度',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '连续型色带',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSelect(
                                defaultValue='色系1',
                                options=[
                                    {
                                        'label': '色系1',
                                        'value': '色系1',
                                        'colors': ['#fff5f5', '#ff8787', '#c92a2a']
                                    },
                                    {
                                        'label': '色系2',
                                        'value': '色系2',
                                        'colors': ['#f8f0fc', '#da77f2', '#862e9c']
                                    },
                                    {
                                        'label': '色系3',
                                        'value': '色系3',
                                        'colors': ['#e7f5ff', '#4dabf7', '#1864ab']
                                    }
                                ],
                                colorsMode='sequential',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '离散型色带',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSelect(
                                defaultValue='色系1',
                                options=[
                                    {
                                        'label': '色系1',
                                        'value': '色系1',
                                        'colors': ['#fff5f5', '#ff8787', '#c92a2a']
                                    },
                                    {
                                        'label': '色系2',
                                        'value': '色系2',
                                        'colors': ['#f8f0fc', '#da77f2', '#862e9c']
                                    },
                                    {
                                        'label': '色系3',
                                        'value': '色系3',
                                        'colors': ['#e7f5ff', '#4dabf7', '#1864ab']
                                    }
                                ],
                                colorsMode='diverging',
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '色带选择模式',
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
    '连续型色带',
    innerTextOrientation='left'
),
fac.AntdSelect(
    defaultValue='色系1',
    options=[
        {
            'label': '色系1',
            'value': '色系1',
            'colors': ['#fff5f5', '#ff8787', '#c92a2a']
        },
        {
            'label': '色系2',
            'value': '色系2',
            'colors': ['#f8f0fc', '#da77f2', '#862e9c']
        },
        {
            'label': '色系3',
            'value': '色系3',
            'colors': ['#e7f5ff', '#4dabf7', '#1864ab']
        }
    ],
    colorsMode='sequential',
    style={
        'width': 200
    }
),

fac.AntdDivider(
    '离散型色带',
    innerTextOrientation='left'
),
fac.AntdSelect(
    defaultValue='色系1',
    options=[
        {
            'label': '色系1',
            'value': '色系1',
            'colors': ['#fff5f5', '#ff8787', '#c92a2a']
        },
        {
            'label': '色系2',
            'value': '色系2',
            'colors': ['#f8f0fc', '#da77f2', '#862e9c']
        },
        {
            'label': '色系3',
            'value': '色系3',
            'colors': ['#e7f5ff', '#4dabf7', '#1864ab']
        }
    ],
    colorsMode='diverging',
    style={
        'width': 200
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
                        id='色带选择模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                disabled=True,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '禁用状态',
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
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    disabled=True,
    style={
        'width': 200
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
                        id='禁用状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                defaultValue='选项1',
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                readOnly=True,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '只读状态',
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
fac.AntdSelect(
    defaultValue='选项1',
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    readOnly=True,
    style={
        'width': 200
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
                        id='只读状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                style={
                                    'width': 200
                                },
                                autoFocus=True
                            ),

                            fac.AntdDivider(
                                '自动获取焦点',
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
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    style={
        'width': 200
    },
    autoFocus=True
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
                        id='自动获取焦点',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        defaultValue='选项1',
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        placeholder=f'status="{status}"',
                                        status=status,
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for status in ['warning', 'error']
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '强制状态渲染',
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
        fac.AntdSelect(
            defaultValue='选项1',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            placeholder=f'status="{status}"',
            status=status,
            style={
                'width': 200
            }
        )
        for status in ['warning', 'error']
    ],
    direction='vertical'
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
                        id='强制状态渲染',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        placeholder=f'size="{size}"',
                                        size=size,
                                        style={
                                            'width': 200
                                        }
                                    )
                                    for size in ['small', 'middle', 'large']
                                ],
                                direction='vertical'
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
        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            placeholder=f'size="{size}"',
            size=size,
            style={
                'width': 200
            }
        )
        for size in ['small', 'middle', 'large']
    ],
    direction='vertical'
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
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                placeholder='请选择',
                                bordered=False,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '无边框',
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
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    placeholder='请选择',
    bordered=False,
    style={
        'width': 200
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
                        id='无边框',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        placeholder=f'placement="{placement}"',
                                        placement=placement,
                                        style={
                                            'width': 400
                                        }
                                    )
                                    for placement in [
                                        'bottomLeft', 'bottomRight',
                                        'topLeft', 'topRight'
                                    ]
                                ],
                                direction='vertical'
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
        fac.AntdSelect(
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            placeholder=f'placement="{placement}"',
            placement=placement,
            style={
                'width': 400
            }
        )
        for placement in [
            'bottomLeft', 'bottomRight',
            'topLeft', 'topRight'
        ]
    ],
    direction='vertical'
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
                            fac.AntdSelect(
                                options=[],
                                emptyContent=fac.AntdResult(
                                    status='warning',
                                    subTitle='暂无可选项',
                                    style={
                                        'padding': 0
                                    }
                                ),
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '自定义无选项时的提示内容',
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
fac.AntdSelect(
    options=[],
    emptyContent=fac.AntdResult(
        status='warning',
        subTitle='暂无可选项',
        style={
            'padding': 0
        }
    ),
    style={
        'width': 200
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
                        id='自定义无选项时的提示内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                options=[
                                    {
                                        'label': f'选项{i}',
                                        'value': f'选项{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                dropdownBefore=fac.AntdInput(
                                    mode='text-area',
                                    placeholder='dropdownBefore示例',
                                    autoSize=True
                                ),
                                dropdownAfter=fac.AntdButton(
                                    'dropdownAfter示例',
                                    type='primary',
                                    block=True
                                ),
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                '开头和末尾添加额外元素',
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
fac.AntdSelect(
    options=[
        {
            'label': f'选项{i}',
            'value': f'选项{i}'
        }
        for i in range(1, 6)
    ],
    dropdownBefore=fac.AntdInput(
        mode='text-area',
        placeholder='dropdownBefore示例',
        autoSize=True
    ),
    dropdownAfter=fac.AntdButton(
        'dropdownAfter示例',
        type='primary',
        block=True
    ),
    style={
        'width': 200
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
                        id='开头和末尾添加额外元素',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        id='select-multiple-mode-search-demo-switch-mode',
                                        options=[
                                            {
                                                'label': mode,
                                                'value': mode
                                            }
                                            for mode in [
                                                'case-insensitive',
                                                'case-sensitive',
                                                'regex'
                                            ]
                                        ],
                                        defaultValue='case-insensitive',
                                        optionType='button'
                                    ),
                                    fac.AntdSelect(
                                        id='select-multiple-mode-search-demo',
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in list('AbCdEf')
                                        ],
                                        style={
                                            'width': 200
                                        }
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '多模式搜索',
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
        fac.AntdRadioGroup(
            id='select-multiple-mode-search-demo-switch-mode',
            options=[
                {
                    'label': mode,
                    'value': mode
                }
                for mode in [
                    'case-insensitive',
                    'case-sensitive',
                    'regex'
                ]
            ],
            defaultValue='case-insensitive',
            optionType='button'
        ),
        fac.AntdSelect(
            id='select-multiple-mode-search-demo',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in list('AbCdEf')
            ],
            style={
                'width': 200
            }
        )
    ],
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

@app.callback(
    Output('select-multiple-mode-search-demo', 'optionFilterMode'),
    Input('select-multiple-mode-search-demo-switch-mode', 'value')
)
def select_multiple_mode_search_demo(value):

    return value
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
                        id='多模式搜索',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        id='select-demo1',
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdText(
                                        id='select-demo1-output'
                                    )
                                ],
                                align='center',
                                style={
                                    'width': '100%',
                                    'marginBottom': 20
                                }
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        id='select-demo2',
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        mode='multiple',
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdText(
                                        id='select-demo2-output'
                                    )
                                ],
                                align='center',
                                style={
                                    'width': '100%'
                                }
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
fac.AntdSpace(
    [
        fac.AntdSelect(
            id='select-demo1',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            style={
                'width': 200
            }
        ),
        fac.AntdText(
            id='select-demo1-output'
        )
    ],
    align='center',
    style={
        'width': '100%',
        'marginBottom': 20
    }
),

fac.AntdSpace(
    [
        fac.AntdSelect(
            id='select-demo2',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            mode='multiple',
            style={
                'width': 200
            }
        ),
        fac.AntdText(
            id='select-demo2-output'
        )
    ],
    align='center',
    style={
        'width': '100%'
    }
)

...

@app.callback(
    Output('select-demo1-output', 'children'),
    Input('select-demo1', 'value'),
)
def select_demo1(value):

    return f'value: {value}'


@app.callback(
    Output('select-demo2-output', 'children'),
    Input('select-demo2', 'value'),
)
def select_demo2(value):

    return f'value: {value}'
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
                            fac.AntdDivider(
                                '监听searchValue',
                                innerTextOrientation='left'
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        id='select-search-value-demo',
                                        placeholder='请输入',
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdText(
                                        id='select-search-value-demo-output'
                                    )
                                ],
                                align='center'
                            ),

                            fac.AntdDivider(
                                '500毫秒防抖监听debounceSearchValue',
                                innerTextOrientation='left'
                            ),

                            fac.AntdSpace(
                                [
                                    fac.AntdSelect(
                                        id='select-debounce-search-value-demo',
                                        placeholder='请输入',
                                        debounceWait=500,
                                        options=[
                                            {
                                                'label': f'选项{i}',
                                                'value': f'选项{i}'
                                            }
                                            for i in range(1, 6)
                                        ],
                                        style={
                                            'width': 200
                                        }
                                    ),
                                    fac.AntdText(
                                        id='select-debounce-search-value-demo-output'
                                    )
                                ],
                                align='center'
                            ),

                            fac.AntdDivider(
                                '监听搜索内容',
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
    '监听searchValue',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdSelect(
            id='select-search-value-demo',
            placeholder='请输入',
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            style={
                'width': 200
            }
        ),
        fac.AntdText(
            id='select-search-value-demo-output'
        )
    ],
    align='center'
),

fac.AntdDivider(
    '500毫秒防抖监听debounceSearchValue',
    innerTextOrientation='left'
),

fac.AntdSpace(
    [
        fac.AntdSelect(
            id='select-debounce-search-value-demo',
            placeholder='请输入',
            debounceWait=500,
            options=[
                {
                    'label': f'选项{i}',
                    'value': f'选项{i}'
                }
                for i in range(1, 6)
            ],
            style={
                'width': 200
            }
        ),
        fac.AntdText(
            id='select-debounce-search-value-demo-output'
        )
    ],
    align='center'
)

...

@app.callback(
    Output('select-search-value-demo-output', 'children'),
    Input('select-search-value-demo', 'searchValue')
)
def select_search_value_demo(searchValue):

    return f'searchValue: {searchValue}'


@app.callback(
    Output('select-debounce-search-value-demo-output', 'children'),
    Input('select-debounce-search-value-demo', 'debounceSearchValue')
)
def select_debounce_search_value_demo(debounceSearchValue):

    return f'debounceSearchValue: {debounceSearchValue}'
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
                        id='监听搜索内容',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSelect(
                                id='select-auto-spin-remote-load-options',
                                placeholder='请输入要搜索的内容',
                                options=[],
                                autoSpin=True,
                                debounceWait=200,
                                style={
                                    'width': 250
                                }
                            ),

                            fac.AntdDivider(
                                '配合autoSpin实现远程选项加载',
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
fac.AntdSelect(
    id='select-auto-spin-remote-load-options',
    placeholder='请输入要搜索的内容',
    options=[],
    autoSpin=True,
    debounceWait=200,
    style={
        'width': 250
    }
)

...

import time

...

@app.callback(
    Output('select-auto-spin-remote-load-options', 'options'),
    Input('select-auto-spin-remote-load-options', 'debounceSearchValue')
)
def select_auto_spin_remote_load_options_demo(debounceSearchValue):

    if debounceSearchValue:

        time.sleep(1)

        return [
            {
                'label': f'{debounceSearchValue}模拟选项{i}',
                'value': f'{debounceSearchValue}模拟选项{i}'
            }
            for i in range(1, 6)
        ]

    return []
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
                        id='配合autoSpin实现远程选项加载',
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
                        {'title': '多选模式', 'href': '#多选模式'},
                        {'title': '自由新增模式', 'href': '#自由新增模式'},
                        {'title': '下拉选项分组', 'href': '#下拉选项分组'},
                        {'title': '下拉菜单最大高度', 'href': '#下拉菜单最大高度'},
                        {'title': '色带选择模式', 'href': '#色带选择模式'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '自动获取焦点', 'href': '#自动获取焦点'},
                        {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                        {'title': '无边框', 'href': '#无边框'},
                        {'title': '不同的悬浮层展开方向', 'href': '#不同的悬浮层展开方向'},
                        {'title': '自定义无选项时的提示内容', 'href': '#自定义无选项时的提示内容'},
                        {'title': '开头和末尾添加额外元素', 'href': '#开头和末尾添加额外元素'},
                        {'title': '多模式搜索', 'href': '#多模式搜索'},
                        {'title': '回调示例', 'href': '#回调示例'},
                        {'title': '监听搜索内容', 'href': '#监听搜索内容'},
                        {'title': '配合autoSpin实现远程选项加载',
                            'href': '#配合autoSpin实现远程选项加载'},
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
                component_name='AntdSelect',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
