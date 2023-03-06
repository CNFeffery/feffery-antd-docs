import dash
import time
import numpy as np
import pandas as pd
from peewee import (
    SqliteDatabase,
    CharField,
    IntegerField,
    Model,
    fn
)
from dash.dependencies import Input, Output, State

from server import app


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

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return data_frame.to_dict('records')

    return dash.no_update


@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-pandas', 'data'),
    [Input('table-server-side-mode-pagination+sort-demo-pandas', 'pagination'),
     Input('table-server-side-mode-pagination+sort-demo-pandas', 'sorter')],
)
def table_server_side_mode_pagination_sort_demo_pandas(pagination, sorter):

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
