import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'ellipsis示例',
                'dataIndex': 'ellipsis示例',
                'renderOptions': {'renderType': 'ellipsis'},
            }
        ],
        data=[{'ellipsis示例': 'bala' * 10}],
        bordered=True,
        style={'width': 200},
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'title': 'ellipsis示例',
            'dataIndex': 'ellipsis示例',
            'renderOptions': {'renderType': 'ellipsis'},
        }
    ],
    data=[{'ellipsis示例': 'bala' * 10}],
    bordered=True,
    style={'width': 200},
)
"""
    }
]
