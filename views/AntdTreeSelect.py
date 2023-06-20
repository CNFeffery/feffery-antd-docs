from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.AntdTreeSelect
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
                        items=(
                            [
                                {
                                    'title': '组件介绍'
                                },
                                {
                                    'title': '数据录入'
                                },
                                {
                                    'title': 'AntdTreeSelect 树选择'
                                }
                            ]
                            if language == '中文' else
                            [
                                {
                                    'title': 'Component Introduction'
                                },
                                {
                                    'title': 'Data Entry'
                                },
                                {
                                    'title': 'AntdTreeSelect'
                                }
                            ]
                        )
                    ),

                    fac.AntdDivider(isDashed=True),

                    fac.AntdParagraph(
                        [
                            fac.AntdText(
                                '　　用于为用户提供在树形结构中选择若干项的功能。'
                                if language == '中文' else
                                '　　Used to provide users with the functionality to select multiple items in a tree-like structure.'
                            )
                        ]
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '基础使用'
                                    if language == '中文' else
                                    'Basic usage'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '基础使用'
                            if language == '中文' else
                            'Basic_usage'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTreeSelect(
                                        treeData=[
                                            {
                                                'key': '节点1',
                                                'value': '1',
                                                'title': '节点1',
                                                'children': [
                                                    {
                                                        'key': f'节点1-{i}',
                                                        'value': f'1-{i}',
                                                        'title': f'节点1-{i}'
                                                    }
                                                    for i in range(1, 5)
                                                ]
                                            },
                                            {
                                                'key': '节点2',
                                                'value': '2',
                                                'title': '节点2'
                                            }
                                        ],
                                        placeholder=f'placement="{placement}"',
                                        placement=placement,
                                        style={
                                            'width': 256
                                        }
                                    )
                                    for placement in [
                                        'bottomLeft', 'bottomRight', 'topLeft', 'topRight'
                                    ]
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                (
                                    '不同的悬浮层展开方位'
                                    if language == '中文' else
                                    'Different positions for expanding pop-up layers'
                                ),
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
        fac.AntdTreeSelect(
            treeData=[
                {
                    'key': '节点1',
                    'value': '1',
                    'title': '节点1',
                    'children': [
                        {
                            'key': f'节点1-{i}',
                            'value': f'1-{i}',
                            'title': f'节点1-{i}'
                        }
                        for i in range(1, 5)
                    ]
                },
                {
                    'key': '节点2',
                    'value': '2',
                    'title': '节点2'
                }
            ],
            placeholder=f'placement="{placement}"',
            placement=placement,
            style={
                'width': 256
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
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '不同的悬浮层展开方位'
                            if language == '中文' else
                            'Different_positions_for_expanding_pop-up_layers'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '多选模式'
                                    if language == '中文' else
                                    'Multi-select mode'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '多选模式'
                            if language == '中文' else
                            'Multi-select_mode'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '带勾选框的多选模式'
                                    if language == '中文' else
                                    'Multi-select mode with checkboxes'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '带勾选框的多选模式'
                            if language == '中文' else
                            'Multi-select_mode_with_checkboxes'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeDataMode='flat',
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1'
                                    },
                                    *[
                                        {
                                            'key': f'节点1-{i}',
                                            'value': f'1-{i}',
                                            'title': f'节点1-{i}',
                                            'parent': '节点1'
                                        }
                                        for i in range(1, 6)
                                    ]
                                ],
                                placeholder='请选择',
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '扁平treeData模式'
                                    if language == '中文' else
                                    'Flat treeData mode'
                                ),
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
fac.AntdTreeSelect(
    treeDataMode='flat',
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1'
        },
        *[
            {
                'key': f'节点1-{i}',
                'value': f'1-{i}',
                'title': f'节点1-{i}',
                'parent': '节点1'
            }
            for i in range(1, 6)
        ]
    ],
    placeholder='请选择',
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '扁平treeData模式'
                            if language == '中文' else
                            'Flat_treeData_mode'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                treeLine=True,
                                treeDefaultExpandAll=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '添加连接线'
                                    if language == '中文' else
                                    'Add connecting lines'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    treeLine=True,
    treeDefaultExpandAll=True,
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '添加连接线'
                            if language == '中文' else
                            'Add_connecting_lines'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                treeCheckStrictly=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '父子节点独立选择'
                                    if language == '中文' else
                                    'Independent selection of parent and child nodes'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    treeCheckStrictly=True,
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '父子节点独立选择'
                            if language == '中文' else
                            'Independent_selection_of_parent_and_child_nodes'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                disabled=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '禁用状态'
                                    if language == '中文' else
                                    'Disabled state'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    disabled=True,
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '禁用状态'
                            if language == '中文' else
                            'Disabled_state'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                'showCheckedStrategy="show-all"（默认）',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                'showCheckedStrategy="show-parent"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                showCheckedStrategy='show-parent',
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                'showCheckedStrategy="show-child"',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                showCheckedStrategy='show-child',
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '已选项回填策略'
                                    if language == '中文' else
                                    'Selected item fill-back policy'
                                ),
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
    'showCheckedStrategy="show-all"（默认）',
    innerTextOrientation='left'
),
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    style={
        'width': 256
    }
),

