import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': f'字段{i}',
                'dataIndex': f'字段{i}',
                'width': 'calc(100% / 3)',
            }
            for i in range(1, 4)
        ],
        data=[
            {
                'key': f'row-{i}',
                '字段1': '第一层',
                '字段2': '第一层',
                '字段3': '第一层',
                'children': [
                    {
                        'key': f'row-{i}{j}',
                        '字段1': '第二层',
                        '字段2': '第二层',
                        '字段3': '第二层',
                    }
                    for j in range(3)
                ],
            }
            for i in range(3)
        ],
        bordered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': f'字段{i}',
            'dataIndex': f'字段{i}',
            'width': 'calc(100% / 3)',
        }
        for i in range(1, 4)
    ],
    data=[
        {
            'key': f'row-{i}',
            '字段1': '第一层',
            '字段2': '第一层',
            '字段3': '第一层',
            'children': [
                {
                    'key': f'row-{i}{j}',
                    '字段1': '第二层',
                    '字段2': '第二层',
                    '字段3': '第二层',
                }
                for j in range(3)
            ],
        }
        for i in range(3)
    ],
    bordered=True,
)
"""
    }
]
