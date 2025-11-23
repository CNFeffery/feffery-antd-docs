import time

import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output
from peewee import fn

from i18n import get_current_locale
from server import app

from .mock_data import DemoTable


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()
    field_names = list(DemoTable._meta.fields.keys())
    col_width = f'calc(100% / {len(field_names)})'

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id='table-server-side-mode-pagination+sort-demo-sql',
                columns=[
                    {
                        'title': column,
                        'dataIndex': column,
                        'width': col_width,
                    }
                    for column in field_names
                ],
                bordered=True,
                mode='server-side',
                pagination={
                    'total': (
                        DemoTable.select(fn.count(DemoTable.id)).scalar()
                    ),
                    'current': 1,
                    'pageSize': 5,
                    'showSizeChanger': True,
                    'pageSizeOptions': [5, 10],
                    'position': 'topCenter',
                    'showQuickJumper': True,
                },
                sortOptions={'sortDataIndexes': field_names},
            ),
            text='数据加载中',
            size='small',
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id='table-server-side-mode-pagination+sort-demo-sql',
                locale='en-us',
                columns=[
                    {
                        'title': (
                            f'Field {column[2:]}'
                            if column.startswith('字段')
                            and column[2:].isdigit()
                            else column
                        ),
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
                    'total': (
                        DemoTable.select(fn.count(DemoTable.id)).scalar()
                    ),
                    'current': 1,
                    'pageSize': 5,
                    'showSizeChanger': True,
                    'pageSizeOptions': [5, 10],
                    'position': 'topCenter',
                    'showQuickJumper': True,
                },
                sortOptions={
                    'sortDataIndexes': list(DemoTable._meta.fields.keys())
                },
            ),
            text='Loading data',
            size='small',
        )

    return demo_contents


@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-sql', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-sql', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-sql', 'sorter'),
    ],
)
def table_server_side_mode_pagination_sort_demo_sql(pagination, sorter):
    if pagination:
        time.sleep(0.5)

        if sorter and sorter.get('columns'):
            data_frame = (
                DemoTable.select()
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

        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )
        return list(data_frame)

    return dash.no_update


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+sort-demo-sql',
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
        sortOptions={
            'sortDataIndexes': list(DemoTable._meta.fields.keys())
        },
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-sql', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-sql', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-sql', 'sorter'),
    ],
)
def table_server_side_mode_pagination_sort_demo_sql(pagination, sorter):
    if pagination:
        time.sleep(0.5)

        if sorter and sorter.get('columns'):
            data_frame = (
                DemoTable.select()
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

        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )
        return list(data_frame)

    return dash.no_update
"""
            }
        ]
    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+sort-demo-sql',
        locale='en-us',
        columns=[
            {
                'title': (
                    f'Field {column[2:]}'
                    if column.startswith('字段')
                    and column[2:].isdigit()
                    else column
                ),
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
            'total': (
                DemoTable.select(fn.count(DemoTable.id)).scalar()
            ),
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True,
        },
        sortOptions={
            'sortDataIndexes': list(DemoTable._meta.fields.keys())
        },
    ),
    text='Loading data',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-sql', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-sql', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-sql', 'sorter'),
    ],
)
def table_server_side_mode_pagination_sort_demo_sql(pagination, sorter):
    if pagination:
        time.sleep(0.5)

        if sorter and sorter.get('columns'):
            data_frame = (
                DemoTable.select()
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

        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )
        return list(data_frame)

    return dash.no_update
"""
            }
        ]
