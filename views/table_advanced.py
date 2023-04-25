import random
import numpy as np
from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.table_advanced_c
from .side_props import render_side_props_layout

docs_content = html.Div(
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
                            'title': '进阶使用'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        fac.AntdText('　　本页文档展示了AntdTable组件的进阶功能。')
                    ]
                ),

                html.Div(
                    id='行选择功能'
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
                                    **{
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    },
                                    'key': f'row-{row+1}'
                                }
                                for row in range(3)
                            ],
                            rowSelectionType='radio'
                        ),

                        fac.AntdDivider(
                            '单选模式',
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
            **{
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            },
            'key': f'row-{row+1}'
        }
        for row in range(3)
    ],
    rowSelectionType='radio'
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
                    id='单选模式',
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
                                    **{
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    },
                                    'key': f'row-{row+1}'
                                }
                                for row in range(3)
                            ],
                            rowSelectionType='checkbox'
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
            **{
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            },
            'key': f'row-{row+1}'
        }
        for row in range(3)
    ],
    rowSelectionType='checkbox'
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
                        fac.AntdTable(
                            id='table-row-selection-demo',
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}'
                                }
                                for i in range(1, 4)
                            ],
                            data=[
                                {
                                    **{
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 4)
                                    },
                                    'key': f'row-{row+1}'
                                }
                                for row in range(3)
                            ],
                            rowSelectionType='checkbox'
                        ),

                        html.Pre(
                            id='table-row-selection-demo-output'
                        ),

                        fac.AntdDivider(
                            '监听已选行key值',
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
    id='table-row-selection-demo',
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}'
        }
        for i in range(1, 4)
    ],
    data=[
        {
            **{
                f'字段{i}': '示例内容'
                for i in range(1, 4)
            },
            'key': f'row-{row+1}'
        }
        for row in range(3)
    ],
    rowSelectionType='checkbox'
),

html.Pre(
    id='table-row-selection-demo-output'
)

...

import json

...

