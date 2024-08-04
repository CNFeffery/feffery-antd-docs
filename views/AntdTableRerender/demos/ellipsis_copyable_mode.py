import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'ellipsis-copyable示例',
                'dataIndex': 'ellipsis-copyable示例',
                'renderOptions': {'renderType': 'ellipsis-copyable'},
            }
        ],
        data=[{'ellipsis-copyable示例': 'bala' * 10}],
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
            'title': 'ellipsis-copyable示例',
            'dataIndex': 'ellipsis-copyable示例',
            'renderOptions': {'renderType': 'ellipsis-copyable'},
        }
    ],
    data=[{'ellipsis-copyable示例': 'bala' * 10}],
    bordered=True,
    style={'width': 200},
)
"""
    }
]
