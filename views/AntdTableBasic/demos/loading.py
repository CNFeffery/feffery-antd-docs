from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpace(
        [
            fac.AntdSwitch(id='table-loading', checked=False),
            fac.AntdTable(
                id='table-loading-demo',
                columns=[
                    {'title': 'int型示例', 'dataIndex': 'int型示例'},
                    {'title': 'float型示例', 'dataIndex': 'float型示例'},
                    {'title': 'str型示例', 'dataIndex': 'str型示例'},
                    {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
                ],
                data=[
                    {
                        'int型示例': 123,
                        'float型示例': 1.23,
                        'str型示例': '示例字符',
                        '日期时间示例': datetime.now(),
                    }
                ]
                * 3,
            ),
        ],
        direction='vertical',
        style={'width': '100%'},
    )

    return demo_contents


@app.callback(
    Output('table-loading-demo', 'loading'),
    Input('table-loading', 'checked'),
    prevent_initial_call=True,
)
def table_loading(checked):
    return checked


code_string = [
    {
        'code': """
fac.AntdSpace(
    [
        fac.AntdSwitch(id='table-loading', checked=False),
        fac.AntdTable(
            id='table-loading-demo',
            columns=[
                {'title': 'int型示例', 'dataIndex': 'int型示例'},
                {'title': 'float型示例', 'dataIndex': 'float型示例'},
                {'title': 'str型示例', 'dataIndex': 'str型示例'},
                {'title': '日期时间示例', 'dataIndex': '日期时间示例'},
            ],
            data=[
                {
                    'int型示例': 123,
                    'float型示例': 1.23,
                    'str型示例': '示例字符',
                    '日期时间示例': datetime.now(),
                }
            ]
            * 3,
        ),
    ],
    direction='vertical',
    style={'width': '100%'},
)

...

@app.callback(
    Output('table-loading-demo', 'loading'),
    Input('table-loading', 'checked'),
    prevent_initial_call=True,
)
def table_loading(checked):
    return checked
"""
    }
]