fac.AntdDivider(
    'showCheckedStrategy="show-parent"',
    innerTextOrientation='left'
),
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    showCheckedStrategy='show-parent',
    style={
        'width': 256
    }
),

fac.AntdDivider(
    'showCheckedStrategy="show-child"',
    innerTextOrientation='left'
),
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    showCheckedStrategy='show-child',
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '已选项回填策略'
                            if language == '中文' else
                            'Selected_item_fill-back_policy'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdRadioGroup(
                                        id='tree-select-multiple-mode-search-demo-switch-mode',
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
                                    fac.AntdTreeSelect(
                                        id='tree-select-multiple-mode-search-demo',
                                        treeData=[
                                            {
                                                'key': f'节点{i}',
                                                'title': f'节点{i}',
                                                'value': f'节点{i}',
                                                'children': [
                                                    {
                                                        'key': f'节点{i}-{j}',
                                                        'title': f'节点{i}-{j}',
                                                        'value': f'节点{i}-{j}',
                                                    }
                                                    for j in range(1, 4)
                                                ]
                                            }
                                            for i in list('AbCdEf')
                                        ],
                                        style={
                                            'width': 300
                                        }
                                    )
                                ],
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '多模式搜索'
                                    if language == '中文' else
                                    'Multi-mode search'
                                ),
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
            id='tree-select-multiple-mode-search-demo-switch-mode',
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
        fac.AntdTreeSelect(
            id='tree-select-multiple-mode-search-demo',
            treeData=[
                {
                    'key': f'节点{i}',
                    'title': f'节点{i}',
                    'value': f'节点{i}',
                    'children': [
                        {
                            'key': f'节点{i}-{j}',
                            'title': f'节点{i}-{j}',
                            'value': f'节点{i}-{j}',
                        }
                        for j in range(1, 4)
                    ]
                }
                for i in list('AbCdEf')
            ],
            style={
                'width': 300
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
    Output('tree-select-multiple-mode-search-demo', 'treeNodeFilterMode'),
    Input('tree-select-multiple-mode-search-demo-switch-mode', 'value')
)
def tree_select_multiple_mode_search_demo(value):

    return value
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '多模式搜索'
                            if language == '中文' else
                            'Multi-mode_search'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdTreeSelect(
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                defaultValue='节点2',
                                readOnly=True,
                                style={
                                    'width': 256
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '只读状态'
                                    if language == '中文' else
                                    'Read-only state'
                                ),
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
fac.AntdTreeSelect(
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    defaultValue='节点2',
    readOnly=True,
    style={
        'width': 256
    }
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '只读状态'
                            if language == '中文' else
                            'Read-only_state'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdSpace(
                                [
                                    fac.AntdTreeSelect(
                                        treeData=[
                                            {
                                                'key': '节点1',
                                                'value': '1',
                                                'title': '节点1',
                                                'children': [
                                                    {
                                                        'key': f'节点1-{i}',
                                                        'value': f'1-{i}',
                                                        'title': f'节点1-{i}'
                                                    }
                                                    for i in range(1, 5)
                                                ]
                                            },
                                            {
                                                'key': '节点2',
                                                'value': '2',
                                                'title': '节点2'
                                            }
                                        ],
                                        placeholder=f'status="{status}"',
                                        status=status,
                                        style={
                                            'width': 256
                                        }
                                    )
                                    for status in ['warning', 'error']
                                ],
                                direction='vertical'
                            ),

                            fac.AntdDivider(
                                (
                                    '强制状态渲染'
                                    if language == '中文' else
                                    'Forced state rendering'
                                ),
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
        fac.AntdTreeSelect(
            treeData=[
                {
                    'key': '节点1',
                    'value': '1',
                    'title': '节点1',
                    'children': [
                        {
                            'key': f'节点1-{i}',
                            'value': f'1-{i}',
                            'title': f'节点1-{i}'
                        }
                        for i in range(1, 5)
                    ]
                },
                {
                    'key': '节点2',
                    'value': '2',
                    'title': '节点2'
                }
            ],
            placeholder=f'status="{status}"',
            status=status,
            style={
                'width': 256
            }
        )
        for status in ['warning', 'error']
    ],
    direction='vertical'
)
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '强制状态渲染'
                            if language == '中文' else
                            'Forced_state_rendering'
                        ),
                        className='div-highlight'
                    ),

                    html.Div(
                        [
                            fac.AntdDivider(
                                '单选示例',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTreeSelect(
                                id='tree-select-demo',
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                style={
                                    'width': 256
                                }
                            ),
                            fac.AntdSpace(
                                id='tree-select-demo-output',
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                '多选示例',
                                innerTextOrientation='left'
                            ),
                            fac.AntdTreeSelect(
                                id='tree-select-multiple-demo',
                                treeData=[
                                    {
                                        'key': '节点1',
                                        'value': '1',
                                        'title': '节点1',
                                        'children': [
                                            {
                                                'key': f'节点1-{i}',
                                                'value': f'1-{i}',
                                                'title': f'节点1-{i}'
                                            }
                                            for i in range(1, 5)
                                        ]
                                    },
                                    {
                                        'key': '节点2',
                                        'value': '2',
                                        'title': '节点2'
                                    }
                                ],
                                placeholder='请选择',
                                multiple=True,
                                treeCheckable=True,
                                style={
                                    'width': 256
                                }
                            ),
                            fac.AntdSpace(
                                id='tree-select-multiple-demo-output',
                                direction='vertical',
                                style={
                                    'width': '100%'
                                }
                            ),

                            fac.AntdDivider(
                                (
                                    '回调示例'
                                    if language == '中文' else
                                    'Callback example'
                                ),
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
    '单选示例',
    innerTextOrientation='left'
),
fac.AntdTreeSelect(
    id='tree-select-demo',
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    style={
        'width': 256
    }
),
fac.AntdSpace(
    id='tree-select-demo-output',
    direction='vertical',
    style={
        'width': '100%'
    }
),

fac.AntdDivider(
    '多选示例',
    innerTextOrientation='left'
),
fac.AntdTreeSelect(
    id='tree-select-multiple-demo',
    treeData=[
        {
            'key': '节点1',
            'value': '1',
            'title': '节点1',
            'children': [
                {
                    'key': f'节点1-{i}',
                    'value': f'1-{i}',
                    'title': f'节点1-{i}'
                }
                for i in range(1, 5)
            ]
        },
        {
            'key': '节点2',
            'value': '2',
            'title': '节点2'
        }
    ],
    placeholder='请选择',
    multiple=True,
    treeCheckable=True,
    style={
        'width': 256
    }
),
fac.AntdSpace(
    id='tree-select-multiple-demo-output',
    direction='vertical',
    style={
        'width': '100%'
    }
)

...

@app.callback(
    Output('tree-select-demo-output', 'children'),
    [Input('tree-select-demo', 'value'),
     Input('tree-select-demo', 'treeExpandedKeys')]
)
def tree_select_demo(value, treeExpandedKeys):

    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}')
    ]


@app.callback(
    Output('tree-select-multiple-demo-output', 'children'),
    [Input('tree-select-multiple-demo', 'value'),
     Input('tree-select-multiple-demo', 'treeExpandedKeys')]
)
def tree_select_multiple_demo(value, treeExpandedKeys):

    return [
        fac.AntdText(f'value: {value}'),
        fac.AntdText(f'treeExpandedKeys: {treeExpandedKeys}')
    ]
'''
                                ),
                                title=(
                                    '点击查看代码'
                                    if language == '中文' else
                                    'Click to view code'
                                ),
                                isOpen=False,
                                ghost=True
                            )
                        ],
                        style={
                            'marginBottom': '40px',
                            'padding': '10px 10px 20px 10px',
                            'border': '1px solid #f0f0f0'
                        },
                        id=(
                            '回调示例'
                            if language == '中文' else
                            'Callback_example'
                        ),
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
                    linkDict=(
                        [
                            {'title': '基础使用', 'href': '#基础使用'},
                            {'title': '不同的悬浮层展开方位', 'href': '#不同的悬浮层展开方位'},
                            {'title': '多选模式', 'href': '#多选模式'},
                            {'title': '带勾选框的多选模式', 'href': '#带勾选框的多选模式'},
                            {'title': '扁平treeData模式', 'href': '#扁平treeData模式'},
                            {'title': '添加连接线', 'href': '#添加连接线'},
                            {'title': '父子节点独立选择', 'href': '#父子节点独立选择'},
                            {'title': '禁用状态', 'href': '#禁用状态'},
                            {'title': '已选项回填策略', 'href': '#已选项回填策略'},
                            {'title': '多模式搜索', 'href': '#多模式搜索'},
                            {'title': '只读状态', 'href': '#只读状态'},
                            {'title': '强制状态渲染', 'href': '#强制状态渲染'},
                            {'title': '回调示例', 'href': '#回调示例'},
                        ]
                        if language == '中文' else
                        [
                            {'title': 'Basic usage', 'href': '#Basic_usage'},
                            {
                                'title': 'Different positions for expanding pop-up layers',
                                'href': '#Different_positions_for_expanding_pop-up_layers'
                            },
                            {
                                'title': 'Multi-select mode',
                                'href': '#Multi-select_mode'
                            },
                            {
                                'title': 'Multi-select mode with checkboxes',
                                'href': '#Multi-select_mode_with_checkboxes'
                            },
                            {
                                'title': 'Flat treeData mode',
                                'href': '#Flat_treeData_mode'
                            },
                            {
                                'title': 'Add connecting lines',
                                'href': '#Add_connecting_lines'
                            },
                            {
                                'title': 'Independent selection of parent and child nodes',
                                'href': '#Independent_selection_of_parent_and_child_nodes'
                            },
                            {'title': 'Disabled state', 'href': '#Disabled_state'},
                            {
                                'title': 'Selected item fill-back policy',
                                'href': '#Selected_item_fill-back_policy'
                            },
                            {
                                'title': 'Multi-mode search',
                                'href': '#Multi-mode_search'
                            },
                            {
                                'title': 'Read-only state',
                                'href': '#Read-only_state'
                            },
                            {
                                'title': 'Forced state rendering',
                                'href': '#Forced_state_rendering'
                            },
                            {
                                'title': 'Callback example',
                                'href': '#Callback_example'
                            },
                        ]
                    ),
                    offsetTop=0
                ),
                style={
                    'flex': 'none',
                    'padding': '25px'
                }
            ),
            # 侧边参数栏
            render_side_props_layout(
                component_name='AntdTreeSelect',
                language=language
            )
        ],
        style={
            'display': 'flex'
        }
    )
