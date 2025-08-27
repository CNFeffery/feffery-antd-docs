import time

import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app

from .mock_data import demo_df


def _en_title(name: str) -> str:
    return (
        f'Field {name[2:]}'
        if name.startswith('字段') and name[2:].isdigit()
        else name
    )


def render() -> Component:
    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id='table-server-side-mode-pagination+sort-demo-pandas',
                columns=[
                    {'title': column, 'dataIndex': column}
                    for column in demo_df.columns
                ],
                bordered=True,
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
                sortOptions={'sortDataIndexes': list(demo_df.columns)},
                tableLayout='fixed',
            ),
            text='数据加载中',
            size='small',
        )

    elif current_locale == 'en-us':
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id='table-server-side-mode-pagination+sort-demo-pandas',
                locale='en-us',
                columns=[
                    {'title': _en_title(col), 'dataIndex': col}
                    for col in demo_df.columns
                ],
                bordered=True,
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
                sortOptions={'sortDataIndexes': list(demo_df.columns)},
                tableLayout='fixed',
            ),
            text='Loading data',
            size='small',
        )

    return demo_contents


@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-pandas', 'data'),
    [
        Input(
            'table-server-side-mode-pagination+sort-demo-pandas', 'pagination'
        ),
        Input('table-server-side-mode-pagination+sort-demo-pandas', 'sorter'),
    ],
)
def table_server_side_mode_pagination_filter_demo_pandas(pagination, sorter):
    if pagination:
        time.sleep(0.5)

        if sorter and sorter.get('columns'):
            data_frame = demo_df.sort_values(
                sorter['columns'][0],
                ascending=(sorter['orders'][0] == 'ascend'),
            ).iloc[
                (pagination['current'] - 1)
                * pagination['pageSize'] : pagination['current']
                * pagination['pageSize'],
                :,
            ]
            return data_frame.to_dict('records')

        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]
        return data_frame.to_dict('records')

    return dash.no_update


def code_string() -> list:
    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
            {
                'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+sort-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
            }
            for column in demo_df.columns
        ],
        bordered=True,
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
        sortOptions={'sortDataIndexes': demo_df.columns},
        tableLayout='fixed',
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-pandas', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-pandas', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-pandas', 'sorter'),
    ],
)
def table_server_side_mode_pagination_filter_demo_pandas(pagination, sorter):
    if pagination:
        time.sleep(0.5)

        if sorter and sorter['columns']:
            data_frame = demo_df.sort_values(
                sorter['columns'][0], ascending=sorter['orders'][0] == 'ascend'
            ).iloc[
                (pagination['current'] - 1) * pagination['pageSize']
                : pagination['current'] * pagination['pageSize'],
                :,
            ]

            return data_frame.to_dict('records')

        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize']
            : pagination['current'] * pagination['pageSize'],
            :,
        ]

        return data_frame.to_dict('records')

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
        id='table-server-side-mode-pagination+sort-demo-pandas',
        locale="en-us",
        columns=[
            {
                'title': (f"Field {col[2:]}" if col.startswith('字段') and col[2:].isdigit() else col),
                'dataIndex': col,
            }
            for col in demo_df.columns
        ],
        bordered=True,
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
        sortOptions={'sortDataIndexes': demo_df.columns},
        tableLayout='fixed',
    ),
    text='Loading data',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-pandas', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-pandas', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-pandas', 'sorter'),
    ],
)
def table_server_side_mode_pagination_filter_demo_pandas(pagination, sorter):
    if pagination:
        time.sleep(0.5)

        if sorter and sorter.get('columns'):
            data_frame = demo_df.sort_values(
                sorter['columns'][0], ascending=(sorter['orders'][0] == 'ascend')
            ).iloc[
                (pagination['current'] - 1) * pagination['pageSize']
                : pagination['current'] * pagination['pageSize'],
                :,
            ]

            return data_frame.to_dict('records')

        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize']
            : pagination['current'] * pagination['pageSize'],
            :,
        ]

        return data_frame.to_dict('records')

    return dash.no_update
"""
            }
        ]
