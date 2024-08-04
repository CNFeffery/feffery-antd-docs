import json
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
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


code_string = [
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

...

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
