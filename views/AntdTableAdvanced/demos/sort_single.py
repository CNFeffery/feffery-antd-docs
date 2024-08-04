import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': 'int型示例', 'dataIndex': 'int型示例', 'width': '25%'},
            {
                'title': 'float型示例',
                'dataIndex': 'float型示例',
                'width': '25%',
            },
            {'title': 'str型示例', 'dataIndex': 'str型示例', 'width': '25%'},
            {
                'title': '日期时间示例',
                'dataIndex': '日期时间示例',
                'width': '25%',
            },
        ],
        data=[
            {
                'int型示例': i,
                'float型示例': round(i * 0.1, 1),
                'str型示例': f'示例字符{i}',
                '日期时间示例': f'2099-01-0{i}',
            }
            for i in [4, 2, 1, 5, 3]
        ],
        sortOptions={
            'sortDataIndexes': [
                'int型示例',
                'float型示例',
                'str型示例',
                '日期时间示例',
            ]
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': 'int型示例', 'dataIndex': 'int型示例', 'width': '25%'},
        {
            'title': 'float型示例',
            'dataIndex': 'float型示例',
            'width': '25%',
        },
        {'title': 'str型示例', 'dataIndex': 'str型示例', 'width': '25%'},
        {
            'title': '日期时间示例',
            'dataIndex': '日期时间示例',
            'width': '25%',
        },
    ],
    data=[
        {
            'int型示例': i,
            'float型示例': round(i * 0.1, 1),
            'str型示例': f'示例字符{i}',
            '日期时间示例': f'2099-01-0{i}',
        }
        for i in [4, 2, 1, 5, 3]
    ],
    sortOptions={
        'sortDataIndexes': [
            'int型示例',
            'float型示例',
            'str型示例',
            '日期时间示例',
        ]
    },
)
"""
    }
]
