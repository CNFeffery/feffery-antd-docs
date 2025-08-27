import json

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output, State

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        col_label = lambda i: f"字段{i}"
        cell_value = lambda i, row: f"字段{i}第{row}行"
    else:  # en-us (fallback to en)
        col_label = lambda i: f"Field {i}"
        cell_value = lambda i, row: f"Field {i} Row {row}"

    columns = [
        {"title": col_label(i), "dataIndex": col_label(i), "width": "20%"}
        for i in range(1, 6)
    ]

    data = [
        {
            "key": f"row-{row}",
            **{col_label(i): cell_value(i, row) for i in range(1, 6)},
        }
        for row in range(1, 6)
    ]

    demo_contents = [
        fac.AntdTable(
            id="table-click-event-demo",
            columns=columns,
            data=data,
            bordered=True,
            # listen on 1,3,5
            enableCellClickListenColumns=[col_label(i) for i in range(1, 6, 2)],
        ),
        html.Pre(id="table-click-event-demo-output"),
    ]

    return demo_contents


@app.callback(
    Output("table-click-event-demo-output", "children"),
    [
        Input("table-click-event-demo", "nClicksCell"),
        Input("table-click-event-demo", "nDoubleClicksCell"),
    ],
    [
        State("table-click-event-demo", "enableCellClickListenColumns"),
        State("table-click-event-demo", "recentlyCellClickColumn"),
        State("table-click-event-demo", "recentlyCellClickRecord"),
        State("table-click-event-demo", "recentlyCellDoubleClickColumn"),
        State("table-click-event-demo", "recentlyCellDoubleClickRecord"),
    ],
    prevent_initial_call=True,
)
def table_click_event_demo(
    nClicksCell,
    nDoubleClicksCell,
    enableCellClickListenColumns,
    recentlyCellClickColumn,
    recentlyCellClickRecord,
    recentlyCellDoubleClickColumn,
    recentlyCellDoubleClickRecord,
):
    return json.dumps(
        dict(
            enableCellClickListenColumns=enableCellClickListenColumns,
            nClicksCell=nClicksCell,
            recentlyCellClickColumn=recentlyCellClickColumn,
            recentlyCellClickRecord=recentlyCellClickRecord,
            nDoubleClicksCell=nDoubleClicksCell,
            recentlyCellDoubleClickColumn=recentlyCellDoubleClickColumn,
            recentlyCellDoubleClickRecord=recentlyCellDoubleClickRecord,
        ),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    from i18n import get_current_locale

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdTable(
        id='table-click-event-demo',
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[
            {
                'key': f'row-{row}',
                **{f'字段{i}': f'字段{i}第{row}行' for i in range(1, 6)},
            }
            for row in range(1, 6)
        ],
        bordered=True,
        enableCellClickListenColumns=[f'字段{i}' for i in range(1, 6, 2)],
    ),
    html.Pre(id='table-click-event-demo-output'),
]

# ...

@app.callback(
    Output('table-click-event-demo-output', 'children'),
    [
        Input('table-click-event-demo', 'nClicksCell'),
        Input('table-click-event-demo', 'nDoubleClicksCell'),
    ],
    [
        State('table-click-event-demo', 'enableCellClickListenColumns'),
        State('table-click-event-demo', 'recentlyCellClickColumn'),
        State('table-click-event-demo', 'recentlyCellClickRecord'),
        State('table-click-event-demo', 'recentlyCellDoubleClickColumn'),
        State('table-click-event-demo', 'recentlyCellDoubleClickRecord'),
    ],
    prevent_initial_call=True,
)
def table_click_event_demo(
    nClicksCell,
    nDoubleClicksCell,
    enableCellClickListenColumns,
    recentlyCellClickColumn,
    recentlyCellClickRecord,
    recentlyCellDoubleClickColumn,
    recentlyCellDoubleClickRecord,
):
    return json.dumps(
        dict(
            enableCellClickListenColumns=enableCellClickListenColumns,
            nClicksCell=nClicksCell,
            recentlyCellClickColumn=recentlyCellClickColumn,
            recentlyCellClickRecord=recentlyCellClickRecord,
            nDoubleClicksCell=nDoubleClicksCell,
            recentlyCellDoubleClickColumn=recentlyCellDoubleClickColumn,
            recentlyCellDoubleClickRecord=recentlyCellDoubleClickRecord,
        ),
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
[
    fac.AntdTable(
        id='table-click-event-demo',
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[
            {
                'key': f'row-{row}',
                **{f'Field {i}': f'Field {i} Row {row}' for i in range(1, 6)},
            }
            for row in range(1, 6)
        ],
        bordered=True,
        enableCellClickListenColumns=[f'Field {i}' for i in range(1, 6, 2)],
    ),
    html.Pre(id='table-click-event-demo-output'),
]

# ...

@app.callback(
    Output('table-click-event-demo-output', 'children'),
    [
        Input('table-click-event-demo', 'nClicksCell'),
        Input('table-click-event-demo', 'nDoubleClicksCell'),
    ],
    [
        State('table-click-event-demo', 'enableCellClickListenColumns'),
        State('table-click-event-demo', 'recentlyCellClickColumn'),
        State('table-click-event-demo', 'recentlyCellClickRecord'),
        State('table-click-event-demo', 'recentlyCellDoubleClickColumn'),
        State('table-click-event-demo', 'recentlyCellDoubleClickRecord'),
    ],
    prevent_initial_call=True,
)
def table_click_event_demo(
    nClicksCell,
    nDoubleClicksCell,
    enableCellClickListenColumns,
    recentlyCellClickColumn,
    recentlyCellClickRecord,
    recentlyCellDoubleClickColumn,
    recentlyCellDoubleClickRecord,
):
    return json.dumps(
        dict(
            enableCellClickListenColumns=enableCellClickListenColumns,
            nClicksCell=nClicksCell,
            recentlyCellClickColumn=recentlyCellClickColumn,
            recentlyCellClickRecord=recentlyCellClickRecord,
            nDoubleClicksCell=nDoubleClicksCell,
            recentlyCellDoubleClickColumn=recentlyCellDoubleClickColumn,
            recentlyCellDoubleClickRecord=recentlyCellDoubleClickRecord,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
