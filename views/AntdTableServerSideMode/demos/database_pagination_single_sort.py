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
            id='table-server-side-mode-pagination+sort-demo-sql',
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
            sortOptions={
                'sortDataIndexes': list(DemoTable._meta.fields.keys())
            },
        ),
        text='数据加载中',
        size='small',
    )

    return demo_contents


@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-sql', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-sql', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-sql', 'sorter'),
    ],
)
def table_server_side_mode_pagination_sort_demo_sql(pagination, sorter):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从DemoTable中抽取对应数据帧
            data_frame = (
                DemoTable.select()
                .order_by(
                    getattr(DemoTable, sorter['columns'][0])
                    if sorter['orders'][0] == 'ascend'
                    else getattr(DemoTable, sorter['columns'][0]).desc()
                )
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return list(data_frame)

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return list(data_frame)

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+sort-demo-sql',
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
        sortOptions={
            'sortDataIndexes': list(DemoTable._meta.fields.keys())
        },
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination+sort-demo-sql', 'data'),
    [
        Input('table-server-side-mode-pagination+sort-demo-sql', 'pagination'),
        Input('table-server-side-mode-pagination+sort-demo-sql', 'sorter'),
    ],
)
def table_server_side_mode_pagination_sort_demo_sql(pagination, sorter):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从DemoTable中抽取对应数据帧
            data_frame = (
                DemoTable.select()
                .order_by(
                    getattr(DemoTable, sorter['columns'][0])
                    if sorter['orders'][0] == 'ascend'
                    else getattr(DemoTable, sorter['columns'][0]).desc()
                )
                .limit(pagination['pageSize'])
                .offset((pagination['current'] - 1) * pagination['pageSize'])
                .dicts()
            )

            return list(data_frame)

        # 根据当前分页的current参数、pageSize参数，从DemoTable中抽取对应数据帧
        data_frame = (
            DemoTable.select()
            .limit(pagination['pageSize'])
            .offset((pagination['current'] - 1) * pagination['pageSize'])
            .dicts()
        )

        return list(data_frame)

    return dash.no_update
"""
    }
]
