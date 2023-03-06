from dash import html
import feffery_antd_components as fac
import feffery_markdown_components as fmc

import callbacks.table_server_side_mode_c
from callbacks.table_server_side_mode_c import (
    demo_df, DemoTable, fn
)
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
                            'title': '服务端数据加载模式'
                        }
                    ]
                ),

                fac.AntdDivider(isDashed=True),

                fac.AntdParagraph(
                    [
                        '本页文档展示了AntdTable组件基于服务端数据加载模式，对大量数据的展示需求进行性能优化，本质上是在设置参数',
                        fac.AntdText(
                            'mode="server-side"',
                            code=True
                        ),
                        '后，通过监听AntdTable中翻页、排序、筛选等常见交互行为对应的监听参数变化，进而通过回调函数传递到后端进行对应数据帧的生成，并传回AntdTable中进行展示，',
                        '相当于任意时刻下，表格中实际加载的数据只有用户所看到的当页数据'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                fac.AntdParagraph(
                    [
                        fac.AntdText(
                            '注意',
                            strong=True
                        ),
                        '，本页文档后续所有与',
                        fac.AntdText(
                            'demo_df',
                            code=True
                        ),
                        '有关的示例中，',
                        fac.AntdText(
                            'demo_df',
                            code=True
                        ),
                        '均为同一个',
                        fac.AntdText(
                            'pandas',
                            strong=True
                        ),
                        '数据框，由下列代码生成：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                fmc.FefferySyntaxHighlighter(
                    showCopyButton=True,
                    showLineNumbers=True,
                    language='python',
                    codeTheme='coy-without-shadows',
                    codeString='''
import pandas as pd

# 生成演示用数据框
demo_df = (
    pd
    .DataFrame(
        {
            'id': list(range(1, 100001)),
            '字段1': np.random.choice(
                [
                    f'{s}{n}'
                    for s in list('abcdefghij')
                    for n in range(1, 10001)
                ],
                100000,
                replace=False
            ),
            '字段2': np.random.choice(
                [
                    f'类型{t}'
                    for t in range(1, 11)
                    for n in range(10000)
                ],
                100000,
                replace=False
            )
        }
    )
    # 打乱顺序
    .sample(frac=1, replace=False)
)
'''
                ),

                fac.AntdParagraph(
                    [
                        '本页文档后续所有与',
                        fac.AntdText(
                            'DemoTable',
                            code=True
                        ),
                        '有关的示例中，',
                        fac.AntdText(
                            'DemoTable',
                            code=True
                        ),
                        '均为同一个基于',
                        fac.AntdText(
                            'peewee',
                            strong=True
                        ),
                        '定义的',
                        fac.AntdText(
                            'ORM',
                            strong=True
                        ),
                        '模型类，由下列代码定义：'
                    ],
                    style={
                        'textIndent': '2rem'
                    }
                ),

                fmc.FefferySyntaxHighlighter(
                    showCopyButton=True,
                    showLineNumbers=True,
                    language='python',
                    codeTheme='coy-without-shadows',
                    codeString='''
from peewee import (
    SqliteDatabase,
    CharField,
    IntegerField,
    Model,
    fn
)

...

# 构造演示用数据库表模型类，基于sqlite+peewee
db = SqliteDatabase('./demo_table.db')


class DemoTable(Model):

    id = IntegerField()

    字段1 = CharField()

    字段2 = CharField()

    class Meta:

        table_name = 'demo_table'
        database = db


# 创建表格并插入示例数据
db.create_tables([DemoTable])

# 为方便调试，先检查数据表中是否已有记录，若有则跳过数据插入
with db.atomic():

    if (
        DemoTable
        .select(fn.count(DemoTable.id))
        .scalar()
    ) == 0:

        # 分批插入
        for batch in range(10):
            (
                DemoTable
                .insert_many(
                    demo_df
                    .iloc[batch*10000:(batch+1)*10000, :]
                    .to_dict('records')
                )
                .execute()
            )
'''
                ),

                fac.AntdDivider(isDashed=True),

                html.Div(
                    id='基于pandas的远程数据加载示例'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination-demo-pandas',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(demo_df.shape[0])
                                    }
                                    for column in demo_df.columns
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': demo_df.shape[0],
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页驱动（pandas示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(demo_df.shape[0])
            }
            for column in demo_df.columns
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': demo_df.shape[0],
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    Output('table-server-side-mode-pagination-demo-pandas', 'data'),
    Input('table-server-side-mode-pagination-demo-pandas', 'pagination')
)
def table_server_side_mode_pagination_demo_pandas(pagination):

    if pagination:
        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
            :
        ]

        time.sleep(0.5) # 渲染加载动画更好看 ^_^
        return data_frame.to_dict('records')

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
                    id='翻页驱动（pandas示例）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination+sort-demo-pandas',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(demo_df.shape[0])
                                    }
                                    for column in demo_df.columns
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': demo_df.shape[0],
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                },
                                sortOptions={
                                    'sortDataIndexes': demo_df.columns
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页+单字段排序驱动（pandas示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+sort-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(demo_df.shape[0])
            }
            for column in demo_df.columns
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': demo_df.shape[0],
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        },
        sortOptions={
            'sortDataIndexes': demo_df.columns
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-pandas', 'data'),
    [Input('table-server-side-mode-pagination+sort-demo-pandas', 'pagination'),
     Input('table-server-side-mode-pagination+sort-demo-pandas', 'sorter')],
)
def table_server_side_mode_pagination_filter_demo_pandas(pagination, sorter):

    if pagination:

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从demo_df中抽取对应数据帧
            data_frame = (
                demo_df
                .sort_values(
                    sorter['columns'][0],
                    ascending=sorter['orders'][0] == 'ascend'
                )
                .iloc[
                    (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
                    :
                ]
            )

            return data_frame.to_dict('records')

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
            :
        ]

        return data_frame.to_dict('records')

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
                    id='翻页+单字段排序驱动（pandas示例）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination+multi-sort-demo-pandas',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(demo_df.shape[0])
                                    }
                                    for column in demo_df.columns
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': demo_df.shape[0],
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                },
                                sortOptions={
                                    'sortDataIndexes': demo_df.columns,
                                    'multiple': 'auto'
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页+组合排序驱动（pandas示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+multi-sort-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(demo_df.shape[0])
            }
            for column in demo_df.columns
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': demo_df.shape[0],
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        },
        sortOptions={
            'sortDataIndexes': demo_df.columns,
            'multiple': 'auto'
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    Output('table-server-side-mode-pagination+multi-sort-demo-pandas', 'data'),
    [Input('table-server-side-mode-pagination+multi-sort-demo-pandas', 'pagination'),
     Input('table-server-side-mode-pagination+multi-sort-demo-pandas', 'sorter')],
)
def table_server_side_mode_pagination_multi_sort_demo_pandas(pagination, sorter):

    if pagination:

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从demo_df中抽取对应数据帧
            data_frame = (
                demo_df
                .sort_values(
                    sorter['columns'],
                    ascending=[
                        item == 'ascend'
                        for item in
                        sorter['orders']
                    ]
                )
                .iloc[
                    (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
                    :
                ]
            )

            return data_frame.to_dict('records')

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
            :
        ]

        return data_frame.to_dict('records')

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
                    id='翻页+组合排序驱动（pandas示例）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination+filter-demo-pandas',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(demo_df.shape[0])
                                    }
                                    for column in demo_df.columns
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': demo_df.shape[0],
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                },
                                filterOptions={
                                    '字段1': {
                                        'filterMode': 'keyword'
                                    },
                                    '字段2': {
                                        'filterCustomItems': demo_df['字段2'].unique(),
                                        'filterMultiple': True,
                                        'filterSearch': True
                                    }
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页+筛选驱动（pandas示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+filter-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(demo_df.shape[0])
            }
            for column in demo_df.columns
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': demo_df.shape[0],
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        },
        filterOptions={
            '字段1': {
                'filterMode': 'keyword'
            },
            '字段2': {
                'filterCustomItems': demo_df['字段2'].unique(),
                'filterMultiple': True,
                'filterSearch': True
            }
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    [Output('table-server-side-mode-pagination+filter-demo-pandas', 'data'),
     Output('table-server-side-mode-pagination+filter-demo-pandas', 'pagination')],
    [Input('table-server-side-mode-pagination+filter-demo-pandas', 'pagination'),
     Input('table-server-side-mode-pagination+filter-demo-pandas', 'filter')],
    State('table-server-side-mode-pagination+filter-demo-pandas', 'filterOptions')
)
def table_server_side_mode_pagination_filter_demo_pandas(pagination,
                                                         filter_,
                                                         filterOptions):

    if pagination:

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):

            # 根据当前分页的current参数、pageSize参数，筛选后从demo_df中抽取对应数据帧
            valid_filters = [(key, value)
                             for key, value in filter_.items() if value]

            filter_conditions = (
                f'`{valid_filters[0][0]}` == {valid_filters[0][1]}'
                if filterOptions[valid_filters[0][0]].get('filterMode') != 'keyword'
                else
                f'`{valid_filters[0][0]}`.str.contains("{valid_filters[0][1][0]}")'
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions += ' and '
                filter_conditions += (
                    f'`{valid_filter[0]}` == {valid_filter[1]}'
                    if filterOptions[valid_filter[0]].get('filterMode') != 'keyword'
                    else
                    f'`{valid_filter[0]}`.str.contains("{valid_filter[1][0]}")'
                )

            # 计算经过筛选后的符合条件记录值数量
            match_records_count = (
                demo_df
                .query(filter_conditions)
                .shape[0]
            )

            data_frame = (
                demo_df
                .query(filter_conditions)
                .iloc[
                    (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
                    :
                ]
            )

            return [
                data_frame.to_dict('records'),
                {
                    **pagination,
                    'total': match_records_count
                }
            ]

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1)*pagination['pageSize']:pagination['current']*pagination['pageSize'],
            :
        ]

        return [
            data_frame.to_dict('records'),
            {
                **pagination,
                'total': demo_df.shape[0]
            }
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
                    id='翻页+筛选驱动（pandas示例）',
                    className='div-highlight'
                ),

                html.Div(
                    id='基于数据库的远程数据加载示例'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination-demo-sql',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
                                    }
                                    for column in DemoTable._meta.fields.keys()
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': (
                                        DemoTable
                                        .select(fn.count(DemoTable.id))
                                        .scalar()
                                    ),
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页驱动（数据库示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination-demo-sql',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': (
                DemoTable
                .select(fn.count(DemoTable.id))
                .scalar()
            ),
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    Output('table-server-side-mode-pagination-demo-sql', 'data'),
    Input('table-server-side-mode-pagination-demo-sql', 'pagination')
)
def table_server_side_mode_pagination_demo_sql(pagination):

    if pagination:
        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable
            .select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return list(data_frame)

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
                    id='翻页驱动（数据库示例）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination+sort-demo-sql',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
                                    }
                                    for column in DemoTable._meta.fields.keys()
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': (
                                        DemoTable
                                        .select(fn.count(DemoTable.id))
                                        .scalar()
                                    ),
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                },
                                sortOptions={
                                    'sortDataIndexes': list(DemoTable._meta.fields.keys())
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页+单字段排序驱动（数据库示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+sort-demo-sql',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': (
                DemoTable
                .select(fn.count(DemoTable.id))
                .scalar()
            ),
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        },
        sortOptions={
            'sortDataIndexes': list(DemoTable._meta.fields.keys())
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-sql', 'data'),
    [Input('table-server-side-mode-pagination+sort-demo-sql', 'pagination'),
     Input('table-server-side-mode-pagination+sort-demo-sql', 'sorter')],
)
def table_server_side_mode_pagination_sort_demo_sql(pagination, sorter):

    if pagination:

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从DemoTable中抽取对应数据帧
            data_frame = (
                DemoTable
                .select()
                .order_by(
                    getattr(DemoTable, sorter['columns'][0])
                    if sorter['orders'][0] == 'ascend'
                    else getattr(DemoTable, sorter['columns'][0]).desc()
                )
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return list(data_frame)

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable
            .select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return list(data_frame)

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
                    id='翻页+单字段排序驱动（数据库示例）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination+multi-sort-demo-sql',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
                                    }
                                    for column in DemoTable._meta.fields.keys()
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': (
                                        DemoTable
                                        .select(fn.count(DemoTable.id))
                                        .scalar()
                                    ),
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                },
                                sortOptions={
                                    'sortDataIndexes': list(DemoTable._meta.fields.keys()),
                                    'multiple': 'auto'
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页+组合排序驱动（数据库示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+multi-sort-demo-sql',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': (
                DemoTable
                .select(fn.count(DemoTable.id))
                .scalar()
            ),
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        },
        sortOptions={
            'sortDataIndexes': list(DemoTable._meta.fields.keys()),
            'multiple': 'auto'
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    Output('table-server-side-mode-pagination+multi-sort-demo-sql', 'data'),
    [Input('table-server-side-mode-pagination+multi-sort-demo-sql', 'pagination'),
     Input('table-server-side-mode-pagination+multi-sort-demo-sql', 'sorter')],
)
def table_server_side_mode_pagination_multi_sort_demo_sql(pagination, sorter):

    if pagination:

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从DemoTable中抽取对应数据帧
            data_frame = (
                DemoTable
                .select()
                .order_by(
                    *[
                        getattr(DemoTable, column)
                        if order == 'ascend'
                        else getattr(DemoTable, column).desc()
                        for column, order in zip(
                            sorter['columns'], sorter['orders']
                        )
                    ]
                )
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return list(data_frame)

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable
            .select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return list(data_frame)

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
                    id='翻页+组合排序驱动（数据库示例）',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            fac.AntdTable(
                                id='table-server-side-mode-pagination+filter-demo-sql',
                                columns=[
                                    {
                                        'title': column,
                                        'dataIndex': column,
                                        'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
                                    }
                                    for column in DemoTable._meta.fields.keys()
                                ],
                                bordered=True,
                                # 关键参数
                                mode='server-side',
                                pagination={
                                    'total': (
                                        DemoTable
                                        .select(fn.count(DemoTable.id))
                                        .scalar()
                                    ),
                                    'current': 1,
                                    'pageSize': 5,
                                    'showSizeChanger': True,
                                    'pageSizeOptions': [5, 10],
                                    'position': 'topCenter',
                                    'showQuickJumper': True
                                },
                                filterOptions={
                                    '字段1': {
                                        'filterMode': 'keyword'
                                    },
                                    '字段2': {
                                        'filterCustomItems': [
                                            item.字段2
                                            for item in (
                                                DemoTable
                                                .select(DemoTable.字段2)
                                                .distinct()
                                            )
                                        ],
                                        'filterMultiple': True,
                                        'filterSearch': True
                                    }
                                }
                            ),
                            text='数据加载中',
                            size='small'
                        ),

                        fac.AntdDivider(
                            '翻页+筛选驱动（数据库示例）',
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
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+filter-demo-sql',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(len(DemoTable._meta.fields))
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': (
                DemoTable
                .select(fn.count(DemoTable.id))
                .scalar()
            ),
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True
        },
        filterOptions={
            '字段1': {
                'filterMode': 'keyword'
            },
            '字段2': {
                'filterCustomItems': [
                    item.字段2
                    for item in (
                        DemoTable
                        .select(DemoTable.字段2)
                        .distinct()
                    )
                ],
                'filterMultiple': True,
                'filterSearch': True
            }
        }
    ),
    text='数据加载中',
    size='small'
)

