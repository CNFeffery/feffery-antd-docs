import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {'title': f'字段{i}', 'dataIndex': f'字段{i}'} for i in range(1, 6)
        ],
        data=[
            {
                **{f'字段{i}': '示例内容' for i in range(1, 6)},
                'key': f'row-{row+1}',
            }
            for row in range(3)
        ],
        rowSelectionType='radio',
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {'title': f'字段{i}', 'dataIndex': f'字段{i}'} for i in range(1, 6)
    ],
    data=[
        {
            **{f'字段{i}': '示例内容' for i in range(1, 6)},
            'key': f'row-{row+1}',
        }
        for row in range(3)
    ],
    rowSelectionType='radio',
)
"""
    }
]
