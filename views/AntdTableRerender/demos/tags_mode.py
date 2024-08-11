import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'tags示例1',
                'dataIndex': 'tags示例1',
                'renderOptions': {'renderType': 'tags'},
            },
            {
                'title': 'tags示例2',
                'dataIndex': 'tags示例2',
                'renderOptions': {'renderType': 'tags'},
            },
        ],
        data=[
            {
                'tags示例1': {'tag': f'标签{i}', 'color': 'cyan'},
                'tags示例2': [
                    {'tag': f'标签{i}-{j}', 'color': color}
                    for j, color in zip(
                        range(1, 4), ['volcano', 'blue', 'geekblue']
                    )
                ],
            }
            for i in range(1, 4)
        ],
        bordered=True,
        style={'width': 400},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': 'tags示例1',
            'dataIndex': 'tags示例1',
            'renderOptions': {'renderType': 'tags'},
        },
        {
            'title': 'tags示例2',
            'dataIndex': 'tags示例2',
            'renderOptions': {'renderType': 'tags'},
        },
    ],
    data=[
        {
            'tags示例1': {'tag': f'标签{i}', 'color': 'cyan'},
            'tags示例2': [
                {'tag': f'标签{i}-{j}', 'color': color}
                for j, color in zip(
                    range(1, 4), ['volcano', 'blue', 'geekblue']
                )
            ],
        }
        for i in range(1, 4)
    ],
    bordered=True,
    style={'width': 400},
)
"""
    }
]
