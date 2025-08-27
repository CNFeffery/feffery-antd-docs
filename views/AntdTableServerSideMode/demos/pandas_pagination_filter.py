import time

import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output, State

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
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id='table-server-side-mode-pagination+filter-demo-pandas',
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

    elif current_locale == 'en-us':
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id='table-server-side-mode-pagination+filter-demo-pandas',
                locale='en-us',
                # Titles translated; dataIndex must remain the original column keys
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
                # filterOptions keys must match dataIndex (original column names)
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
            text='Loading data',
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

        if filter_ and any([value for value in filter_.values()]):
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


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == 'zh-cn':
        return [
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
"""
            }
        ]
    elif current_locale == 'en-us':
        return [
            {
                'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+filter-demo-pandas',
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
        # filterOptions keys must match the original dataIndex values
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
    text='Loading data',
    size='small',
)
"""
            }
        ]
