from dash import html
from faker import Faker
from datetime import datetime
import feffery_antd_components as fac
import feffery_markdown_components as fmc

# 绑定回调
import callbacks.table_basic_c
from .side_props import render_side_props_layout

faker = Faker(locale='zh_CN')


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
                                'title': '基础使用'
                            }
                        ]
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText('　　本页文档展示了AntdTable组件的基础功能。')
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'int型示例',
                                        'dataIndex': 'int型示例'
                                    },
                                    {
                                        'title': 'float型示例',
                                        'dataIndex': 'float型示例'
                                    },
                                    {
                                        'title': 'str型示例',
                                        'dataIndex': 'str型示例'
                                    },
                                    {
                                        'title': '日期时间示例',
                                        'dataIndex': '日期时间示例'
                                    },
                                ],
                                data=[
                                    {
                                        'int型示例': 123,
                                        'float型示例': 1.23,
                                        'str型示例': '示例字符',
                                        '日期时间示例': datetime.now()
                                    }
                                ] * 3
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
from datetime import datetime

...

fac.AntdTable(
    columns=[
        {
            'title': 'int型示例',
            'dataIndex': 'int型示例'
        },
        {
            'title': 'float型示例',
            'dataIndex': 'float型示例'
        },
        {
            'title': 'str型示例',
            'dataIndex': 'str型示例'
        },
        {
            'title': '日期时间示例',
            'dataIndex': '日期时间示例'
        },
    ],
    data=[
        {
            'int型示例': 123,
            'float型示例': 1.23,
            'str型示例': '示例字符',
            '日期时间示例': datetime.now()
        }
    ] * 3
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
                        id='设置列宽'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': f'字段{i}',
                                        'dataIndex': f'字段{i}',
                                        'width': width
                                    }
                                    for i, width in zip(
                                        range(1, 6),
                                        [
                                            '10%', '20%', '30%', '25%', '15%'
                                        ]
                                    )
                                ],
                                data=[
                                    {
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    }
                                ] * 3
                            ),

                            fac.AntdDivider(
                                '百分比列宽',
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
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': width
        }
        for i, width in zip(
            range(1, 6),
            [
                '10%', '20%', '30%', '25%', '15%'
            ]
        )
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 3
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
                        id='百分比列宽',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': f'字段{i}',
                                        'dataIndex': f'字段{i}',
                                        'width': width
                                    }
                                    for i, width in zip(
                                        range(1, 6),
                                        [
                                            50, 100, 50, 100, 50
                                        ]
                                    )
                                ],
                                data=[
                                    {
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    }
                                ] * 3
                            ),

                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': f'字段{i}',
                                        'dataIndex': f'字段{i}',
                                        'width': width
                                    }
                                    for i, width in zip(
                                        range(1, 6),
                                        [
                                            5000, 10000, 5000, 10000, 5000
                                        ]
                                    )
                                ],
                                data=[
                                    {
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    }
                                ] * 3
                            ),

                            fac.AntdDivider(
                                '数值型列宽',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '默认情况下，为各字段设置数值型列宽后，会自动计算转换为比例，作为各个字段的百分比列宽'
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
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': width
        }
        for i, width in zip(
            range(1, 6),
            [
                50, 100, 50, 100, 50
            ]
        )
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 3
),

