import time

import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State
from peewee import fn

from i18n import get_current_locale
from server import app

from .mock_data import DemoTable


def _en_title(name: str) -> str:
    # 简单的“字段N” -> “Field N”映射；其他字段名保持不变
    return (
        f"Field {name[2:]}" if name.startswith("字段") and name[2:].isdigit() else name
    )


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()
    field_names = list(DemoTable._meta.fields.keys())
    col_width = f"calc(100% / {len(field_names)})"

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id="table-server-side-mode-pagination+filter-demo-sql",
                columns=[
                    {
                        "title": column,
                        "dataIndex": column,
                        "width": col_width,
                    }
                    for column in field_names
                ],
                bordered=True,
                mode="server-side",
                pagination={
                    "total": (DemoTable.select(fn.count(DemoTable.id)).scalar()),
                    "current": 1,
                    "pageSize": 5,
                    "showSizeChanger": True,
                    "pageSizeOptions": [5, 10],
                    "position": "topCenter",
                    "showQuickJumper": True,
                },
                filterOptions={
                    "字段1": {"filterMode": "keyword"},
                    "字段2": {
                        "filterCustomItems": [
                            item.字段2
                            for item in (DemoTable.select(DemoTable.字段2).distinct())
                        ],
                        "filterMultiple": True,
                        "filterSearch": True,
                    },
                },
            ),
            text="数据加载中",
            size="small",
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id="table-server-side-mode-pagination+filter-demo-sql",
                locale="en-us",
                columns=[
                    {
                        "title": _en_title(column),
                        "dataIndex": column,  # dataIndex 必须匹配底层数据字段名
                        "width": col_width,
                    }
                    for column in field_names
                ],
                bordered=True,
                mode="server-side",
                pagination={
                    "total": (DemoTable.select(fn.count(DemoTable.id)).scalar()),
                    "current": 1,
                    "pageSize": 5,
                    "showSizeChanger": True,
                    "pageSizeOptions": [5, 10],
                    "position": "topCenter",
                    "showQuickJumper": True,
                },
                # 过滤键必须与 dataIndex 一致（保持底层字段名）
                filterOptions={
                    "Field 1" if False else "字段1": {"filterMode": "keyword"},
                    "Field 2" if False else "字段2": {
                        "filterCustomItems": [
                            item.字段2
                            for item in (DemoTable.select(DemoTable.字段2).distinct())
                        ],
                        "filterMultiple": True,
                        "filterSearch": True,
                    },
                },
            ),
            text="Loading data",
            size="small",
        )

    return demo_contents


@app.callback(
    [
        Output("table-server-side-mode-pagination+filter-demo-sql", "data"),
        Output("table-server-side-mode-pagination+filter-demo-sql", "pagination"),
    ],
    [
        Input("table-server-side-mode-pagination+filter-demo-sql", "pagination"),
        Input("table-server-side-mode-pagination+filter-demo-sql", "filter"),
    ],
    State("table-server-side-mode-pagination+filter-demo-sql", "filterOptions"),
)
def table_server_side_mode_pagination_filter_demo_sql(
    pagination, filter_, filterOptions
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在至少一项有效的筛选操作
        if filter_ and any([value for value in filter_.values()]):
            # 根据当前分页，从 DemoTable 中抽取对应记录
            valid_filters = [(key, value) for key, value in filter_.items() if value]

            filter_conditions = (
                getattr(DemoTable, valid_filters[0][0]) << valid_filters[0][1]
                if filterOptions[valid_filters[0][0]].get("filterMode") != "keyword"
                else getattr(DemoTable, valid_filters[0][0]).contains(
                    valid_filters[0][1][0]
                )
            )

            for valid_filter in valid_filters[1:]:
                filter_conditions = filter_conditions & (
                    getattr(DemoTable, valid_filter[0]) << valid_filter[1]
                    if filterOptions[valid_filter[0]].get("filterMode") != "keyword"
                    else getattr(DemoTable, valid_filter[0]).contains(
                        valid_filter[1][0]
                    )
                )

            match_records_count = (
                DemoTable.select(fn.count(DemoTable.id))
                .where(filter_conditions)
                .scalar()
            )

            data_frame = (
                DemoTable.select()
                .where(filter_conditions)
                .limit(pagination["pageSize"])
                .offset((pagination["current"] - 1) * pagination["pageSize"])
                .dicts()
            )

            return [list(data_frame), {**pagination, "total": match_records_count}]

        # 无筛选：按分页直接返回
        data_frame = (
            DemoTable.select()
            .limit(pagination["pageSize"])
            .offset((pagination["current"] - 1) * pagination["pageSize"])
            .dicts()
        )

        return [
            list(data_frame),
            {
                **pagination,
                "total": (DemoTable.select(fn.count(DemoTable.id)).scalar()),
            },
        ]

    return dash.no_update


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
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
                    for item in (DemoTable.select(DemoTable.字段2).distinct())
                ],
                'filterMultiple': True,
                'filterSearch': True,
            },
        },
    ),
    text='数据加载中',
    size='small',
)
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+filter-demo-sql',
        locale="en-us",
        columns=[
            {
                'title': (f"Field {column[2:]}" if column.startswith('字段') and column[2:].isdigit() else column),
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(
                    len(DemoTable._meta.fields)
                ),
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
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
        # filterOptions 的键必须与 dataIndex 完全一致（保留底层字段名）
        filterOptions={
            '字段1': {'filterMode': 'keyword'},
            '字段2': {
                'filterCustomItems': [
                    item.字段2
                    for item in (DemoTable.select(DemoTable.字段2).distinct())
                ],
                'filterMultiple': True,
                'filterSearch': True,
            },
        },
    ),
    text='Loading data',
    size='small',
)
"""
            }
        ]
