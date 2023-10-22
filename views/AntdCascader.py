from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdCascader
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
                                'title': 'AntdCascader 级联选择'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　用于为用户提供一组具有层级信息的选项进行选择。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ]
                            ),

                            fac.AntdDivider(
                                '基础使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText('　　默认参数下，'),
                                    fac.AntdText('AntdCascader', strong=True),
                                    fac.AntdText('以单选的模式，供用户进行末端叶节点的选择')
                                ]
                            ),

                            fac.AntdCollapse(
                                fmc.FefferySyntaxHighlighter(
                                    showCopyButton=True,
                                    showLineNumbers=True,
                                    language='python',
                                    codeTheme='coy-without-shadows',
                                    codeString='''
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
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
                            fac.AntdSpace(
                                [
                                    fac.AntdCascader(
                                        placeholder=f'placement="{placement}"',
                                        options=[
                                            {
                                                'value': '节点1',
                                                'label': '节点1',
                                                'children': [
                                                    {
                                                        'value': '节点1-1',
                                                        'label': '节点1-1'
                                                    },
                                                    {
                                                        'value': '节点1-2',
                                                        'label': '节点1-2',
                                                        'children': [
                                                            {
                                                                'value': '节点1-2-1',
                                                                'label': '节点1-2-1'
                                                            },
                                                            {
                                                                'value': '节点1-2-2',
                                                                'label': '节点1-2-2'
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ],
                                        placement=placement,
                                        style={
                                            'width': '200px'
                                        }
                                    )
                                    for placement in [
                                        'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
                                    ]
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                '不同的悬浮层展开方位',
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
        fac.AntdCascader(
            placeholder=f'placement="{placement}"',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                }
            ],
            placement=placement,
            style={
                'width': '200px'
            }
        )
        for placement in [
            'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
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
                        id='不同的悬浮层展开方位',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ],
                                expandTrigger='hover',
                                style={
                                    'width': '200px'
                                }
                            ),

                            fac.AntdDivider(
                                '鼠标悬停触发子选项展开',
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
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        }
    ],
    expandTrigger='hover',
    style={
        'width': '200px'
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
                        id='鼠标悬停触发子选项展开',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCascader(
                                placeholder='多选模式：',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                multiple=True,
                                style={
                                    'width': '200px'
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
fac.AntdCascader(
    placeholder='多选模式：',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    multiple=True,
    style={
        'width': '200px'
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
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                changeOnSelect=True,
                                style={
                                    'width': '200px'
                                }
                            ),

                            fac.AntdDivider(
                                '允许非末端节点被选中',
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
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    changeOnSelect=True,
    style={
        'width': '200px'
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
                        id='允许非末端节点被选中',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCascader(
                                placeholder='请选择',
                                optionsMode='flat',
                                options=[
                                    {
                                        'value': '1',
                                        'label': '节点1',
                                        'key': '1'
                                    },
                                    *[
                                        {
                                            'value': f'1-{i}',
                                            'label': f'节点1-{i}',
                                            'key': f'1-{i}',
                                            'parent': '1'
                                        }
                                        for i in range(1, 4)
                                    ],
                                    {
                                        'value': '2',
                                        'label': '节点2',
                                        'key': '2'
                                    },
                                    {
                                        'value': '2-1',
                                        'label': '节点2-1',
                                        'key': '2-1',
                                        'parent': '2'
                                    },
                                    {
                                        'value': '2-2',
                                        'label': '节点2-2',
                                        'key': '2-2',
                                        'parent': '2'
                                    },
                                    *[
                                        {
                                            'value': f'2-2-{i}',
                                            'label': f'节点2-2-{i}',
                                            'key': f'2-2-{i}',
                                            'parent': '2-2'
                                        }
                                        for i in range(1, 4)
                                    ],
                                ]
                            ),

                            fac.AntdDivider(
                                '扁平options模式',
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
fac.AntdCascader(
    placeholder='请选择',
    optionsMode='flat',
    options=[
        {
            'value': '1',
            'label': '节点1',
            'key': '1'
        },
        *[
            {
                'value': f'1-{i}',
                'label': f'节点1-{i}',
                'key': f'1-{i}',
                'parent': '1'
            }
            for i in range(1, 4)
        ],
        {
            'value': '2',
            'label': '节点2',
            'key': '2'
        },
        {
            'value': '2-1',
            'label': '节点2-1',
            'key': '2-1',
            'parent': '2'
        },
        {
            'value': '2-2',
            'label': '节点2-2',
            'key': '2-2',
            'parent': '2'
        },
        *[
            {
                'value': f'2-2-{i}',
                'label': f'节点2-2-{i}',
                'key': f'2-2-{i}',
                'parent': '2-2'
            }
            for i in range(1, 4)
        ],
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
                        id='扁平options模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                disabled=True
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
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    disabled=True
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
                            fac.AntdDivider(
                                'showCheckedStrategy="show-parent"（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                multiple=True
                            ),

                            fac.AntdDivider(
                                'showCheckedStrategy="show-child"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdCascader(
                                placeholder='请选择（单选）',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                showCheckedStrategy='show-child'
                            ),
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                showCheckedStrategy='show-child',
                                multiple=True
                            ),

                            fac.AntdDivider(
                                '已选项回填策略',
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
    'showCheckedStrategy="show-parent"（默认）',
    innerTextOrientation='left'
),
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    multiple=True
),

fac.AntdDivider(
    'showCheckedStrategy="show-child"',
    innerTextOrientation='left'
),
fac.AntdCascader(
    placeholder='请选择（单选）',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    showCheckedStrategy='show-child'
),
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    showCheckedStrategy='show-child',
    multiple=True
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
                        id='已选项回填策略',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdCascader(
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                readOnly=True,
                                value=[
                                    ['节点1', '节点1-1']
                                ]
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
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    readOnly=True,
    value=[
        ['节点1', '节点1-1']
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
                        id='只读状态',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdCascader(
                                        placeholder=f'status="{status}"',
                                        options=[
                                            {
                                                'value': '节点1',
                                                'label': '节点1',
                                                'children': [
                                                    {
                                                        'value': '节点1-1',
                                                        'label': '节点1-1'
                                                    },
                                                    {
                                                        'value': '节点1-2',
                                                        'label': '节点1-2',
                                                        'children': [
                                                            {
                                                                'value': '节点1-2-1',
                                                                'label': '节点1-2-1'
                                                            },
                                                            {
                                                                'value': '节点1-2-2',
                                                                'label': '节点1-2-2'
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'value': '节点2',
                                                'label': '节点2',
                                                'children': [
                                                    {
                                                        'value': '节点2-1',
                                                        'label': '节点2-1'
                                                    },
                                                    {
                                                        'value': '节点2-2',
                                                        'label': '节点2-2'
                                                    }
                                                ]
                                            }
                                        ],
                                        status=status
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
        fac.AntdCascader(
            placeholder=f'status="{status}"',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            status=status
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
                            fac.AntdDivider(
                                'changeOnSelect=False（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdCascader(
                                        id='cascader-demo1',
                                        placeholder='请选择',
                                        options=[
                                            {
                                                'value': '节点1',
                                                'label': '节点1',
                                                'children': [
                                                    {
                                                        'value': '节点1-1',
                                                        'label': '节点1-1'
                                                    },
                                                    {
                                                        'value': '节点1-2',
                                                        'label': '节点1-2',
                                                        'children': [
                                                            {
                                                                'value': '节点1-2-1',
                                                                'label': '节点1-2-1'
                                                            },
                                                            {
                                                                'value': '节点1-2-2',
                                                                'label': '节点1-2-2'
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'value': '节点2',
                                                'label': '节点2',
                                                'children': [
                                                    {
                                                        'value': '节点2-1',
                                                        'label': '节点2-1'
                                                    },
                                                    {
                                                        'value': '节点2-2',
                                                        'label': '节点2-2'
                                                    }
                                                ]
                                            }
                                        ],
                                        style={
                                            'width': '200px'
                                        }
                                    ),
                                    fac.AntdText(id='cascader-demo1-output')
                                ]
                            ),

                            fac.AntdDivider(
                                'changeOnSelect=True',
                                innerTextOrientation='left'
                            ),
                            fac.AntdSpace(
                                [
                                    fac.AntdCascader(
                                        id='cascader-demo2',
                                        placeholder='请选择',
                                        options=[
                                            {
                                                'value': '节点1',
                                                'label': '节点1',
                                                'children': [
                                                    {
                                                        'value': '节点1-1',
                                                        'label': '节点1-1'
                                                    },
                                                    {
                                                        'value': '节点1-2',
                                                        'label': '节点1-2',
                                                        'children': [
                                                            {
                                                                'value': '节点1-2-1',
                                                                'label': '节点1-2-1'
                                                            },
                                                            {
                                                                'value': '节点1-2-2',
                                                                'label': '节点1-2-2'
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                'value': '节点2',
                                                'label': '节点2',
                                                'children': [
                                                    {
                                                        'value': '节点2-1',
                                                        'label': '节点2-1'
                                                    },
                                                    {
                                                        'value': '节点2-2',
                                                        'label': '节点2-2'
                                                    }
                                                ]
                                            }
                                        ],
                                        changeOnSelect=True,
                                        style={
                                            'width': '200px'
                                        }
                                    ),
                                    fac.AntdText(id='cascader-demo2-output')
                                ]
                            ),

                            fac.AntdDivider(
                                '多选模式',
                                innerTextOrientation='left'
                            ),
                            fac.AntdCascader(
                                id='cascader-demo3',
                                placeholder='请选择',
                                options=[
                                    {
                                        'value': '节点1',
                                        'label': '节点1',
                                        'children': [
                                            {
                                                'value': '节点1-1',
                                                'label': '节点1-1'
                                            },
                                            {
                                                'value': '节点1-2',
                                                'label': '节点1-2',
                                                'children': [
                                                    {
                                                        'value': '节点1-2-1',
                                                        'label': '节点1-2-1'
                                                    },
                                                    {
                                                        'value': '节点1-2-2',
                                                        'label': '节点1-2-2'
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        'value': '节点2',
                                        'label': '节点2',
                                        'children': [
                                            {
                                                'value': '节点2-1',
                                                'label': '节点2-1'
                                            },
                                            {
                                                'value': '节点2-2',
                                                'label': '节点2-2'
                                            }
                                        ]
                                    }
                                ],
                                multiple=True,
                                placement='topLeft',
                                style={
                                    'width': '200px'
                                }
                            ),
                            html.Pre(id='cascader-demo3-output'),

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
fac.AntdDivider(
    'changeOnSelect=False（默认）',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdCascader(
            id='cascader-demo1',
            placeholder='请选择',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            style={
                'width': '200px'
            }
        ),
        fac.AntdText(id='cascader-demo1-output')
    ]
),

fac.AntdDivider(
    'changeOnSelect=True',
    innerTextOrientation='left'
),
fac.AntdSpace(
    [
        fac.AntdCascader(
            id='cascader-demo2',
            placeholder='请选择',
            options=[
                {
                    'value': '节点1',
                    'label': '节点1',
                    'children': [
                        {
                            'value': '节点1-1',
                            'label': '节点1-1'
                        },
                        {
                            'value': '节点1-2',
                            'label': '节点1-2',
                            'children': [
                                {
                                    'value': '节点1-2-1',
                                    'label': '节点1-2-1'
                                },
                                {
                                    'value': '节点1-2-2',
                                    'label': '节点1-2-2'
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': '节点2',
                    'label': '节点2',
                    'children': [
                        {
                            'value': '节点2-1',
                            'label': '节点2-1'
                        },
                        {
                            'value': '节点2-2',
                            'label': '节点2-2'
                        }
                    ]
                }
            ],
            changeOnSelect=True,
            style={
                'width': '200px'
            }
        ),
        fac.AntdText(id='cascader-demo2-output')
    ]
),

fac.AntdDivider(
    '多选模式',
    innerTextOrientation='left'
),
fac.AntdCascader(
    id='cascader-demo3',
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    multiple=True,
    placement='topLeft',
    style={
        'width': '200px'
    }
),
html.Pre(id='cascader-demo3-output')

...

@app.callback(
    Output('cascader-demo1-output', 'children'),
    Input('cascader-demo1', 'value'),
    prevent_initial_call=True
)
def cascader_demo1(value):

    return str(value)


@app.callback(
    Output('cascader-demo2-output', 'children'),
    Input('cascader-demo2', 'value'),
    prevent_initial_call=True
)
def cascader_demo2(value):

    return str(value)


@app.callback(
    Output('cascader-demo3-output', 'children'),
    Input('cascader-demo3', 'value'),
    prevent_initial_call=True
)
def cascader_demo3(value):

    return json.dumps(
        value,
        indent=4,
        ensure_ascii=False
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
                        id='回调示例',
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
                        {'title': '不同的悬浮层展开方位', 'href': '#不同的悬浮层展开方位'},
                        {'title': '鼠标悬停触发子选项展开', 'href': '#鼠标悬停触发子选项展开'},
                        {'title': '多选模式', 'href': '#多选模式'},
                        {'title': '允许非末端节点被选中', 'href': '#允许非末端节点被选中'},
                        {'title': '扁平options模式', 'href': '#扁平options模式'},
                        {'title': '禁用状态', 'href': '#禁用状态'},
                        {'title': '已选项回填策略', 'href': '#已选项回填策略'},
                        {'title': '只读状态', 'href': '#只读状态'},
                        {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                        {'title': '回调示例', 'href': '#回调示例'},
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
                component_name='AntdCascader',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
