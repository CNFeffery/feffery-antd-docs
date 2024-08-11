import json
import random
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            id='table-sort-demo',
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
                for i in range(1, 6)
            ],
            data=[
                {f'字段{j}': random.randint(1, 4) for j in range(1, 6)}
                for i in range(10)
            ],
            bordered=True,
            sortOptions={
                'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
                'multiple': True,
            },
        ),
        html.Pre(id='table-sort-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-sort-demo-output', 'children'),
    Input('table-sort-demo', 'sorter'),
    prevent_initial_call=True,
)
def table_sort_demo(sorter):
    return json.dumps(sorter, indent=4, ensure_ascii=False)


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        id='table-sort-demo',
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': '20%'}
            for i in range(1, 6)
        ],
        data=[
            {f'字段{j}': random.randint(1, 4) for j in range(1, 6)}
            for i in range(10)
        ],
        bordered=True,
        sortOptions={
            'sortDataIndexes': ['字段1', '字段2', '字段4', '字段5'],
            'multiple': True,
        },
    ),
    html.Pre(id='table-sort-demo-output'),
]

...

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
