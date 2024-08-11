import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'dropdown-links示例1',
                'dataIndex': 'dropdown-links示例1',
                'renderOptions': {'renderType': 'dropdown-links'},
                'width': '30%',
            },
            {
                'title': 'dropdown-links示例2',
                'dataIndex': 'dropdown-links示例2',
                'renderOptions': {
                    'renderType': 'dropdown-links',
                    'dropdownProps': {'title': '更多'},
                },
                'width': '70%',
            },
        ],
        data=[
            {
                'dropdown-links示例1': [
                    {
                        'title': f'image示例{i}.png',
                        'href': f'assets/imgs/image示例{i}.png',
                    }
                    for i in range(1, 8)
                ],
                'dropdown-links示例2': [
                    {
                        'title': f'image示例{i}.png',
                        'href': f'assets/imgs/image示例{i}.png',
                    }
                    for i in range(1, 8)
                ],
            }
        ]
        * 3,
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
            'title': 'dropdown-links示例1',
            'dataIndex': 'dropdown-links示例1',
            'renderOptions': {'renderType': 'dropdown-links'},
            'width': '30%',
        },
        {
            'title': 'dropdown-links示例2',
            'dataIndex': 'dropdown-links示例2',
            'renderOptions': {
                'renderType': 'dropdown-links',
                'dropdownProps': {'title': '更多'},
            },
            'width': '70%',
        },
    ],
    data=[
        {
            'dropdown-links示例1': [
                {
                    'title': f'image示例{i}.png',
                    'href': f'assets/imgs/image示例{i}.png',
                }
                for i in range(1, 8)
            ],
            'dropdown-links示例2': [
                {
                    'title': f'image示例{i}.png',
                    'href': f'assets/imgs/image示例{i}.png',
                }
                for i in range(1, 8)
            ],
        }
    ]
    * 3,
    bordered=True,
    style={'width': 400},
)
"""
    }
]
