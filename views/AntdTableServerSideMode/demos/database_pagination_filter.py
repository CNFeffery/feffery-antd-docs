import dash
import time
from peewee import fn
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

from server import app
from .mock_data import DemoTable


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpin(
        fac.AntdTable(
            id='table-server-side-mode-pagination+filter-demo-sql',
            columns=[
                {
                    'title': column,
                    'dataIndex': column,
                    'width': 'calc(100% / {})'.format(
                        len(DemoTable._meta.fields)
                    ),
                }
                for column in DemoTable._meta.fields.keys()
            ],
            bordered=True,
            # 关键参数
            mode='server-side',
            pagination={
                'total': (DemoTable.select(fn.count(DemoTable.id)).scalar()),
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
                    'filterCustomItems': [
                        item.字段2
                        for item in (
                            DemoTable.select(DemoTable.字段2).distinct()
                        )
                    ],
                    'filterMultiple': True,
                    'filterSearch': True,
                },
            },
        ),
        text='数据加载中',
        size='small',
    )

    return demo_contents


@app.callback(
    [
        Output('table-server-side-mode-pagination+filter-demo-sql', 'data'),
        Output(
            'table-server-side-mode-pagination+filter-demo-sql', 'pagination'
        ),
    ],
    [
        Input(
            'table-server-side-mode-pagination+filter-demo-sql', 'pagination'
        ),
        Input('table-server-side-mode-pagination+filter-demo-sql', 'filter'),
    ],
    State('table-server-side-mode-pagination+filter-demo-sql', 'filterOptions'),
)
def table_server_side_mode_pagination_filter_demo_sql(
    pagination, filter_, filterOptions
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):
            # 根据当前分页的current参数、pageSize参数，筛选后从DemoTable中抽取对应数据帧
            valid_filters = [
                (key, value) for key, value in filter_.items() if value
            ]

            filter_conditions = (
                getattr(DemoTable, valid_filters[0][0]) << valid_filters[0][1]
                if filterOptions[valid_filters[0][0]].get('filterMode')
                != 'keyword'
                else getattr(DemoTable, valid_filters[0][0]).contains(
                    valid_filters[0][1][0]
                )
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions = filter_conditions & (
                    getattr(DemoTable, valid_filter[0]) << valid_filter[1]
                    if filterOptions[valid_filter[0]].get('filterMode')
                    != 'keyword'
                    else getattr(DemoTable, valid_filter[0]).contains(
                        valid_filter[1][0]
                    )
                )

            # 计算经过筛选后的符合条件记录值数量
            match_records_count = (
                DemoTable.select(fn.count(DemoTable.id))
                .where(filter_conditions)
                .scalar()
            )

            data_frame = (
                DemoTable.select()
                .where(filter_conditions)
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return [
                list(data_frame),
                {**pagination, 'total': match_records_count},
            ]

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return [
            list(data_frame),
            {
                **pagination,
                'total': (DemoTable.select(fn.count(DemoTable.id)).scalar()),
            },
        ]

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+filter-demo-sql',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(
                    len(DemoTable._meta.fields)
                ),
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': (DemoTable.select(fn.count(DemoTable.id)).scalar()),
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
                'filterCustomItems': [
                    item.字段2
                    for item in (
                        DemoTable.select(DemoTable.字段2).distinct()
                    )
                ],
                'filterMultiple': True,
                'filterSearch': True,
            },
        },
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    [
        Output('table-server-side-mode-pagination+filter-demo-sql', 'data'),
        Output(
            'table-server-side-mode-pagination+filter-demo-sql', 'pagination'
        ),
    ],
    [
        Input(
            'table-server-side-mode-pagination+filter-demo-sql', 'pagination'
        ),
        Input('table-server-side-mode-pagination+filter-demo-sql', 'filter'),
    ],
    State('table-server-side-mode-pagination+filter-demo-sql', 'filterOptions'),
)
def table_server_side_mode_pagination_filter_demo_sql(
    pagination, filter_, filterOptions
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):
            # 根据当前分页的current参数、pageSize参数，筛选后从DemoTable中抽取对应数据帧
            valid_filters = [
                (key, value) for key, value in filter_.items() if value
            ]

            filter_conditions = (
                getattr(DemoTable, valid_filters[0][0]) << valid_filters[0][1]
                if filterOptions[valid_filters[0][0]].get('filterMode')
                != 'keyword'
                else getattr(DemoTable, valid_filters[0][0]).contains(
                    valid_filters[0][1][0]
                )
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions = filter_conditions & (
                    getattr(DemoTable, valid_filter[0]) << valid_filter[1]
                    if filterOptions[valid_filter[0]].get('filterMode')
                    != 'keyword'
                    else getattr(DemoTable, valid_filter[0]).contains(
                        valid_filter[1][0]
                    )
                )

            # 计算经过筛选后的符合条件记录值数量
            match_records_count = (
                DemoTable.select(fn.count(DemoTable.id))
                .where(filter_conditions)
                .scalar()
            )

            data_frame = (
                DemoTable.select()
                .where(filter_conditions)
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return [
                list(data_frame),
                {**pagination, 'total': match_records_count},
            ]

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return [
            list(data_frame),
            {
                **pagination,
                'total': (DemoTable.select(fn.count(DemoTable.id)).scalar()),
            },
        ]

    return dash.no_update
"""
    }
]