@app.callback(
    Output('table-row-selection-demo-output', 'children'),
    [Input('table-row-selection-demo', 'selectedRowKeys'),
     Input('table-row-selection-demo', 'selectedRows')],
    prevent_initial_call=True
)
def table_row_selection_demo(selectedRowKeys, selectedRows):

    return json.dumps(
        dict(
            selectedRowKeys=selectedRowKeys,
            selectedRows=selectedRows
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
                    id='监听已选行key值',
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
                                for i in range(1, 4)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 4)
                                }
                                for row in range(30)
                            ],
                            sticky=True,
                            size='large',
                            pagination={
                                'pageSize': 999
                            }
                        ),

                        fac.AntdDivider(
                            '粘性表头功能',
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
        for i in range(1, 4)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 4)
        }
        for row in range(30)
    ],
    sticky=True,
    size='large',
    pagination={
        'pageSize': 999
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
                    id='粘性表头功能',
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
                                    **{
                                        f'字段{i}': '示例内容'
                                        for i in range(1, 6)
                                    },
                                    'key': f'row-{row+1}'
                                }
                                for row in range(3)
                            ],
                            titlePopoverInfo={
                                f'字段{i}': {
                                    'title': f'字段{i}说明',
                                    'content': f'这是字段{i}的说明巴拉巴拉巴拉',
                                    'placement': 'top'
                                }
                                for i in range(1, 6)
                            }
                        ),

                        fac.AntdDivider(
                            '字段标题额外说明信息',
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
            **{
                f'字段{i}': '示例内容'
                for i in range(1, 6)
            },
            'key': f'row-{row+1}'
        }
        for row in range(3)
    ],
    titlePopoverInfo={
        f'字段{i}': {
            'title': f'字段{i}说明',
            'content': f'这是字段{i}的说明巴拉巴拉巴拉',
            'placement': 'top'
        }
        for i in range(1, 6)
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
                    id='字段标题额外说明信息',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '纯数字约束',
                                    'dataIndex': '纯数字约束',
                                    'editable': True,
                                    'width': '25%'
                                },
                                {
                                    'title': '纯字母约束',
                                    'dataIndex': '纯字母约束',
                                    'editable': True,
                                    'width': '25%'
                                },
                                {
                                    'title': '日期格式约束',
                                    'dataIndex': '日期格式约束',
                                    'editable': True,
                                    'width': '25%'
                                },
                                {
                                    'title': '纯汉字约束',
                                    'dataIndex': '纯汉字约束',
                                    'editable': True,
                                    'width': '25%'
                                }
                            ],
                            data=[
                                {
                                    '纯数字约束': '12345',
                                    '纯字母约束': 'fac',
                                    '日期格式约束': '2099-01-01',
                                    '纯汉字约束': '测试'
                                }
                            ],
                            columnsFormatConstraint={
                                '纯数字约束': {
                                    'rule': '^[0-9]+$',
                                    'content': '不符合纯数字输入要求'
                                },
                                '纯字母约束': {
                                    'rule': '^[a-zA-Z]+$',
                                    'content': '不符合纯字母输入要求'
                                },
                                '日期格式约束': {
                                    'rule': '^\d{4}-\d{2}-\d{2}$',
                                    'content': '不符合日期格式输入要求'
                                },
                                '纯汉字约束': {
                                    'rule': '^[\u4e00-\u9fa5]+$',
                                    'content': '不符合纯汉字输入要求'
                                }
                            }
                        ),

                        fac.AntdDivider(
                            '编辑模式配置内容格式校验',
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
            'title': '纯数字约束',
            'dataIndex': '纯数字约束',
            'editable': True,
            'width': '25%'
        },
        {
            'title': '纯字母约束',
            'dataIndex': '纯字母约束',
            'editable': True,
            'width': '25%'
        },
        {
            'title': '日期格式约束',
            'dataIndex': '日期格式约束',
            'editable': True,
            'width': '25%'
        },
        {
            'title': '纯汉字约束',
            'dataIndex': '纯汉字约束',
            'editable': True,
            'width': '25%'
        }
    ],
    data=[
        {
            '纯数字约束': '12345',
            '纯字母约束': 'fac',
            '日期格式约束': '2099-01-01',
            '纯汉字约束': '测试'
        }
    ],
    columnsFormatConstraint={
        '纯数字约束': {
            'rule': '^[0-9]+$',
            'content': '不符合纯数字输入要求'
        },
        '纯字母约束': {
            'rule': '^[a-zA-Z]+$',
            'content': '不符合纯字母输入要求'
        },
        '日期格式约束': {
            'rule': '^\d{4}-\d{2}-\d{2}$',
            'content': '不符合日期格式输入要求'
        },
        '纯汉字约束': {
            'rule': '^[\u4e00-\u9fa5]+$',
            'content': '不符合纯汉字输入要求'
        }
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
                    id='编辑模式配置内容格式校验',
                    className='div-highlight'
                ),

                html.Div(
                    id='排序功能'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': 'int型示例',
                                    'dataIndex': 'int型示例',
                                    'width': '25%'
                                },
                                {
                                    'title': 'float型示例',
                                    'dataIndex': 'float型示例',
                                    'width': '25%'
                                },
                                {
                                    'title': 'str型示例',
                                    'dataIndex': 'str型示例',
                                    'width': '25%'
                                },
                                {
                                    'title': '日期时间示例',
                                    'dataIndex': '日期时间示例',
                                    'width': '25%'
                                },
                            ],
                            data=[
                                {
                                    'int型示例': i,
                                    'float型示例': round(i * 0.1, 1),
                                    'str型示例': f'示例字符{i}',
                                    '日期时间示例': f'2099-01-0{i}'
                                }
                                for i in [4, 2, 1, 5, 3]
                            ],
                            sortOptions={
                                'sortDataIndexes': [
                                    'int型示例', 'float型示例',
                                    'str型示例', '日期时间示例'
                                ]
                            }
                        ),

                        fac.AntdDivider(
                            '单字段排序',
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
            'width': '25%'
        },
        {
            'title': 'float型示例',
            'dataIndex': 'float型示例',
            'width': '25%'
        },
        {
            'title': 'str型示例',
            'dataIndex': 'str型示例',
            'width': '25%'
        },
        {
            'title': '日期时间示例',
            'dataIndex': '日期时间示例',
            'width': '25%'
        },
    ],
    data=[
        {
            'int型示例': i,
            'float型示例': round(i * 0.1, 1),
            'str型示例': f'示例字符{i}',
            '日期时间示例': f'2099-01-0{i}'
        }
        for i in [4, 2, 1, 5, 3]
    ],
    sortOptions={
        'sortDataIndexes': [
            'int型示例', 'float型示例',
            'str型示例', '日期时间示例'
        ]
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
                    id='单字段排序',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{j}': random.randint(1, 4)
                                    for j in range(1, 6)
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            sortOptions={
                                'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                                'multiple': True
                            }
                        ),

                        fac.AntdDivider(
                            '多字段组合排序',
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
import random

...

fac.AntdTable(
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{j}': random.randint(1, 4)
            for j in range(1, 6)
        }
        for i in range(10)
    ],
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
        'multiple': True
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
                    id='多字段组合排序',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{j}': random.randint(1, 4)
                                    for j in range(1, 6)
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            sortOptions={
                                'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                                'multiple': 'auto'
                            }
                        ),

                        fac.AntdDivider(
                            '多字段组合排序（动态优先级）',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '设置参数',
                                fac.AntdText(
                                    '"multiple": "auto"',
                                    code=True
                                ),
                                '后，多字段组合排序的字段优先级顺序将动态遵循用户的排序点击顺序'
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
import random

...

fac.AntdTable(
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{j}': random.randint(1, 4)
            for j in range(1, 6)
        }
        for i in range(10)
    ],
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
        'multiple': 'auto'
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
                    id='多字段组合排序（动态优先级）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            id='table-sort-demo',
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{j}': random.randint(1, 4)
                                    for j in range(1, 6)
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            sortOptions={
                                'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                                'multiple': True
                            }
                        ),

                        html.Pre(
                            id='table-sort-demo-output'
                        ),

                        fac.AntdDivider(
                            '监听排序情况',
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
import json

...

fac.AntdTable(
    id='table-sort-demo',
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{j}': random.randint(1, 4)
            for j in range(1, 6)
        }
        for i in range(10)
    ],
    bordered=True,
    sortOptions={
        'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
        'multiple': True
    }
),

