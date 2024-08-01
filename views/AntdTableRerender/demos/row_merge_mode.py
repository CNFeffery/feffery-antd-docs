import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'row-merge示例1',
                'dataIndex': 'row-merge示例1',
                'renderOptions': {'renderType': 'row-merge'},
                'width': '50%',
            },
            {
                'title': 'row-merge示例2',
                'dataIndex': 'row-merge示例2',
                'renderOptions': {'renderType': 'row-merge'},
                'width': '50%',
            },
        ],
        data=[
            {
                'row-merge示例1': {'content': '示例1-1', 'rowSpan': 1},
                'row-merge示例2': {'content': '示例2-1', 'rowSpan': 2},
            },
            {
                'row-merge示例1': {'content': '示例1-2', 'rowSpan': 2},
                'row-merge示例2': {'rowSpan': 0},
            },
            {
                'row-merge示例1': {'rowSpan': 0},
                'row-merge示例2': {'content': '示例2-2', 'rowSpan': 1},
            },
        ],
        bordered=True,
        style={'width': 300},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': 'row-merge示例1',
            'dataIndex': 'row-merge示例1',
            'renderOptions': {'renderType': 'row-merge'},
            'width': '50%',
        },
        {
            'title': 'row-merge示例2',
            'dataIndex': 'row-merge示例2',
            'renderOptions': {'renderType': 'row-merge'},
            'width': '50%',
        },
    ],
    data=[
        {
            'row-merge示例1': {'content': '示例1-1', 'rowSpan': 1},
            'row-merge示例2': {'content': '示例2-1', 'rowSpan': 2},
        },
        {
            'row-merge示例1': {'content': '示例1-2', 'rowSpan': 2},
            'row-merge示例2': {'rowSpan': 0},
        },
        {
            'row-merge示例1': {'rowSpan': 0},
            'row-merge示例2': {'content': '示例2-2', 'rowSpan': 1},
        },
    ],
    bordered=True,
    style={'width': 300},
)
"""
    }
]
