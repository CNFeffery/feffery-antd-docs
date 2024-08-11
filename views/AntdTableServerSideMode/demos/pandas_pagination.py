import dash
import time
import feffery_antd_components as fac
from dash.dependencies import Component, Input, Output

from server import app
from .mock_data import demo_df


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdSpin(
        fac.AntdTable(
            id='table-server-side-mode-pagination-demo-pandas',
            columns=[
                {
                    'title': column,
                    'dataIndex': column,
                    'width': 'calc(100% / {})'.format(demo_df.shape[0]),
                }
                for column in demo_df.columns
            ],
            bordered=True,
            # 关键参数
            mode='server-side',
            pagination={
                'total': demo_df.shape[0],
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
    Output('table-server-side-mode-pagination-demo-pandas', 'data'),
    Input('table-server-side-mode-pagination-demo-pandas', 'pagination'),
)
def table_server_side_mode_pagination_demo_pandas(pagination):
    if pagination:
        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return data_frame.to_dict('records')

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
                'width': 'calc(100% / {})'.format(demo_df.shape[0]),
            }
            for column in demo_df.columns
        ],
        bordered=True,
        # 关键参数
        mode='server-side',
        pagination={
            'total': demo_df.shape[0],
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
    Output('table-server-side-mode-pagination-demo-pandas', 'data'),
    Input('table-server-side-mode-pagination-demo-pandas', 'pagination'),
)
def table_server_side_mode_pagination_demo_pandas(pagination):
    if pagination:
        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]

        time.sleep(0.5)  # 渲染加载动画更好看 ^_^
        return data_frame.to_dict('records')

    return dash.no_update
"""
    }
]
