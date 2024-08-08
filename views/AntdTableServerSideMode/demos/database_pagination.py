import dash
import time
from peewee import fn
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from .mock_data import DemoTable


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpin(
        fac.AntdTable(
            id='table-server-side-mode-pagination-demo-sql',
            columns=[
                {
                    'title': column,
                    'dataIndex': column,
                    'width': 'calc(100% / {})'.format(
                        len(DemoTable._meta.fields)
                    ),
                }
                for column in DemoTable._meta.fields.keys()
            ],
            bordered=True,
            # 关键参数
            mode='server-side',
            pagination={
                'total': (DemoTable.select(fn.count(DemoTable.id)).scalar()),
                'current': 1,
                'pageSize': 5,
                'showSizeChanger': True,
                'pageSizeOptions': [5, 10],
                'position': 'topCenter',
                'showQuickJumper': True,
            },
        ),
        text='数据加载中',
        size='small',
    )

    return demo_contents


@app.callback(
    Output('table-server-side-mode-pagination-demo-sql', 'data'),
    Input('table-server-side-mode-pagination-demo-sql', 'pagination'),
)
def table_server_side_mode_pagination_demo_sql(pagination):
    if pagination:
        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return list(data_frame)

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination-demo-sql',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(
                    len(DemoTable._meta.fields)
                ),
            }
            for column in DemoTable._meta.fields.keys()
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': (DemoTable.select(fn.count(DemoTable.id)).scalar()),
            'current': 1,
            'pageSize': 5,
            'showSizeChanger': True,
            'pageSizeOptions': [5, 10],
            'position': 'topCenter',
            'showQuickJumper': True,
        },
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination-demo-sql', 'data'),
    Input('table-server-side-mode-pagination-demo-sql', 'pagination'),
)
def table_server_side_mode_pagination_demo_sql(pagination):
    if pagination:
        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return list(data_frame)

    return dash.no_update
"""
    }
]