import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': 400}
            for i in range(5)
        ],
        data=[
            {**{f'字段{j}': i for j in range(5)}, 'key': f'row-{i}'}
            for i in range(10)
        ],
        bordered=True,
        expandedRowKeyToContent=[
            {
                'key': f'row-{i}',
                'content': fac.AntdButton(
                    f'第{i}行展开内容示例', type='primary'
                ),
            }
            for i in range(0, 10, 2)
        ],
        defaultExpandedRowKeys=['row-2', 'row-6'],
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': 400}
        for i in range(5)
    ],
    data=[
        {**{f'字段{j}': i for j in range(5)}, 'key': f'row-{i}'}
        for i in range(10)
    ],
    bordered=True,
    expandedRowKeyToContent=[
        {
            'key': f'row-{i}',
            'content': fac.AntdButton(
                f'第{i}行展开内容示例', type='primary'
            ),
        }
        for i in range(0, 10, 2)
    ],
    defaultExpandedRowKeys=['row-2', 'row-6'],
)
"""
    }
]
