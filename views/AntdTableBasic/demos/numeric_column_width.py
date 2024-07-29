import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = [
        fac.AntdTable(
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': width}
                for i, width in zip(range(1, 6), [50, 100, 50, 100, 50])
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
        ),
        fac.AntdTable(
            columns=[
                {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': width}
                for i, width in zip(
                    range(1, 6), [5000, 10000, 5000, 10000, 5000]
                )
            ],
            data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
        ),
    ]

    return demo_contents


code_string = [
    {
        'code': """
[
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': width}
            for i, width in zip(range(1, 6), [50, 100, 50, 100, 50])
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
    ),
    fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}', 'width': width}
            for i, width in zip(
                range(1, 6), [5000, 10000, 5000, 10000, 5000]
            )
        ],
        data=[{f'字段{i}': '示例内容' for i in range(1, 6)}] * 3,
    ),
]
"""
    }
]
