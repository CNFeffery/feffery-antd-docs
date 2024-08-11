import json
from dash import html
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            id='table-editable-demo',
            columns=[
                {
                    'title': 'int型示例',
                    'dataIndex': 'int型示例',
                    'editable': True,
                    'width': '25%',
                },
                {
                    'title': 'float型示例',
                    'dataIndex': 'float型示例',
                    'editable': True,
                    'width': '25%',
                },
                {
                    'title': 'str型示例',
                    'dataIndex': 'str型示例',
                    'editable': True,
                    'width': '25%',
                },
                {
                    'title': '日期时间示例',
                    'dataIndex': '日期时间示例',
                    'editable': True,
                    'width': '25%',
                },
            ],
            data=[
                {
                    'key': f'row-{i}',
                    'int型示例': 123,
                    'float型示例': 1.23,
                    'str型示例': '示例字符',
                    '日期时间示例': datetime.now().strftime(
                        '%Y-%m-%d %H:%M:%S'
                    ),
                }
                for i in range(1, 4)
            ],
            bordered=True,
        ),
        html.Pre(id='table-editable-demo-output'),
    ]

    return demo_contents


@app.callback(
    Output('table-editable-demo-output', 'children'),
    [
        Input('table-editable-demo', 'recentlyChangedRow'),
        Input('table-editable-demo', 'recentlyChangedColumn'),
    ],
    prevent_initial_call=True,
)
def table_editable_demo(recentlyChangedRow, recentlyChangedColumn):
    return json.dumps(
        dict(
            recentlyChangedRow=recentlyChangedRow,
            recentlyChangedColumn=recentlyChangedColumn,
        ),
        indent=4,
        ensure_ascii=False,
    )


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        id='table-editable-demo',
        columns=[
            {
                'title': 'int型示例',
                'dataIndex': 'int型示例',
                'editable': True,
                'width': '25%',
            },
            {
                'title': 'float型示例',
                'dataIndex': 'float型示例',
                'editable': True,
                'width': '25%',
            },
            {
                'title': 'str型示例',
                'dataIndex': 'str型示例',
                'editable': True,
                'width': '25%',
            },
            {
                'title': '日期时间示例',
                'dataIndex': '日期时间示例',
                'editable': True,
                'width': '25%',
            },
        ],
        data=[
            {
                'key': f'row-{i}',
                'int型示例': 123,
                'float型示例': 1.23,
                'str型示例': '示例字符',
                '日期时间示例': datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S'
                ),
            }
            for i in range(1, 4)
        ],
        bordered=True,
    ),
    html.Pre(id='table-editable-demo-output'),
]

...

@app.callback(
    Output('table-editable-demo-output', 'children'),
    [
        Input('table-editable-demo', 'recentlyChangedRow'),
        Input('table-editable-demo', 'recentlyChangedColumn'),
    ],
    prevent_initial_call=True,
)
def table_editable_demo(recentlyChangedRow, recentlyChangedColumn):
    return json.dumps(
        dict(
            recentlyChangedRow=recentlyChangedRow,
            recentlyChangedColumn=recentlyChangedColumn,
        ),
        indent=4,
        ensure_ascii=False,
    )
"""
    }
]
