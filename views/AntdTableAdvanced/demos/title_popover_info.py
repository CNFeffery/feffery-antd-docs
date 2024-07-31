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
        titlePopoverInfo={
            f'字段{i}': {
                'title': f'字段{i}说明',
                'content': f'这是字段{i}的说明巴拉巴拉巴拉',
                'placement': 'top',
            }
            for i in range(1, 6)
        },
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
    titlePopoverInfo={
        f'字段{i}': {
            'title': f'字段{i}说明',
            'content': f'这是字段{i}的说明巴拉巴拉巴拉',
            'placement': 'top',
        }
        for i in range(1, 6)
    },
)
"""
    }
]
