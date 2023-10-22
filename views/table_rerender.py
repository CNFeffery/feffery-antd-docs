import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.table_rerender_c
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
                                'title': 'AntdTable'
                            },
                            {
                                'title': '再渲染模式'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　本页文档展示了AntdTable组件的各种再渲染模式功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'link示例1',
                                        'dataIndex': 'link示例1',
                                        'renderOptions': {
                                            'renderType': 'link'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'link示例2',
                                        'dataIndex': 'link示例2',
                                        'renderOptions': {
                                            'renderType': 'link',
                                            'renderLinkText': '示例链接'
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'link示例1': {
                                            'content': f'{content}仓库',
                                            'href': href
                                        },
                                        'link示例2': {
                                            'href': '/AntdTable-rerender'
                                        }
                                    }
                                    for href, content in zip(
                                        [
                                            'https://github.com/CNFeffery/feffery-antd-components',
                                            'https://github.com/CNFeffery/feffery-utils-components',
                                            'https://github.com/CNFeffery/feffery-antd-charts',
                                            'https://github.com/CNFeffery/feffery-markdown-components',
                                            'https://github.com/CNFeffery/feffery-leaflet-components'
                                        ],
                                        [
                                            'fac', 'fuc', 'fact', 'fmc', 'flc'
                                        ]
                                    )
                                ],
                                bordered=True,
                                style={
                                    'width': 400
                                }
                            ),

                            fac.AntdDivider(
                                'link链接模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'link示例1',
            'dataIndex': 'link示例1',
            'renderOptions': {
                'renderType': 'link'
            },
            'width': '50%'
        },
        {
            'title': 'link示例2',
            'dataIndex': 'link示例2',
            'renderOptions': {
                'renderType': 'link',
                'renderLinkText': '示例链接'
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'link示例1': {
                'content': f'{content}仓库',
                'href': href
            },
            'link示例2': {
                'href': '/AntdTable-rerender'
            }
        }
        for href, content in zip(
            [
                'https://github.com/CNFeffery/feffery-antd-components',
                'https://github.com/CNFeffery/feffery-utils-components',
                'https://github.com/CNFeffery/feffery-antd-charts',
                'https://github.com/CNFeffery/feffery-markdown-components',
                'https://github.com/CNFeffery/feffery-leaflet-components'
            ],
            [
                'fac', 'fuc', 'fact', 'fmc', 'flc'
            ]
        )
    ],
    bordered=True,
    style={
        'width': 400
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
                        id='link链接模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'ellipsis示例',
                                        'dataIndex': 'ellipsis示例',
                                        'renderOptions': {
                                            'renderType': 'ellipsis'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'ellipsis示例': 'bala'*10
                                    }
                                ],
                                bordered=True,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                'ellipsis长内容省略模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'ellipsis示例',
            'dataIndex': 'ellipsis示例',
            'renderOptions': {
                'renderType': 'ellipsis'
            }
        }
    ],
    data=[
        {
            'ellipsis示例': 'bala'*10
        }
    ],
    bordered=True,
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
                        id='ellipsis长内容省略模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'ellipsis-copyable示例',
                                        'dataIndex': 'ellipsis-copyable示例',
                                        'renderOptions': {
                                            'renderType': 'ellipsis-copyable'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'ellipsis-copyable示例': f'内容示例{i}'*10
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True,
                                style={
                                    'width': 200
                                }
                            ),

                            fac.AntdDivider(
                                'ellipsis-copyable长内容省略+可复制模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'ellipsis-copyable示例',
            'dataIndex': 'ellipsis-copyable示例',
            'renderOptions': {
                'renderType': 'ellipsis-copyable'
            }
        }
    ],
    data=[
        {
            'ellipsis-copyable示例': f'内容示例{i}'*10
        }
        for i in range(1, 4)
    ],
    bordered=True,
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
                        id='ellipsis-copyable长内容省略+可复制模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'tags示例1',
                                        'dataIndex': 'tags示例1',
                                        'renderOptions': {
                                            'renderType': 'tags'
                                        }
                                    },
                                    {
                                        'title': 'tags示例2',
                                        'dataIndex': 'tags示例2',
                                        'renderOptions': {
                                            'renderType': 'tags'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'tags示例1': {
                                            'tag': f'标签{i}',
                                            'color': 'cyan'
                                        },
                                        'tags示例2': [
                                            {
                                                'tag': f'标签{i}-{j}',
                                                'color': color
                                            }
                                            for j, color in zip(
                                                range(1, 4),
                                                [
                                                    'volcano',
                                                    'blue',
                                                    'geekblue'
                                                ]
                                            )
                                        ]
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True,
                                style={
                                    'width': 400
                                }
                            ),

                            fac.AntdDivider(
                                'tags标签模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'tags示例1',
            'dataIndex': 'tags示例1',
            'renderOptions': {
                'renderType': 'tags'
            }
        },
        {
            'title': 'tags示例2',
            'dataIndex': 'tags示例2',
            'renderOptions': {
                'renderType': 'tags'
            }
        }
    ],
    data=[
        {
            'tags示例1': {
                'tag': f'标签{i}',
                'color': 'cyan'
            },
            'tags示例2': [
                {
                    'tag': f'标签{i}-{j}',
                    'color': color
                }
                for j, color in zip(
                    range(1, 4),
                    [
                        'volcano',
                        'blue',
                        'geekblue'
                    ]
                )
            ]
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={
        'width': 400
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
                        id='tags标签模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '状态徽标示例',
                                        'dataIndex': '状态徽标示例',
                                        'renderOptions': {
                                            'renderType': 'status-badge'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'key': i,
                                        '状态徽标示例': {
                                            'status': status,
                                            'text': status + '状态示例'
                                        }
                                    }
                                    for i, status in enumerate(['success', 'processing', 'default', 'error', 'warning'])
                                ],
                                style={
                                    'width': '250px'
                                }
                            ),

                            fac.AntdDivider(
                                'status-badge状态徽标模式',
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
fac.AntdTable(
    columns=[
        {
            'title': '状态徽标示例',
            'dataIndex': '状态徽标示例',
            'renderOptions': {
                'renderType': 'status-badge'
            }
        }
    ],
    data=[
        {
            'key': i,
            '状态徽标示例': {
                'status': status,
                'text': status + '状态示例'
            }
        }
        for i, status in enumerate(['success', 'processing', 'default', 'error', 'warning'])
    ],
    style={
        'width': '250px'
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
                        id='status-badge状态徽标模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '交互式图片',
                                        'dataIndex': '交互式图片',
                                        'renderOptions': {
                                            'renderType': 'image'
                                        }
                                    },
                                    {
                                        'title': '静态图片',
                                        'dataIndex': '静态图片',
                                        'renderOptions': {
                                            'renderType': 'image'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        '交互式图片': {
                                            'src': '/assets/imgs/fac-logo.svg',
                                            'height': '75px'
                                        },
                                        '静态图片': {
                                            'src': '/assets/imgs/fac-logo.svg',
                                            'height': '75px',
                                            'preview': False
                                        }
                                    }
                                    for i in range(5)
                                ],
                                bordered=True,
                                style={
                                    'width': '300px'
                                }
                            ),

                            fac.AntdDivider(
                                'image图片模式',
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
fac.AntdTable(
    columns=[
        {
            'title': '交互式图片',
            'dataIndex': '交互式图片',
            'renderOptions': {
                'renderType': 'image'
            }
        },
        {
            'title': '静态图片',
            'dataIndex': '静态图片',
            'renderOptions': {
                'renderType': 'image'
            }
        }
    ],
    data=[
        {
            '交互式图片': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px'
            },
            '静态图片': {
                'src': '/assets/imgs/fac-logo.svg',
                'height': '75px',
                'preview': False
            }
        }
        for i in range(5)
    ],
    bordered=True,
    style={
        'width': '300px'
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
                        id='image图片模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '数值测试1',
                                        'dataIndex': '数值测试1',
                                        'width': '50%',
                                        'renderOptions': {
                                            'renderType': 'custom-format'
                                        }
                                    },
                                    {
                                        'title': '数值测试2',
                                        'dataIndex': '数值测试2',
                                        'width': '50%',
                                        'renderOptions': {
                                            'renderType': 'custom-format'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        '数值测试1': np.random.rand(),
                                        '数值测试2': np.random.rand()
                                    }
                                    for i in range(10)
                                ],
                                sortOptions={
                                    'sortDataIndexes': ['数值测试1', '数值测试2']
                                },
                                bordered=True,
                                customFormatFuncs={
                                    '数值测试1': '(x) => `${(x*100).toFixed(2)}%`',
                                    '数值测试2': '(x) => x <= 0.5 ? `低水平：${x.toFixed(2)}` : `高水平：${x.toFixed(2)}`',
                                },
                                style={
                                    'width': '500px'
                                }
                            ),

                            fac.AntdDivider(
                                'custom-format自定义格式模式',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    fac.AntdText('在这个例子中，'),
                                    fac.AntdText('数值测试1', strong=True),
                                    fac.AntdText('与'),
                                    fac.AntdText('数值测试2', strong=True),
                                    fac.AntdText('字段本质上都是数值型，但在'),
                                    fac.AntdText("'custom-format'", code=True),
                                    fac.AntdText('模式下，可通过参数'),
                                    fac.AntdText(
                                        'customFormatFuncs', code=True),
                                    fac.AntdText('自定义的js函数来改变单元格中表面上所渲染出的文字内容')
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
fac.AntdTable(
    columns=[
        {
            'title': '数值测试1',
            'dataIndex': '数值测试1',
            'width': '50%',
            'renderOptions': {
                'renderType': 'custom-format'
            }
        },
        {
            'title': '数值测试2',
            'dataIndex': '数值测试2',
            'width': '50%',
            'renderOptions': {
                'renderType': 'custom-format'
            }
        }
    ],
    data=[
        {
            '数值测试1': np.random.rand(),
            '数值测试2': np.random.rand()
        }
        for i in range(10)
    ],
    sortOptions={
        'sortDataIndexes': ['数值测试1', '数值测试2']
    },
    bordered=True,
    customFormatFuncs={
        '数值测试1': '(x) => `${(x*100).toFixed(2)}%`',
        '数值测试2': '(x) => x <= 0.5 ? `低水平：${x.toFixed(2)}` : `高水平：${x.toFixed(2)}`',
    },
    style={
        'width': '500px'
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
                        id='custom-format自定义格式模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                size='small',
                                columns=[
                                    {
                                        'title': '角标模式',
                                        'dataIndex': '角标模式',
                                        'renderOptions': {'renderType': 'corner-mark'}
                                    }
                                ],
                                data=[
                                    {
                                        'key': i,
                                        '角标模式': {
                                            'content': '角标模式',
                                            'color': ['red', 'blue', 'green'][i],
                                            'offsetX': -7.5,
                                            'offsetY': -8.5,
                                            'placement': 'top-left',
                                            'hide': [False, True, False][i]
                                        }
                                    }
                                    for i in range(3)
                                ],
                                bordered=True,
                                style={
                                    'width': '200px'
                                }
                            ),

                            fac.AntdDivider(
                                'corner-mark角标模式',
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

fac.AntdTable(
    size='small',
    columns=[
        {
            'title': '角标模式',
            'dataIndex': '角标模式',
            'renderOptions': {'renderType': 'corner-mark'}
        }
    ],
    data=[
        {
            'key': i,
            '角标模式': {
                'content': '角标模式',
                'color': ['red', 'blue', 'green'][i],
                'offsetX': -7.5,
                'offsetY': -8.5,
                'placement': 'top-left',
                'hide': [False, True, False][i]
            }
        }
        for i in range(3)
    ],
    bordered=True,
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
                        id='corner-mark角标模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'row-merge示例1',
                                        'dataIndex': 'row-merge示例1',
                                        'renderOptions': {
                                            'renderType': 'row-merge'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'row-merge示例2',
                                        'dataIndex': 'row-merge示例2',
                                        'renderOptions': {
                                            'renderType': 'row-merge'
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'row-merge示例1': {
                                            'content': '示例1-1',
                                            'rowSpan': 1
                                        },
                                        'row-merge示例2': {
                                            'content': '示例2-1',
                                            'rowSpan': 2
                                        }
                                    },
                                    {
                                        'row-merge示例1': {
                                            'content': '示例1-2',
                                            'rowSpan': 2
                                        },
                                        'row-merge示例2': {
                                            'rowSpan': 0
                                        }
                                    },
                                    {
                                        'row-merge示例1': {
                                            'rowSpan': 0
                                        },
                                        'row-merge示例2': {
                                            'content': '示例2-2',
                                            'rowSpan': 1
                                        }
                                    }
                                ],
                                bordered=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'row-merge跨行合并单元格模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'row-merge示例1',
            'dataIndex': 'row-merge示例1',
            'renderOptions': {
                'renderType': 'row-merge'
            },
            'width': '50%'
        },
        {
            'title': 'row-merge示例2',
            'dataIndex': 'row-merge示例2',
            'renderOptions': {
                'renderType': 'row-merge'
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'row-merge示例1': {
                'content': '示例1-1',
                'rowSpan': 1
            },
            'row-merge示例2': {
                'content': '示例2-1',
                'rowSpan': 2
            }
        },
        {
            'row-merge示例1': {
                'content': '示例1-2',
                'rowSpan': 2
            },
            'row-merge示例2': {
                'rowSpan': 0
            }
        },
        {
            'row-merge示例1': {
                'rowSpan': 0
            },
            'row-merge示例2': {
                'content': '示例2-2',
                'rowSpan': 1
            }
        }
    ],
    bordered=True,
    style={
        'width': 300
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
                        id='row-merge跨行合并单元格模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'dropdown-links示例1',
                                        'dataIndex': 'dropdown-links示例1',
                                        'renderOptions': {
                                            'renderType': 'dropdown-links'
                                        },
                                        'width': '30%'
                                    },
                                    {
                                        'title': 'dropdown-links示例2',
                                        'dataIndex': 'dropdown-links示例2',
                                        'renderOptions': {
                                            'renderType': 'dropdown-links',
                                            'dropdownProps': {
                                                'title': '更多'
                                            }
                                        },
                                        'width': '70%'
                                    }
                                ],
                                data=[
                                    {
                                        'dropdown-links示例1': [
                                            {
                                                'title': f'image示例{i}.png',
                                                'href': f'assets/imgs/image示例{i}.png'
                                            }
                                            for i in range(1, 8)
                                        ],
                                        'dropdown-links示例2': [
                                            {
                                                'title': f'image示例{i}.png',
                                                'href': f'assets/imgs/image示例{i}.png'
                                            }
                                            for i in range(1, 8)
                                        ]
                                    }
                                ] * 3,
                                bordered=True,
                                style={
                                    'width': 400
                                }
                            ),

                            fac.AntdDivider(
                                'dropdown-links下拉链接菜单模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'dropdown-links示例1',
            'dataIndex': 'dropdown-links示例1',
            'renderOptions': {
                'renderType': 'dropdown-links'
            },
            'width': '30%'
        },
        {
            'title': 'dropdown-links示例2',
            'dataIndex': 'dropdown-links示例2',
            'renderOptions': {
                'renderType': 'dropdown-links',
                'dropdownProps': {
                    'title': '更多'
                }
            },
            'width': '70%'
        }
    ],
    data=[
        {
            'dropdown-links示例1': [
                {
                    'title': f'image示例{i}.png',
                    'href': f'assets/imgs/image示例{i}.png'
                }
                for i in range(1, 8)
            ],
            'dropdown-links示例2': [
                {
                    'title': f'image示例{i}.png',
                    'href': f'assets/imgs/image示例{i}.png'
                }
                for i in range(1, 8)
            ]
        }
    ] * 3,
    bordered=True,
    style={
        'width': 400
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
                        id='dropdown-links下拉链接菜单模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'image-avatar示例1',
                                        'dataIndex': 'image-avatar示例1',
                                        'renderOptions': {
                                            'renderType': 'image-avatar'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'image-avatar示例2',
                                        'dataIndex': 'image-avatar示例2',
                                        'renderOptions': {
                                            'renderType': 'image-avatar'
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'image-avatar示例1': {
                                            'src': 'assets/imgs/avatar-demo.jpg'
                                        },
                                        'image-avatar示例2': {
                                            'src': 'assets/imgs/avatar-demo.jpg',
                                            'shape': 'square'
                                        }
                                    }
                                ] * 3,
                                bordered=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'image-avatar图片型头像模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'image-avatar示例1',
            'dataIndex': 'image-avatar示例1',
            'renderOptions': {
                'renderType': 'image-avatar'
            },
            'width': '50%'
        },
        {
            'title': 'image-avatar示例2',
            'dataIndex': 'image-avatar示例2',
            'renderOptions': {
                'renderType': 'image-avatar'
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'image-avatar示例1': {
                'src': 'assets/imgs/avatar-demo.jpg'
            },
            'image-avatar示例2': {
                'src': 'assets/imgs/avatar-demo.jpg',
                'shape': 'square'
            }
        }
    ] * 3,
    bordered=True,
    style={
        'width': 300
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
                        id='image-avatar图片型头像模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'mini-line示例1',
                                        'dataIndex': 'mini-line示例1',
                                        'renderOptions': {
                                            'renderType': 'mini-line'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'mini-line示例2',
                                        'dataIndex': 'mini-line示例2',
                                        'renderOptions': {
                                            'renderType': 'mini-line',
                                            'tooltipCustomContent': '''(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`'''
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'mini-line示例1': [
                                            np.random.rand()
                                            for i in range(25)
                                        ],
                                        'mini-line示例2': [
                                            np.random.rand()
                                            for i in range(25)
                                        ]
                                    }
                                ] * 3,
                                bordered=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'mini-line迷你折线图模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'mini-line示例1',
            'dataIndex': 'mini-line示例1',
            'renderOptions': {
                'renderType': 'mini-line'
            },
            'width': '50%'
        },
        {
            'title': 'mini-line示例2',
            'dataIndex': 'mini-line示例2',
            'renderOptions': {
                'renderType': 'mini-line',
                'tooltipCustomContent': '''(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`'''
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'mini-line示例1': [
                np.random.rand()
                for i in range(25)
            ],
            'mini-line示例2': [
                np.random.rand()
                for i in range(25)
            ]
        }
    ] * 3,
    bordered=True,
    style={
        'width': 300
    }
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
                        id='mini-line迷你折线图模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'mini-bar示例1',
                                        'dataIndex': 'mini-bar示例1',
                                        'renderOptions': {
                                            'renderType': 'mini-bar'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'mini-bar示例2',
                                        'dataIndex': 'mini-bar示例2',
                                        'renderOptions': {
                                            'renderType': 'mini-bar',
                                            'tooltipCustomContent': '''(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`'''
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'mini-bar示例1': [
                                            np.random.rand()
                                            for i in range(25)
                                        ],
                                        'mini-bar示例2': [
                                            np.random.rand()
                                            for i in range(25)
                                        ]
                                    }
                                ] * 3,
                                bordered=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'mini-bar迷你柱状图模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'mini-bar示例1',
            'dataIndex': 'mini-bar示例1',
            'renderOptions': {
                'renderType': 'mini-bar'
            },
            'width': '50%'
        },
        {
            'title': 'mini-bar示例2',
            'dataIndex': 'mini-bar示例2',
            'renderOptions': {
                'renderType': 'mini-bar',
                'tooltipCustomContent': '''(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`'''
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'mini-bar示例1': [
                np.random.rand()
                for i in range(25)
            ],
            'mini-bar示例2': [
                np.random.rand()
                for i in range(25)
            ]
        }
    ] * 3,
    bordered=True,
    style={
        'width': 300
    }
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
                        id='mini-bar迷你柱状图模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'mini-area示例1',
                                        'dataIndex': 'mini-area示例1',
                                        'renderOptions': {
                                            'renderType': 'mini-area'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'mini-area示例2',
                                        'dataIndex': 'mini-area示例2',
                                        'renderOptions': {
                                            'renderType': 'mini-area',
                                            'tooltipCustomContent': '''(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`'''
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'mini-area示例1': [
                                            np.random.rand()
                                            for i in range(25)
                                        ],
                                        'mini-area示例2': [
                                            np.random.rand()
                                            for i in range(25)
                                        ]
                                    }
                                ] * 3,
                                bordered=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'mini-area迷你面积图模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'mini-area示例1',
            'dataIndex': 'mini-area示例1',
            'renderOptions': {
                'renderType': 'mini-area'
            },
            'width': '50%'
        },
        {
            'title': 'mini-area示例2',
            'dataIndex': 'mini-area示例2',
            'renderOptions': {
                'renderType': 'mini-area',
                'tooltipCustomContent': '''(x, data) => `数值：${data[0]?.data?.y.toFixed(3)}`'''
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'mini-area示例1': [
                np.random.rand()
                for i in range(25)
            ],
            'mini-area示例2': [
                np.random.rand()
                for i in range(25)
            ]
        }
    ] * 3,
    bordered=True,
    style={
        'width': 300
    }
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
                        id='mini-area迷你面积图模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'mini-progress示例1',
                                        'dataIndex': 'mini-progress示例1',
                                        'renderOptions': {
                                            'renderType': 'mini-progress'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'mini-progress示例2',
                                        'dataIndex': 'mini-progress示例2',
                                        'renderOptions': {
                                            'renderType': 'mini-progress',
                                            'progressOneHundredPercentColor': '#f08c00'
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'mini-progress示例1': x,
                                        'mini-progress示例2': x
                                    }
                                    for x in [0, 0.66, 1]
                                ],
                                bordered=True,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'mini-progress迷你进度图模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'mini-progress示例1',
            'dataIndex': 'mini-progress示例1',
            'renderOptions': {
                'renderType': 'mini-progress'
            },
            'width': '50%'
        },
        {
            'title': 'mini-progress示例2',
            'dataIndex': 'mini-progress示例2',
            'renderOptions': {
                'renderType': 'mini-progress',
                'progressOneHundredPercentColor': '#f08c00'
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'mini-progress示例1': x,
            'mini-progress示例2': x
        }
        for x in [0, 0.66, 1]
    ],
    bordered=True,
    style={
        'width': 300
    }
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
                        id='mini-progress迷你进度图模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'mini-ring-progress示例1',
                                        'dataIndex': 'mini-ring-progress示例1',
                                        'renderOptions': {
                                            'renderType': 'mini-ring-progress'
                                        },
                                        'width': '50%'
                                    },
                                    {
                                        'title': 'mini-ring-progress示例2',
                                        'dataIndex': 'mini-ring-progress示例2',
                                        'renderOptions': {
                                            'renderType': 'mini-ring-progress',
                                            'progressOneHundredPercentColor': '#f08c00',
                                            'ringProgressFontSize': 8
                                        },
                                        'width': '50%'
                                    }
                                ],
                                data=[
                                    {
                                        'mini-ring-progress示例1': x,
                                        'mini-ring-progress示例2': x
                                    }
                                    for x in [0, 0.66, 1]
                                ],
                                bordered=True,
                                miniChartHeight=75,
                                style={
                                    'width': 300
                                }
                            ),

                            fac.AntdDivider(
                                'mini-ring-progress迷你环形进度图模式',
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
fac.AntdTable(
    columns=[
        {
            'title': 'mini-ring-progress示例1',
            'dataIndex': 'mini-ring-progress示例1',
            'renderOptions': {
                'renderType': 'mini-ring-progress'
            },
            'width': '50%'
        },
        {
            'title': 'mini-ring-progress示例2',
            'dataIndex': 'mini-ring-progress示例2',
            'renderOptions': {
                'renderType': 'mini-ring-progress',
                'progressOneHundredPercentColor': '#f08c00',
                'ringProgressFontSize': 8
            },
            'width': '50%'
        }
    ],
    data=[
        {
            'mini-ring-progress示例1': x,
            'mini-ring-progress示例2': x
        }
        for x in [0, 0.66, 1]
    ],
    bordered=True,
    miniChartHeight=75,
    style={
        'width': 300
    }
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
                        id='mini-ring-progress迷你环形进度图模式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                id='table-rerender-button-demo',
                                columns=[
                                    {
                                        'title': 'button示例1',
                                        'dataIndex': 'button示例1',
                                        'renderOptions': {
                                            'renderType': 'button'
                                        }
                                    },
                                    {
                                        'title': 'button示例2',
                                        'dataIndex': 'button示例2',
                                        'renderOptions': {
                                            'renderType': 'button'
                                        }
                                    },
                                    {
                                        'title': 'button示例3',
                                        'dataIndex': 'button示例3',
                                        'renderOptions': {
                                            'renderType': 'button',
                                            'renderButtonPopConfirmProps': {
                                                'title': '确认执行？',
                                                'okText': '确认',
                                                'cancelText': '取消'
                                            }
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'button示例1': {
                                            'content': f'按钮1-{i}',
                                            'type': 'link',
                                            'custom': 'balabalabalabala'
                                        },
                                        'button示例2': [
                                            {
                                                'content': f'按钮2-{i}-{j}',
                                                'type': 'primary',
                                                'custom': 'balabalabalabala'
                                            }
                                            for j in range(1, 3)
                                        ],
                                        'button示例3': [
                                            {
                                                'content': f'按钮3-{i}-{j}',
                                                'type': 'dashed',
                                                'danger': True,
                                                'custom': 'balabalabalabala'
                                            }
                                            for j in range(1, 3)
                                        ]
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True
                            ),

                            html.Pre(
                                id='table-rerender-button-demo-output'
                            ),

                            fac.AntdDivider(
                                'button按钮模式及回调示例',
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
fac.AntdTable(
    id='table-rerender-button-demo',
    columns=[
        {
            'title': 'button示例1',
            'dataIndex': 'button示例1',
            'renderOptions': {
                'renderType': 'button'
            }
        },
        {
            'title': 'button示例2',
            'dataIndex': 'button示例2',
            'renderOptions': {
                'renderType': 'button'
            }
        },
        {
            'title': 'button示例3',
            'dataIndex': 'button示例3',
            'renderOptions': {
                'renderType': 'button',
                'renderButtonPopConfirmProps': {
                    'title': '确认执行？',
                    'okText': '确认',
                    'cancelText': '取消'
                }
            }
        }
    ],
    data=[
        {
            'button示例1': {
                'content': f'按钮1-{i}',
                'type': 'link',
                'custom': 'balabalabalabala'
            },
            'button示例2': [
                {
                    'content': f'按钮2-{i}-{j}',
                    'type': 'primary',
                    'custom': 'balabalabalabala'
                }
                for j in range(1, 3)
            ],
            'button示例3': [
                {
                    'content': f'按钮3-{i}-{j}',
                    'type': 'dashed',
                    'danger': True,
                    'custom': 'balabalabalabala'
                }
                for j in range(1, 3)
            ]
        }
        for i in range(1, 4)
    ],
    bordered=True
),

html.Pre(
    id='table-rerender-button-demo-output'
)

...

import json

...

@app.callback(
    Output('table-rerender-button-demo-output', 'children'),
    Input('table-rerender-button-demo', 'nClicksButton'),
    [State('table-rerender-button-demo', 'clickedContent'),
     State('table-rerender-button-demo', 'clickedCustom'),
     State('table-rerender-button-demo', 'recentlyButtonClickedDataIndex'),
     State('table-rerender-button-demo', 'recentlyButtonClickedRow')],
    prevent_initial_call=True
)
def table_rerender_button_demo(nClicksButton,
                               clickedContent,
                               clickedCustom,
                               recentlyButtonClickedDataIndex,
                               recentlyButtonClickedRow):

    return json.dumps(
        dict(
            nClicksButton=nClicksButton,
            clickedContent=clickedContent,
            clickedCustom=clickedCustom,
            recentlyButtonClickedDataIndex=recentlyButtonClickedDataIndex,
            recentlyButtonClickedRow=recentlyButtonClickedRow
        ),
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
                        id='button按钮模式及回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                id='table-rerender-checkbox-demo',
                                columns=[
                                    {
                                        'title': 'checkbox示例',
                                        'dataIndex': 'checkbox示例',
                                        'renderOptions': {
                                            'renderType': 'checkbox'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'checkbox示例': {
                                            'checked': i % 2 == 0,
                                            'label': f'选项{i}',
                                            'custom': 'balabalabalabala'
                                        }
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True,
                                style={
                                    'width': 200
                                }
                            ),

                            html.Pre(
                                id='table-rerender-checkbox-demo-output'
                            ),

                            fac.AntdDivider(
                                'checkbox勾选框模式及回调示例',
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
fac.AntdTable(
    id='table-rerender-checkbox-demo',
    columns=[
        {
            'title': 'checkbox示例',
            'dataIndex': 'checkbox示例',
            'renderOptions': {
                'renderType': 'checkbox'
            }
        }
    ],
    data=[
        {
            'checkbox示例': {
                'checked': i % 2 == 0,
                'label': f'选项{i}',
                'custom': 'balabalabalabala'
            }
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={
        'width': 200
    }
),

html.Pre(
    id='table-rerender-checkbox-demo-output'
)

...

import json

...

@app.callback(
    Output('table-rerender-checkbox-demo-output', 'children'),
    [Input('table-rerender-checkbox-demo', 'recentlyCheckedLabel'),
     Input('table-rerender-checkbox-demo', 'recentlyCheckedDataIndex'),
     Input('table-rerender-checkbox-demo', 'recentlyCheckedStatus'),
     Input('table-rerender-checkbox-demo', 'recentlyCheckedRow')],
    prevent_initial_call=True
)
def table_rerender_checkbox_demo(recentlyCheckedLabel,
                                 recentlyCheckedDataIndex,
                                 recentlyCheckedStatus,
                                 recentlyCheckedRow):

    return json.dumps(
        dict(
            recentlyCheckedLabel=recentlyCheckedLabel,
            recentlyCheckedDataIndex=recentlyCheckedDataIndex,
            recentlyCheckedStatus=recentlyCheckedStatus,
            recentlyCheckedRow=recentlyCheckedRow
        ),
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
                        id='checkbox勾选框模式及回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                id='table-rerender-switch-demo',
                                columns=[
                                    {
                                        'title': 'switch示例',
                                        'dataIndex': 'switch示例',
                                        'renderOptions': {
                                            'renderType': 'switch'
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'switch示例': {
                                            'checked': i % 2 == 0,
                                            'checkedChildren': '开',
                                            'unCheckedChildren': '关',
                                            'custom': 'balabalabalabala'
                                        }
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True,
                                style={
                                    'width': 200
                                }
                            ),

                            html.Pre(
                                id='table-rerender-switch-demo-output'
                            ),

                            fac.AntdDivider(
                                'switch开关模式及回调示例',
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
fac.AntdTable(
    id='table-rerender-switch-demo',
    columns=[
        {
            'title': 'switch示例',
            'dataIndex': 'switch示例',
            'renderOptions': {
                'renderType': 'switch'
            }
        }
    ],
    data=[
        {
            'switch示例': {
                'checked': i % 2 == 0,
                'checkedChildren': '开',
                'unCheckedChildren': '关',
                'custom': 'balabalabalabala'
            }
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={
        'width': 200
    }
),

html.Pre(
    id='table-rerender-switch-demo-output'
)

...

import json

...

@app.callback(
    Output('table-rerender-switch-demo-output', 'children'),
    [Input('table-rerender-switch-demo', 'recentlySwitchDataIndex'),
     Input('table-rerender-switch-demo', 'recentlySwitchStatus'),
     Input('table-rerender-switch-demo', 'recentlySwitchRow')],
    prevent_initial_call=True
)
def table_rerender_switch_demo(recentlySwitchDataIndex,
                               recentlySwitchStatus,
                               recentlySwitchRow):

    return json.dumps(
        dict(
            recentlySwitchDataIndex=recentlySwitchDataIndex,
            recentlySwitchStatus=recentlySwitchStatus,
            recentlySwitchRow=recentlySwitchRow
        ),
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
                        id='switch开关模式及回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                id='table-rerender-dropdown-demo',
                                columns=[
                                    {
                                        'title': 'dropdown示例1',
                                        'dataIndex': 'dropdown示例1',
                                        'renderOptions': {
                                            'renderType': 'dropdown'
                                        }
                                    },
                                    {
                                        'title': 'dropdown示例2',
                                        'dataIndex': 'dropdown示例2',
                                        'renderOptions': {
                                            'renderType': 'dropdown',
                                            'dropdownProps': {
                                                'title': '更多'
                                            }
                                        }
                                    }
                                ],
                                data=[
                                    {
                                        'dropdown示例1': [
                                            {
                                                'title': f'示例1-{i}-{j}',
                                                'custom': 'balabalabalabala'
                                            }
                                            for j in range(1, 6)
                                        ],
                                        'dropdown示例2': [
                                            {
                                                'title': f'示例2-{i}-{j}',
                                                'custom': 'balabalabalabala'
                                            }
                                            for j in range(1, 6)
                                        ]
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True,
                                style={
                                    'width': 200
                                }
                            ),

                            html.Pre(
                                id='table-rerender-dropdown-demo-output'
                            ),

                            fac.AntdDivider(
                                'dropdown下拉选择菜单模式及回调示例',
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
fac.AntdTable(
    id='table-rerender-dropdown-demo',
    columns=[
        {
            'title': 'dropdown示例1',
            'dataIndex': 'dropdown示例1',
            'renderOptions': {
                'renderType': 'dropdown'
            }
        },
        {
            'title': 'dropdown示例2',
            'dataIndex': 'dropdown示例2',
            'renderOptions': {
                'renderType': 'dropdown',
                'dropdownProps': {
                    'title': '更多'
                }
            }
        }
    ],
    data=[
        {
            'dropdown示例1': [
                {
                    'title': f'示例1-{i}-{j}',
                    'custom': 'balabalabalabala'
                }
                for j in range(1, 6)
            ],
            'dropdown示例2': [
                {
                    'title': f'示例2-{i}-{j}',
                    'custom': 'balabalabalabala'
                }
                for j in range(1, 6)
            ]
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={
        'width': 200
    }
),

html.Pre(
    id='table-rerender-dropdown-demo-output'
)

...

import json

...

@app.callback(
    Output('table-rerender-dropdown-demo-output', 'children'),
    Input('table-rerender-dropdown-demo', 'nClicksDropdownItem'),
    [State('table-rerender-dropdown-demo', 'recentlyClickedDropdownItemTitle'),
     State('table-rerender-dropdown-demo',
           'recentlyDropdownItemClickedDataIndex'),
     State('table-rerender-dropdown-demo', 'recentlyDropdownItemClickedRow')],
    prevent_initial_call=True
)
def table_rerender_dropdown_demo(nClicksDropdownItem,
                                 recentlyClickedDropdownItemTitle,
                                 recentlyDropdownItemClickedDataIndex,
                                 recentlyDropdownItemClickedRow):

    return json.dumps(
        dict(
            nClicksDropdownItem=nClicksDropdownItem,
            recentlyClickedDropdownItemTitle=recentlyClickedDropdownItemTitle,
            recentlyDropdownItemClickedDataIndex=recentlyDropdownItemClickedDataIndex,
            recentlyDropdownItemClickedRow=recentlyDropdownItemClickedRow
        ),
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
                        id='dropdown下拉选择菜单模式及回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                id='table-rerender-select-demo',
                                columns=[
                                    {
                                        'title': 'select示例1',
                                        'dataIndex': 'select示例1',
                                        'renderOptions': {
                                            'renderType': 'select'
                                        },
                                        'width': 'calc(100% / 3)'
                                    },
                                    {
                                        'title': 'select示例2',
                                        'dataIndex': 'select示例2',
                                        'renderOptions': {
                                            'renderType': 'select'
                                        },
                                        'width': 'calc(100% / 3)'
                                    },
                                    {
                                        'title': 'select示例3',
                                        'dataIndex': 'select示例3',
                                        'renderOptions': {
                                            'renderType': 'select'
                                        },
                                        'width': 'calc(100% / 3)'
                                    }
                                ],
                                data=[
                                    {
                                        'select示例1': {
                                            'options': [
                                                {
                                                    'label': f'选项{j}',
                                                    'value': f'选项{j}'
                                                }
                                                for j in range(5)
                                            ],
                                            'allowClear': True,
                                            'placeholder': '请选择'
                                        },
                                        'select示例2': {
                                            'options': [
                                                {
                                                    'label': f'选项{j}',
                                                    'value': f'选项{j}'
                                                }
                                                for j in range(5)
                                            ],
                                            'mode': 'multiple',
                                            'allowClear': True,
                                            'placeholder': '请选择'
                                        },
                                        'select示例3': {
                                            'options': [
                                                {
                                                    'label': f'选项{j}',
                                                    'value': f'选项{j}'
                                                }
                                                for j in range(5)
                                            ],
                                            'mode': 'tags',
                                            'allowClear': True,
                                            'placeholder': '请选择'
                                        }
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True,
                                style={
                                    'width': 600
                                }
                            ),

                            html.Pre(
                                id='table-rerender-select-demo-output'
                            ),

                            fac.AntdDivider(
                                'select下拉选择模式及回调示例',
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
fac.AntdTable(
    id='table-rerender-select-demo',
    columns=[
        {
            'title': 'select示例1',
            'dataIndex': 'select示例1',
            'renderOptions': {
                'renderType': 'select'
            },
            'width': 'calc(100% / 3)'
        },
        {
            'title': 'select示例2',
            'dataIndex': 'select示例2',
            'renderOptions': {
                'renderType': 'select'
            },
            'width': 'calc(100% / 3)'
        },
        {
            'title': 'select示例3',
            'dataIndex': 'select示例3',
            'renderOptions': {
                'renderType': 'select'
            },
            'width': 'calc(100% / 3)'
        }
    ],
    data=[
        {
            'select示例1': {
                'options': [
                    {
                        'label': f'选项{j}',
                        'value': f'选项{j}'
                    }
                    for j in range(5)
                ],
                'allowClear': True,
                'placeholder': '请选择'
            },
            'select示例2': {
                'options': [
                    {
                        'label': f'选项{j}',
                        'value': f'选项{j}'
                    }
                    for j in range(5)
                ],
                'mode': 'multiple',
                'allowClear': True,
                'placeholder': '请选择'
            },
            'select示例3': {
                'options': [
                    {
                        'label': f'选项{j}',
                        'value': f'选项{j}'
                    }
                    for j in range(5)
                ],
                'mode': 'tags',
                'allowClear': True,
                'placeholder': '请选择'
            }
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={
        'width': 600
    }
),

html.Pre(
    id='table-rerender-select-demo-output'
)

...

import json

...

@app.callback(
    Output('table-rerender-select-demo-output', 'children'),
    [Input('table-rerender-select-demo', 'recentlySelectRow'),
     Input('table-rerender-select-demo', 'recentlySelectDataIndex'),
     Input('table-rerender-select-demo', 'recentlySelectValue')],
    prevent_initial_call=True
)
def table_rerender_select_demo(recentlySelectRow,
                               recentlySelectDataIndex,
                               recentlySelectValue):

    return json.dumps(
        dict(
            recentlySelectRow=recentlySelectRow,
            recentlySelectDataIndex=recentlySelectDataIndex,
            recentlySelectValue=recentlySelectValue
        ),
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
                        id='select下拉选择模式及回调示例',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '自定义元素示例',
                                        'dataIndex': '自定义元素示例'
                                    }
                                ],
                                data=[
                                    {
                                        '自定义元素示例': html.Div(
                                            fac.AntdText(
                                                '示例内容'*100,
                                                style={
                                                    'textIndent': '2rem'
                                                }
                                            ),
                                            style={
                                                'maxHeight': 50,
                                                'overflowY': 'auto',
                                                'textAlign': 'left'
                                            }
                                        )
                                    },
                                    {
                                        '自定义元素示例': fmc.FefferyMarkdown(
                                            markdownStr='''
```python
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
```
'''
                                        )
                                    },
                                    {
                                        '自定义元素示例': fuc.FefferyQRCode(
                                            value='FefferyQRCode示例'
                                        )
                                    }
                                ],
                                bordered=True,
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '自定义单元格元素',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '目前已有的快捷再渲染模式满足不了你的需求？没关系，任何组件元素都可以作为单元格值被传入😉！',
                                    '（此特性建议仅用作静态展示使用）'
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
fac.AntdTable(
    columns=[
        {
            'title': '自定义元素示例',
            'dataIndex': '自定义元素示例'
        }
    ],
    data=[
        {
            '自定义元素示例': html.Div(
                fac.AntdText(
                    '示例内容'*100,
                    style={
                        'textIndent': '2rem'
                    }
                ),
                style={
                    'maxHeight': 50,
                    'overflowY': 'auto',
                    'textAlign': 'left'
                }
            )
        },
        {
            '自定义元素示例': fmc.FefferyMarkdown(
                markdownStr='''
```python
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc
```
'''
            )
        },
        {
            '自定义元素示例': fuc.FefferyQRCode(
                value='FefferyQRCode示例'
            )
        }
    ],
    bordered=True,
    style={
        'width': '100%'
    }
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
                        id='自定义单元格元素',
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
                        {'title': 'link链接模式', 'href': '#link链接模式'},
                        {'title': 'ellipsis长内容省略模式', 'href': '#ellipsis长内容省略模式'},
                        {'title': 'copyable可复制模式', 'href': '#copyable可复制模式'},
                        {
                            'title': 'ellipsis-copyable长内容省略+可复制模式',
                            'href': '#ellipsis-copyable长内容省略+可复制模式'
                        },
                        {'title': 'tags标签模式', 'href': '#tags标签模式'},
                        {'title': 'status-badge状态徽标模式',
                            'href': '#status-badge状态徽标模式'},
                        {'title': 'image图片模式', 'href': '#image图片模式'},
                        {
                            'title': 'custom-format自定义格式模式',
                            'href': '#custom-format自定义格式模式'
                        },
                        {'title': 'corner-mark角标模式', 'href': '#corner-mark角标模式'},
                        {'title': 'row-merge跨行合并单元格模式',
                            'href': '#row-merge跨行合并单元格模式'},
                        {
                            'title': 'dropdown-links下拉链接菜单模式',
                            'href': '#dropdown-links下拉链接菜单模式'
                        },
                        {
                            'title': 'image-avatar图片型头像模式',
                            'href': '#image-avatar图片型头像模式'
                        },
                        {'title': 'mini-line迷你折线图模式', 'href': '#mini-line迷你折线图模式'},
                        {'title': 'mini-bar迷你柱状图模式', 'href': '#mini-bar迷你柱状图模式'},
                        {'title': 'mini-area迷你面积图模式', 'href': '#mini-area迷你面积图模式'},
                        {
                            'title': 'mini-progress迷你进度图模式',
                            'href': '#mini-progress迷你进度图模式'
                        },
                        {
                            'title': 'mini-ring-progress迷你环形进度图模式',
                            'href': '#mini-ring-progress迷你环形进度图模式'
                        },
                        {'title': 'button按钮模式及回调示例', 'href': '#button按钮模式及回调示例'},
                        {
                            'title': 'checkbox勾选框模式及回调示例',
                            'href': '#checkbox勾选框模式及回调示例'
                        },
                        {'title': 'switch开关模式及回调示例', 'href': '#switch开关模式及回调示例'},
                        {
                            'title': 'dropdown下拉选择菜单模式及回调示例',
                            'href': '#dropdown下拉选择菜单模式及回调示例'
                        },
                        {
                            'title': 'select下拉选择模式及回调示例',
                            'href': '#select下拉选择模式及回调示例'
                        },
                        {
                            'title': '自定义单元格元素',
                            'href': '#自定义单元格元素'
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
                component_name='AntdTable',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
