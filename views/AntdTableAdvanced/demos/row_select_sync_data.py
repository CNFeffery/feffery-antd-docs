import json
import random

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == "zh-cn":
        btn_text = "刷新数据"
        title = lambda i: f"字段{i}"
        key = lambda i: f"字段{i}"
    else:  # en-us fallback
        btn_text = "Refresh Data"
        title = lambda i: f"Field {i}"
        key = lambda i: f"Field {i}"

    columns = [{"title": title(i), "dataIndex": key(i)} for i in range(1, 4)]
    data = [
        {
            **{key(i): round(random.uniform(0, 10), 3) for i in range(1, 4)},
            "key": f"row-{row+1}",
        }
        for row in range(3)
    ]

    demo_contents = fac.AntdSpace(
        [
            fac.AntdButton(
                btn_text,
                id="table-row-selection-sync-selected-rows-demo-update-data",
                type="primary",
            ),
            fac.AntdTable(
                id="table-row-selection-sync-selected-rows-demo",
                columns=columns,
                data=data,
                rowSelectionType="checkbox",
                selectedRowsSyncWithData=True,
            ),
            html.Pre(id="table-row-selection-sync-selected-rows-demo-output"),
        ],
        direction="vertical",
        style={"width": "100%"},
    )

    return demo_contents


@app.callback(
    Output("table-row-selection-sync-selected-rows-demo", "data"),
    Input("table-row-selection-sync-selected-rows-demo-update-data", "nClicks"),
    prevent_initial_call=True,
)
def table_row_selection_sync_selected_rows_demo_update_data(nClicks):
    # Keep keys aligned with whatever was rendered (Chinese or English)
    locale = get_current_locale()
    key_fn = (lambda i: f"字段{i}") if locale == "zh-cn" else (lambda i: f"Field {i}")

    return [
        {
            **{key_fn(i): round(random.uniform(0, 10), 3) for i in range(1, 4)},
            "key": f"row-{row+1}",
        }
        for row in range(3)
    ]


@app.callback(
    Output("table-row-selection-sync-selected-rows-demo-output", "children"),
    [
        Input("table-row-selection-sync-selected-rows-demo", "selectedRowKeys"),
        Input("table-row-selection-sync-selected-rows-demo", "selectedRows"),
    ],
)
def table_row_selection_sync_selected_rows_demo(selectedRowKeys, selectedRows):
    return json.dumps(
        dict(selectedRowKeys=selectedRowKeys, selectedRows=selectedRows),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdButton(
            '刷新数据',
            id='table-row-selection-sync-selected-rows-demo-update-data',
            type='primary',
        ),
        fac.AntdTable(
            id='table-row-selection-sync-selected-rows-demo',
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
                for i in range(1, 4)
            ],
            data=[
                {
                    **{f'字段{i}': round(random.uniform(0, 10), 3) for i in range(1, 4)},
                    'key': f'row-{row+1}',
                }
                for row in range(3)
            ],
            rowSelectionType='checkbox',
            selectedRowsSyncWithData=True,
        ),
        html.Pre(id='table-row-selection-sync-selected-rows-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

# ...

@app.callback(
    Output('table-row-selection-sync-selected-rows-demo', 'data'),
    Input('table-row-selection-sync-selected-rows-demo-update-data', 'nClicks'),
    prevent_initial_call=True,
)
def table_row_selection_sync_selected_rows_demo_update_data(nClicks):
    return [
        {
            **{f'字段{i}': round(random.uniform(0, 10), 3) for i in range(1, 4)},
            'key': f'row-{row+1}',
        }
        for row in range(3)
    ]


@app.callback(
    Output('table-row-selection-sync-selected-rows-demo-output', 'children'),
    [
        Input('table-row-selection-sync-selected-rows-demo', 'selectedRowKeys'),
        Input('table-row-selection-sync-selected-rows-demo', 'selectedRows'),
    ],
)
def table_row_selection_sync_selected_rows_demo(selectedRowKeys, selectedRows):
    return json.dumps(
        dict(selectedRowKeys=selectedRowKeys, selectedRows=selectedRows),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
    else:  # en-us
        return [
            {
                "code": """
fac.AntdSpace(
    [
        fac.AntdButton(
            'Refresh Data',
            id='table-row-selection-sync-selected-rows-demo-update-data',
            type='primary',
        ),
        fac.AntdTable(
            id='table-row-selection-sync-selected-rows-demo',
            columns=[
                {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
                for i in range(1, 4)
            ],
            data=[
                {
                    **{f'Field {i}': round(random.uniform(0, 10), 3) for i in range(1, 4)},
                    'key': f'row-{row+1}',
                }
                for row in range(3)
            ],
            rowSelectionType='checkbox',
            selectedRowsSyncWithData=True,
        ),
        html.Pre(id='table-row-selection-sync-selected-rows-demo-output'),
    ],
    direction='vertical',
    style={'width': '100%'},
)

# ...

@app.callback(
    Output('table-row-selection-sync-selected-rows-demo', 'data'),
    Input('table-row-selection-sync-selected-rows-demo-update-data', 'nClicks'),
    prevent_initial_call=True,
)
def table_row_selection_sync_selected_rows_demo_update_data(nClicks):
    return [
        {
            **{f'Field {i}': round(random.uniform(0, 10), 3) for i in range(1, 4)},
            'key': f'row-{row+1}',
        }
        for row in range(3)
    ]


@app.callback(
    Output('table-row-selection-sync-selected-rows-demo-output', 'children'),
    [
        Input('table-row-selection-sync-selected-rows-demo', 'selectedRowKeys'),
        Input('table-row-selection-sync-selected-rows-demo', 'selectedRows'),
    ],
)
def table_row_selection_sync_selected_rows_demo(selectedRowKeys, selectedRows):
    return json.dumps(
        dict(selectedRowKeys=selectedRowKeys, selectedRows=selectedRows),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
