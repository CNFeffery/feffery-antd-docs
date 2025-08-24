import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        col_label = lambda i: f"字段{i}"
        cell_value = lambda i, row: f"字段{i}第{row}行"
    else:  # en-us fallback
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
            id="table-hover-event-demo",
            columns=columns,
            data=data,
            bordered=True,
            enableHoverListen=True,
        ),
        html.Pre(id="table-hover-event-demo-output"),
    ]

    return demo_contents


app.clientside_callback(
    """( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }""",
    Output("table-hover-event-demo-output", "children"),
    [
        Input("table-hover-event-demo", "recentlyMouseEnterColumnDataIndex"),
        Input("table-hover-event-demo", "recentlyMouseEnterRowKey"),
        Input("table-hover-event-demo", "recentlyMouseEnterRow"),
    ],
    prevent_initial_call=True,
)


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    current_locale = get_current_locale()

    if current_locale == "zh-cn":
        return [
            {
                "code": '''
[
    fac.AntdTable(
        id="table-hover-event-demo",
        columns=[
            {"title": f"字段{i}", "dataIndex": f"字段{i}", "width": "20%"}
            for i in range(1, 6)
        ],
        data=[
            {
                "key": f"row-{row}",
                **{f"字段{i}": f"字段{i}第{row}行" for i in range(1, 6)},
            }
            for row in range(1, 6)
        ],
        bordered=True,
        enableHoverListen=True,
    ),
    html.Pre(id="table-hover-event-demo-output"),
]

# ...

app.clientside_callback(
    """( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }""",
    Output("table-hover-event-demo-output", "children"),
    [
        Input("table-hover-event-demo", "recentlyMouseEnterColumnDataIndex"),
        Input("table-hover-event-demo", "recentlyMouseEnterRowKey"),
        Input("table-hover-event-demo", "recentlyMouseEnterRow"),
    ],
    prevent_initial_call=True,
)
'''
            }
        ]
    else:  # en-us
        return [
            {
                "code": '''
[
    fac.AntdTable(
        id="table-hover-event-demo",
        columns=[
            {"title": f"Field {i}", "dataIndex": f"Field {i}", "width": "20%"}
            for i in range(1, 6)
        ],
        data=[
            {
                "key": f"row-{row}",
                **{f"Field {i}": f"Field {i} Row {row}" for i in range(1, 6)},
            }
            for row in range(1, 6)
        ],
        bordered=True,
        enableHoverListen=True,
    ),
    html.Pre(id="table-hover-event-demo-output"),
]

# ...

app.clientside_callback(
    """( recentlyMouseEnterColumnDataIndex,
         recentlyMouseEnterRowKey,
         recentlyMouseEnterRow ) => {
        return JSON.stringify(
            {
                recentlyMouseEnterColumnDataIndex,
                recentlyMouseEnterRowKey,
                recentlyMouseEnterRow
            },
            null,
            4
        );
    }""",
    Output("table-hover-event-demo-output", "children"),
    [
        Input("table-hover-event-demo", "recentlyMouseEnterColumnDataIndex"),
        Input("table-hover-event-demo", "recentlyMouseEnterRowKey"),
        Input("table-hover-event-demo", "recentlyMouseEnterRow"),
    ],
    prevent_initial_call=True,
)
'''
            }
        ]
