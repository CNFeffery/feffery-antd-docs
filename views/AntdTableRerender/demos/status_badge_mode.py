import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': '状态徽标示例',
                'dataIndex': '状态徽标示例',
                'renderOptions': {'renderType': 'status-badge'},
            }
        ],
        data=[
            {
                'key': i,
                '状态徽标示例': {'status': status, 'text': status + '状态示例'},
            }
            for i, status in enumerate(
                ['success', 'processing', 'default', 'error', 'warning']
            )
        ],
        style={'width': '250px'},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': '状态徽标示例',
            'dataIndex': '状态徽标示例',
            'renderOptions': {'renderType': 'status-badge'},
        }
    ],
    data=[
        {
            'key': i,
            '状态徽标示例': {'status': status, 'text': status + '状态示例'},
        }
        for i, status in enumerate(
            ['success', 'processing', 'default', 'error', 'warning']
        )
    ],
    style={'width': '250px'},
)
"""
    }
]
