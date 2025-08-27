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
        label = lambda i: f"字段{i}"
        sort_keys = [label(1), label(2), label(4), label(5)]
    else:  # en-us fallback
        label = lambda i: f"Field {i}"
        sort_keys = [label(1), label(2), label(4), label(5)]

    columns = [
        {"title": label(i), "dataIndex": label(i), "width": "20%"} for i in range(1, 6)
    ]
    data = [{label(j): random.randint(1, 4) for j in range(1, 6)} for _ in range(10)]

    demo_contents = [
        fac.AntdTable(
            id="table-sort-demo",
            columns=columns,
            data=data,
            bordered=True,
            sortOptions={
                "sortDataIndexes": sort_keys,
                "multiple": True,
            },
        ),
        html.Pre(id="table-sort-demo-output"),
    ]

    return demo_contents


@app.callback(
    Output("table-sort-demo-output", "children"),
    Input("table-sort-demo", "sorter"),
    prevent_initial_call=True,
)
def table_sort_demo(sorter):
    return json.dumps(sorter, indent=4, ensure_ascii=False)


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""

    locale = get_current_locale()

    if locale == "zh-cn":
        return [
            {
                "code": """
[
    fac.AntdTable(
        id='table-sort-demo',
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[
            {f'字段{j}': random.randint(1, 4) for j in range(1, 6)}
            for _ in range(10)
        ],
        bordered=True,
        sortOptions={
            'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
            'multiple': True,
        },
    ),
    html.Pre(id='table-sort-demo-output'),
]

# ...

@app.callback(
    Output('table-sort-demo-output', 'children'),
    Input('table-sort-demo', 'sorter'),
    prevent_initial_call=True,
)
def table_sort_demo(sorter):
    return json.dumps(sorter, indent=4, ensure_ascii=False)
"""
            }
        ]
    else:  # en-us
        return [
            {
                "code": """
[
    fac.AntdTable(
        id='table-sort-demo',
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[
            {f'Field {j}': random.randint(1, 4) for j in range(1, 6)}
            for _ in range(10)
        ],
        bordered=True,
        sortOptions={
            'sortDataIndexes': ['Field 1', 'Field 2', 'Field 4', 'Field 5'],
            'multiple': True,
        },
    ),
    html.Pre(id='table-sort-demo-output'),
]

# ...

@app.callback(
    Output('table-sort-demo-output', 'children'),
    Input('table-sort-demo', 'sorter'),
    prevent_initial_call=True,
)
def table_sort_demo(sorter):
    return json.dumps(sorter, indent=4, ensure_ascii=False)
"""
            }
        ]