html.Pre(
    id='table-sort-demo-output'
)

...

import json

...

@app.callback(
    Output('table-sort-demo-output', 'children'),
    Input('table-sort-demo', 'sorter'),
    prevent_initial_call=True
)
def table_sort_demo(sorter):

    return json.dumps(
        sorter,
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
                    id='监听排序情况',
                    className='div-highlight'
                ),

                html.Div(
                    id='筛选功能'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '基础示例',
                                    'dataIndex': '基础示例',
                                    'width': '25%'
                                },
                                {
                                    'title': '自定义选项',
                                    'dataIndex': '自定义选项',
                                    'width': '25%'
                                },
                                {
                                    'title': '单选模式',
                                    'dataIndex': '单选模式',
                                    'width': '25%'
                                },
                                {
                                    'title': '启用搜索框',
                                    'dataIndex': '启用搜索框',
                                    'width': '25%'
                                }
                            ],
                            data=[
                                {
                                    '基础示例': s,
                                    '自定义选项': s,
                                    '单选模式': s,
                                    '启用搜索框': s,
                                }
                                for s in list('abced')
                            ],
                            filterOptions={
                                '基础示例': {},
                                '自定义选项': {
                                    'filterCustomItems': list('abcdefghijk')
                                },
                                '单选模式': {
                                    'filterMultiple': False
                                },
                                '启用搜索框': {
                                    'filterSearch': True
                                }
                            }
                        ),

                        fac.AntdDivider(
                            '勾选型筛选',
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
            'title': '基础示例',
            'dataIndex': '基础示例',
            'width': '25%'
        },
        {
            'title': '自定义选项',
            'dataIndex': '自定义选项',
            'width': '25%'
        },
        {
            'title': '单选模式',
            'dataIndex': '单选模式',
            'width': '25%'
        },
        {
            'title': '启用搜索框',
            'dataIndex': '启用搜索框',
            'width': '25%'
        }
    ],
    data=[
        {
            '基础示例': s,
            '自定义选项': s,
            '单选模式': s,
            '启用搜索框': s,
        }
        for s in list('abced')
    ],
    filterOptions={
        '基础示例': {},
        '自定义选项': {
            'filterCustomItems': list('abcdefghijk')
        },
        '单选模式': {
            'filterMultiple': False
        },
        '启用搜索框': {
            'filterSearch': True
        }
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
                    id='勾选型筛选',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '搜索型筛选',
                                    'dataIndex': '搜索型筛选',
                                }
                            ],
                            data=[
                                {
                                    '搜索型筛选': s
                                }
                                for s in list('abced')
                            ],
                            filterOptions={
                                '搜索型筛选': {
                                    'filterMode': 'keyword'
                                }
                            },
                            style={
                                'width': 200
                            }
                        ),

                        fac.AntdDivider(
                            '搜索型筛选',
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
            'title': '搜索型筛选',
            'dataIndex': '搜索型筛选',
        }
    ],
    data=[
        {
            '搜索型筛选': s
        }
        for s in list('abced')
    ],
    filterOptions={
        '搜索型筛选': {
            'filterMode': 'keyword'
        }
    },
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
                    id='搜索型筛选',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            id='table-filter-demo',
                            columns=[
                                {
                                    'title': '基础示例',
                                    'dataIndex': '基础示例',
                                    'width': '20%'
                                },
                                {
                                    'title': '自定义选项',
                                    'dataIndex': '自定义选项',
                                    'width': '20%'
                                },
                                {
                                    'title': '单选模式',
                                    'dataIndex': '单选模式',
                                    'width': '20%'
                                },
                                {
                                    'title': '启用搜索框',
                                    'dataIndex': '启用搜索框',
                                    'width': '20%'
                                },
                                {
                                    'title': '搜索型筛选',
                                    'dataIndex': '搜索型筛选',
                                    'width': '20%'
                                }
                            ],
                            data=[
                                {
                                    '基础示例': s,
                                    '自定义选项': s,
                                    '单选模式': s,
                                    '启用搜索框': s,
                                    '搜索型筛选': s
                                }
                                for s in list('abced')
                            ],
                            filterOptions={
                                '基础示例': {},
                                '自定义选项': {
                                    'filterCustomItems': list('abcdefghijk')
                                },
                                '单选模式': {
                                    'filterMultiple': False
                                },
                                '启用搜索框': {
                                    'filterSearch': True
                                },
                                '搜索型筛选': {
                                    'filterMode': 'keyword'
                                }
                            }
                        ),

                        html.Pre(
                            id='table-filter-demo-output'
                        ),

                        fac.AntdDivider(
                            '监听筛选情况',
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
    id='table-filter-demo',
    columns=[
        {
            'title': '基础示例',
            'dataIndex': '基础示例',
            'width': '20%'
        },
        {
            'title': '自定义选项',
            'dataIndex': '自定义选项',
            'width': '20%'
        },
        {
            'title': '单选模式',
            'dataIndex': '单选模式',
            'width': '20%'
        },
        {
            'title': '启用搜索框',
            'dataIndex': '启用搜索框',
            'width': '20%'
        },
        {
            'title': '搜索型筛选',
            'dataIndex': '搜索型筛选',
            'width': '20%'
        }
    ],
    data=[
        {
            '基础示例': s,
            '自定义选项': s,
            '单选模式': s,
            '启用搜索框': s,
            '搜索型筛选': s
        }
        for s in list('abced')
    ],
    filterOptions={
        '基础示例': {},
        '自定义选项': {
            'filterCustomItems': list('abcdefghijk')
        },
        '单选模式': {
            'filterMultiple': False
        },
        '启用搜索框': {
            'filterSearch': True
        },
        '搜索型筛选': {
            'filterMode': 'keyword'
        }
    }
),

