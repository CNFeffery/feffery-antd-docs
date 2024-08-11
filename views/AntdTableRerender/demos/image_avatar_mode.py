import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'image-avatar示例1',
                'dataIndex': 'image-avatar示例1',
                'renderOptions': {'renderType': 'image-avatar'},
                'width': '50%',
            },
            {
                'title': 'image-avatar示例2',
                'dataIndex': 'image-avatar示例2',
                'renderOptions': {'renderType': 'image-avatar'},
                'width': '50%',
            },
        ],
        data=[
            {
                'image-avatar示例1': {
                    'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg'
                },
                'image-avatar示例2': {
                    'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                    'shape': 'square',
                },
            }
        ]
        * 3,
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
            'title': 'image-avatar示例1',
            'dataIndex': 'image-avatar示例1',
            'renderOptions': {'renderType': 'image-avatar'},
            'width': '50%',
        },
        {
            'title': 'image-avatar示例2',
            'dataIndex': 'image-avatar示例2',
            'renderOptions': {'renderType': 'image-avatar'},
            'width': '50%',
        },
    ],
    data=[
        {
            'image-avatar示例1': {
                'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg'
            },
            'image-avatar示例2': {
                'src': 'assets/imgs/components/AntdAvatar/avatar-demo.jpg',
                'shape': 'square',
            },
        }
    ]
    * 3,
    bordered=True,
    style={'width': 300},
)
"""
    }
]
