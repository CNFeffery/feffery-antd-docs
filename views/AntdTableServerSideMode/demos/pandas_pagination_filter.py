import dash
import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app
from .mock_data import demo_df


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpin(
        fac.AntdTable(
            id='table-server-side-mode-pagination+filter-demo-pandas',
            columns=[
                {
                    'title': column,
                    'dataIndex': column,
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
                'showQuickJumper': True,
            },
            filterOptions={
                '字段1': {'filterMode': 'keyword'},
                '字段2': {
                    'filterCustomItems': demo_df['字段2'].unique(),
                    'filterMultiple': True,
                    'filterSearch': True,
                },
            },
            tableLayout='fixed',
        ),
        text='数据加载中',
        size='small',
    )

    return demo_contents


@app.callback(
    [
        Output('table-server-side-mode-pagination+filter-demo-pandas', 'data'),
        Output(
            'table-server-side-mode-pagination+filter-demo-pandas', 'pagination'
        ),
    ],
    [
        Input(
            'table-server-side-mode-pagination+filter-demo-pandas', 'pagination'
        ),
        Input('table-server-side-mode-pagination+filter-demo-pandas', 'filter'),
    ],
    State(
        'table-server-side-mode-pagination+filter-demo-pandas', 'filterOptions'
    ),
)
def table_server_side_mode_pagination_filter_demo_pandas(
    pagination, filter_, filterOptions
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):
            # 根据当前分页的current参数、pageSize参数，筛选后从demo_df中抽取对应数据帧
            valid_filters = [
                (key, value) for key, value in filter_.items() if value
            ]

            filter_conditions = (
                f'`{valid_filters[0][0]}` == {valid_filters[0][1]}'
                if filterOptions[valid_filters[0][0]].get('filterMode')
                != 'keyword'
                else f'`{valid_filters[0][0]}`.str.contains("{valid_filters[0][1][0]}")'
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions += ' and '
                filter_conditions += (
                    f'`{valid_filter[0]}` == {valid_filter[1]}'
                    if filterOptions[valid_filter[0]].get('filterMode')
                    != 'keyword'
                    else f'`{valid_filter[0]}`.str.contains("{valid_filter[1][0]}")'
                )

            # 计算经过筛选后的符合条件记录值数量
            match_records_count = demo_df.query(filter_conditions).shape[0]

            data_frame = demo_df.query(filter_conditions).iloc[
                (pagination['current'] - 1)
                * pagination['pageSize'] : pagination['current']
                * pagination['pageSize'],
                :,
            ]

            return [
                data_frame.to_dict('records'),
                {**pagination, 'total': match_records_count},
            ]

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]

        return [
            data_frame.to_dict('records'),
            {**pagination, 'total': demo_df.shape[0]},
        ]

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+filter-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
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
            'showQuickJumper': True,
        },
        filterOptions={
            '字段1': {'filterMode': 'keyword'},
            '字段2': {
                'filterCustomItems': demo_df['字段2'].unique(),
                'filterMultiple': True,
                'filterSearch': True,
            },
        },
        tableLayout='fixed',
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    [
        Output('table-server-side-mode-pagination+filter-demo-pandas', 'data'),
        Output(
            'table-server-side-mode-pagination+filter-demo-pandas', 'pagination'
        ),
    ],
    [
        Input(
            'table-server-side-mode-pagination+filter-demo-pandas', 'pagination'
        ),
        Input('table-server-side-mode-pagination+filter-demo-pandas', 'filter'),
    ],
    State(
        'table-server-side-mode-pagination+filter-demo-pandas', 'filterOptions'
    ),
)
def table_server_side_mode_pagination_filter_demo_pandas(
    pagination, filter_, filterOptions
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):
            # 根据当前分页的current参数、pageSize参数，筛选后从demo_df中抽取对应数据帧
            valid_filters = [
                (key, value) for key, value in filter_.items() if value
            ]

            filter_conditions = (
                f'`{valid_filters[0][0]}` == {valid_filters[0][1]}'
                if filterOptions[valid_filters[0][0]].get('filterMode')
                != 'keyword'
                else f'`{valid_filters[0][0]}`.str.contains("{valid_filters[0][1][0]}")'
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions += ' and '
                filter_conditions += (
                    f'`{valid_filter[0]}` == {valid_filter[1]}'
                    if filterOptions[valid_filter[0]].get('filterMode')
                    != 'keyword'
                    else f'`{valid_filter[0]}`.str.contains("{valid_filter[1][0]}")'
                )

            # 计算经过筛选后的符合条件记录值数量
            match_records_count = demo_df.query(filter_conditions).shape[0]

            data_frame = demo_df.query(filter_conditions).iloc[
                (pagination['current'] - 1)
                * pagination['pageSize'] : pagination['current']
                * pagination['pageSize'],
                :,
            ]

            return [
                data_frame.to_dict('records'),
                {**pagination, 'total': match_records_count},
            ]

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]

        return [
            data_frame.to_dict('records'),
            {**pagination, 'total': demo_df.shape[0]},
        ]

    return dash.no_update
"""
    }
]
