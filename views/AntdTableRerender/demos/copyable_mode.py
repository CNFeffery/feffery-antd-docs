import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'title': 'copyable示例',
                'dataIndex': 'copyable示例',
                'renderOptions': {'renderType': 'copyable'},
            }
        ],
        data=[{'copyable示例': '可复制内容'}],
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
            'title': 'copyable示例',
            'dataIndex': 'copyable示例',
            'renderOptions': {'renderType': 'copyable'},
        }
    ],
    data=[{'copyable示例': '可复制内容'}],
    bordered=True,
    style={'width': 200},
)
"""
    }
]
