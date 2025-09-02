import json

import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component, Input, Output

from i18n import get_current_locale
from server import app


def render() -> Component:
    """渲染当前演示用例 / Render the current demo"""

    locale = get_current_locale()

    if locale == 'zh-cn':
        title = lambda i: f'字段{i}'
        key = lambda i: f'字段{i}'
        cell = '示例内容'
    else:  # en-us fallback
        title = lambda i: f'Field {i}'
        key = lambda i: f'Field {i}'
        cell = 'Sample Content'

    columns = [{'title': title(i), 'dataIndex': key(i)} for i in range(1, 4)]
    data = [
        {**{key(i): cell for i in range(1, 4)}, 'key': f'row-{row + 1}'}
        for row in range(3)
    ]

    demo_contents = [
        fac.AntdTable(
            id='table-row-selection-demo',
            columns=columns,
            data=data,
            rowSelectionType='checkbox',
        ),
        html.Pre(id='table-row-selection-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-row-selection-demo-output', 'children'),
    [
        Input('table-row-selection-demo', 'selectedRowKeys'),
        Input('table-row-selection-demo', 'selectedRows'),
    ],
    prevent_initial_call=True,
)
def table_row_selection_demo(selectedRowKeys, selectedRows):
    return json.dumps(
        dict(selectedRowKeys=selectedRowKeys, selectedRows=selectedRows),
        indent=4,
        ensure_ascii=False,
    )


def code_string() -> list:
    """返回当前语种对应的演示代码 / Return demo code for the current locale"""
    locale = get_current_locale()

    if locale == 'zh-cn':
        return [
            {
                'code': """
[
    fac.AntdTable(
        id='table-row-selection-demo',
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}'}
            for i in range(1, 4)
        ],
        data=[
            {
                **{f'字段{i}': '示例内容' for i in range(1, 4)},
                'key': f'row-{row+1}',
            }
            for row in range(3)
        ],
        rowSelectionType='checkbox',
    ),
    html.Pre(id='table-row-selection-demo-output'),
]

# ...

@app.callback(
    Output('table-row-selection-demo-output', 'children'),
    [
        Input('table-row-selection-demo', 'selectedRowKeys'),
        Input('table-row-selection-demo', 'selectedRows'),
    ],
    prevent_initial_call=True,
)
def table_row_selection_demo(selectedRowKeys, selectedRows):
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
                'code': """
[
    fac.AntdTable(
        id='table-row-selection-demo',
        columns=[
            {'title': f'Field {i}', 'dataIndex': f'Field {i}'}
            for i in range(1, 4)
        ],
        data=[
            {
                **{f'Field {i}': 'Sample Content' for i in range(1, 4)},
                'key': f'row-{row+1}',
            }
            for row in range(3)
        ],
        rowSelectionType='checkbox',
    ),
    html.Pre(id='table-row-selection-demo-output'),
]

# ...

@app.callback(
    Output('table-row-selection-demo-output', 'children'),
    [
        Input('table-row-selection-demo', 'selectedRowKeys'),
        Input('table-row-selection-demo', 'selectedRows'),
    ],
    prevent_initial_call=True,
)
def table_row_selection_demo(selectedRowKeys, selectedRows):
    return json.dumps(
        dict(selectedRowKeys=selectedRowKeys, selectedRows=selectedRows),
        indent=4,
        ensure_ascii=False,
    )
"""
            }
        ]