fac.AntdTable(
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': width
        }
        for i, width in zip(
            range(1, 6),
            [
                5000, 10000, 5000, 10000, 5000
            ]
        )
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 3
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
                        id='数值型列宽',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': f'字段{i}',
                                        'dataIndex': f'字段{i}',
                                        'width': 'calc(100% / 5)'
                                    }
                                    for i in range(1, 6)
                                ],
                                data=[
                                    {
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    }
                                ] * 3
                            ),

                            fac.AntdDivider(
                                '自定义css列宽',
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
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': 'calc(100% / 5)'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 3
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
                        id='自定义css列宽',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': f'字段{i}',
                                        'dataIndex': f'字段{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                data=[
                                    {
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    }
                                ] * 10,
                                maxHeight=150
                            ),

                            fac.AntdDivider(
                                'maxHeight的使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '设置参数',
                                    fac.AntdText(
                                        'maxHeight',
                                        code=True
                                    ),
                                    '后，当表格实际像素高度超出',
                                    fac.AntdText(
                                        'maxHeight',
                                        code=True
                                    ),
                                    '所设定值时，会自动开启滚动条'
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
            'title': f'字段{i}',
            'dataIndex': f'字段{i}'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 10,
    maxHeight=150
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
                        id='maxHeight的使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            html.Div(
                                fac.AntdTable(
                                    columns=[
                                        {
                                            'title': f'字段{i}',
                                            'dataIndex': f'字段{i}'
                                        }
                                        for i in range(1, 6)
                                    ],
                                    data=[
                                        {
                                            f'字段{i}': '示例内容'
                                            for i in range(1, 6)
                                        }
                                    ] * 3,
                                    maxWidth=900
                                ),
                                style={
                                    'width': 700,
                                    'margin': '0 auto'
                                }
                            ),

                            fac.AntdDivider(
                                'maxWidth的使用',
                                lineColor='#f0f0f0',
                                innerTextOrientation='left'
                            ),

                            fac.AntdParagraph(
                                [
                                    '设置参数',
                                    fac.AntdText(
                                        'maxWidth',
                                        code=True
                                    ),
                                    '后，当表格实际像素宽度小于',
                                    fac.AntdText(
                                        'maxWidth',
                                        code=True
                                    ),
                                    '所设定值时，会自动开启横向滚动条'
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
    fac.AntdTable(
        columns=[
            {
                'title': f'字段{i}',
                'dataIndex': f'字段{i}'
            }
            for i in range(1, 6)
        ],
        data=[
            {
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            }
        ] * 3,
        maxWidth=900
    ),
    style={
        'width': 700,
        'margin': '0 auto'
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
                        id='maxWidth的使用',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '冻结在左侧',
                                innerTextOrientation='left'
                            ),
                            html.Div(
                                fac.AntdTable(
                                    columns=[
                                        {
                                            'title': f'字段{i}',
                                            'dataIndex': f'字段{i}',
                                            'fixed': 'left' if i == 1 else None
                                        }
                                        for i in range(1, 6)
                                    ],
                                    data=[
                                        {
                                            f'字段{i}': '示例内容'
                                            for i in range(1, 6)
                                        }
                                    ] * 3,
                                    maxWidth=900
                                ),
                                style={
                                    'width': 700,
                                    'margin': '0 auto'
                                }
                            ),

                            fac.AntdDivider(
                                '冻结在右侧',
                                innerTextOrientation='left'
                            ),
                            html.Div(
                                fac.AntdTable(
                                    columns=[
                                        {
                                            'title': f'字段{i}',
                                            'dataIndex': f'字段{i}',
                                            'fixed': 'right' if i == 5 else None
                                        }
                                        for i in range(1, 6)
                                    ],
                                    data=[
                                        {
                                            f'字段{i}': '示例内容'
                                            for i in range(1, 6)
                                        }
                                    ] * 3,
                                    maxWidth=900
                                ),
                                style={
                                    'width': 700,
                                    'margin': '0 auto'
                                }
                            ),

                            fac.AntdDivider(
                                '双侧同时冻结',
                                innerTextOrientation='left'
                            ),
                            html.Div(
                                fac.AntdTable(
                                    columns=[
                                        {
                                            'title': f'字段{i}',
                                            'dataIndex': f'字段{i}',
                                            'fixed': (
                                                'left' if i == 1
                                                else (
                                                    'right' if i == 5
                                                    else None
                                                )
                                            )
                                        }
                                        for i in range(1, 6)
                                    ],
                                    data=[
                                        {
                                            f'字段{i}': '示例内容'
                                            for i in range(1, 6)
                                        }
                                    ] * 3,
                                    maxWidth=900
                                ),
                                style={
                                    'width': 700,
                                    'margin': '0 auto'
                                }
                            ),

                            fac.AntdDivider(
                                '冻结部分列',
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
    '冻结在左侧',
    innerTextOrientation='left'
),
html.Div(
    fac.AntdTable(
        columns=[
            {
                'title': f'字段{i}',
                'dataIndex': f'字段{i}',
                'fixed': 'left' if i == 1 else None
            }
            for i in range(1, 6)
        ],
        data=[
            {
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            }
        ] * 3,
        maxWidth=900
    ),
    style={
        'width': 700,
        'margin': '0 auto'
    }
),

fac.AntdDivider(
    '冻结在右侧',
    innerTextOrientation='left'
),
html.Div(
    fac.AntdTable(
        columns=[
            {
                'title': f'字段{i}',
                'dataIndex': f'字段{i}',
                'fixed': 'right' if i == 5 else None
            }
            for i in range(1, 6)
        ],
        data=[
            {
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            }
        ] * 3,
        maxWidth=900
    ),
    style={
        'width': 700,
        'margin': '0 auto'
    }
),

fac.AntdDivider(
    '双侧同时冻结',
    innerTextOrientation='left'
),
html.Div(
    fac.AntdTable(
        columns=[
            {
                'title': f'字段{i}',
                'dataIndex': f'字段{i}',
                'fixed': (
                    'left' if i == 1
                    else (
                        'right' if i == 5
                        else None
                    )
                )
            }
            for i in range(1, 6)
        ],
        data=[
            {
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            }
        ] * 3,
        maxWidth=900
    ),
    style={
        'width': 700,
        'margin': '0 auto'
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
                        id='冻结部分列',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': f'字段{i}',
                                        'dataIndex': f'字段{i}'
                                    }
                                    for i in range(1, 6)
                                ],
                                data=[
                                    {
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    }
                                ] * 3,
                                bordered=True
                            ),

                            fac.AntdDivider(
                                '添加边框线',
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
            'title': f'字段{i}',
            'dataIndex': f'字段{i}'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 3,
    bordered=True
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
                        id='添加边框线',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': align,
                                        'dataIndex': align,
                                        'align': align
                                    }
                                    for align in [
                                        'left', 'center', 'right'
                                    ]
                                ],
                                data=[
                                    {
                                        align: 999
                                        for align in [
                                            'left', 'center', 'right'
                                        ]
                                    }
                                ] * 3,
                                bordered=True
                            ),

                            fac.AntdDivider(
                                '字段内容对齐方式',
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
            'title': align,
            'dataIndex': align,
            'align': align
        }
        for align in [
            'left', 'center', 'right'
        ]
    ],
    data=[
        {
            align: 999
            for align in [
                'left', 'center', 'right'
            ]
        }
    ] * 3,
    bordered=True
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
                        id='字段内容对齐方式',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': 'int型示例',
                                        'dataIndex': 'int型示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                    {
                                        'title': 'float型示例',
                                        'dataIndex': 'float型示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                    {
                                        'title': 'str型示例',
                                        'dataIndex': 'str型示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                    {
                                        'title': '日期时间示例',
                                        'dataIndex': '日期时间示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                ],
                                data=[
                                    {
                                        'int型示例': 123,
                                        'float型示例': 1.23,
                                        'str型示例': '示例字符',
                                        '日期时间示例': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    }
                                ] * 3,
                                bordered=True
                            ),

                            fac.AntdDivider(
                                '可编辑单元格',
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
            'title': 'int型示例',
            'dataIndex': 'int型示例',
            'editable': True,
            'width': '25%'
        },
        {
            'title': 'float型示例',
            'dataIndex': 'float型示例',
            'editable': True,
            'width': '25%'
        },
        {
            'title': 'str型示例',
            'dataIndex': 'str型示例',
            'editable': True,
            'width': '25%'
        },
        {
            'title': '日期时间示例',
            'dataIndex': '日期时间示例',
            'editable': True,
            'width': '25%'
        },
    ],
    data=[
        {
            'int型示例': 123,
            'float型示例': 1.23,
            'str型示例': '示例字符',
            '日期时间示例': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    ] * 3,
    bordered=True
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
                        id='可编辑单元格',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTable(
                                id='table-editable-demo',
                                columns=[
                                    {
                                        'title': 'int型示例',
                                        'dataIndex': 'int型示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                    {
                                        'title': 'float型示例',
                                        'dataIndex': 'float型示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                    {
                                        'title': 'str型示例',
                                        'dataIndex': 'str型示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                    {
                                        'title': '日期时间示例',
                                        'dataIndex': '日期时间示例',
                                        'editable': True,
                                        'width': '25%'
                                    },
                                ],
                                data=[
                                    {
                                        'key': f'row-{i}',
                                        'int型示例': 123,
                                        'float型示例': 1.23,
                                        'str型示例': '示例字符',
                                        '日期时间示例': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    }
                                    for i in range(1, 4)
                                ],
                                bordered=True
                            ),

                            html.Pre(
                                id='table-editable-demo-output'
                            ),

                            fac.AntdDivider(
                                '通过回调监听编辑记录',
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
    id='table-editable-demo',
    columns=[
        {
            'title': 'int型示例',
            'dataIndex': 'int型示例',
            'editable': True,
            'width': '25%'
        },
        {
            'title': 'float型示例',
            'dataIndex': 'float型示例',
            'editable': True,
            'width': '25%'
        },
        {
            'title': 'str型示例',
            'dataIndex': 'str型示例',
            'editable': True,
            'width': '25%'
        },
        {
            'title': '日期时间示例',
            'dataIndex': '日期时间示例',
            'editable': True,
            'width': '25%'
        },
    ],
    data=[
        {
            'key': f'row-{i}',
            'int型示例': 123,
            'float型示例': 1.23,
            'str型示例': '示例字符',
            '日期时间示例': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        for i in range(1, 4)
    ],
    bordered=True
),

html.Pre(
    id='table-editable-demo-output'
)

...

import json

...

@app.callback(
    Output('table-editable-demo-output', 'children'),
    Input('table-editable-demo', 'recentlyChangedRow'),
    prevent_initial_call=True
)
def table_editable_demo(recentlyChangedRow):

    return json.dumps(
        recentlyChangedRow,
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
                        id='通过回调监听编辑记录',
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdSpace(
                                        [
                                            fac.AntdDivider(
                                                f'size="{size}"',
                                                innerTextOrientation='left'
                                            ),
                                            fac.AntdTable(
                                                columns=[
                                                    {
                                                        'title': 'int型示例',
                                                        'dataIndex': 'int型示例'
                                                    },
                                                    {
                                                        'title': 'float型示例',
                                                        'dataIndex': 'float型示例'
                                                    },
                                                    {
                                                        'title': 'str型示例',
                                                        'dataIndex': 'str型示例'
                                                    },
                                                    {
                                                        'title': '日期时间示例',
                                                        'dataIndex': '日期时间示例'
                                                    },
                                                ],
                                                data=[
                                                    {
                                                        'int型示例': 123,
                                                        'float型示例': 1.23,
                                                        'str型示例': '示例字符',
                                                        '日期时间示例': datetime.now()
                                                    }
                                                ],
                                                size=size,
                                                bordered=True
                                            )
                                        ],
                                        direction='vertical',
                                        style={
                                            'width': '100%'
                                        }
                                    )
                                    for size in ['small', 'default', 'large']
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
        fac.AntdSpace(
            [
                fac.AntdDivider(
                    f'size="{size}"',
                    innerTextOrientation='left'
                ),
                fac.AntdTable(
                    columns=[
                        {
                            'title': 'int型示例',
                            'dataIndex': 'int型示例'
                        },
                        {
                            'title': 'float型示例',
                            'dataIndex': 'float型示例'
                        },
                        {
                            'title': 'str型示例',
                            'dataIndex': 'str型示例'
                        },
                        {
                            'title': '日期时间示例',
                            'dataIndex': '日期时间示例'
                        },
                    ],
                    data=[
                        {
                            'int型示例': 123,
                            'float型示例': 1.23,
                            'str型示例': '示例字符',
                            '日期时间示例': datetime.now()
                        }
                    ],
                    size=size,
                    bordered=True
                )
            ],
            direction='vertical',
            style={
                'width': '100%'
            }
        )
        for size in ['small', 'default', 'large']
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
                            fac.AntdTable(
                                columns=[
                                    {
                                        'title': '字段1-1',
                                        'dataIndex': '字段1-1',
                                        'group': '字段1'
                                    },
                                    {
                                        'title': '字段1-2',
                                        'dataIndex': '字段1-2',
                                        'group': '字段1'
                                    },
                                    {
                                        'title': '字段2',
                                        'dataIndex': '字段2'
                                    },
                                    {
                                        'title': '字段3-1',
                                        'dataIndex': '字段3-1',
                                        'group': '字段3'
                                    },
                                    {
                                        'title': '字段3-2',
                                        'dataIndex': '字段3-2',
                                        'group': '字段3'
                                    },
                                    {
                                        'title': '字段3-3',
                                        'dataIndex': '字段3-3',
                                        'group': '字段3'
                                    },
                                ],
                                data=[
                                    {
                                        '字段1-1': 1,
                                        '字段1-2': 1,
                                        '字段2': 1,
                                        '字段3-1': 1,
                                        '字段3-2': 1,
                                        '字段3-3': 1
                                    }
                                ] * 5,
                                bordered=True
                            ),

                            fac.AntdDivider(
                                '为字段分组',
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
            'title': '字段1-1',
            'dataIndex': '字段1-1',
            'group': '字段1'
        },
        {
            'title': '字段1-2',
            'dataIndex': '字段1-2',
            'group': '字段1'
        },
        {
            'title': '字段2',
            'dataIndex': '字段2'
        },
        {
            'title': '字段3-1',
            'dataIndex': '字段3-1',
            'group': '字段3'
        },
        {
            'title': '字段3-2',
            'dataIndex': '字段3-2',
            'group': '字段3'
        },
        {
            'title': '字段3-3',
            'dataIndex': '字段3-3',
            'group': '字段3'
        },
    ],
    data=[
        {
            '字段1-1': 1,
            '字段1-2': 1,
            '字段2': 1,
            '字段3-1': 1,
            '字段3-2': 1,
            '字段3-3': 1
        }
    ] * 5,
    bordered=True
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
                        id='为字段分组',
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
                        {'title': '基础使用', 'href': '#基础使用'},
                        {
                            'title': '设置列宽',
                            'href': '#设置列宽',
                            'children': [
                                {
                                    'title': '百分比列宽',
                                    'href': '#百分比列宽'
                                },
                                {
                                    'title': '数值型列宽',
                                    'href': '#数值型列宽'
                                },
                                {
                                    'title': '自定义css列宽',
                                    'href': '#自定义css列宽'
                                }
                            ]
                        },
                        {'title': 'maxHeight的使用', 'href': '#maxHeight的使用'},
                        {'title': 'maxWidth的使用', 'href': '#maxWidth的使用'},
                        {'title': '冻结部分列', 'href': '#冻结部分列'},
                        {'title': '添加边框线', 'href': '#添加边框线'},
                        {'title': '字段内容对齐方式', 'href': '#字段内容对齐方式'},
                        {'title': '可编辑单元格', 'href': '#可编辑单元格'},
                        {'title': '通过回调监听编辑记录', 'href': '#通过回调监听编辑记录'},
                        {'title': '不同的尺寸规格', 'href': '#不同的尺寸规格'},
                        {'title': '为字段分组', 'href': '#为字段分组'},
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
