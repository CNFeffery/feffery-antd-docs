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
            id='table-server-side-mode-pagination+multi-sort-demo-pandas',
            columns=[
                {
                    'title': column,
                    'dataIndex': column,
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
            sortOptions={
                'sortDataIndexes': demo_df.columns,
                'multiple': 'auto',
            },
            tableLayout='fixed',
        ),
        text='数据加载中',
        size='small',
    )

    return demo_contents


@app.callback(
    Output('table-server-side-mode-pagination+multi-sort-demo-pandas', 'data'),
    [
        Input(
            'table-server-side-mode-pagination+multi-sort-demo-pandas',
            'pagination',
        ),
        Input(
            'table-server-side-mode-pagination+multi-sort-demo-pandas', 'sorter'
        ),
    ],
)
def table_server_side_mode_pagination_multi_sort_demo_pandas(
    pagination, sorter
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从demo_df中抽取对应数据帧
            data_frame = demo_df.sort_values(
                sorter['columns'],
                ascending=[item == 'ascend' for item in sorter['orders']],
            ).iloc[
                (pagination['current'] - 1)
                * pagination['pageSize'] : pagination['current']
                * pagination['pageSize'],
                :,
            ]

            return data_frame.to_dict('records')

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]

        return data_frame.to_dict('records')

    return dash.no_update


code_string = [
    {
        'code': """
fac.AntdSpin(
    fac.AntdTable(
        id='table-server-side-mode-pagination+multi-sort-demo-pandas',
        columns=[
            {
                'title': column,
                'dataIndex': column,
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
        sortOptions={
            'sortDataIndexes': demo_df.columns,
            'multiple': 'auto',
        },
        tableLayout='fixed',
    ),
    text='数据加载中',
    size='small',
)

...

@app.callback(
    Output('table-server-side-mode-pagination+multi-sort-demo-pandas', 'data'),
    [
        Input(
            'table-server-side-mode-pagination+multi-sort-demo-pandas',
            'pagination',
        ),
        Input(
            'table-server-side-mode-pagination+multi-sort-demo-pandas', 'sorter'
        ),
    ],
)
def table_server_side_mode_pagination_multi_sort_demo_pandas(
    pagination, sorter
):
    if pagination:
        time.sleep(0.5)  # 渲染加载动画更好看 ^_^

        # 若存在有效的排序操作
        if sorter and sorter['columns']:
            # 根据当前分页的current参数、pageSize参数，排序后从demo_df中抽取对应数据帧
            data_frame = demo_df.sort_values(
                sorter['columns'],
                ascending=[item == 'ascend' for item in sorter['orders']],
            ).iloc[
                (pagination['current'] - 1)
                * pagination['pageSize'] : pagination['current']
                * pagination['pageSize'],
                :,
            ]

            return data_frame.to_dict('records')

        # 根据当前分页的current参数、pageSize参数，从demo_df中抽取对应数据帧
        data_frame = demo_df.iloc[
            (pagination['current'] - 1) * pagination['pageSize'] : pagination[
                'current'
            ]
            * pagination['pageSize'],
            :,
        ]

        return data_frame.to_dict('records')

    return dash.no_update
"""
    }
]