...

@app.callback(
    [Output('table-server-side-mode-pagination+filter-demo-sql', 'data'),
     Output('table-server-side-mode-pagination+filter-demo-sql', 'pagination')],
    [Input('table-server-side-mode-pagination+filter-demo-sql', 'pagination'),
     Input('table-server-side-mode-pagination+filter-demo-sql', 'filter')],
    State('table-server-side-mode-pagination+filter-demo-sql', 'filterOptions')
)
def table_server_side_mode_pagination_filter_demo_sql(pagination,
                                                      filter_,
                                                      filterOptions):

    if pagination:

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):

            # 根据当前分页的current参数、pageSize参数，筛选后从DemoTable中抽取对应数据帧
            valid_filters = [(key, value)
                             for key, value in filter_.items() if value]

            filter_conditions = (
                getattr(DemoTable, valid_filters[0][0]) << valid_filters[0][1]
                if filterOptions[valid_filters[0][0]].get('filterMode') != 'keyword'
                else
                getattr(DemoTable, valid_filters[0][0])
                .contains(valid_filters[0][1][0])
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions = filter_conditions & (
                    getattr(
                        DemoTable, valid_filter[0]) == valid_filter[1]
                    if filterOptions[valid_filter[0]].get('filterMode') != 'keyword'
                    else
                    getattr(DemoTable, valid_filter[0])
                    .contains(valid_filter[1][0])
                )

            # 计算经过筛选后的符合条件记录值数量
            match_records_count = (
                DemoTable
                .select(fn.count(DemoTable.id))
                .where(filter_conditions)
                .scalar()
            )

            data_frame = (
                DemoTable
                .select()
                .where(filter_conditions)
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return [
                list(data_frame),
                {
                    **pagination,
                    'total': match_records_count
                }
            ]

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable
            .select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return [
            list(data_frame),
            {
                **pagination,
                'total': (
                    DemoTable
                    .select(fn.count(DemoTable.id))
                    .scalar()
                )
            }
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
                    id='翻页+筛选驱动（数据库示例）',
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
                    {
                        'title': '基于pandas的远程数据加载示例',
                        'href': '#基于pandas的远程数据加载示例',
                        'children': [
                            {'title': '翻页驱动（pandas示例）', 'href': '#翻页驱动（pandas示例）'},
                            {
                                'title': '翻页+单字段排序驱动（pandas示例）',
                                'href': '#翻页+单字段排序驱动（pandas示例）'
                            },
                            {
                                'title': '翻页+组合排序驱动（pandas示例）',
                                'href': '#翻页+组合排序驱动（pandas示例）'
                            },
                            {
                                'title': '翻页+筛选驱动（pandas示例）',
                                'href': '#翻页+筛选驱动（pandas示例）'
                            }
                        ]
                    },
                    {
                        'title': '基于数据库的远程数据加载示例',
                        'href': '#基于数据库的远程数据加载示例',
                        'children': [
                            {'title': '翻页驱动（数据库示例）', 'href': '#翻页驱动（数据库示例）'},
                            {
                                'title': '翻页+单字段排序驱动（数据库示例）',
                                'href': '#翻页+单字段排序驱动（数据库示例）'
                            },
                            {
                                'title': '翻页+组合排序驱动（数据库示例）',
                                'href': '#翻页+组合排序驱动（数据库示例）'
                            },
                            {
                                'title': '翻页+筛选驱动（数据库示例）',
                                'href': '#翻页+筛选驱动（数据库示例）'
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
            component_name='AntdTable'
        )
    ],
    style={
        'display': 'flex'
    }
)
