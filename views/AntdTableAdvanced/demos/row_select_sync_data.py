import json
import random
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
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
                        **{
                            f'字段{i}': round(random.uniform(0, 10), 3)
                            for i in range(1, 4)
                        },
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

    return demo_contents


@app.callback(
    Output('table-row-selection-sync-selected-rows-demo', 'data'),
    Input('table-row-selection-sync-selected-rows-demo-update-data', 'nClicks'),
    prevent_initial_call=True,
)
def table_row_selection_sync_selected_rows_demo_update_data(nClicks):
    return [
        {
            **{
                f'字段{i}': round(random.uniform(0, 10), 3) for i in range(1, 4)
            },
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


code_string = [
    {
        'code': """
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
                    **{
                        f'字段{i}': round(random.uniform(0, 10), 3)
                        for i in range(1, 4)
                    },
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

...

@app.callback(
    Output('table-row-selection-sync-selected-rows-demo', 'data'),
    Input('table-row-selection-sync-selected-rows-demo-update-data', 'nClicks'),
    prevent_initial_call=True,
)
def table_row_selection_sync_selected_rows_demo_update_data(nClicks):
    return [
        {
            **{
                f'字段{i}': round(random.uniform(0, 10), 3) for i in range(1, 4)
            },
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
