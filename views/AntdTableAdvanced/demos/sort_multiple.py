import random
import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
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
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
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
)
"""
    }
]
