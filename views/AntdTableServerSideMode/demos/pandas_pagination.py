import time

import dash
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app

from .mock_data import demo_df


def _en_title(name: str) -> str:
    return (
        f"Field {name[2:]}" if name.startswith("字段") and name[2:].isdigit() else name
    )


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id="table-server-side-mode-pagination-demo-pandas",
                columns=[
                    {"title": column, "dataIndex": column} for column in demo_df.columns
                ],
                bordered=True,
                mode="server-side",
                pagination={
                    "total": demo_df.shape[0],
                    "current": 1,
                    "pageSize": 5,
                    "showSizeChanger": True,
                    "pageSizeOptions": [5, 10],
                    "position": "topCenter",
                    "showQuickJumper": True,
                },
                tableLayout="fixed",
            ),
            text="数据加载中",
            size="small",
        )

    elif current_locale == "en-us":
        demo_contents = fac.AntdSpin(
            fac.AntdTable(
                id="table-server-side-mode-pagination-demo-pandas",
                locale="en-us",
                # translate titles; keep dataIndex as original keys
                columns=[
                    {"title": _en_title(col), "dataIndex": col}
                    for col in demo_df.columns
                ],
                bordered=True,
                mode="server-side",
                pagination={
                    "total": demo_df.shape[0],
                    "current": 1,
                    "pageSize": 5,
                    "showSizeChanger": True,
                    "pageSizeOptions": [5, 10],
                    "position": "topCenter",
                    "showQuickJumper": True,
                },
                tableLayout="fixed",
            ),
            text="Loading data",
            size="small",
        )

    return demo_contents


@app.callback(
    Output("table-server-side-mode-pagination-demo-pandas", "data"),
    Input("table-server-side-mode-pagination-demo-pandas", "pagination"),
)
def table_server_side_mode_pagination_demo_pandas(pagination):
    if pagination:
        data_frame = demo_df.iloc[
            (pagination["current"] - 1)
            * pagination["pageSize"] : pagination["current"]
            * pagination["pageSize"],
            :,
        ]

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return data_frame.to_dict("records")

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
        id='table-server-side-mode-pagination-demo-pandas',
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
        tableLayout='fixed',
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination-demo-pandas', 'data'),
    Input('table-server-side-mode-pagination-demo-pandas', 'pagination'),
)
def table_server_side_mode_pagination_demo_pandas(pagination):
    if pagination:
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize']
            : pagination['current'] * pagination['pageSize'],
            :,
        ]

        time.sleep(0.5)
        return data_frame.to_dict('records')

    return dash.no_update
"""
            }
        ]
    elif current_locale == "en-us":
        return [
            {
                "code": """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination-demo-pandas',
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
        tableLayout='fixed',
    ),
    text='Loading data',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination-demo-pandas', 'data'),
    Input('table-server-side-mode-pagination-demo-pandas', 'pagination'),
)
def table_server_side_mode_pagination_demo_pandas(pagination):
    if pagination:
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize']
            : pagination['current'] * pagination['pageSize'],
            :,
        ]

        time.sleep(0.5)
        return data_frame.to_dict('records')

    return dash.no_update
"""
            }
        ]
