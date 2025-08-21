import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdTable(
        columns=[
            {
                'dataIndex': '按钮示例',
                'title': '按钮示例',
                'renderOptions': {'renderType': 'button'},
            },
        ],
        data=[
            {
                '按钮示例': [
                    {
                        'content': '带tooltip',
                        'tooltip': {'title': 'tooltip示例'},
                    },
                    {
                        'content': '不带tooltip',
                    },
                ]
            }
        ],
        bordered=True,
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdTable(
    columns=[
        {
            'dataIndex': '按钮示例',
            'title': '按钮示例',
            'renderOptions': {'renderType': 'button'},
        },
    ],
    data=[
        {
            '按钮示例': [
                {
                    'content': '带tooltip',
                    'tooltip': {'title': 'tooltip示例'},
                },
                {
                    'content': '不带tooltip',
                },
            ]
        }
    ],
    bordered=True,
)
"""
    }
]