html.Pre(
    id='table-filter-demo-output'
)

...

import json

...

@app.callback(
    Output('table-filter-demo-output', 'children'),
    Input('table-filter-demo', 'filter'),
    prevent_initial_call=True
)
def table_filter_demo(filter_):

    return json.dumps(
        filter_,
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
                    id='监听筛选情况',
                    className='div-highlight'
                ),

                html.Div(
                    id='分页功能'
                ),

                html.Div(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdSpace(
                                    [
                                        fac.AntdDivider(
                                            f'placement="{placement}"',
                                            innerTextOrientation='left'
                                        ),
                                        fac.AntdTable(
                                            columns=[
                                                {
                                                    'title': f'字段{i}',
                                                    'dataIndex': f'字段{i}',
                                                    'width': '20%'
                                                }
                                                for i in range(1, 6)
                                            ],
                                            data=[
                                                {
                                                    f'字段{i}': '示例内容'
                                                    for i in range(1, 6)
                                                }
                                            ],
                                            pagination={
                                                'position': placement
                                            }
                                        )
                                    ],
                                    direction='vertical',
                                    style={
                                        'width': '100%'
                                    }
                                )
                                for placement in [
                                    'topLeft', 'topCenter', 'topRight',
                                    'bottomLeft', 'bottomCenter', 'bottomRight',
                                ]
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        ),

                        fac.AntdDivider(
                            '调整分页控件位置',
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
                    f'placement="{placement}"',
                    innerTextOrientation='left'
                ),
                fac.AntdTable(
                    columns=[
                        {
                            'title': f'字段{i}',
                            'dataIndex': f'字段{i}',
                            'width': '20%'
                        }
                        for i in range(1, 6)
                    ],
                    data=[
                        {
                            f'字段{i}': '示例内容'
                            for i in range(1, 6)
                        }
                    ],
                    pagination={
                        'position': placement
                    }
                )
            ],
            direction='vertical',
            style={
                'width': '100%'
            }
        )
        for placement in [
            'topLeft', 'topCenter', 'topRight',
            'bottomLeft', 'bottomCenter', 'bottomRight',
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
                    id='调整分页控件位置',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 10,
                            pagination={
                                'pageSize': 7
                            }
                        ),

                        fac.AntdDivider(
                            '调整每页记录数',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 10,
    pagination={
        'pageSize': 7
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
                    id='调整每页记录数',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 20,
                            pagination={
                                'pageSize': 5,
                                'showSizeChanger': True,
                                'pageSizeOptions': [5, 10, 20]
                            }
                        ),

                        fac.AntdDivider(
                            '允许用户调整每页记录数',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 20,
    pagination={
        'pageSize': 5,
        'showSizeChanger': True,
        'pageSizeOptions': [5, 10, 20]
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
                    id='允许用户调整每页记录数',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 10,
                            pagination={
                                'pageSize': 2,
                                'showQuickJumper': True
                            }
                        ),

                        fac.AntdDivider(
                            '开启快捷跳页功能',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 10,
    pagination={
        'pageSize': 2,
        'showQuickJumper': True
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
                    id='开启快捷跳页功能',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 3,
                            pagination={
                                'pageSize': 10,
                                'hideOnSinglePage': True
                            }
                        ),

                        fac.AntdDivider(
                            '记录不足1页时隐藏分页控件',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 3,
    pagination={
        'pageSize': 10,
        'hideOnSinglePage': True
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
                    id='记录不足1页时隐藏分页控件',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 10,
                            pagination={
                                'pageSize': 2,
                                'simple': True
                            }
                        ),

                        fac.AntdDivider(
                            '简洁分页模式',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 10,
    pagination={
        'pageSize': 2,
        'simple': True
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
                    id='简洁分页模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 20,
                            pagination={
                                'disabled': True,
                                'pageSize': 5
                            }
                        ),

                        fac.AntdDivider(
                            '禁用分页',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 20,
    pagination={
        'disabled': True,
        'pageSize': 5
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
                    id='禁用分页',
                    className='div-highlight'
                ),

                html.Div(
                    id='总结栏'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 5,
                            bordered=True,
                            summaryRowContents=[
                                {
                                    'content': '第1列总结'
                                },
                                {
                                    'content': '第2到4列总结',
                                    'colSpan': 3,
                                    'align': 'center'
                                },
                                {
                                    'content': '第5列总结',
                                    'align': 'right'
                                }
                            ]
                        ),

                        fac.AntdDivider(
                            '常规总结栏',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 5,
    bordered=True,
    summaryRowContents=[
        {
            'content': '第1列总结'
        },
        {
            'content': '第2到4列总结',
            'colSpan': 3,
            'align': 'center'
        },
        {
            'content': '第5列总结',
            'align': 'right'
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
                    id='常规总结栏',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    f'字段{i}': '示例内容'
                                    for i in range(1, 6)
                                }
                            ] * 10,
                            bordered=True,
                            summaryRowContents=[
                                {
                                    'content': '第1列总结'
                                },
                                {
                                    'content': '第2到4列总结',
                                    'colSpan': 3,
                                    'align': 'center'
                                },
                                {
                                    'content': '第5列总结',
                                    'align': 'right'
                                }
                            ],
                            summaryRowFixed=True,
                            maxHeight=150
                        ),

                        fac.AntdDivider(
                            '固定在底端',
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            f'字段{i}': '示例内容'
            for i in range(1, 6)
        }
    ] * 10,
    bordered=True,
    summaryRowContents=[
        {
            'content': '第1列总结'
        },
        {
            'content': '第2到4列总结',
            'colSpan': 3,
            'align': 'center'
        },
        {
            'content': '第5列总结',
            'align': 'right'
        }
    ],
    summaryRowFixed=True,
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
                    id='固定在底端',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': '示例字段1',
                                    'dataIndex': '示例字段1',
                                    'width': '100'
                                },
                                {
                                    'title': '示例字段2',
                                    'dataIndex': '示例字段2',
                                    'width': '100'
                                },
                                {
                                    'title': '示例字段3',
                                    'dataIndex': '示例字段3',
                                    'width': '100'
                                }
                            ],
                            data=[
                                {
                                    '示例字段1': i,
                                    '示例字段2': i,
                                    '示例字段3': round(np.random.rand(), 3)
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            conditionalStyleFuncs={
                                '示例字段1': '''
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                backgroundColor: "#ebfbee"
            }
        }
    }
}
''',
                                '示例字段2': '''
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                color: "red"
            }
        }
    }
}
''',
                                '示例字段3': '''
(record, index) => {
    if ( record['示例字段3'] <= 0.5 ) {
        return {
            style: {
                background: `linear-gradient(90deg, rgb(61, 153, 112) 0%, rgb(61, 153, 112) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
                backgroundClip: 'padding-box'
            }
        };
    }
    return {
        style: {
            background: `linear-gradient(90deg, rgb(255, 65, 54) 0%, rgb(255, 65, 54) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
            backgroundClip: 'padding-box'
        }
    };
}
'''
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
                                codeString="""
fac.AntdTable(
    columns=[
        {
            'title': '示例字段1',
            'dataIndex': '示例字段1',
            'width': '100'
        },
        {
            'title': '示例字段2',
            'dataIndex': '示例字段2',
            'width': '100'
        },
        {
            'title': '示例字段3',
            'dataIndex': '示例字段3',
            'width': '100'
        }
    ],
    data=[
        {
            '示例字段1': i,
            '示例字段2': i,
            '示例字段3': round(np.random.rand(), 3)
        }
        for i in range(10)
    ],
    bordered=True,
    conditionalStyleFuncs={
        '示例字段1': '''
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                backgroundColor: "#ebfbee"
            }
        }
    }
}
''',
        '示例字段2': '''
(record, index) => {
    if ( index % 2 === 1 ) {
        return {
            style: {
                color: "red"
            }
        }
    }
}
''',
        '示例字段3': '''
(record, index) => {
    if ( record['示例字段3'] <= 0.5 ) {
        return {
            style: {
                background: `linear-gradient(90deg, rgb(61, 153, 112) 0%, rgb(61, 153, 112) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
                backgroundClip: 'padding-box'
            }
        };
    }
    return {
        style: {
            background: `linear-gradient(90deg, rgb(255, 65, 54) 0%, rgb(255, 65, 54) ${record['示例字段3']*100}%, white ${record['示例字段3']*100}%, white 100%)`,
            backgroundClip: 'padding-box'
        }
    };
}
'''
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
                    id='自定义样式',
                    className='div-highlight'
                ),

                html.Div(
                    id='行展开功能'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': 400
                                }
                                for i in range(5)
                            ],
                            data=[
                                {
                                    **{
                                        f'字段{j}': i
                                        for j in range(5)
                                    },
                                    'key': f'row-{i}'
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            expandedRowKeyToContent=[
                                {
                                    'key': f'row-{i}',
                                    'content': fac.AntdButton(
                                        f'第{i}行展开内容示例',
                                        type='primary'
                                    )
                                }
                                for i in range(0, 10, 2)
                            ]
                        ),

                        fac.AntdDivider(
                            '基础的行展开',
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
            'width': 400
        }
        for i in range(5)
    ],
    data=[
        {
            **{
                f'字段{j}': i
                for j in range(5)
            },
            'key': f'row-{i}'
        }
        for i in range(10)
    ],
    bordered=True,
    expandedRowKeyToContent=[
        {
            'key': f'row-{i}',
            'content': fac.AntdButton(
                f'第{i}行展开内容示例',
                type='primary'
            )
        }
        for i in range(0, 10, 2)
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
                    id='基础的行展开',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': 400
                                }
                                for i in range(5)
                            ],
                            data=[
                                {
                                    **{
                                        f'字段{j}': i
                                        for j in range(5)
                                    },
                                    'key': f'row-{i}'
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            expandedRowKeyToContent=[
                                {
                                    'key': f'row-{i}',
                                    'content': fac.AntdButton(
                                        f'第{i}行展开内容示例',
                                        type='primary'
                                    )
                                }
                                for i in range(0, 10, 2)
                            ],
                            defaultExpandedRowKeys=[
                                'row-2', 'row-6'
                            ]
                        ),

                        fac.AntdDivider(
                            '设置初始化展开行',
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
            'width': 400
        }
        for i in range(5)
    ],
    data=[
        {
            **{
                f'字段{j}': i
                for j in range(5)
            },
            'key': f'row-{i}'
        }
        for i in range(10)
    ],
    bordered=True,
    expandedRowKeyToContent=[
        {
            'key': f'row-{i}',
            'content': fac.AntdButton(
                f'第{i}行展开内容示例',
                type='primary'
            )
        }
        for i in range(0, 10, 2)
    ],
    defaultExpandedRowKeys=[
        'row-2', 'row-6'
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
                    id='设置初始化展开行',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': 400
                                }
                                for i in range(5)
                            ],
                            data=[
                                {
                                    **{
                                        f'字段{j}': i
                                        for j in range(5)
                                    },
                                    'key': f'row-{i}'
                                }
                                for i in range(10)
                            ],
                            bordered=True,
                            expandedRowKeyToContent=[
                                {
                                    'key': f'row-{i}',
                                    'content': fac.AntdButton(
                                        f'第{i}行展开内容示例',
                                        type='primary'
                                    )
                                }
                                for i in range(0, 10, 2)
                            ],
                            expandRowByClick=True
                        ),

                        fac.AntdDivider(
                            '点击所在行展开折叠',
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
            'width': 400
        }
        for i in range(5)
    ],
    data=[
        {
            **{
                f'字段{j}': i
                for j in range(5)
            },
            'key': f'row-{i}'
        }
        for i in range(10)
    ],
    bordered=True,
    expandedRowKeyToContent=[
        {
            'key': f'row-{i}',
            'content': fac.AntdButton(
                f'第{i}行展开内容示例',
                type='primary'
            )
        }
        for i in range(0, 10, 2)
    ],
    expandRowByClick=True
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
                    id='点击所在行展开折叠',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            id='table-click-event-demo',
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    'key': f'row-{row}',
                                    **{
                                        f'字段{i}': f'字段{i}第{row}行'
                                        for i in range(1, 6)
                                    }
                                }
                                for row in range(1, 6)
                            ],
                            bordered=True,
                            enableCellClickListenColumns=[
                                f'字段{i}' for i in range(1, 6, 2)
                            ]
                        ),

                        html.Pre(
                            id='table-click-event-demo-output'
                        ),

                        fac.AntdDivider(
                            '监听表格内点击事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '针对参数',
                                fac.AntdText(
                                    'enableCellClickListenColumns',
                                    code=True
                                ),
                                '内声明的字段，可以监听到用户在相关单元格内的单击和双击事件'
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
    id='table-click-event-demo',
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            'key': f'row-{row}',
            **{
                f'字段{i}': f'字段{i}第{row}行'
                for i in range(1, 6)
            }
        }
        for row in range(1, 6)
    ],
    bordered=True,
    enableCellClickListenColumns=[
        f'字段{i}' for i in range(1, 6, 2)
    ]
),

html.Pre(
    id='table-click-event-demo-output'
)

...

import json

...

@app.callback(
    Output('table-click-event-demo-output', 'children'),
    [Input('table-click-event-demo', 'nClicksCell'),
     Input('table-click-event-demo', 'nDoubleClicksCell')],
    [State('table-click-event-demo', 'enableCellClickListenColumns'),
     State('table-click-event-demo', 'recentlyCellClickColumn'),
     State('table-click-event-demo', 'recentlyCellClickRecord'),
     State('table-click-event-demo', 'recentlyCellDoubleClickColumn'),
     State('table-click-event-demo', 'recentlyCellDoubleClickRecord')],
    prevent_initial_call=True
)
def table_click_event_demo(nClicksCell,
                           nDoubleClicksCell,
                           enableCellClickListenColumns,
                           recentlyCellClickColumn,
                           recentlyCellClickRecord,
                           recentlyCellDoubleClickColumn,
                           recentlyCellDoubleClickRecord):

    return json.dumps(
        dict(
            enableCellClickListenColumns=enableCellClickListenColumns,
            nClicksCell=nClicksCell,
            recentlyCellClickColumn=recentlyCellClickColumn,
            recentlyCellClickRecord=recentlyCellClickRecord,
            nDoubleClicksCell=nDoubleClicksCell,
            recentlyCellDoubleClickColumn=recentlyCellDoubleClickColumn,
            recentlyCellDoubleClickRecord=recentlyCellDoubleClickRecord
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
                    id='监听表格内点击事件',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            id='table-hover-event-demo',
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            data=[
                                {
                                    'key': f'row-{row}',
                                    **{
                                        f'字段{i}': f'字段{i}第{row}行'
                                        for i in range(1, 6)
                                    }
                                }
                                for row in range(1, 6)
                            ],
                            bordered=True,
                            enableHoverListen=True
                        ),

                        html.Pre(
                            id='table-hover-event-demo-output'
                        ),

                        fac.AntdDivider(
                            '监听表格内鼠标悬停事件',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '当设置参数',
                                fac.AntdText(
                                    'enableHoverListen=True',
                                    code=True
                                ),
                                '后，可对用户鼠标在表格不同单元格间的鼠标移入事件进行监听'
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
    id='table-hover-event-demo',
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    data=[
        {
            'key': f'row-{row}',
            **{
                f'字段{i}': f'字段{i}第{row}行'
                for i in range(1, 6)
            }
        }
        for row in range(1, 6)
    ],
    bordered=True,
    enableHoverListen=True
),

html.Pre(
    id='table-hover-event-demo-output'
)

...

# 为方便演示，这里使用浏览器端回调
app.clientside_callback(
    '''( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }''',
    Output('table-hover-event-demo-output', 'children'),
    [Input('table-hover-event-demo', 'recentlyMouseEnterColumnDataIndex'),
     Input('table-hover-event-demo', 'recentlyMouseEnterRowKey'),
     Input('table-hover-event-demo', 'recentlyMouseEnterRow')],
    prevent_initial_call=True
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
                    id='监听表格内鼠标悬停事件',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTable(
                            columns=[
                                {
                                    'title': f'字段{i}',
                                    'dataIndex': f'字段{i}',
                                    'width': '20%'
                                }
                                for i in range(1, 6)
                            ],
                            emptyContent=fac.AntdEmpty(
                                image='/assets/imgs/empty占位图示例1.png',
                                description=fac.AntdText(
                                    '没有数据哦~',
                                    type='secondary'
                                ),
                                imageStyle={
                                    'height': 150
                                }
                            )
                        ),

                        fac.AntdDivider(
                            '自定义空内容',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '通过组件型参数',
                                fac.AntdText(
                                    'emptyContent',
                                    code=True
                                ),
                                '可以自定义表格数据为空时的提示信息'
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
            'width': '20%'
        }
        for i in range(1, 6)
    ],
    emptyContent=fac.AntdEmpty(
        image='/assets/imgs/empty占位图示例1.png',
        description=fac.AntdText(
            '没有数据哦~',
            type='secondary'
        ),
        imageStyle={
            'height': 150
        }
    )
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
                    id='自定义空内容',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdTitle(
                            '左例（未设置） 右例（设置containerId参数）',
                            level=5
                        ),
                        html.Div(
                            [
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
                                                    f'字段{j}': np.random.randint(1, 5)
                                                    for j in range(1, 6)
                                                }
                                                for i in range(10)
                                            ],
                                            filterOptions={
                                                '字段1': {
                                                    'filterMode': 'keyword'
                                                },
                                                '字段3': {
                                                    'filterMode': 'checkbox',
                                                    'filterCustomItems': [1, 2, 3]
                                                }
                                            }
                                        ),
                                        html.Div(
                                            style={
                                                'height': '400px'
                                            }
                                        )
                                    ],
                                    style={
                                        'flex': '1',
                                        'padding': '20px',
                                        'maxHeight': '400px',
                                        'overflowY': 'auto'
                                    }
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
                                                    f'字段{j}': np.random.randint(1, 5)
                                                    for j in range(1, 6)
                                                }
                                                for i in range(10)
                                            ],
                                            filterOptions={
                                                '字段1': {
                                                    'filterMode': 'keyword'
                                                },
                                                '字段3': {
                                                    'filterMode': 'checkbox',
                                                    'filterCustomItems': [1, 2, 3]
                                                }
                                            },
                                            containerId='containerId-container-demo'
                                        ),
                                        html.Div(
                                            style={
                                                'height': '400px'
                                            }
                                        )
                                    ],
                                    id='containerId-container-demo',
                                    style={
                                        'flex': '1',
                                        'padding': '20px',
                                        'maxHeight': '400px',
                                        'overflowY': 'auto',
                                        'position': 'relative'
                                    }
                                )
                            ],
                            style={
                                'display': 'flex'
                            }
                        ),

                        fac.AntdDivider(
                            '局部容器内悬浮层锚点配置',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                '与表格部分功能有关的悬浮层控件，譬如字段筛选对应的下拉菜单等，默认是以页面根节点为滚动事件参考容器',
                                '，因此当表格置于局部容器内时，已展开的悬浮层控件会不跟随局部容器滑轮滚动事件移动，这种情况下可以设置参数',
                                fac.AntdText(
                                    'containerId="局部容器id"',
                                    code=True
                                ),
                                '来进行优化'
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
import numpy as np

...

fac.AntdTitle(
    '左例（未设置） 右例（设置containerId参数）',
    level=5
),
html.Div(
    [
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
                            f'字段{j}': np.random.randint(1, 5)
                            for j in range(1, 6)
                        }
                        for i in range(10)
                    ],
                    filterOptions={
                        '字段1': {
                            'filterMode': 'keyword'
                        },
                        '字段3': {
                            'filterMode': 'checkbox',
                            'filterCustomItems': [1, 2, 3]
                        }
                    }
                ),
                html.Div(
                    style={
                        'height': '400px'
                    }
                )
            ],
            style={
                'flex': '1',
                'padding': '20px',
                'maxHeight': '400px',
                'overflowY': 'auto'
            }
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
                            f'字段{j}': np.random.randint(1, 5)
                            for j in range(1, 6)
                        }
                        for i in range(10)
                    ],
                    filterOptions={
                        '字段1': {
                            'filterMode': 'keyword'
                        },
                        '字段3': {
                            'filterMode': 'checkbox',
                            'filterCustomItems': [1, 2, 3]
                        }
                    },
                    containerId='containerId-container-demo'
                ),
                html.Div(
                    style={
                        'height': '400px'
                    }
                )
            ],
            id='containerId-container-demo',
            style={
                'flex': '1',
                'padding': '20px',
                'maxHeight': '400px',
                'overflowY': 'auto',
                'position': 'relative'
            }
        )
    ],
    style={
        'display': 'flex'
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
                    id='局部容器内悬浮层锚点配置',
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
                    {
                        'title': '行选择功能',
                        'href': '#行选择功能',
                        'children': [
                            {
                                'title': '单选模式',
                                'href': '#单选模式'
                            },
                            {
                                'title': '多选模式',
                                'href': '#多选模式'
                            },
                            {
                                'title': '监听已选行key值',
                                'href': '#监听已选行key值'
                            }
                        ]
                    },
                    {'title': '粘性表头功能', 'href': '#粘性表头功能'},
                    {'title': '字段标题额外说明信息', 'href': '#字段标题额外说明信息'},
                    {'title': '编辑模式配置内容格式校验', 'href': '#编辑模式配置内容格式校验'},
                    {
                        'title': '排序功能',
                        'href': '#排序功能',
                        'children': [
                            {
                                'title': '单字段排序',
                                'href': '#单字段排序'
                            },
                            {
                                'title': '多字段组合排序',
                                'href': '#多字段组合排序'
                            },
                            {
                                'title': '多字段组合排序（动态优先级）',
                                'href': '#多字段组合排序（动态优先级）'
                            },
                            {
                                'title': '监听排序情况',
                                'href': '#监听排序情况'
                            },
                        ]
                    },
                    {
                        'title': '筛选功能',
                        'href': '#筛选功能',
                        'children': [
                            {
                                'title': '勾选型筛选',
                                'href': '#勾选型筛选'
                            },
                            {
                                'title': '搜索型筛选',
                                'href': '#搜索型筛选'
                            },
                            {
                                'title': '监听筛选情况',
                                'href': '#监听筛选情况'
                            },
                        ]
                    },
                    {
                        'title': '分页功能',
                        'href': '#分页功能',
                        'children': [
                            {
                                'title': '调整分页控件位置',
                                'href': '#调整分页控件位置'
                            },
                            {
                                'title': '调整每页记录数',
                                'href': '#调整每页记录数'
                            },
                            {
                                'title': '允许用户调整每页记录数',
                                'href': '#允许用户调整每页记录数'
                            },
                            {
                                'title': '开启快捷跳页功能',
                                'href': '#开启快捷跳页功能'
                            },
                            {
                                'title': '记录不足1页时隐藏分页控件',
                                'href': '#记录不足1页时隐藏分页控件'
                            },
                            {
                                'title': '简洁分页',
                                'href': '#简洁分页'
                            },
                            {
                                'title': '禁用分页',
                                'href': '#禁用分页'
                            },
                        ]
                    },
                    {
                        'title': '总结栏',
                        'href': '#总结栏',
                        'children': [
                            {
                                'title': '常规总结栏',
                                'href': '#常规总结栏'
                            },
                            {
                                'title': '固定在底端',
                                'href': '#固定在底端'
                            }
                        ]
                    },
                    {'title': '自定义样式', 'href': '#自定义样式'},
                    {
                        'title': '行展开功能',
                        'href': '#行展开功能',
                        'children': [
                            {
                                'title': '基础的行展开',
                                'href': '#基础的行展开',
                            },
                            {
                                'title': '设置初始化展开行',
                                'href': '#设置初始化展开行',
                            },
                            {
                                'title': '点击所在行展开折叠',
                                'href': '#点击所在行展开折叠',
                            }
                        ]
                    },
                    {'title': '监听表格内点击事件', 'href': '#监听表格内点击事件'},
                    {'title': '监听表格内鼠标悬停事件', 'href': '#监听表格内鼠标悬停事件'},
                    {'title': '自定义空内容', 'href': '#自定义空内容'},
                    {'title': '局部容器内悬浮层锚点配置', 'href': '#局部容器内悬浮层锚点配置'}
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
            component_name='AntdTable'
        )
    ],
    style={
        'display': 'flex'
    }
)
